import asyncio
import concurrent.futures
import sys
from contextlib import ExitStack
from contextvars import copy_context
from types import TracebackType
from typing import (
    AsyncContextManager,
    Awaitable,
    Callable,
    ContextManager,
    Optional,
    Protocol,
    TypeVar,
)

from typing_extensions import ParamSpec

from langgraph.errors import GraphInterrupt

P = ParamSpec("P")
T = TypeVar("T")


class Submit(Protocol[P, T]):
    def __call__(
        self,
        fn: Callable[P, T],
        *args: P.args,
        __name__: Optional[str] = None,
        __cancel_on_exit__: bool = False,
        **kwargs: P.kwargs,
    ) -> concurrent.futures.Future[T]:
        ...

class AsyncBackgroundExecutor(AsyncContextManager):
    def __init__(self) -> None:
        self.context_not_supported = sys.version_info < (3, 11)
        self.tasks: dict[asyncio.Task, bool] = {}
        self.sentinel = object()

    def submit(
        self,
        fn: Callable[P, Awaitable[T]],
        *args: P.args,
        __name__: Optional[str] = None,
        __cancel_on_exit__: bool = False,
        **kwargs: P.kwargs,
    ) -> asyncio.Task[T]:
        coro = fn(*args, **kwargs)
        if self.context_not_supported:
            task = asyncio.create_task(coro, name=__name__)
        else:
            task = asyncio.create_task(coro, name=__name__, context=copy_context())
        self.tasks[task] = __cancel_on_exit__
        task.add_done_callback(self.done)
        return task

    def done(self, task: asyncio.Task) -> None:
        try:
            task.result()
        except GraphInterrupt:
            # This exception is an interruption signal, not an error
            # so we don't want to re-raise it on exit
            self.tasks.pop(task)
        except BaseException:
            pass
        else:
            self.tasks.pop(task)

    async def __aenter__(self) -> Submit:
        return self.submit

    async def exit(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        # cancel all tasks that should be cancelled
        for task, cancel in self.tasks.items():
            if cancel:
                task.cancel(self.sentinel)
        # wait for all tasks to finish
        if self.tasks:
            await asyncio.wait(self.tasks)
        # re-raise the first exception that occurred in a task
        if exc_type is None:
            # if there's already an exception being raised, don't raise another one
            for task in self.tasks:
                try:
                    task.result()
                except asyncio.CancelledError:
                    pass

    async def __aexit__(
        self,
        exc_type: Optional[type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        # we cannot use `await` outside of asyncio.shield, as this code can run
        # after owning task is cancelled, so pulling async logic to separate method

        # wait for all background tasks to finish, shielded from cancellation
        await asyncio.shield(self.exit(exc_type, exc_value, traceback))

import asyncio
from typing import Awaitable, Callable


async def do_some_work(name: str) -> None:
    print(f"Starting work: {name}")
    await asyncio.sleep(2)
    print(f"Finished work: {name}")

async def main():
    async with AsyncBackgroundExecutor() as executor:
        # Submit a task that should be cancelled on exit
        task1 = executor.submit(do_some_work, "Task 1", __cancel_on_exit__=True)

        # Submit a task that should not be cancelled on exit
        task2 = executor.submit(do_some_work, "Task 2", __cancel_on_exit__=False)

        # Wait for the tasks to complete
        await asyncio.gather(task1, task2)

        print("All tasks completed!")

asyncio.run(main())