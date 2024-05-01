import oracledb


while True:
    cursor = conn.cursor()

    id = input("아이디을 입력하세요 (-1.종료) >>")
    if id == '-1':
        break
    
    # id를 가지고 검색을 먼저한 후 데이터를 입력하도록 해야 함.
    id = input("아이디를 입력하세요 (-1: 취소)")
    if id == '-1': break
      
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor.execute(sql)
    
    sql = f"select id from member where id = '{id}'"
    data = cursor.fetchall()
    # print("id의 개수 ", len(data))

    # ID가 존재하는지 확인
    if len(data) == 1:
        print("아이디가 존재합니다.")
        print()
        continue
    
    # ID가 존재하지 않으면 계속 입력
    pw = input("패스워드을 입력하세요 >>")
    name = input("이름을 입력하세요 >>")
    gender = input("성별을 입력하세요 >>")

    sql = f"insert into member values (member_seq.nextval,'{id}','{pw}','{name}','{gender}',sysdate)"
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    cursor.execute(sql)
    cursor.execute("commit")
    
    print("입력이 완료되었습니다")
    print()
        

    # db연결 해제
    cursor.close()
    conn.close()