import aiohttp
import asyncio

class ConfigurableHTTPProxy:
    def __init__(self, api_url):
        self.api_url = api_url

    async def api_request(self, method, path, body=None):
        url = self.api_url + path
        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, json=body) as resp:
                response_text = await resp.text()
                if resp.status in [200, 201, 204]:
                    try:
                        return await resp.json()
                    except aiohttp.ContentTypeError:
                        return response_text
                else:
                    return {'status': resp.status, 'text': response_text}

    async def add_route(self, routespec, target, user=None, server_name=None):
        body = {
            'target': target,
            'user': user,
            'server_name': server_name,
        }
        return await self.api_request('POST', f'/api/routes{routespec}', body)

    async def delete_route(self, routespec):
        return await self.api_request('DELETE', f'/api/routes{routespec}')

async def main():
    proxy = ConfigurableHTTPProxy(api_url='http://localhost:8002')
    # 添加路由
    response = await proxy.add_route('/user/test/', 'http://127.0.0.1:8888/')
    print("Add route response:", response)

    # 发送请求通过代理
    async with aiohttp.ClientSession() as session:
        async with session.get('http://localhost:8001/user/test/') as response:
            text = await response.text()
            print("Response from proxy:", text)

    # 清除路由
    response = await proxy.delete_route('/user/test/')
    print("Delete route response:", response)

# 运行主函数
asyncio.run(main())
