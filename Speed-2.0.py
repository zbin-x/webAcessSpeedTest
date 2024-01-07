import datetime
import requests
import csv

# this is set device type
DT = ["Mobile","Desktop"]
date = datetime.datetime.now().strftime('22-%m-%d-%H')
# this is url
urla = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
urlb = "&key=AIzaSyDj9IJ5vosj8t6MvNjzYykrHdZL8Ryo-yI"
urlmob = "&strategy=mobile"
# dict to store www name for display web_name at csv
web1 = {}
# dict to store www_name name for make long link by urls
webdict1 = {}
# dict for save date when testing
shopscore1 = {}
shoptime1 = {}
wwwscore1 = {}
wwwtime1 = {}

shop_list1 = ("https://shop.elephantrobotics.com/",
"https://shop.elephantrobotics.com/pages/tutorials",
"https://shop.elephantrobotics.com/blogs/news",
"https://shop.elephantrobotics.com/cart",
"https://shop.elephantrobotics.com/account/login",
"https://shop.elephantrobotics.com/collections/mycobot",
"https://shop.elephantrobotics.com/collections/holiday-special",
"https://shop.elephantrobotics.com/collections/mycobot",
"https://shop.elephantrobotics.com/collections/mycobot-accessories",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320",
"https://shop.elephantrobotics.com/collections/mycobot-pro-600",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320-accessories",
"https://shop.elephantrobotics.com/collections/mypalletize",
"https://shop.elephantrobotics.com/collections/mypalletizer-accessories",
"https://shop.elephantrobotics.com/collections/myagv",
"https://shop.elephantrobotics.com/collections/robotic-cat",
"https://shop.elephantrobotics.com/collections/bionic-cat-accessories",
"https://shop.elephantrobotics.com/collections/companion-cat",
"https://shop.elephantrobotics.com/collections/holiday-special/products/mycobot-320-pi-adaptive-gripper",
"https://shop.elephantrobotics.com/collections/holiday-special/products/holiday-mycobot-pi-raspberry-pi-powered-6-dof-collaborative-robot",
"https://shop.elephantrobotics.com/collections/holiday-special/products/holliday-special-mypalletizer-gift-box",
"https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-worlds-smallest-and-lightest-six-axis-collaborative-robot",
"https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-pi-worlds-smallest-and-lightest-six-axis-collaborative-robot",
"https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-280-for-arduino-6-dof-collaborative-robot",
"https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-280-jetson-nano",
"https://shop.elephantrobotics.com/collections/mycobot-accessories/products/mycobot-artificial-intelligence-kit",
"https://shop.elephantrobotics.com/collections/mycobot-accessories/products/mycobot-adaptive-gripper",
"https://shop.elephantrobotics.com/collections/mycobot-accessories/products/mycobot-g-shape-base",
"https://shop.elephantrobotics.com/collections/mycobot-accessories/products/mycobot-flat-base",
"https://shop.elephantrobotics.com/collections/mycobot-accessories/products/mycobot-suction-pump",
"https://shop.elephantrobotics.com/collections/mycobot-accessories/products/mycobot-camera-flange",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/commercial-and-economic-six-axis-collaborative-robot",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/mycobot-pro-raspberry-pi",
"https://shop.elephantrobotics.com/collections/mycobot-pro-600/products/mycobot-pro-600-2kg-payload-commercial-6-dof-cobot",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320-accessories/products/electric-parallel-gripper",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320-accessories/products/mycobot-pro-adaptive-gripper",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320-accessories/products/vacuum-suction-cups-air-compressor",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320-accessories/products/air-parallel-grippers-air-compressor",
"https://shop.elephantrobotics.com/collections/mycobot-pro-320-accessories/products/mycobot-pro-soft-gripper",
"https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer",
"https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer-260-raspberrypi-4-axis-robotic-arm",
"https://shop.elephantrobotics.com/collections/mypalletizer-accessories/products/mypalletizer-suction-pump",
"https://shop.elephantrobotics.com/collections/mypalletizer-accessories/products/mypalletizer-adaptive-gripper",
"https://shop.elephantrobotics.com/collections/mypalletizer-accessories/products/mypalletizer-g-shape-base",
"https://shop.elephantrobotics.com/collections/mypalletizer-accessories/products/mypalletizer-camera-flange",
"https://shop.elephantrobotics.com/collections/myagv/products/myagv",
"https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot",
"https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-bowl",
"https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/elephant-robotics-marscat-charger-station",
"https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-neck",
"https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-tail",
"https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-ears",
"https://shop.elephantrobotics.com/collections/companion-cat/products/metacat",
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39585938833494',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39587435642966',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39585940996182',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39585943978070',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39763820740694',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-pi-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39585945649238',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-pi-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39763826901078',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-pi-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39585945682006',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-pi-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39585945714774',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-pi-worlds-smallest-and-lightest-six-axis-collaborative-robot?variant=39611098693718',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-280-for-arduino-6-dof-collaborative-robot?variant=39768060919894',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-280-for-arduino-6-dof-collaborative-robot?variant=39768060985430',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-280-for-arduino-6-dof-collaborative-robot?variant=39768061018198',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-280-jetson-nano?variant=39763793084502',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-280-jetson-nano?variant=39763793150038',
'https://shop.elephantrobotics.com/collections/mycobot/products/mycobot-280-jetson-nano?variant=39763793182806',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/mycobot-pro-raspberry-pi?variant=39586309111894',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/mycobot-pro-raspberry-pi?variant=39586309144662',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/commercial-and-economic-six-axis-collaborative-robot?variant=39811192422486',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/commercial-and-economic-six-axis-collaborative-robot?variant=39811192455254',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/commercial-and-economic-six-axis-collaborative-robot?variant=39811273326678',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/commercial-and-economic-six-axis-collaborative-robot?variant=39811273359446',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320/products/commercial-and-economic-six-axis-collaborative-robot?variant=39811273392214',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320-accessories/products/vacuum-suction-cups-air-compressor?variant=39344447553622',
'https://shop.elephantrobotics.com/collections/mycobot-pro-320-accessories/products/air-parallel-grippers-air-compressor?variant=39344449847382',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer?variant=39586280734806',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer?variant=39586280767574',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer?variant=39780556144726',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer?variant=39780556177494',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer?variant=39780556210262',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer?variant=39586280800342',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer-260-raspberrypi-4-axis-robotic-arm?variant=39794538086486',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer-260-raspberrypi-4-axis-robotic-arm?variant=39794538119254',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer-260-raspberrypi-4-axis-robotic-arm?variant=39794538152022',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer-260-raspberrypi-4-axis-robotic-arm?variant=39794538184790',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer-260-raspberrypi-4-axis-robotic-arm?variant=39794538217558',
'https://shop.elephantrobotics.com/collections/mypalletize/products/mypalletizer-260-raspberrypi-4-axis-robotic-arm?variant=39794538250326',
'https://shop.elephantrobotics.com/collections/myagv/products/myagv?variant=39485298835542',
'https://shop.elephantrobotics.com/collections/myagv/products/myagv?variant=39485298868310',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39742746460246',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39742746493014',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39742746525782',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39742746689622',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39742746591318',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39742746624086',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39742746656854',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39741327081558',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39741326786646',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39741326884950',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39741326983254',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39741327474774',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39741327179862',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39741327278166',
'https://shop.elephantrobotics.com/collections/robotic-cat/products/marscat-a-bionic-cat-a-home-robot?variant=39741327376470',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-neck?variant=39422801608790',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-neck?variant=39422801641558',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-neck?variant=39422801674326',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-tail?variant=39422782832726',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-tail?variant=39422802362454',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-tail?variant=39422802559062',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-ears?variant=39422778179670',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-ears?variant=39422800625750',
'https://shop.elephantrobotics.com/collections/bionic-cat-accessories/products/marscat-ears?variant=39422800920662'
)
www_list1 = ("https://www.elephantrobotics.com",
"https://www.elephantrobotics.com/myCobot/",
"https://www.elephantrobotics.com/mycobot-RPi/",
"https://www.elephantrobotics.com/mycobot-280jetsonnano-cn/",
"https://www.elephantrobotics.com/mycobot-280arduino-cn/",
"https://www.elephantrobotics.com/artificial-intelligence-kit/",
"https://www.elephantrobotics.com/myagv/",
"https://www.elephantrobotics.com/mycobot-320-m5-cn/",
"https://www.elephantrobotics.com/mycobot-pro-pi/",
"https://www.elephantrobotics.com/mypalletizer-260-m5/cn",
"https://www.elephantrobotics.com/mypalletizer-260-pi/cn",
"https://www.elephantrobotics.com/marscat/",
"https://www.elephantrobotics.com/metacat/cn",
"https://www.elephantrobotics.com/catbot/",
"https://www.elephantrobotics.com/panda/",
"https://www.elephantrobotics.com/mycobot-pro-600/cn",
"https://www.elephantrobotics.com/robotic-module/",
"https://www.elephantrobotics.com/support/",
"https://www.elephantrobotics.com/download/",
"https://www.elephantrobotics.com/introduction/",
"https://www.elephantrobotics.com/elephant-blog/",
"https://www.elephantrobotics.com/join-us/",
"https://www.elephantrobotics.com/contact-us/"
             )
print(len(shop_list1))
print(len(www_list1))
# assign name to www1 shop1 and call easy
for i in range(len(shop_list1)):
    shop_names= (f"{shop_list1[i]}")

    web1[f'shop{i+1}']=shop_names
    shop_names = (f"{urla}"f"{shop_list1[i]}"f"{urlb}")
    webdict1[f'shop_name{i + 1}'] = shop_names

for i in range(len(www_list1)):
    www_names= (f"{www_list1[i]}")
    web1[f'www{i+1}']=www_names
    www_names = (f"{urla}"f"{www_list1[i]}"f"{urlb}")
    webdict1[f'www_name{i + 1}'] = www_names

# 请求地址 dict for get json
urls1 = {}
urlsm1 = {}
urlw1 = {}
urlwm1 = {}
rs1 = {}
rsm1 = {}
rw1 = {}
rwm1 = {}
speedsdict1 = {}
speedsdictm1 = {}
speedwdict1 = {}
speedwdictm1 = {}

# url ->r -> dict

for i in range(len(shop_list1)):
    urls = f"{webdict1[f'shop_name{i+1}']}"

    urls1[f'urlshop{i+1}'] = urls
    urlsm = f"{webdict1[f'shop_name{i+1}']}{urlmob}"
    urlsm1[f'urlshopm{i + 1}'] = urlsm
    rss = requests.get(urls1[f'urlshop{i+1}'])
    rs1[f'rshop{i+1}'] = rss
    rssm = requests.get(urlsm1[f'urlshopm{i+1}'])
    rsm1[f'rshopm{i+1}'] = rssm

    sdict1 = dict()
    sdict1 = (rs1[f'rshop{i+1}'].json())
    speedsdict1[f'shopspeed{i+1}'] = sdict1
    smdict1 = dict()
    smdict1 = (rsm1[f'rshopm{i+1}'].json())
    speedsdictm1[f'shopspeedm{i + 1}'] = smdict1
for i in range(len(www_list1)):
    urlw = f"{webdict1['www_name1']}"
    urlw1[f"urlwww{i+1}"] = urlw
    urlwm = f"{webdict1[f'www_name{i+1}']}{urlmob}"
    urlwm1[f"urlwwwm{i+1}"] = urlwm
    rww = requests.get(urlw1[f'urlwww{i+1}'])
    rw1[f'rwww{i+1}'] = rww
    rwwm = requests.get(urlwm1[f'urlwwwm{i+1}'])
    rwm1[f'rwwwm{i+1}'] = rwwm
    wdict1 = dict()
    wdict1 = (rw1[f'rwww{i+1}'].json())
    speedwdict1[f'wwwspeed{i+1}'] = wdict1
    wmdict1 = dict()
    wmdict1 = (rwm1[f'rwwwm{i+1}'].json())
    speedwdictm1[f'wwwspeedm{i + 1}'] = wmdict1

# ------------------next is shop-----------------------------
# 1.使用items()方法，取出字典中所有的键-值对，返回一个键值对列表
for i in range(len(shop_list1)):
    for key_1, value_1 in speedsdict1[f'shopspeed{i+1}'].items():
        # 2.打印每次循环遍历后返回的键值对数据
        if key_1 == "lighthouseResult" :
           # print(f"取出的key为：{key_1} ,取出的value为：{value_1}")

        # 3.使用 isinstance() 方法判断取出的 value 数据类型是否为：dict
            if isinstance(value_1, dict):
                #print("\n")
                # 4.对于获取到 dict 类型的 value 进行二次遍历，
                for key_2, value_2 in value_1.items():
                    # 5.打印每次循环遍历后返回的键值对数据
                    if key_2 == "categories" :
                        #print(f"嵌套字典取出的key为：{key_2} ,取出的value为：{value_2}")
                        if isinstance(value_2, dict):
                            #print("\n")
                            # 4.对于获取到 dict 类型的 value 进行二次遍历，
                            for key_3, value_3 in value_2.items():
                                # 5.打印每次循环遍历后返回的键值对数据
                                if key_3 == "performance":
                                    #print(f"嵌套字典取出的key为：{key_3} ,取出的value为：{value_3}")
                                    if isinstance(value_3, dict):
                                        # print("\n")
                                        # 4.对于获取到 dict 类型的 value 进行二次遍历，
                                        for key_4, value_4 in value_3.items():
                                            # 5.打印每次循环遍历后返回的键值对数据
                                            if key_4 == "score":
                                                value1 = value_4 * 100
                                                valuelast = int(value1)
                                                shopscore1[f'SC{i + 1}'] = valuelast
                                                print(f'SC{i + 1}')
                                                #print(f"Your Web speed score is : {shopsSCcore1}")
    for key_1, value_1 in speedsdict1[f'shopspeed{i+1}'].items():
        # 2.打印每次循环遍历后返回的键值对数据
        if key_1 == "loadingExperience" :
           # print(f"取出的key为：{key_1} ,取出的value为：{value_1}")
        # 3.使用 isinstance() 方法判断取出的 value 数据类型是否为：dict
            if isinstance(value_1, dict):
                #print("\n")
                # 4.对于获取到 dict 类型的 value 进行二次遍历，
                for key_2, value_2 in value_1.items():
                    # 5.打印每次循环遍历后返回的键值对数据
                    if key_2 == "metrics" :
                        #print(f"嵌套字典取出的key为：{key_2} ,取出的value为：{value_2}")
                        if isinstance(value_2, dict):
                            #print("\n")
                            # 4.对于获取到 dict 类型的 value 进行二次遍历，
                            for key_3, value_3 in value_2.items():
                                # 5.打印每次循环遍历后返回的键值对数据
                                if key_3 == "FIRST_CONTENTFUL_PAINT_MS":
                                    #print(f"嵌套字典取出的key为：{key_3} ,取出的value为：{value_3}")
                                    if isinstance(value_3, dict):
                                        # print("\n")
                                        # 4.对于获取到 dict 类型的 value 进行二次遍历，
                                        for key_4, value_4 in value_3.items():
                                            # 5.打印每次循环遍历后返回的键值对数据
                                            if key_4 == "percentile":
                                                value1 = value_4 / 1000
                                                valuelast = value1
                                                shoptime1[f'ST{i + 1}'] = valuelast
                                                #print(f'ST{i + 1}')
                                                #shoptime1 = value1  #int(value1)
                                                #print(f"Your Web speed time is : {shoptime1}")
    for key_1, value_1 in speedsdictm1[f'shopspeedm{i + 1}'].items():
        # 2.打印每次循环遍历后返回的键值对数据
        if key_1 == "lighthouseResult" :
           # print(f"取出的key为：{key_1} ,取出的value为：{value_1}")

        # 3.使用 isinstance() 方法判断取出的 value 数据类型是否为：dict
            if isinstance(value_1, dict):
                #print("\n")
                # 4.对于获取到 dict 类型的 value 进行二次遍历，
                for key_2, value_2 in value_1.items():
                    # 5.打印每次循环遍历后返回的键值对数据
                    if key_2 == "categories" :
                        #print(f"嵌套字典取出的key为：{key_2} ,取出的value为：{value_2}")
                        if isinstance(value_2, dict):
                            #print("\n")
                            # 4.对于获取到 dict 类型的 value 进行二次遍历，
                            for key_3, value_3 in value_2.items():
                                # 5.打印每次循环遍历后返回的键值对数据
                                if key_3 == "performance":
                                    #print(f"嵌套字典取出的key为：{key_3} ,取出的value为：{value_3}")
                                    if isinstance(value_3, dict):
                                        # print("\n")
                                        # 4.对于获取到 dict 类型的 value 进行二次遍历，
                                        for key_4, value_4 in value_3.items():
                                            # 5.打印每次循环遍历后返回的键值对数据
                                            if key_4 == "score":
                                                value1 = value_4 * 100
                                                valuelast = int(value1)
                                                shopscore1[f'SCm{i + 1}'] = valuelast
                                                #print(f'SCm{i + 1}')
                                                #shopscore1_1 = int(value1)
                                                #print(f"Your Web speed score is : {shopscore1_1}")
    for key_1, value_1 in speedsdictm1[f'shopspeedm{i + 1}'].items():
        # 2.打印每次循环遍历后返回的键值对数据
        if key_1 == "loadingExperience" :
           # print(f"取出的key为：{key_1} ,取出的value为：{value_1}")
        # 3.使用 isinstance() 方法判断取出的 value 数据类型是否为：dict
            if isinstance(value_1, dict):
                #print("\n")
                # 4.对于获取到 dict 类型的 value 进行二次遍历，
                for key_2, value_2 in value_1.items():
                    # 5.打印每次循环遍历后返回的键值对数据
                    if key_2 == "metrics" :
                        #print(f"嵌套字典取出的key为：{key_2} ,取出的value为：{value_2}")
                        if isinstance(value_2, dict):
                            #print("\n")
                            # 4.对于获取到 dict 类型的 value 进行二次遍历，
                            for key_3, value_3 in value_2.items():
                                # 5.打印每次循环遍历后返回的键值对数据
                                if key_3 == "FIRST_CONTENTFUL_PAINT_MS":
                                    #print(f"嵌套字典取出的key为：{key_3} ,取出的value为：{value_3}")
                                    if isinstance(value_3, dict):
                                        # print("\n")
                                        # 4.对于获取到 dict 类型的 value 进行二次遍历，
                                        for key_4, value_4 in value_3.items():
                                            # 5.打印每次循环遍历后返回的键值对数据
                                            if key_4 == "percentile":
                                                value1 = value_4 / 1000
                                                valuelast = value1
                                                shoptime1[f'STm{i + 1}'] = valuelast
                                                #print(f'STm{i + 1}')
                                                #shoptime1_1 = value1  #int(value1)
                                                #print(f"Your Web speed time is : {shoptime1_1}")

# ------------------next is www-----------------------------
for i in range(len(www_list1)):
    for key_1, value_1 in speedwdict1[f'wwwspeed{i+1}'].items():
        # 2.打印每次循环遍历后返回的键值对数据
        if key_1 == "lighthouseResult" :
           # print(f"取出的key为：{key_1} ,取出的value为：{value_1}")
        # 3.使用 isinstance() 方法判断取出的 value 数据类型是否为：dict
            if isinstance(value_1, dict):
                #print("\n")
                # 4.对于获取到 dict 类型的 value 进行二次遍历，
                for key_2, value_2 in value_1.items():
                    # 5.打印每次循环遍历后返回的键值对数据
                    if key_2 == "categories" :
                        #print(f"嵌套字典取出的key为：{key_2} ,取出的value为：{value_2}")
                        if isinstance(value_2, dict):
                            #print("\n")
                            # 4.对于获取到 dict 类型的 value 进行二次遍历，
                            for key_3, value_3 in value_2.items():
                                # 5.打印每次循环遍历后返回的键值对数据
                                if key_3 == "performance":
                                    #print(f"嵌套字典取出的key为：{key_3} ,取出的value为：{value_3}")
                                    if isinstance(value_3, dict):
                                        # print("\n")
                                        # 4.对于获取到 dict 类型的 value 进行二次遍历，
                                        for key_4, value_4 in value_3.items():
                                            # 5.打印每次循环遍历后返回的键值对数据
                                            if key_4 == "score":
                                                value1 = value_4 * 100
                                                valuelast = int(value1)
                                                wwwscore1[f'WC{i + 1}'] = valuelast
                                                print(f'WC{i + 1}')
                                                #print(f"Your Web speed score is : {shopsSCcore1}")
    for key_1, value_1 in speedwdict1[f'wwwspeed{i+1}'].items():
        # 2.打印每次循环遍历后返回的键值对数据
        if key_1 == "loadingExperience" :
           # print(f"取出的key为：{key_1} ,取出的value为：{value_1}")
        # 3.使用 isinstance() 方法判断取出的 value 数据类型是否为：dict
            if isinstance(value_1, dict):
                #print("\n")
                # 4.对于获取到 dict 类型的 value 进行二次遍历，
                for key_2, value_2 in value_1.items():
                    # 5.打印每次循环遍历后返回的键值对数据
                    if key_2 == "metrics" :
                        #print(f"嵌套字典取出的key为：{key_2} ,取出的value为：{value_2}")
                        if isinstance(value_2, dict):
                            #print("\n")
                            # 4.对于获取到 dict 类型的 value 进行二次遍历，
                            for key_3, value_3 in value_2.items():
                                # 5.打印每次循环遍历后返回的键值对数据
                                if key_3 == "FIRST_CONTENTFUL_PAINT_MS":
                                    #print(f"嵌套字典取出的key为：{key_3} ,取出的value为：{value_3}")
                                    if isinstance(value_3, dict):
                                        # print("\n")
                                        # 4.对于获取到 dict 类型的 value 进行二次遍历，
                                        for key_4, value_4 in value_3.items():
                                            # 5.打印每次循环遍历后返回的键值对数据
                                            if key_4 == "percentile":
                                                value1 = value_4 / 1000
                                                valuelast = value1
                                                wwwtime1[f'WT{i + 1}'] = valuelast
                                                #shoptime1 = value1  #int(value1)
                                                #print(f"Your Web speed time is : {shoptime1}")
    for key_1, value_1 in speedwdictm1[f'wwwspeedm{i + 1}'].items():
        # 2.打印每次循环遍历后返回的键值对数据
        if key_1 == "lighthouseResult" :
           # print(f"取出的key为：{key_1} ,取出的value为：{value_1}")
        # 3.使用 isinstance() 方法判断取出的 value 数据类型是否为：dict
            if isinstance(value_1, dict):
                #print("\n")
                # 4.对于获取到 dict 类型的 value 进行二次遍历，
                for key_2, value_2 in value_1.items():
                    # 5.打印每次循环遍历后返回的键值对数据
                    if key_2 == "categories" :
                        #print(f"嵌套字典取出的key为：{key_2} ,取出的value为：{value_2}")
                        if isinstance(value_2, dict):
                            #print("\n")
                            # 4.对于获取到 dict 类型的 value 进行二次遍历，
                            for key_3, value_3 in value_2.items():
                                # 5.打印每次循环遍历后返回的键值对数据
                                if key_3 == "performance":
                                    #print(f"嵌套字典取出的key为：{key_3} ,取出的value为：{value_3}")
                                    if isinstance(value_3, dict):
                                        # print("\n")
                                        # 4.对于获取到 dict 类型的 value 进行二次遍历，
                                        for key_4, value_4 in value_3.items():
                                            # 5.打印每次循环遍历后返回的键值对数据
                                            if key_4 == "score":
                                                value1 = value_4 * 100
                                                valuelast = int(value1)
                                                wwwscore1[f'WCm{i + 1}'] = valuelast
                                                #shopscore1_1 = int(value1)
                                                #print(f"Your Web speed score is : {shopscore1_1}")
    for key_1, value_1 in speedwdictm1[f'wwwspeedm{i + 1}'].items():
        # 2.打印每次循环遍历后返回的键值对数据
        if key_1 == "loadingExperience" :
           # print(f"取出的key为：{key_1} ,取出的value为：{value_1}")
        # 3.使用 isinstance() 方法判断取出的 value 数据类型是否为：dict
            if isinstance(value_1, dict):
                #print("\n")
                # 4.对于获取到 dict 类型的 value 进行二次遍历，
                for key_2, value_2 in value_1.items():
                    # 5.打印每次循环遍历后返回的键值对数据
                    if key_2 == "metrics" :
                        #print(f"嵌套字典取出的key为：{key_2} ,取出的value为：{value_2}")
                        if isinstance(value_2, dict):
                            #print("\n")
                            # 4.对于获取到 dict 类型的 value 进行二次遍历，
                            for key_3, value_3 in value_2.items():
                                # 5.打印每次循环遍历后返回的键值对数据
                                if key_3 == "FIRST_CONTENTFUL_PAINT_MS":
                                    #print(f"嵌套字典取出的key为：{key_3} ,取出的value为：{value_3}")
                                    if isinstance(value_3, dict):
                                        # print("\n")
                                        # 4.对于获取到 dict 类型的 value 进行二次遍历，
                                        for key_4, value_4 in value_3.items():
                                            # 5.打印每次循环遍历后返回的键值对数据
                                            if key_4 == "percentile":
                                                value1 = value_4 / 1000
                                                valuelast = value1
                                                wwwtime1[f'WTm{i + 1}'] = valuelast
                                                #shoptime1_1 = value1  #int(value1)
                                                #print(f"Your Web speed time is : {shoptime1_1}")

# this is output csv
with open(f"speedtest_result{date}.csv","w") as f:
    writer = csv.writer(f)
    writer.writerow(["WEBSITE                              NAME", "", "", "", "", "", "", "","","","","","Device Type", "", "          Score", "Respond Time"])
    for i in range(len(shop_list1)):
        writer.writerow([f"{web1[f'shop{i + 1}']}", "", "", "", "", "", "","","","","","", f"{DT[1]}", "", f"{shopscore1[f'SC{i+1}']}", f"{shoptime1[f'ST{i+1}']} s"])
        writer.writerow([f"{web1[f'shop{i + 1}']}", "", "", "", "", "", "","","","","","", f"{DT[0]}", "", f"{shopscore1[f'SCm{i+1}']}", f"{shoptime1[f'STm{i+1}']} s"])
    for i in range(len(www_list1)):
        writer.writerow(
            [f"{web1[f'www{i + 1}']}", "", "", "", "", "", "","","","","","", f"{DT[1]}", "", f"{wwwscore1[f'WC{i+1}']}",
             f"{wwwtime1[f'WT{i + 1}']} s"])
        writer.writerow(
            [f"{web1[f'www{i + 1}']}", "", "", "", "", "", "","","","","","", f"{DT[0]}", "", f"{wwwscore1[f'WCm{i+1}']}",
             f"{wwwtime1[f'WTm{i + 1}']} s"])

