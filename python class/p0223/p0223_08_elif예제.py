# 점수를 입력받아서
# 90점 이상이면 A, 80점 이상이면 B, 70점 이상이면 C, 나머지는 F를 출력해보세요

score = int(input("점수를 입력하세요 >> "))
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")   
else :
    print("F")        
            
            
# 98점 이상이면 A+, 90-93 사이는 A-
# B+, B-, C+, C-

score = int(input("점수를 입력하세요 >> "))


if score >= 90 :
    if score >= 98 :
        print("A+")
    elif 90 <= score <= 93 :
        print("A-")
    else :
        print("A")
elif score >= 80 :
    if score >=88 :
        print("B+")
    elif score >= 93:
        print("B")
    else :
        print("B-")
elif score >= 70 :
    if score >= 78 :
        print("C+")
    elif score >= 73 :
        print("C")
    else :
        print("C-")  
else :
    print("F") 
    print("2주 후 재시험 있습니다") 
 
 
score = int(input("점수를 입력하세요 >> "))
attendance = int(input("결석 수를 입력하세요 >> "))
 
if score >= 90 and attendance <=2 :
    if score >= 98 :
        print("A+")
    elif 90 <= score <= 93 :
        print("A-")
    else :
        print("A")
elif score >= 80 and attendance <=2 :
    if score >=88 :
        print("B+")
    elif score >= 93:
        print("B")
    else :
        print("B-")
elif score >= 70 and attendance <=2 :
    if score >= 78 :
        print("C+")
    elif score >= 73 :
        print("C")
    else :
        print("C-")  
elif attendance >= 5 :
    print("FA")
    print("놀았냐?")
else :
    print("F") 
