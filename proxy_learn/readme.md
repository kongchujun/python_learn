# start up node proxy
npm install -g configurable-http-proxy  
configurable-http-proxy --default-target http://127.0.0.1:8888 --port 8001 --api-port 8002  
configurable-http-proxy  --port 8001 --api-port 8002  
run Flask or fastapi web server
run single_proxy.py
# explain
```angular2html
--default-target 参数在 configurable-http-proxy 中用于指定默认的转发目标地址，这意味着如果代理接收到没有明确匹配任何配置路由的请求，它将会把这些请求转发到这个默认目标。

是否提前写好 --default-target 取决于你的具体使用场景：

当你应该设置 --default-target:
简化配置：如果大部分请求都应该转发到同一个目标，设置一个默认目标可以简化路由配置。
保证服务连续性：在动态添加和删除路由的应用中，设置一个默认目标可以确保即使删除了特定的路由，请求仍然可以被处理，而不是返回错误。
作为后备：在某些应用中，你可能想要确保所有未明确匹配的请求都被转发到某个后备服务或警告页面。
当你不需要设置 --default-target:
精确控制：如果你想要精确控制所有路由，并且希望所有未配置路由的请求都明确失败（例如返回 404），则无需设置默认目标。
安全考虑：在安全敏感的应用中，你可能不希望未知的或未经授权的请求被随意转发到默认目标，尤其是当默认目标可能处理敏感数据或操作时。
因此，是否设置 --default-target 应根据你的具体需求和预期行为来决定。如果你的应用逻辑要求所有请求都必须经过严格的路由匹配，那么可能不需要设置默认目标。如果你希望提供一个通用的后备服务或简化配置，则设置一个默认目标会很有帮助
```
# parameter
```angular2html
在使用 configurable-http-proxy 时指定 --port 和 --api-port 参数是为了定义不同的服务端口，这两个端口各自承担不同的角色：

--port 8001：

这是 configurable-http-proxy 作为代理服务器监听客户端请求的端口。
用户或前端服务（如 JupyterHub）会将请求发送到这个端口。
代理将根据配置的路由将请求转发到正确的后端服务（比如一个 web 服务器或应用服务器）。
--api-port 8002：

这是 configurable-http-proxy 的 API 接口使用的端口。
通过这个端口，可以进行代理的配置操作，如添加或删除路由。
通常这个端口不会被普通用户直接访问，而是由管理代理配置的应用程序（如 JupyterHub 的管理后台）使用。
这个端口用于接收 REST API 调用，允许动态修改代理的行为（例如更改路由规则）
```

## disadvantage
不能动态切换路由:  
http://localhost:8001/user/test/  -> http://127.0.0.1:8888/user/test/  


