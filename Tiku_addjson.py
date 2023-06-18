# -*- coding:utf-8 -*-
import json,os

#修改 题库 json数据库 添加新题，比较题目 题目相同判断答案
#传入参数 title_timu,date,files,tiku | 题目 答案列表 文件位置 题库 答案 

class ti_add():
    #查询数据库，没有则添加
    def alter(title_timu,date,files,tiku,answer_da):
        if answer_da == None:
            kong = ""
        elif len(answer_da) >=1:
            kong = answer_da
        ## 此块为垃圾代码，为了节约脑力，索性每次启动都要读取一次文本
        weizhi = os.path.dirname(os.path.abspath(__file__))
        with open(weizhi+files,"r",encoding="utf-8") as f:
            intlat_by = f.read()
        intlat_json = json.loads(intlat_by)
        ## ↑↑垃圾代码
        print(weizhi+files)
        if isinstance(date,list) is True:     
            date = ' '.join(date)
        if intlat_json["name"] == tiku:
            shu = len(intlat_json["Tiku"])
            for chaxun in range(shu):
                title_tiku = (intlat_json["Tiku"][chaxun]["title"])
                if title_timu == title_tiku:
                    title_answer = (intlat_json["Tiku"][chaxun]["answer"])
                    print(intlat_json["Tiku"][chaxun]["title"])
                    if title_answer == kong:
                        return {"题库系统":"数据库有这个题"+"当前题库数量："+str(shu)},"NO"
                #出现不知名bug ： "" 内信息 仍被强赋值 使用笨办法 让被强赋值的值的强赋值等于值
                #笨办法依靠bug运行
            alter_json_all = str(intlat_json["Tiku"])
            alter_json_all = alter_json_all.strip().strip('[]')
            name_qiangfuzhi = "title"
            date_qiangfuzhi = "date"
            answer_qianfuzhi = "answer"
            alter_json_all += ",{" + "name_qiangfuzhi" + ":'" + title_timu + "'," + "date_qiangfuzhi" + ":'" + date + "'," + "answer_qianfuzhi" + ":'" + kong + "'}"
            alter_json_all_ = eval(alter_json_all)
            intlat_json["Tiku"] = alter_json_all_
            intlat_json_write = json.dumps(intlat_json,indent=4,ensure_ascii=False)
            with open(weizhi+files,"w",encoding="utf-8") as alter:
                alter.write(intlat_json_write)
            shu=+1
            return {"题库系统":"成功添加"+(title_timu)+"至数据库"+"当前题库数量："+str(shu)},"OK"

#             alter_json_all += ",{" + "name_qiangfuzhi" + ":'" + title_timu + "'," + "date_qiangfuzhi" + ":'" + date + "'}"

if __name__ == "__main__":
    title_timu = "你好aaaa"
    date = "测试 呀呀131231232"
    file = "/json/Tiku_ppt.json"
    tiku = "桥帮主读书日ppt题库"
    answer_da = "呀呀呐221694123124120"
    start = ti_add.alter(title_timu,date,file,tiku,answer_da)
    print(start)