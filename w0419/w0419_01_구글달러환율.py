import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC&sca_esv=125395e02bc1fefe&sxsrf=ACQVn096VDIR_UTz27Tp2BEZzPjDgyq4SA%3A1713507001982&source=hp&ei=uQoiZunLJLHh2roPq5OigA8&iflsig=ANes7DEAAAAAZiIYyfFUrOQWfipl1Pbp0GzA5HztWydd&udm=&oq=%ED%99%98%EC%9C%A8&gs_lp=Egdnd3Mtd2l6IgbtmZjsnKgqAggAMgoQIxiABBgnGIoFMgoQIxiABBgnGIoFMhAQABiABBixAxiDARgUGIcCMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyBBAAGAMyCxAAGIAEGLEDGIMBSOQUUF1Yww1wAngAkAEAmAF7oAGyBqoBAzMuNbgBA8gBAPgBAZgCB6ACmgSoAgrCAgcQIxgnGOoCwgIQEC4YgAQY0QMYxwEYJxiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgIPECMYgAQYJxiKBRhGGIICwgIIEAAYgAQYsQPCAgsQLhiABBixAxiDAcICDhAAGIAEGLEDGIMBGIoFmAMIkgcDNC4zoAepUg&sclient=gws-wiz"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# with open ('google.html',"w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print(soup)

# input: 태그,  aria-label: 속성

print(soup.title.text) # 선생님 풀이

# 해당태그를 출력
print("미국달러 : ", soup.find("input",{"class":"lWzCpb a61j6"}))

# 해당태그의 속성값 모두출력
print("미국달러 : ", soup.find("input",{"class":"lWzCpb a61j6"}).attrs)

# 해당태그의 특정속성값 1개을 출력
print("미국달러 : ", soup.find("input",{"class":"lWzCpb ZEB7Fb"})["value"])

# 대한민국 원
print("대한민국 원 : ", soup.find("input",{"class":"lWzCpb a61j6"})["value"])


# 내가 푼것 -> input 태그 이용
print(soup.find("title").text) # 내가 푼것
print(soup.find_all("input",{"aria-label":"통화 액수 입력란"}))
print(soup.find("input",{"aria-label":"통화 액수 입력란"})["value"])
# 마무리하기 : 내가 생각한것으로 꼭 끝을 보자