import pandas as pd

df= pd.read_csv('score.csv',index_col='지원번호')
df

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
df['키'].count()  # NaN 데이터는 개수에 들어가지 않음
df['키'].describe()
df['키'].info()
df['국어'].sum()
df['학교'].unique() # 중복제거 -> array[]
df['학교'].nunique()  # 중복제거후 개수출력

df.values       # rows 데이터 배열로 출력
df.index        # index 정보
df.columns      # 컬럼 정보 
df.shape        # 데이터 크기 정보 : (8, 9) -> 데이터, 컬럼수 의미


# 컬럼별 호출
df['키']
df['이름']


# 컬럼의 모든 데이터를 가져오기
df[['키','이름']] # [[]] 2개 이상의 컬럼에서 [] 2개 사용 중요!
# 컬럼만 가져오기
df.columns[[1,4,6]]

df.iloc[0] 

df.columns  

# 복수개를 for문을 돌리지 않고도 비교가능
df['키'] > df['키'].mean()



##  <  Rows  >
# loc[인덱스명] , iloc[인덱스번호]

df
df.loc['1번']
df.iloc[0]