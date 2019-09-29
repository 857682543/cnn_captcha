import json
import time
import base64
import os

import requests


url = "http://212.64.127.151:6002/ocr_captcha"
path = "./img/"
img_name = "1567562289.jpg"
headers = {'Content-Type': 'application/json'}
img_path = "/Users/adks/Desktop/AmazonSpider/captcha_recognize/cnn_captcha/cnn_captcha/sample/origin/"

img_filename_list = os.listdir(img_path)

count = 0

for img_filename in img_filename_list:
    # with open(path + img_name, "rb") as f:
    
    with open(img_path + img_filename, "rb") as f:
        data0 = f.read()
        data = {
            "image_base64": str(base64.b64encode(data0),'utf-8'),
            "app_id": "857682543",
            "ocr_code":"0000"
        }

    t = time.time()
    try:
        response = requests.post(url=url, data= json.dumps(data), headers = headers)
        # print(response.json())  # {'errorcode': 0, 'errormsg': 'OK', 'string': 'TQEULA'}
        res = response.json()
        if res["errormsg"] == "OK":
            count += 1

            code = res["string"]
            new_img_filename = img_path + code + "_" + str(int(time.time() * 100000)) + ".jpg"
            os.rename(img_path + img_filename, new_img_filename)

            print("耗时 :{}s".format(time.time() - t))
            print("成功数量: {}, 原图片名: {}, 新图片名:{}".format(count, img_filename, new_img_filename))
            print()
    except Exception as err:
        print("验证码标注请求出错: {}, 下一张...".format(err))




