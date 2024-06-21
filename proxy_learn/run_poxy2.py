import subprocess
import requests
import time

def start_proxy(port=8000, api_port=8001):
    """启动配置代理."""
    command = [
        'configurable-http-proxy',
        '--default-target', 'http://localhost:3000',
        '--port', str(port),
        '--api-port', str(api_port),
        '--ip', '127.0.0.1',
        '--error-target', 'http://localhost:3001'
    ]
    return subprocess.Popen(command)

def add_route(path, target, api_port=8001):
    """添加路由."""
    url = f'http://localhost:{api_port}/api/routes{path}'
    response = requests.post(url, json={"target": target})
    return response.status_code, response.json()

def remove_route(path, api_port=8001):
    """移除路由."""
    url = f'http://localhost:{api_port}/api/routes{path}'
    response = requests.delete(url)
    return response.status_code

if __name__ == "__main__":
    # 启动代理
    proxy_process = start_proxy()

    try:
        # 给它一点时间启动
        time.sleep(2)

        # 添加路由
        status_code, response = add_route('/app', 'http://localhost:4000')
        print('Add route status:', status_code, response)

        # 用完之后清理，这里只是示例，实际使用中可能不会这么快移除
        time.sleep(10)
        status_code = remove_route('/app')
        print('Remove route status:', status_code)
    finally:
        # 确保代理进程被终止
        proxy_process.terminate()
