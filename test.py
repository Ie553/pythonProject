import requests
import random,string
from requests_toolbelt import MultipartEncoder


url = "https://capi.tianyancha.com/cloud-third-party/batch/search/import"

# files = {
#     # 'name': ('file', ,'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')),
#     'filename': ('7.xlsx',open(r'C:\Users\joy\Desktop\商标网项目\导天眼查\7.xlsx', 'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
# }
fields = {
    'file': (r'C:\Users\joy\Desktop\商标网项目\导天眼查\1.xlsx', open(r"C:\Users\joy\Desktop\商标网项目\导天眼查\1.xlsx", "rb"), "xlsx"),
}
# 因为16位数随机的，每次都不一样
boundary = '----WebKitFormBoundary' \
           + ''.join(random.sample(string.ascii_letters + string.digits, 16))
print(boundary)
m = MultipartEncoder(fields=fields, boundary=boundary)
headers = {
    "Content-Type": m.content_type
}

headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    # 'Content-Length':'68579',
    'Content-Type':f'multipart/form-data; boundary={boundary}',
    'Cookie':'TYCID=05a6a590b32611edbd3563314b2a71a4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2236043377%22%2C%22first_id%22%3A%221867c35b919258-03ccf0c267cdfe8-74525476-2073600-1867c35b91ab90%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg2N2MzNWI5MTkyNTgtMDNjY2YwYzI2N2NkZmU4LTc0NTI1NDc2LTIwNzM2MDAtMTg2N2MzNWI5MWFiOTAiLCIkaWRlbnRpdHlfbG9naW5faWQiOiIzNjA0MzM3NyJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2236043377%22%7D%2C%22%24device_id%22%3A%221867c35b919258-03ccf0c267cdfe8-74525476-2073600-1867c35b91ab90%22%7D; ssuid=2550186940; _ga=GA1.2.272775012.1677121163; jsid=http%3A%2F%2Fwww.tianyancha.com%2F%3Fjsid%3DSEM-BAIDU-PZ-SY-2021112-JRGW; show_activity_id_92=92; tyc-user-info=%7B%22state%22%3A%225%22%2C%22vipManager%22%3A%220%22%2C%22mobile%22%3A%2218608162300%22%2C%22isExpired%22%3A%220%22%7D; tyc-user-info-save-time=1679892068946; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwODE2MjMwMCIsImlhdCI6MTY3OTg5MjA2NywiZXhwIjoxNjgyNDg0MDY3fQ.OCbVlvHj0_qxWOS0q_OWwR9KxxCZHscCOwCIit0eZV--BKTLQJmp2AOhA8BNN0a3Mmy0am2FvSwu72IZDiiOSA; _gid=GA1.2.529253867.1679892075; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1679892057,1679920699; bannerFlag=true; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1679920703; HWWAFSESID=0e70fc01e39adbeb032; HWWAFSESTIME=1679920709543',
    'Host':'capi.tianyancha.com',
    'Origin':'https://www.tianyancha.com',
    'Pragma':'no-cache',
    'Referer':'https://www.tianyancha.com/',
    'sec-ch-ua':'"Microsoft Edge";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"Windows"',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-site',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54',
    'version':'TYC-Web',
    'X-AUTH-TOKEN':'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODYwODE2MjMwMCIsImlhdCI6MTY3OTg5MjA2NywiZXhwIjoxNjgyNDg0MDY3fQ.OCbVlvHj0_qxWOS0q_OWwR9KxxCZHscCOwCIit0eZV--BKTLQJmp2AOhA8BNN0a3Mmy0am2FvSwu72IZDiiOSA',
}

req = requests.post(url=url, headers=headers,
             data=m)
print(req.request.body)
print(req.text)