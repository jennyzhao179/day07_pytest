import unittest

from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts", pattern="test*.py")
with open("./report/ihrm_report.html", "wb") as f:
    HTMLTestRunner(stream=f).run(suite)