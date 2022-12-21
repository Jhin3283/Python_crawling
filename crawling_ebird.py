import urllib.request
from urllib.error import HTTPError
from urllib.error import URLError

# mem = urllib.request.urlopen("https://www.mouser.kr/images/marketingid/2022/microsites/110075971/Charging%20Connectors.png").read()
# print(mem)
# with open("test.jpg",mode="wb")as f:
#     f.write(mem)
#     print("저장완료")

try:
    html = urllib.request.urlopen("https://m.media-amazon.com/images/I/515bJnst1mL._AC_SL1500_.jpg")
except HTTPError as e:
    print("HTTP 에러입니다.")
except URLError as e:
    print("존재하지 않는 사이트입니다.")
else:
    print(html.read())