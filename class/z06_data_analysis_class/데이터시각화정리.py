import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import requests

matplotlib.rcParams['axes.unicode_minus'] = False 
matplotlib.rcParams['font.family'] = 'Malgun Gothic'  # : windows 사용자용
matplotlib.rcParams['font.size'] = '10' 

# 기본 형태
plt.plot(x,y)
plt.plot(x,y,label='국어',linestyle=':',marker='o')
plt.legend(loc='upper center')  / plt.legend(loc=(0.2,0.5))
plt.show()


# 크기, 용량
plt.figure(dpi=200)
plt.figure(figsize=(10,5))

# 저장
plt.savefig('g.png')
plt.savefig('g2.png',dpi=300)

plt.yticks([165,170,180,190,200,210])
plt.xticks(rotation=90)
plt.ylim(165,210)

# 위치 바꾸기 : 컬럼과 인덱스
df = df.T


# 그래프 그리기, 선두께 : linewidth=5 label : 범례

# 마커
marker='o'/'x'
markersize = ms : 마커 크기
markeredgecolor = mec : 마커테두리색상
markerfacecolor = mfc : 마커색상
alpha : 투명도

# 컬러지정
colors = ['r','g','b','y','pink'] => 꺾은선 그래프의 경우 자동지정
plt.bar(x,y1, label='국어', color=colors)

# 그래프에 눈금표시
plt.grid(ls='--',alpha=0.5)
# plt.grid(axis='y',ls='--',alpha=0.5) y축만

# 패턴
bar = plt.bar(x,y3, label ='국어', width=0.2, alpha =0.5)
bar[0].set_hatch('/')
bar[1].set_hatch('x')
bar[2].set_hatch('..')


# 다중막대
plt.bar(index-0.2,y,width=0.2,label='국어')
plt.bar(index,y2,width=0.2,label='영어')
plt.bar(index+0.2,y3,width=0.2, label='수학')

# 누적막대
plt.bar(x,y1,label='국어')
plt.bar(x,y2,bottom=y1, label='영어')
plt.bar(x,y3, bottom=y1+y2,label='수학')


# 값을 그래프에 넣기
plt.text(x[i],y[i]+0.5, txt, ha='center', color='blue')
for i,txt in enumerate(y1):
    plt.text(x[i],y[i]-12, txt, ha='center')
for i,txt in enumerate(y2):
    plt.text(x[i],y1[i]+y2[i]-15,txt,ha='center')
for i,txt in enumerate(y3):
    plt.text(x[i],y1[i]+y2[i]+y3[i]-11,txt,ha='center')


# 배열을 랜덤으로
np.random.rand(8)*1000

# 산점도
plt.scatter(x,y)
# s : 크기 조절
plt.scatter(df['영어'],df['수학'],s = 1000) 
# 학년별 크기조절 1*500 = 500 , 2*500 = 1000, 3*500 = 1500
sizes = df['학년']*500
plt.scatter(df['영어'],df['수학'],s = sizes) 
# c : 컬러 적용 -> 기준컬럼 명시
plt.scatter(df['영어'],df['수학'],s = sizes, c = df['학년'],cmap='viridis') 

# 컬러바 눈금표시  -  ticks : 범위지정 /  라벨표시 : label   /  컬러바크기조절 : shrink   /  하단배치 : orientation='horizontal'
plt.colorbar(ticks=[1,2,3], label='학년', shrink=0.3, orientation='horizontal')


# 여러개의 산점도그래프 : subplots
fig,axs= plt.subplots(2,2, figsize=(10,10))
# 0,0 번째 그래프 작성
# 범례  :  label
axs[0,0].bar(df['이름'],df['국어'], label='국어점수')
# 범례출력 : legend
axs[0,0].legend()
# 상단 타이틀 : set_title
axs[0,0].set_title('국어 그래프')
# x,y축 글자 표시
axs[0,0].set(xlabel='이름', ylabel='국어점수')
# 그래프내 색상 : set_facecolor
axs[0,0].set_facecolor('#efefef') # 배경색
# 격자표시 : grid
axs[0,0].grid(ls='--',alpha=0.5)



# 2개의 다른 그래프 합치기
fig,ax1 = plt.subplots(2,2,figsize=(10,7))  
# 상단타이틀 출력
fig.suptitle('출생아수 및 합계출산율')
ax2 = ax1.twinx() # x축을 함계 사용 :  twinsx
ax1,ax2 따로 정의하면 


# 상관도
df.corr()
# annot : 수치
sns.heatmap(data_corr,annot=True) 
# 히스토그램 : 각 컬럼의 데이터 구성을 확인
df.hist(figsize=(14,14))
df['Age'].hist()