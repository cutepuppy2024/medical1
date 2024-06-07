# < numpy >
https://numpy.org/



df.to_numpy()


np.zeros(), np.ones(), np.NaN, np.full((),)
no.eye(정사각행렬- 길이만 지정)
np.tri()삼각행렬 np.empty() 초기화하지 않은 배열, 초기화가 없어서 배열생성비용 저렴하고 빠름, 어떤 값이 들어갈지 모름
np.zeros_like()ones_like, full_like()

np.array()
np.arange() 정수범위로 배열 생성
np.linspace : 범위 내에서 균등간격으로 로그 스케일로 배열 생성
np.logspace(0.1,1,20)


# 배열
def array_info(array):
print(array)
array.ndim 차원
shape
dtype
size 개수
itemsize 바이트
nbytes 전체바이트
strides 차원이 넘어가는 수

array_info(a2) 2차원

# indexing
a1[0]
a2[0,1]
a2[0,1,2]

# slicing : 리스트와 같음
a1[0:2:1]
a2[1,:]

# boolean indexing
true만 출력

print(a2)
bi = np.random.randing(0,2,(3,3), dtype=bool)
print(bi)
print(a2[bi])

# fancy indexing
a1[0], a1[2]
a1[ind]
ind = np.array([0,1],[2,0])
print(a1[ind]) 1차원인데 2차원결과출력

row=np.array([0,2])
col=np.array([1,2])


# 배열 값 삽입
insert(a1, 1, 10,axis=0/1) : 배열의 특정 위치에 삽입 axis는 0: 행 1: 열에 전체값이 변경

# 수정 : 딕셔너리처럼
a1[0] = 1
a1[:1] = 9

i = np.array([1,3,4])
a1[i] = 0
a1[i] +=4

# 삭제 
delete()
a2_sub[:,1] = 0 리스트는 원본파일유지되나 넘파이는 달라짐

a2_sub_copy = a2[:2,:2].copy() : 배열이나 하위 배열 내의 값을 명시적으로 복사

# 추가
append()
np.append(a2,b2, axis0/1)

concatenate() : 튜플이나 배열의 리스트를 인수로 사용해 배열 연결
np.concatenate([a2,a2])

# 스ㅐㄱ
vstack: 수직스택, 1차원으로 연결
hstack: 수평스택
dstack: 깊이스택
np.stack: 새로운 차원으로 연결

# 배열분할
split()
vsplit() : 수직분할
hsplit() : 수평분할
dsplit()



# 배열연산
- 브로드캐스팅

a1+1
np.add(a1,10) 범용함수
np.subtract(a1,10)
-a1
np.negative(a1)
np.multiply()
np.divide()
np.floor_divide(a1,2) 내림
np.power(a1,2) 지수
np.mod(a1,2) 나머지

a1 +-*/ // ** % b1 배열끼리의 연산도 가능

a1 = np.arange(1,10).reshape(3,3)
b1 = np.random.randint(1,10, size=(3,3))

# 절대값
absolute(), abs()

# 제곱/제곱근
square(), strt() 

# 지수와 로그함수
np.exp(a1)
np.exp2()
np.power()

np.log()
np.log2()
np.log10()

# 삼각함수
np.sin()
cos, tan, arcsin, 
np.linspace(0,np.pi,3)
np.arcsin/arccos/arctan

# 집계함수
np.sum(a1,axis=0)/np.nansum() a1.sum(axis=1)
np.cumsum()/np.nancumsum() : 누적합
np.diff() : 차분
np.prod() : 곱 

np.dot(a2,b2) = np.matmul()

tensordot(a2,b2,axis=0) : 텐서곱 a2각 값을 b2 전체에 곱함 => 둘다 (3,3)이면 9개

cross() 벡터곱

inner() = dot()
outer()

mean() axis지정
std()
var() 분산계산

argmin()/ argmax() : 최소/최대값 인덱스 
median()
percentile(a1,[0,20,40,60,80,100], interpolation='linear'/higher,lower,nearest,midpoint) : 백분위 수

any() 하나라도 True면 True
all() 전체가 True면 True

# 비교연산 : boolean타입
np.equal
np.not_equal()
np.less()
np.greater()
np.greater_equal()

np.count_nonzero(a2>5)
np.sum(a2>5), axis=1

np.isclose() : 배열 두개가 가까우면 True, 
isinf() : 배열 inf무한대 이면 True  np.NINF()
isfinite() : 무한대가 아닌것
isnan()

# 불리언 연산자 : 조건
(a2>5) & (a2<8)
a2[(a2>5) & (a2<8)]
& np.bitwise_and
| np.bitwise_or
^ np.bitwise_xor
~ np.bitwise_not

# 배열정렬
np.sort()
argsort() : 인덱스/위치값만 출력

np.sort(a2, axis=) 
np.partition(a2, 3) : 정렬된 값 중 k개의 값을 출력 , 2차원일 경우 앞부분으로

# 배열 입출력
np.save("파일명",a2) : numpy 배열 객체 1개를 파일에 저장 바이너리
!ls 실행확인
 a.npy 넘파이 바이너리 파일
np.savez("ab",a2,b2) : 여러개를 하나의 파일로 저장
 ab.npz a.npy

npy = np.load("a.npy")
np.load()
np.load(npz,filtes)  파일개수

np.loadtxt("a.csv", a2, delimiter=',') : 텍스트 파일로부터 배열 로딩
!cat a.csv 실수형태

np.savetxt("a.csv", a2, delimiter=',',fmt='%.2e', header = 'c1,c2,c3,c4,c5') : 텍스트 파일에 넘파이 배열객체 저장

, a.reshape(())
np.unique()

np.add(,), np.multiply(,), np.divide(,), np.substract(,)
dot(,) # 행열의 곱
sum(), prod(), mean(), std() / axis = 0(컬럼) 1(행)


# 선형대수함수, 배열전치
a.T = a2.swapaxes(1,0)
a3.T 90도 회전

a3.swapaxes(0,1) 행, 안, 열 앞면-> 윗면
a3.swapaxes(1,2) 행-> 열


# 배열변환
reshape(): 배열의 형상을 변화

newaxis() : 새로운 축 추가
n1[np.newaxis, :5]
n1[:5, np.newaxis]

# 배열 모양만 변경
n2.resize((5,2))
(5,5 ) 없으면 0으로 채워짐



# 난수생성
np.random.random()배열만 주면 됨
np.random.radint(0,10,(3,3))
np.random.seed() # 유사난수생성
np.random.uniform() 
np.random.normal() # 정규분포
np.random.rand()
randn()
np.random.shuffle()

# 날짜/시간
date = np.array('2020-01-01',dtype=np.datetime64)
date + np.arange(12) 기준날짜에서 더해서 배열로 생성
datetime = np.datetime64( '2020-01-01 12:00')

np.column_skack() # 컬럼화
np.concatenate() # 배열합치기

# numpy로 랜덤데이터 분리시키기
np.random.seed(0)
idx = np.arange()
np.random.shuffle(idx)
df.iloc[idx[:],:]
# <-> 파이썬으로 랜덤데이터 분리시키기
idx = [i for i in range()]
random.shuffle(idx)
df.iloc[idx[:],:]