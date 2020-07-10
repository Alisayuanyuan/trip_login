# coding = utf-8

import requests
url = 'http://47.98.200.110/api/Sign/SignIn'
header = {
                "ApplicationType": "ANDROID",
                "userId": "55318",
                "AppVersion": "3.8.3",
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "okhttp/3.11.0"
            }
data = {
                    "ApplicationType": "ANDROID",
                    "Idfa": "865987043461583",
                    "Mobile": "18667160715",
                    "Password": "a1234567",
                    "timestamp": "1592379887645"
                }

re = requests.post(url,headers=header,json=data)

return re
