import os,json

#去数据库中的重复项
#并写入文件中

#目标文件
files = "/json/Tiku_C.json"
#修改后的文件
files_x = "\json\w.json"

weizhi = os.path.dirname(os.path.abspath(__file__))
with open(weizhi+files,"r",encoding="utf-8") as f:
        intlat_by = f.read()
        intlat_json = json.loads(intlat_by)




alter_json_all = str(intlat_json["Tiku"])

alter_json_all = alter_json_all.strip().strip('[]')
alter_json_all_ = eval(alter_json_all)
alter_json_all = { each['date'] : each for each in alter_json_all_ }.values()
intlat_json_write = json.dumps(list(alter_json_all),indent=4,ensure_ascii=False)
with open(weizhi+files_x,"w",encoding="utf-8") as alter:
        alter.write(intlat_json_write)
print(f"成功合并,输出文件位置\n{weizhi}{files_x}")