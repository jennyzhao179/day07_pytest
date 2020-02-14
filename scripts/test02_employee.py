import unittest

import api
from api.api_employee import ApiEmployee
from tools.assert_common import assert_common
from parameterized import parameterized

from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log= GetLog.get_logger()

class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.api = ApiEmployee()
    @parameterized.expand(read_yaml("emloyee_post.yaml"))
    def test01_post(self, username, mobile, workNumber):
        r = self.api.api_post_employee(username, mobile, workNumber)
        assert_common(self,r)
        log.info("新增员工结果为：{}".format(r.json()))
        api.user_id = r.json().get("data").get("id")
        print("员工user_id的值为", api.user_id)
        log.info("新增员工后提取的员工id为{}".format(api.user_id))

    def test02_put(self):
        r = self.api.api_put_employee()
        log.info("更新员工结果为{}".format(r.json()))
        assert_common(self, r)
    def test03_get(self):
        r = self.api.api_get_employee()
        log.info("查询员工结果为{}".format(r.json()))
        assert_common(self, r)
    def test04_delete(self):
        r = self.api.api_delete_employee()
        print("删除结果为： ", r.json())
        log.info("删除员工结果为{}".format(r.json()))
        assert_common(self,r)