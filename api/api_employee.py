import requests

import api
from tools.get_log import GetLog

log = GetLog.get_logger()

class ApiEmployee(object):
    # 1.初始化
    def __init__(self):
        # 定义新增url
        self.post_url = api.host + "/api/sys/user"
        # 定义修改、查询、删除url
        self.url = api.host + "/api/sys/user/{}"
        log.info("新增员工url:{}".format(self.post_url))
        log.info("删除、更新、查询url模板:{}".format(self.url))

    # 2.新增员工
    def api_post_employee(self, username, mobile, workNumber):
        # 1. 参数数据
        data = {"username": username,
                "mobile": mobile,
                "workNumber": workNumber
                }
        log.info("新增员工数据：{} 新增员工请求信息头： {}".format(data, api.headers))
        # 1. 参数数据
        # 2.调用post方法 ->返回响应对象
        return requests.post(url=self.post_url, json=data, headers=api.headers)

    # 3.修改员工
    def api_put_employee(self):
        # 1.参数数据
        data = {"username": "tom888"}
        log.info("修改员工请求url:{} 修改员工数据{} 修改员工请求信息头{}".format(self.url.format(api.user_id),data,api.headers))
        # 2.调用put方法->返回响应对象
        return requests.put(url=self.url.format(api.user_id), json=data, headers=api.headers)

    # 4.查询员工
    def api_get_employee(self):
        # 1.调用get方法 ->返回响应数据
        log.info("查询员工请求url:{} 查询员工请求信息头{}".format(self.url.format(api.user_id), api.headers))
        return requests.get(url=self.url.format(api.user_id), headers=api.headers)

    # 5.删除员工
    def api_delete_employee(self):
        log.info("删除员工请求url:{} 删除员工请求信息头：{}".format(self.url.format(api.user_id),api.headers))
        # 1.调用delete 方法 ->返回响应数据
        return requests.delete(url=self.url.format(api.user_id), headers=api.headers)