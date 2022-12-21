#################### 구글 이미지 크롤링 ####################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
from selenium.webdriver.common.by import By

# 크롬 드라이버 크롬에 맞는 버전 다운, 설정
driver = webdriver.Chrome()
# 이미지 검색결과의 URL을 입력
driver.get("https://www.google.com/search?q=ev+charger+connector&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi99Ii3o4f8AhW7CbcAHalHA3wQ_AUoAXoECAEQAw&biw=1920&bih=937&dpr=1")

#elem = driver.find_element_by_name("q")
#elem.send_keys("魚探")
#elem.send_keys(Keys.RETURN) #엔터누르기
#driver.find_element_by_css_selector(".BcUvif").click()



SCROLL_PAUSE_TIME = 1

# Get scroll height 스크롤 높이 구함
last_height = driver.execute_script("return document.body.scrollHeight")

# 스크롤 끝까지 내림
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
        except:
            break
    last_height = new_height

# 이미지 위치 기억함
images = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
# 이미지 하나씩 눌러서 저장함
count=1
for image in images:
    try:
        image.click()
        time.sleep(2)
        # imgurl = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute("src")
        # try:
        imgurl = driver.find_element(By.CSS_SELECTOR,".n3VNCb.KAlRDb").get_attribute("src")
        print(imgurl)
        # 이름 설정해서 저장 
        # urllib.request.urlretrieve(imgurl, "connector_" + str(count) + ".jpg")
        # print("done")
        # mem = urllib.request.urlopen(imgurl,headers={'User-Agent':'Chrome/66.0.3359.181'}).read()
        
        mem = urllib.request.urlopen(imgurl).read()
        print(mem)
        with open("connector_" + str(count) + ".jpg",mode="wb")as f:
            f.write(mem)
            print("저장완료")
        # except:
        #     imgurl = driver.find_element(By.XPATH,"/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
        #     urllib.request.urlretrieve(imgurl, "connector_" + str(count) + ".jpg")
        count = count+1
        #if count==400:
        #    break
        #else:
        #    print(count)
    except:
        print("저장오류")
        pass    #오류 넘기고 그 다음 것 하기

driver.close()