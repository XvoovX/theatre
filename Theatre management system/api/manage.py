#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
   入口程序
"""

from app import create_app
from flask import request, jsonify
from utils.response_code import RET

# 创建 Flask 的 app 对象
app = create_app("develop")

# 启用调试模式
if app.config.get("DEBUG", False):
    app.debug = True

# 创建全站拦截器, 每个请求之前做处理
@app.before_request
def user_validation():
    print(request.endpoint)  # 方便跟踪调试
    if not request.endpoint:  # 如果请求点为空
        return jsonify(code=RET.URLNOTFOUND, message="url not found", error="url not found")

@app.before_request
def user_require_token():
    # 不需要 token 验证的请求点列表
    permission = [
        'apiversion.Apiversion', 'adminfunctions.Adminfunctions', 'shows.queryShowID', 'shows.Shows',
        'refunds.Refunds', 'ticketprices.Ticketprices', 'orders.Orders', 'administrators.Administrators',
        'theaters.Theaters', 'users.Users', 'users.login', 'users.register', 'users.information',
        'ticketprices.ticketprices', 'ticketprices.TicketpricesQuery', 'theaters.theaters',
        'shows.adminpost', 'shows.queryShowName', 'shows.adminadvise', 'shows.admindelete',
        'administrators.administrators', 'orders.orders', 'orders.queryUser', 'refunds.refunds',
        'refunds.refundsOrder', 'adminfunctions.adminfunctions', 'shows.queryITheaterID'
    ]

    # 如果不是请求上述列表中的接口，需要验证 token
    if request.endpoint not in permission:
        # 在请求头上拿到 token
        token = request.headers.get("Token")
        if not token:
            return jsonify(code=RET.PARAMERR, message="缺少参数 Token 或请求非法")

        # 校验 token 格式正确与过期时间
        secret_key = app.config['SECRET_KEY']
        from utils.jwt_util import JwtToken

        verify_status, payload_data = JwtToken.parse_token(token, secret_key=secret_key)
        if not verify_status:
            # 单平台用户登录失效
            app.logger.error(payload_data.get("err"))
            return jsonify(code=RET.SESSIONERR, message='用户未登录或登录已过期', error=payload_data.get("err"))

# 创建全站拦截器，每个请求之后根据请求方法统一设置返回头
@app.after_request
def process_response(response):
    allow_cors = ['OPTIONS', 'PUT', 'DELETE', 'GET', 'POST']
    if request.method in allow_cors:
        response.headers["Access-Control-Allow-Origin"] = '*'
        if request.headers.get('Origin') and request.headers['Origin'] == 'http://api.youwebsite.com':
            response.headers["Access-Control-Allow-Origin"] = 'http://api.youwebsite.com'

        response.headers["Access-Control-Allow-Credentials"] = 'true'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,GET,POST,PUT,DELETE'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,Token,Authorization'
        response.headers['Access-Control-Expose-Headers'] = 'VerifyCodeID,ext'
    return response

if __name__ == "__main__":
    # 使用内置调试服务器启动应用
    app.run(host="0.0.0.0", port=5000, debug=True)
