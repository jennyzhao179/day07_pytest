from tools.get_log import GetLog

log = GetLog.get_logger()
def assert_common(self, response, status_code=200, success=True, code=10000, message="操作成功！" ):
    """

    :param self: TestCase 实例
    :param response: 响应对象

    """
    try:
        r = response.json()
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(success, r.get("success"))
        self.assertEqual(code, r.get("code"))
        self.assertEqual(message, r.get("message"))
    except Exception as e:
        log.error(e)
        raise