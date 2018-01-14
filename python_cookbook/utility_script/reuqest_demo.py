
import json
import random

import requests
import time


#
# domain = "http://127.0.0.1:"
# port = "8080"
#
# prefix ="/demo"
#
# url_router_1 = "/hello"
#
# url_router_2 ="/world"
#
# url_router_3 = "/code"
#
# url_router_4="/more"
#
# url1 =domain+port+prefix+url_router_1
#
#
# headers={"user-agent":"Moliza webkit"}
#
# payload ={"msg":"我靠那个人好像个大傻瓜"}
# print(url1)
# res = requests.get(url1,payload,headers=headers)
# print(res.text)
# print(res.json())
# print(res.status_code)
#
# print(res.headers.get('content-type'))
#
# url2 = domain+port+prefix+url_router_2
# payload={"msg":"DVA爱你哟"}
# res = requests.put(url2,payload)
# print("DVA爱你哟")
# print(res.text)
#
# parsed_json =json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
# print(parsed_json)
# cookie_info = dict(jsessionid="1123",username ="yanjinbin")
# res = requests.get(url2,params=payload,cookies=cookie_info)
# print(res.cookies.get("username"))
#
#
# print(random.randint(1,10))
# print(int(time.time()))
#
#
#
# class Person(json.JSONEncoder):
#     version = 0.1
#     def __init__(self):
#         self.version =2.0
#         print("version",self.version)
#
#     def show_name(self,msg):
#         print("MSG IS \t\t",msg)
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__,
#                           sort_keys=True, indent=4)
#     def default(self, o):
#         if isinstance(o, Person):
#             return str(o.version)
#         return json.JSONEncoder.default(self, o)




cookie_info ="_AJSESSIONID=d6a833b0f73e11e79ed8522233007f8a; username=yanjinbin; sso_local_sign=3573961c8ffd449f5fa73c9c60b6afba4099b53a"

url_up = "http://up-profit.bilibili.co/cooperate/api/web_api/v1/agent?page=1&size=10&test_account=1&rand=1515723554452"
header_up={'cookie':cookie_info}
proxy_ip = {'http': '172.18.35.12'}
res = requests.get(url_up, headers=header_up, proxies=proxy_ip)
print(res.json())
print(json.dump(res.content, indent=4))

# # 上传文件
# file= {
#     'image':open('simple.jpg','rb'),
# }
# requests.post('http:localhost:8080',files=file)