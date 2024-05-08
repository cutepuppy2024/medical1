def func(n,*val, a=2):     # 기본매개변수, 가변매개변수, 키워드매개변수 순으로!!
    for i in range(n):
        for v in val:
            print(v)
            
            
func(5,"안녕","안녕하세요","반갑습니다","매개변수")