# -*- coding:utf-8 -*-
import os
from Tiku_addjson import ti_add
import requests,json
import time

#收录题库系统
#此题库收集系统利用  官方的API接口   每次调用都有不一样的题目   并且收集到题库中
#优点 效率极高 实测 120秒可以收录500道题
#缺点 没有答案 需要人工手动答题 ，且不能保证正确率


hand = {
    "host":"19276789-157.hdpyqd.com",
    "content-length":"730",
    "accept":"*/*",
    "content-type":"application/x-www-form-urlencoded; charset=UTF-8",
    "x-requested-with":"XMLHttpRequest",
    "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36",
    "sec-ch-ua-platform":"Android",
    "origin":"https://19276789-157.hdpyqd.com",
    "referer":"https://19276789-157.hdpyqd.com/19276789/Gsye5pFz5J30acjVeGRZLw/nldtz.html?appid=wx50775cad5d08d7ad&editQrcode=true&_source=1&fromQrcode=true&canal=-1&canal=-1",
}

body = "questionObj=%7B%22gameId%22%3A157%2C%22req_Type%22%3A%22get%22%2C%22isManage%22%3Afalse%2C%22titleIndex%22%3Anull%2C%22playerAnswer%22%3Anull%2C%22qtInfoParam%22%3A%7B%22exposure_QtList%22%3A%5B170%5D%2C%22score_Qt%22%3A%7B%22score%22%3A0%2C%22encryptScore%22%3A%2274500d2ba12b8a449a19736ad509541c%22%7D%2C%22qtNum%22%3A15%2C%22qtScore%22%3A10%2C%22moreAnswer%22%3Afalse%2C%22allAnswerList%22%3A%5B%7B%22answer%22%3A%22%E9%94%99%E8%AF%AF%22%2C%22sign%22%3A%22d11bc10340ee2a0e5edd2bd6e1f0f630%22%7D%5D%2C%22r_List%22%3A%5B%7B%22answer%22%3A%22%E6%AD%A3%E7%A1%AE%22%2C%22sign%22%3A%2271d039db16d4f948647d5523a993d40a%22%7D%5D%2C%22analyze%22%3A%22%22%7D%2C%22openId%22%3A%22oosnVwoBokZk3QoPMuJEMc465j3I%22%2C%22isOrder%22%3Afalse%7D"

url = "https://19276789-160.hdpyqd.com/api/game4Qt/qtGame_Req?aid=19276789&canal=-1&playerOrigin=4&uid=&extra=&aid=19276789&gameId=160&_openId=oosnVwoBokZk3QoPMuJEMc465j3I"

file = "\json\http\Tiku_SPSS_http.json"
tiku = "桥帮主读书日SPSS题库"
shoulu_OK = 0
shoulu_NO = 0
shoulu_Error = 0
start_time = time.time()
for wx in range(2000):
    
    get_url = requests.post(url,headers=hand,data=body)

    #全部信息
    timu_now = json.loads(get_url.text)
    print(timu_now)
    #题目
    title_now = timu_now["data"]["title"]
    print(title_now)
    #选项
    #选项数
    allAnswerList_shu = len(timu_now["data"]["allAnswerList"])
    print(allAnswerList_shu)
    #选项列表
    allAnswerList_list = []
    for xuanx in range(allAnswerList_shu):
        allAnswerList_list.append(timu_now["data"]["allAnswerList"][xuanx]["answer"])
    print(allAnswerList_list)
    try:
        start = ti_add.alter(title_now,allAnswerList_list,file,tiku," ")
        if start[1] == "OK":
            shoulu_OK+=1
        else:
            shoulu_NO+=1
    except:
        print("题与系统发生冲突，收录失败")
        shoulu_Error+=1
    print(start)
print(f"本次运行收录总题数：{shoulu_OK+shoulu_NO+shoulu_Error} 道，成功收录：{shoulu_OK} 道，重复收录：{shoulu_NO} 道，收录失败：{shoulu_Error} 道")
end_time = time.time()
print("耗时: {:.2f}秒".format(end_time - start_time))