#!/usr/bin/env python

def mockFoo():
    mockData={
        "request" :{
            "json":{
                "username": "nn.chen@yuneec.com",
                "password":"a1234567890"
            }

        },

        "response":{
            "message": "10000",
            "status": "success",
            "data": {
                "headIcon": "https://ycob.oss-us-west-1.aliyuncs.com/20180131/172413169-FD9FCAB23B764DB69AD785944A46277F.png",
                "token": "C605E2F21E3770476783B46DDD8D301A",
                "nickname": "mock_tt",
                "province": "",
                "userid": 16086,
                "gender": "1",
                "grade": 0,
                "lastname": "tt",
                "firstname": "tt",
                "city": "",
                "country":""
            }
        }
}
    return mockData.get("response")
# print(mockFoo())