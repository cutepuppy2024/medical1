# k001.csv 파일에서 전국 인원수를 출력하시오

f = open('k001.csv','r',encoding='utf8')
cnt = 0
sum = 0
while True:
    cont = f.readline()
    if cnt == 0:
        cnt+= 1
        continue
    if cont == '': break   
    a_list = cont.split(',')
    a_list[4] = int(a_list[4])
    sum += a_list[-2]
print(sum)    

f.close()

