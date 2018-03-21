import unittest
import json
import requests
from driver import myunit

class resetPasswordtest(myunit.MyTest):

    """用户忘记密码是凭邮箱中的验证码重置密码"""

    base_url = myunit.MyTest.base_url+"resetPassword"

    def test_resetPassword_SetVercodeSUCCESS(self):

        payload = {"username":"nn.chen@yuneec.com","newPassword":"789012",
                   "verCode":"905531"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10000")
