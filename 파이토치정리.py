# 파이토치

torch, autograd 자동미분기능 nn: 신경망구축, multiprocessing, optim utils 유틸리티 기능 제공, onnx  다른 프레임워크간의 모델을 공유
datasets

transforms 전처리

# 텐서: 데이터 표현을 위한 기본구조 - 다차원 표현 / 넘파이 ndarray와 유사

scalar rank: 0
vector rank: 1
1D
torch.tensor([1,2,3])
2D
torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
3D 큐브 
가로 : timesteps, sample, feature
4D : 큐브가 1열
컬러 이미지 데이터가 대표적, 흑백 이미지는 3D로 가능, *channel
width, height, channel, samples

5D 
비디오 데이터
frames


torch.__version__ # 버전확인

# 초기화 되지 않은 텐서
x = torch.empty(4,2)
print(x) 

torch.rand(4,2)

torch.zeros(4,2, dtype=torch.long)

terch.tensor([3,2.3])

x.new_ones(2,4,dtype=torch.float64)

torch.randn_like(x, dtype=torch.float)

# 데이터 타입
tensor.FloatTensor([1.2.3])  기본 float32 int32
.double() .half()

# CUDA 텐서옮기기
torch.randn(1) 
x.item() 실제값은 길다 
x.dtype()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

x.to(device)

# 연산
import math
torch.clamp(a, -0.5,0.5) # 이 사이의 값

x.max(dim=0/1) # axis대신

torch.add(a,b)

result = torch.empty(2,4)
torch.add(x,y, out = result) 결과값을 넣음

x.copy_(y) : x를 카피한 것이 y가 됨, x.t_() #in-place 방식으로 텐서의 값을 변경하는 연산뒤에는 _가 붙음
y.add_(x) y에는 x를 더한 값을 리턴

x.sub(y)
x.mul(y)
x.div(y)

torch.matmul(x,y) # 내적 mm으로 쓰기도 함

# 조작
torch.Tensor()# indexing

# 크기, 모양변경
x =torch.randn(4,5)
x.view(20)
x.view(5,-1) 열만 지정

item : 텐서에 값이 단 하나라도 존재하면숫자값을 얻을 수 있음
x.randn(1)
x.item()

차원축소
torch.rand(1,3,3)
tensor.shape
tensor.squeeze() => (3,3)
t.unsqueeze(dim=0)

# stack : 텐서간 결합
torch.stack([x,y,z])

torch.cat((a,b), dim=0) dim이 존재해야 함

#chunk : 텐서를 여러개로 나눌 때 사용( 몇 개로 나눌 것인가)
torch.chunk(tensor,3,dim=1) 몇개로 나눌지

split(tensor,3,dim=1) 텐서당 크기가 몇개인지

# 넘파이변환 : 텐서가 CPU에 있으면 공유되기 때문에 함께 바뀜
a = np.ones()
b = torch.from_numpy(a)
np.add(a,1,out =a)

# 자동미분 : 코드를 어떻게 작성ㄹ하여 실행하느냐에 따라 역전파가 정의된다
requires_grad : True 연산추적을 시작

grad_fn: 미분값을 계산한 함수에 대한 정보저장(어떤 함수에 대해서 backprop 했는지)

# 기울기
x = torch.ones() requires_grad : True 걸어놓으면 자동으로 grad_fn가 출력

grad: data가 거쳐온 layer에 대한 미분값 저장
detach() : 내용물은 같지만 requires_grad가 다른 텐서를 가져올 때


transforms.Compose([transforms.ToTensor(), transforms.Normalize(mean=(0.5,),std=(1.0))])

trainset = datsets.MNIST(root =경로지정
                         train=True, download=True, transform*mnist_transform)

dataloader: 데이터 전체를 보관했다가 실제모델 학습할 때 batch_size 크기만큼 데이터를 가져옴
train_loader =  DataLoader(trainset,batch_size=6, shuffle=True, num_workers=2)
test_loader =  DataLoader(testset,batch_size=6, shuffle=False, num_workers=2)

dataiter = iter(train_loader)
images, labels = dataiter.next()

=> torch.Size([6,1,28,28] torch.Size([8])) 배치사이즈만큼의 이미지, 1= 흑백, 28*28

# 신경망 레이어-모듈-모델


nn.Conv2d(16,33,3, stride=(2,1), padding(4,2), dilatiion(3,1))

# 컨볼루션 레이어 : 컨볼루션을 통해 전체에서 일부를 샘플링하여 특징점을 찾아냄
in_channel : 채널의 개수
out_channel : 출력채널의 개수
kernel_size : 커널(필터) 사이즈


# 풀링 레이어
MaxPool2d 절반으로

# 선형레이어
.view를 사용해 1로 펼쳐주어야함
nn.Linear(20,30)(flatten)

# 비선형 활성화
nn.ReLU

# 신경망종류


# 모델

nn.Module
nn.Sequential  : __init__ layer1

BSELoss
MSELoss
CrossEntropy

# 옵티마이저
step()을 통해 전달받은 파라미터를 모델 업데이터
torch.optim.Optimizer(params, defaults)클래스 사용
zero_grad()를 이용해 옵티마이저에 사용된 파라미터들의 기울기를 0으로 설정
torch.optim.lr_scheduler를 이용해 에포크에 따라 학습률 조절

# 학습률스케쥴러
LambdaLR, StepLR, ReduceLR...




