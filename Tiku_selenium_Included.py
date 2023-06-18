from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from Tiku_addjson import ti_add
from selenium.webdriver.common.by import By
import os,json

#收录题库系统
#此题库收集系统利用 每次答题会纠正错误  使用selenium 去捕捉 纠正错误的 标签 就可以查询到正确答案 并且收录到数据库中
#此方案 每一次最多收录14道题 且需要人工辅助
#优点 正确率100%
#缺点 效率极慢

def selenium_start():
    global driver
    chromeOptions = webdriver.ChromeOptions()

    WIDTH = 400
    HEIGHT = 650
    PIXEL_RATIO = 3.0
    UA = "Mozilla/5.0 (Linux; Android 13; 22081212C Build/TKQ1.220829.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.36 XWEB/5023 MMWEBSDK/20230303 MMWEBID/6973 MicroMessenger/8.0.34.2340(0x2800225B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64"
    mobile_emulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO}, "userAgent": UA}
    chromeOptions.add_experimental_option("mobileEmulation", mobile_emulation)
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

#寻题函数
#回答题目后会获得 正确与错误的验证，此时正确与错误分别会比其他答案多出一个div  再通过 正确与错误的标签判断 得出正确答案
def answer():
    try:
        daan_1 = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]/div[2]').text
        daan_1_p = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]/div[2]').get_attribute('class')
        if daan_1_p == "questionAnswer questionAnswer_right":
                return daan_1
    except:
            pass

    try:
        daan_2 = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[2]/div[2]').text
        daan_2_p = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[2]/div[2]').get_attribute('class')
        if daan_2_p == "questionAnswer questionAnswer_right":
                return daan_2
    except:
            pass
    try:
        daan_3 = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[3]/div[2]').text
        daan_3_p = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[3]/div[2]').get_attribute('class')
        if daan_3_p == "questionAnswer questionAnswer_right":
                return daan_3
    except:
            pass
    try:
        daan_4 = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[4]/div[2]').text
        daan_4_p = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[4]/div[2]').get_attribute('class')
        if daan_4_p == "questionAnswer questionAnswer_right":
                return daan_4
    except:
            return None

#收集题库 答案列表 用作收集 万一那天就用上了
def answer_list():
    answer_list_shouji = []
    try:
        answer_list_shouji.append(driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]').text)
        answer_list_shouji.append(driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[2]').text)
        answer_list_shouji.append(driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[3]').text)
        answer_list_shouji.append(driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[4]').text)
    except:
        return answer_list_shouji
    return answer_list_shouji

#初始化 从配置文件里导入用户cookie与一些基本信息
def intst():
    global cook1,cook2,cook3,cook4,cook5,cook6,cook7,cook8,cook9,cook10,cook11,cook12,file,Tiku_name,Tiku_url,Tiku_url_shu
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
    print("          题库收集系统 selenium版             ")
    print("仅供学习,请在24小时内删除！")
    print("此程序造成的任何后果请自行承担,本作者不承担任何法律责任")
    print("需要配合相应的chromedriver.exe版本使用")
    print("联系方式：lanzeweie@foxmail.com")
    print("\n")
    print("如果闪退则是没有chromedriver.exe或者版本不匹配chrome")
    print("chromedriver.exe下载地址：")
    print("https://chromedriver.storage.googleapis.com/index.html")
    print("\n\n\n")
    print(f"题库数：{Tiku_url_shu}")
    print(f"题库名：{Tiku_name}")
    print(f"题库位置：{file}")
    print(f"题库链接：{Tiku_url}")


#初始化 重复次数与收录题数
cfcs = 0
shoulu_OK = 0
shoulu_NO = 0
shoulu_Error = 0
#启动
intst()
time.sleep(5)
selenium_start()

while True:
    try:
        kaishi = driver.find_element(By.XPATH, '//*[@id="tip_txt"]/p[1]').text
    except:
        continue
    try:
        ActionChains(driver).move_by_offset(200, 100).click().perform()
    except:
        pass
    if kaishi == "提示":
        try:
            driver.find_element(By.XPATH, '//*[@id="startBtnImg"]').click()
            break
        except:
            continue
#运作主函数
#运行方式 判断题目数没有则重新来，有题目数后开始判断是否刷出答案选项，选择后开始收录答案 循环
while True:
    try:
        errow = driver.find_element(By.XPATH, '//*[@id="resule-status-scrollWrap"]/div[3]/div[4]/div[1]/div[3]/span').text
        if errow == "再试一次":
             driver.refresh()
    except:
         pass
    now_tishu = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[3]/div/span[1]').text
    if len(now_tishu) >= 1:
        if now_tishu == "14":
            cfcs = cfcs+1
            print(f"重复第{cfcs}次")
            #driver.quit()
            time.sleep(0.5)
            driver.refresh()
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
    else:
        continue

    try:
        daan_1_start = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]').text
    except:
        continue
    if len(daan_1_start) >= 1:
        try:
            driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[3]/div[1]/div').click()
        except:
            pass
        answer_ti = answer()

        now_timu = driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[1]').text
        if answer_ti is None:
            continue
        if len(answer_ti) >=1:
            print(f"题目：{now_timu}")
            print(f"答案：{answer_ti}")
            #将题收录文本
            
            answer_list_lu = answer_list()
            try:
                back_add = ti_add.alter(now_timu,answer_list_lu,file,Tiku_name,answer_ti)
                if back_add[1] == "OK":
                    shoulu_OK+=1
                else:
                    shoulu_NO+=1
                    print(back_add)
                    print(f"本次运行收录总题数：{shoulu_OK+shoulu_NO+shoulu_Error} 道，成功收录：{shoulu_OK} 道，重复收录：{shoulu_NO} 道，收录失败：{shoulu_Error} 道")
            except:
                print("题与分析系统发生冲突，跳过此题")
                shoulu_Error+=1

    
        while True:
            if now_timu == driver.find_element(By.XPATH, '//*[@id="gameLayerBox"]/div[1]/div/div[1]').text:
                continue
            else:
                break




