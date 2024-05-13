import pandas as pd

# 파일저장
df.to_csv('../z20_data/score.csv',encoding='utf-8-sig')
df.to_csv('../z20_data/score.txt',encoding='utf-8-sig')
df.to_excel('../z20_data/score.xlsx')

# 파일 불러오기
df= pd.read_csv('score.csv',index_col='지원번호')
df


# 파일 읽어와 기본처리
df = pd.read_excel('20122022_출생.xlsx',skiprows=2,nrows=3, usecols='B:M',index_col=0)
df.index.name = '제목'  # index 만들기


df.describe()   # 컬럼별 대략적인 정보, 최소값, 최대값, 평균 등 확인
df.head()       # 상단 5개 출력
df.tail()       # 하단 5개 출력
df.info()       # 컬럼별 타입, 크기 정보
df.nlargest(3)  # 가장 큰 값
df.nsmallest(4) # 가장 작은 값


## <  컬럼  >

df['키'].max()
df['키'].min()
df['키'].mean()
df['키'].count()     # NaN 데이터는 개수에 들어가지 않음
df['키'].describe()  # 대략적 통계정보를 보여줌
df['키'].info()      # 컬럼의 index 개수와 타입
df['국어'].sum()      # 컬럼/index 별 합계 연산 가능
df['학교'].unique()   # 중복제거 -> array[]
df['학교'].nunique()  # 중복제거후 개수출력
df['order_id'].astype()   # 타입변경

df['SW특기'].count()            # 전체개수, Nan데이터는 개수에 들어가지 않음.
df['item_name'].value_counts() # 선택한 컬럼의 값 당 개수
df['키'].nlargest(4)  # 키 큰순으로 3개 가져옴.
df['키'].nsmallest(3) # 키 작은순으로 3개 가져옴

# zip()과 같은 형태로, value_cout에 2개 컬럼을 1개 묶어 list 저장
item_count = df['item_name'].value_counts()
list(item_count.items())


df.values       # rows 데이터 배열로 출력(리스트 내의 리스트)
# for df in df.values: -> 각 row를 리스트 형태로 출력
#     print(df)
df.index        # index 정보
df.columns      # 컬럼 정보 
df.shape        # 데이터 크기 정보 : (8, 9) -> rows, 컬럼수 의미


# 컬럼별 호출
df['키']
df[df.columns[-1]]
df['이름']
df[['키','이름']][1:4]
df[df.columns[[1,3,4]]][1:4]
# 컬럼만 가져오기
df.columns
df.columns[0:3]
df.columns[[1,4,6]]


# 컬럼의 모든 데이터를 가져오기
df[['키','이름']] # [[]] 2개 이상의 컬럼에서 [] 2개 사용 중요!
# 컬럼명만 가져오기
df.columns[[1,4,6]]

# 컬럼의 합계 식으로 연산가능
df['합계'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
df['합계'] = df[df.columns[3]] + df[df.columns[4]] + df[df.columns[5]] + df[df.columns[6]] + df[df.columns[7]]
df['국어'] = df['국어'] +10
df['avg'] = df['total']/4

# 컬럼의 문자열에 문자열 추가 
df['학교'] = df['학교'] +'등학교'
df['키'] = df['키'] + 'cm'

# 컬럼의 순서 변경 : column의 배열을 리스트로 만들어 변경
a_list[0:4]+[a_list[-1]]+a_list[4:-1]
cols = list(df.columns)
cols = df[cols[0:2]+[cols[-1]]+cols[2:-1]]

# 컬럼 이름변경 : 딕셔너리
df.rename(columns={"이름":"name","학교":"school"},inplace=True)



##  <  Rows  >
# loc[인덱스명] , iloc[인덱스번호]
df.loc['1번']
df.iloc[0]

df[0:3]
df[5:]
df.iloc[[0,1,3]]   # rows데이터 부분적으로 가져오기
df.head()
df.tail(2)

# 2개의 rows 데이터 출력  : [[]]
df.loc[['1번','5번']]
# row에 해당하는 컬럼의 값
df.loc['1번','키']
df.loc['1번',['이름','키']] # 1번 학생의 이름,키 출력
df.loc[['1번','5번'],['이름','키']]
df.loc['1번':'5번','국어':'사회']


# 선택한 컬럼의 최소값/최대값 index
df['영어'].idxmin()
df['영어'].idxmax()

df.loc[df['영어'].idxmax()]  # -> 행 전체의 데이터



## <  문자열  > 
# split : 문자열 분리
df_str = pd.DataFrame(data)
s_data = df_str['d_split'].str.split(',') #배열로 분리되어 리턴
s_data
# 리스트를 딕셔너리 형태로
a_list = ['데이터,분석가','영희,철수,바둑이','국어,영어,수학,과학,사회']
data = {"d_split":a_list}
# slice : 문자열 자르기
df_str['idx'].str.slice(1,3)
df_str['idx'].map(lambda x:x[1:3])  #map(함수) , lambda : 익명함수
# replace:문자열 처리, strip:공백제거
df.iloc[0] = df.iloc[0].str.replace(",","")
df.iloc[0].astype(int)  
df['국어'] = df['국어'].astype(int) # 타입변경 후 info를 확인해 보면 확인가능

# 찾기
filt = df['이름'].str.startswith('강')
filt = df['이름'].str.contains('동')



## <  데이터 추출  >

## 조건문 &, |
filt  = df['키']>188  # True/False로 출력
df[filt]  # 조건에 해당하는 데이터를 DataFrame으로 출력
df.loc[filt] # 조건에 해당하는 row들을 출력

# 복수개를 for문을 돌리지 않고도 비교가능
df['키'] > df['키'].mean()
# 조건문을 바로 사용가능
df[df['키']> 189] 
# 조건문의 부정
df[~(df['키']> 189)] 
# 2개의 컬럼에 해당하는 rows 출력
df.loc[~(df['키']>189),['이름','키']]
# 2개의 조건문
df[(df['키'] >=180) & (df['학교'] == '구로고')]
# 2개이상 조건 검색부분
lang = ['Python','Java']
filt = df['SW특기'].isin(lang)
df[filt]

## 정렬
# 1) index를 가지고 정렬
df.sort_index()
# ascending = True : 순차정렬  /  ascending = False : 역순정렬
df.sort_index(ascending=False)
# 2) 선택한 컬럼으로 정렬

df['키'].sort_values()  # 분류기준을 함수 안에()
df.sort_values('키',ascending=False)
# 3) 같은 값이 있는 경우만 2번째 선택한 컬럼으로 정렬
df.sort_values(['키','이름'],ascending=False)
# 4) 2가지 컬럼의 정렬을 따로 지정
df.sort_values(['키','이름'],ascending=[False,True])
# 5) 정렬의 순서 결정 - 먼저 정렬하고자 하는 순서에 따라 정렬된 데이터의 결과가 달라짐
df.sort_values(['id','kor'],ascending=[True,False])
df.sort_values(['kor','id'],ascending=[False,True])
# 6) 조건문으로 데이터프레임 추출 후 정렬
filt = df['avg'] >=75
df[filt].sort_values(['avg','id'],ascending=[False,True])


## zip을 사용하여 배열을 묶기
# 1) zip을 사용하여 묶기
name = ['aaa','bbb','ccc','ddd','eee']
births = [968,155,77,578,973]
custom = [1,5,25,13,23232]
# zip(name,births)
list(zip(name,births,custom))
# 2) 변수로 지정하여 DataFrame에 넣어 출력
bSet = list(zip(name,births,custom))
df = pd.DataFrame(data=bSet,columns=['name','births','custom'])
df



## <  데이터 추가  >
# 딕셔너리처럼 없는 컬럼이면 자동추가
data['id'] = 'aaa'
# index 기준으로 추가 : 없는 index 번호를 입력하면 추가가 됨
df.loc['9번'] = ['홍길동','디지털고',191,90,80,70,60,90,'python']

# 각각의 index의 합을 '합계' 라는 컬럼을 생성하여 저장
df['합계'] = 0
# df.iloc[0].sum()
for i in range(len(df.index)):  
    df.iloc[i,-1] = df.iloc[i].sum()




## <  데이터 수정  >
# 데이터 수정
# 1) 선택한 컬럼의 전체 데이터 수정
df['학교'] = "디지털고"

# 2) numpy 사용하여 na로 변경
import numpy as np
df['학교'] = np.nan
df
# 3) 2개의 컬럼에 NaN가 있는 경우 -> 컬럼을 명확히 정의, 어떻게 바꿀지 선택

# 4) 1개의 값 수정 :  df.loc[조건문, 컬럼] =  값
## 총합 350점 이상이면 결과 컬럼에 합격을 넣으시오
df['합계'] >= 350
df.loc[df['합계'] >= 350, "결과"] = '합격'
df

# 5) 컬럼내의 값 2개를 수정
df['학교'].replace({"구로고등학교":"디지털고","단지고등학교":"영등포고"},inplace=True)
df

# 6) 위치점을 찾아 수정
df.loc['5번',['학교','키']] = ['디지털고',190] 

# 7) 랜덤입력
# 0-6까지의 숫자를 랜덤으로 입력
# df['요일'] = 0
for i in range(8):
    df.iloc[i,-1] = random.randint(0,6)



## <  데이터 삭제  >
# 컬럼 삭제  : drop(columns=[컬럼명])
df.drop(columns = ['국어','영어','수학'],inplace=True)

# index 삭제  : drop(index= [인덱스명]) ->  index에 index를 넣어야 한다 
df.drop(index='1번',inplace=True)
df.drop(index=df[df['국어']>80].index,inplace=True)  # 조건문 적용하여 삭제

df.drop(index=['3번','5번'],inplace=True) # index 여러개 삭제 


# NaN 삭제
df.dropna(inplace=True)  # NaN이 들어가 있는 모든 행렬을 삭제
# 행별/컬럼별 삭제 - axis : index, colums /  1개라도/전체 - how: any,all

# NaN 데이터가 들어가 있는 컬럼을 전체 삭제
df.dropna(axis='columns',inplace=True)
# Nan 데이터가 들어가 있는 컬럼에서 모든 컬럼이 Nan 인것만 삭제
df.dropna(axis='columns', how='all', inplace=True)
# Nan 데이터가 들어가 있는 컬럼에서 1개라도 Nan이 포함되어 있으면 삭제
df.dropna(axis='columns', how='any', inplace = True)





# <  NaN  > 
df.fillna('없음',inplace=True) # 원하는 단어나 값으로 변경
import numpy as np
# 컬럼의 모든 값을 NaN으로 바꾸기
df['학교'] = np.nan
df
# 1개의 데이터를 Nan으로 바꾸기
df.loc['4번','영어'] = np.nan



## <  함수 선언하여 호출  >
# 함수선언 : def 함수이름(매개변수) -> apply 함수 적용(for문과 같은 효과)
def add_cm(height):
    return str(height)+"cm"
df['키'] = df['키'].apply(add_cm)

# 람다함수 : 익명함수 / 매개변수: 리턴값 if 조건문
df['결과'] = df['평균'].apply(lambda score:'합격' if score>= 70 else "불합격")
df['결과'] = df['평균'].apply(lambda score:'합격' if score>= 65 else ("재시험" if score==65 else "불합격"))

# notnull : null이 아닌지 확인  /   isnull  : null인지 확인
def lower_change(lang):
    if pd.notnull(lang) : return lang.lower()
    else : return "python"


## <  그룹화  >
# 그룹화하여 특정 그룹의 데이터만 출력
df.groupby('학교').get_group('단지고')
# 그룹화하여 개수를 출력
df.groupby('학교').size()  
#  그룹화하여 특정 컬럼의 크기만 출력
df.groupby('학교').size()['구로고']  # 그룹화한 데이터 명과 개수만 출력
# 전체 카운트 : 개수로 NaN이 어디에 있는지 확인할 수 있다
df.groupby(['학교','학년']).count()  # 전체 데이터프레임 형태로 전체가 출력
# 그룹한 컬럼의 평균
df.groupby('학교')['키'].mean()
# 선택한 컬럼으로 그룹별 함수적용한 값들을 각각 구하여, 컬럼을 나열하여 DataFrame출력
df.groupby('학교')[['키','국어','영어','과학','사회']].mean() 
# 2개의 기준으로 그룹화 -> 2차원 테이블로 출력
df.groupby(['학교','학년']).size()
# 그룹화 한 데이터에 함수 적용
df.groupby(['학교','학년'])['키'].mean()
# 함수적용한 데이터에 특정 값에 해당하는 데이터만 출력
df.groupby(['school','grade'])['kor'].mean()['구로고']

df.groupby(['학교','학년']).value_counts()

# 아래의 3가지가 같음
df[['학교','학년']].value_counts()
df.groupby(['학교','학년']).size()
school = df.groupby('학교')
school['학년'].value_counts()

school = df.groupby('학교')
school['학년'].value_counts().loc['구로고']
# 퍼센트 출력
school['학년'].value_counts(normalize=True).loc['구로고']
(school['학년'].value_counts(normalize=True).loc['구로고']*100).astype(str)+'%'


# groupby한 결과값의 컬럼 지정 -> []
df.groupby(['school','gender'])[['kor','eng','math']].mean()['kor']
# groupby한 결과값의 index 지정 -> loc[]
df.groupby(['school','gender'])[['kor','eng','math']].mean().loc['디지털고']

df.groupby(['school','gender'])[['kor','eng','math']].mean().sort_values('kor',ascending=False)



##  <  agg함수  >
df.groupby('grade')['total'].agg(['mean','min','max','sum']) 



