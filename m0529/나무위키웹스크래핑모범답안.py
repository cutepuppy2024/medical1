from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import random
# 데이터를 크롤링하는 함수 정의
def data_mining(url_list):
    title_list = []  # 제목을 저장할 리스트
    category_list = []  # 분류를 저장할 리스트
    content_list = []  # 개요 내용을 저장할 리스트
    # URL 리스트에서 하나씩 가져와서 크롤링
    for url in url_list:
        # 브라우저 열기
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(random.random() + 3)  # 랜덤한 시간 동안 대기
        # 제목 크롤링
        try:
            title = browser.find_element(By.TAG_NAME, 'h1').text
            title_list.append(title)
        except:
            title_list.append('없음')  # 제목이 없을 경우 '없음' 추가
        time.sleep(random.random())
        # 분류 크롤링
        try:
            category = browser.find_element(By.TAG_NAME, 'ul').text
            category_list.append(category)
        except:
            category_list.append('없음')  # 분류가 없을 경우 '없음' 추가
        time.sleep(random.random())
        # 개요 내용 크롤링
        try:
            content = browser.find_element(By.CLASS_NAME, 'nA6im+12').text
            content_list.append(content)
        except:
            content_list.append('없음')  # 내용이 없을 경우 '없음' 추가
        time.sleep(random.random())
        # 브라우저 닫기
        browser.quit()
    return title_list, category_list, content_list  # 크롤링한 데이터를 반환
# 주어진 URL에서 최근 변경 사항을 가져오는 부분
browser = webdriver.Chrome()
url = 'https://namu.wiki/RecentChanges'
browser.get(url)
time.sleep(3)
# 최근 변경 사항 목록에서 데이터 추출
data_list = browser.find_elements(By.CLASS_NAME, 'b5G6-Ki+')[1:]
url_list = []
for data in data_list[:50]:  # 상위 50개의 URL만 사용
    elem = data.find_element(By.TAG_NAME, 'a')
    url_list.append(elem.get_attribute('href'))
# 브라우저 닫기
browser.quit()
# URL 리스트를 사용하여 크롤링 수행
title_l, cate_l, cont_l = data_mining(url_list)
# 데이터를 데이터프레임으로 변환
title_df = pd.DataFrame(title_l, columns=['Title'])
category_df = pd.DataFrame(cate_l, columns=['Category'])
content_df = pd.DataFrame(cont_l, columns=['Content'])
# 데이터프레임을 하나로 결합
df = pd.concat([title_df, category_df, content_df], axis=1)
# 결과를 CSV 파일로 저장
df.to_csv('namu.csv', index=False)  # 인덱스를 제외하고 저장