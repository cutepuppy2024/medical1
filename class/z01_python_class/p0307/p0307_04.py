# < key 값 >

stuInfo = {                               #  database에 저장할 때 key값이 한글인 경우 error가 나는 경우가 있어서 영문으로 작성하는 것이 좋다
    "stuNo": 1, 
    "id":"aaa", 
    "pass":"1111", 
    "name":"홍길동", 
    "nicName":"길동스"
}

# print(stuInfo["tel"])  #error
print(stuInfo.get('tel')) # None