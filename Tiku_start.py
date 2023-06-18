import re
from turtle import pen
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from Tiku_addjson import ti_add
import os,json
from selenium.webdriver.common.by import By

#答题 与获取题库共用配置文件

def selenium_start():
    global driver
    chromeOptions = webdriver.ChromeOptions()

    WIDTH = 400
    HEIGHT = 650
    PIXEL_RATIO = 3.0
    UA = "Mozilla/5.0 (Linux; Android 11; Redmi K30 5G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3211 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/6973 MicroMessenger/8.0.7.1920(0x28000753) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64"
    mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio":PIXEL_RATIO}, "userAgent": UA}
    chromeOptions.add_experimental_option('mobileEmulation',mobileEmulation)
    chromeOptions.add_argument("--auto-open-devtools-for-tabs")
    chromeOptions.add_argument("--mute-audio")
    #chromeOptions.add_argument('user-agent="Mozilla/5.0 (Linux; Android 11; Redmi K30 5G Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3211 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/6973 MicroMessenger/8.0.7.1920(0x28000753) Process/toolsmp WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64"')

    driver = webdriver.Chrome(chrome_options=chromeOptions)
    #插入cookie需要与cookie相同的页面的域名，下面这个链接不需要登录就能打开
    driver.get(f"https://19276789-{Tiku_url_shu}.hd.ysfaisco.cn")
    try:
        driver.add_cookie(cookie_dict=cook1)
        driver.add_cookie(cookie_dict=cook2)
        driver.add_cookie(cookie_dict=cook3)
        driver.add_cookie(cookie_dict=cook4)
        driver.add_cookie(cookie_dict=cook5)
        driver.add_cookie(cookie_dict=cook6)
        driver.add_cookie(cookie_dict=cook7)
        driver.add_cookie(cookie_dict=cook8)
        driver.add_cookie(cookie_dict=cook9)
        #driver.add_cookie(cookie_dict=cook10)
        driver.add_cookie(cookie_dict=cook11)
        driver.add_cookie(cookie_dict=cook12)
    except:
        pass
    #插完后需要刷新，就是登录状态
    driver.refresh()

    driver.get(Tiku_url)

#初始化 从配置文件里导入用户cookie与一些基本信息
def intst():
    global cook1,cook2,cook3,cook4,cook5,cook6,cook7,cook8,cook9,cook10,cook11,cook12,file,Tiku_name,Tiku_url,Tiku_url_shu,intlat_by_sjk,intlat_json_sjk,Tiku_start_time
    weizhi = os.path.dirname(os.path.abspath(__file__))
    with open(weizhi+"/Tiku_user.json","r",encoding="utf-8") as f:
        intlat_by = f.read()
    intlat_json = json.loads(intlat_by)
    try:
        cook1 = {"name":intlat_json["cook1"][0]["name"],"value":intlat_json["cook1"][0]["value"]}
        cook2 = {"name":intlat_json["cook2"][0]["name"],"value":intlat_json["cook2"][0]["value"]}
        cook3 = {"name":intlat_json["cook3"][0]["name"],"value":intlat_json["cook3"][0]["value"]}
        cook4 = {"name":intlat_json["cook4"][0]["name"],"value":intlat_json["cook4"][0]["value"]}
        cook5 = {"name":intlat_json["cook5"][0]["name"],"value":intlat_json["cook5"][0]["value"]}
        cook6 = {"name":intlat_json["cook6"][0]["name"],"value":intlat_json["cook6"][0]["value"]}
        cook7 = {"name":intlat_json["cook7"][0]["name"],"value":intlat_json["cook7"][0]["value"]}
        cook8 = {"name":intlat_json["cook8"][0]["name"],"value":intlat_json["cook8"][0]["value"]}
        cook9 = {"name":intlat_json["cook9"][0]["name"],"value":intlat_json["cook9"][0]["value"]}
        #cook10 = {"name":intlat_json["cook10"][0]["name"],"value":intlat_json["cook10"][0]["value"]}
        cook11 = {"name":intlat_json["cook11"][0]["name"],"value":intlat_json["cook11"][0]["value"]}
        cook12 = {"name":intlat_json["cook12"][0]["name"],"value":intlat_json["cook12"][0]["value"]}
    except:
        pass
    file = intlat_json["file"]
    Tiku_name = intlat_json["Tiku_name"]
    Tiku_url = intlat_json["Tiku_url"]
    Tiku_url_shu = intlat_json["Tiku_url_shu"]
    Tiku_start_time = intlat_json["Tiku_start_time"]
    print("          答题系统 selenium版             ")
    print("仅供学习,请在24小时内删除！")
    print("此程序造成的任何后果请自行承担,本作者不承担任何法律责任")
    print("需要配合相应的chromedriver.exe版本使用")
    print("联系方式：lanzeweie@foxmail.com")
    print("\n")
    print("如果闪退则是没有chromedriver.exe或者版本不匹配chrome")
    print("chromedriver.exe下载地址：")
    print("https://chromedriver.storage.googleapis.com/index.html")
    print("\n")
    print("-----------------配置------------------")
    print("用户信息Tiku_user.json  题目数据库json\\")
    print("\n\n\n")
    print(f"题库名：{Tiku_name}")
    print(f"题库位置：{file}")
    with open(weizhi+file,"r",encoding="utf-8") as f:
        intlat_by_sjk = f.read()
    intlat_json_sjk = json.loads(intlat_by_sjk)

def start(now_timu):
    daan_shujuku = alter(now_timu)[1]
    if daan_shujuku == "":
        return {"题库系统":"题库中有相同题目，但答案未匹配"}
    if daan_shujuku == None:
        return {"题库系统":"没能查询到此题"}
    else:
        daan_1 = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]/div').text
        daan_2 = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[2]/div').text
        daan_3 = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[3]/div').text
        daan_4 = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[4]/div').text
        if daan_shujuku == daan_1:
            driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]/div').click()
            return {"题库系统":"成功查询到此题"},daan_shujuku
        if daan_shujuku == daan_2:
            driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[2]/div').click()
            return {"题库系统":"成功查询到此题"},daan_shujuku
        if daan_shujuku == daan_3:
            driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[3]/div').click()
            return {"题库系统":"成功查询到此题"},daan_shujuku
        if daan_shujuku == daan_4:
            driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[4]/div').click()
            return {"题库系统":"成功查询到此题"},daan_shujuku
        else:
            daan_sjk_erci = [daan_1,daan_2,daan_3,daan_4]
            #date = ' '.join(daan_sjk_erci)

            daan_shujuku_2 = alter_start(daan_sjk_erci)[1]

            if daan_shujuku_2 == "":
                return {"题库系统":"题库中有相同题目，但答案未匹配"}
            if daan_shujuku_2 == None:
                return {"题库系统":"没能查询到此题"}
            else:
                if daan_shujuku_2 == daan_1:
                    driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]/div').click()
                    return {"题库系统":"成功查询到此题"},daan_shujuku
                if daan_shujuku_2 == daan_2:
                    driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[2]/div').click()
                    return {"题库系统":"成功查询到此题"},daan_shujuku
                if daan_shujuku_2 == daan_3:
                    driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[3]/div').click()
                    return {"题库系统":"成功查询到此题"},daan_shujuku
                if daan_shujuku_2 == daan_4:
                    driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[4]/div').click()
                    return {"题库系统":"成功查询到此题"},daan_shujuku

#查询数据库
def alter(now_timu):
    start_time = time.time()
    
    title_timu = now_timu
    if intlat_json_sjk["name"] == Tiku_name:
        shu = len(intlat_json_sjk["Tiku"])
        for chaxun in range(shu):
            title_tiku = (intlat_json_sjk["Tiku"][chaxun]["title"])
            if title_timu == title_tiku:
                end_time = time.time()
                print("耗时: {:.3f}秒".format(end_time - start_time))
                daan = (intlat_json_sjk["Tiku"][chaxun]["answer"])
                print(f"题目：{title_timu}")
                return {"题库系统":"成功查询到此题"},daan
            else:
                continue
        end_time = time.time()
        print("从数据库查找耗时: {:.3f}秒".format(end_time - start_time))
        print(f"题目：{title_timu}")
        return {"题库系统":"没能查询到此题"},None

def alter_start(date):
    print(date)
    for cishu in date:
        print(cishu)
        start_time = time.time()
        title_timu = now_timu
        if intlat_json_sjk["name"] == Tiku_name:
            shu = len(intlat_json_sjk["Tiku"])
            for chaxun in range(shu):
                title_tiku = (intlat_json_sjk["Tiku"][chaxun]["title"])
                if title_timu == title_tiku:
                    Tiku_daan = (intlat_json_sjk["Tiku"][chaxun]["answer"])
                    if Tiku_daan == cishu:
                        end_time = time.time()
                        print("耗时: {:.3f}秒".format(end_time - start_time))
                        print(f"题目：{title_timu}")
                        return {"题库系统":"成功查询到此题"},cishu
                else:
                    continue
    end_time = time.time()
    print("从数据库查找耗时: {:.3f}秒".format(end_time - start_time))
    print(f"题目：{title_timu}")
    return {"题库系统":"没能查询到此题"},None
#启动
intst()
time.sleep(5)
selenium_start()
while True:
    try:
        kaishi = driver.find_element(By.XPATH, '//*[@id="startBtnImg"]').get_attribute('class')
    except:
        continue
    try:
        ActionChains(driver).move_by_offset(200, 100).click().perform()
    except:
        pass
    if kaishi == "slaveImg abs startTada":
        driver.find_element(By.XPATH, '//*[@id="startBtnImg"]').click()
        break
#运作主函数
#运行方式 
while True:
    now_tishu = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[3]/div/span[1]').text
    if len(now_tishu) >= 1:
        if now_tishu == "15":
            while True:
                now_time = driver.find_element(By.XPATH, '//*[@id="gameTopBar"]/div[2]/span').text
                shengyu = 300 - float(now_time)
                shengyu2 = 300 - shengyu
                os.system("cls")
                shengyu_format = "{:.3f}".format(shengyu)
                print(f"等待到达预定时间 {shengyu2} 预定时间 {Tiku_start_time} 当前所花时间 {shengyu_format}")
                if shengyu2 <= 300 - float(Tiku_start_time):
                    now_timu = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[1]').text
                    print(start(now_timu))
                    break
            break
    else:
        continue

    try:
        daan_1_start = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]').text
    except:
        continue
    if len(daan_1_start) >= 1:
        
        now_timu = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[1]').text
        print(start(now_timu))

        while True:
            if now_timu == driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[1]').text:
                continue
            else:
                break
input("按下任何按键退出")




