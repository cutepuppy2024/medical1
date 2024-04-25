class Student:
    def __init__(self,name="",total=0):
        self.name = name
        # self.total = total
        self.__total = total             # 프라이빗 변수 : 클래스 내부에서만 접근
        
    def __str__(self):
        return (f"이름 : {self.name}, 합계 : {self.__total}")  # 내부의 함수로 찍기 때문에 외부의 함수로 규정된 값이 출려되지 않음
    
    def set_total(self,total,log_id):
        if log_id == 'admin':                  # 접근권한이 있는 사람만 가능
            self.__total = total
        else:
            print("admin 관리자가 아니면 수정이 불가능합니다.")
    def get_total(self):
        return self.__total
    
    # def __gt__(self,s):
    #     return self.total > s.total
               
    # def stu_print(self):
    #     print("학생성적 출력합니다")
            
            
s = Student("홍길동",95)                 # 객체선언할 때 무조건 init() 호출
s2 = Student("유관순",100)

print(s)
print(s2)


# print(s>s2)                             # 함수를 사용하지 않고 클래스 자체를 비교하는 식을 사용하면 주소값끼리 비교가 되므로 에러
# print(s.total>s2.total)                 # 함수를 사용하지 않는 경우


s.total = 300   
s.set_total(400,'admin')
# print(s.__total)                          # 변수로는 접근이 안된다. => get 함수 필요
print(s.get_total())
print(s)                        