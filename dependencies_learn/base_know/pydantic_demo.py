from pydantic import BaseModel, ValidationError
from typing import Optional
from datetime import datetime
class User(BaseModel):
    id: int
    name: str
    age: int
    signup_ts: Optional[datetime] = None

# 创建 User 实例，Pydantic 会自动进行类型转换和验证
user_data = {
    "id": "123",  # 注意这里故意用字符串代表数字
    "name": "John Doe",
    "age": 30
}

try:
    user = User(**user_data)
    print(user)
except ValidationError as e:
    print(e)

# 输出:
# id=123 name='John Doe' age=30 signup_ts=None
