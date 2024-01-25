import sqlite3
print()

# 연결 객체 (파일로 저장)
con = sqlite3.connect("./test.db")
# 커서 객체
cur = con.cursor()
# table 생성 (테이블이 없는 경우 )
cur.execute("create table if not exists PhoneBook (name text, phoneNum text);")
# 한 건 입력
cur.execute("insert into PhoneBook values ('길동쓰', '010-2222-4444');")
# 입력 파라미터 처리
name = "전우치"
phone_num = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phone_num))

# 여러 정보를 동시에 입력
data_sets = (("이순신", "02-984"), ("장보고", "010-8080"))
cur.executemany("insert into PhoneBook values (?, ?);", data_sets)

# 검색
cur.execute("select * from PhoneBook order by name;")
for row in cur:
    print(row)
print()
# 주의! 구문을 실행하고 commit을 하지 않으면 다 날아감!!
print("과연?")
cur.fetchall() # 아무것도 안 나옴!
# 작업 정상 완료처리
con.commit()


con_test = sqlite3.connect("./test.db")
cur_test = con_test.cursor()
cur.execute("select*from PhoneBook;")
cur.fetchall()
