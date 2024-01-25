# DB 작업
# 1) Connection class : 연결 작업
    # Connection.cursor() : 커서 객체를 생성
    # Connection.rollback() : 작업 내용을 반영하지 않고 이전 상태로 돌림
    # Connection.commit() : 지금까지의 작업을 반영
    # Connection.close() : 작업 종료
# 2) Cursor calss : SQL 구문 실행 + 결과 셋도 처리
    # exe로 시작하는 것들
    # Cursor.execute() : SQL 문장 실행
    # Cursor.executemany() : 여러 SQL 구문을 실행 할때 쓰임
    # Cursor.executescript() : ; 으로 구분된 SQL 문장을 실행
    # fetch로 시작하는 것들

# 트랜잭션 작업(TP)

# 계좌이체 (여러 개의 구문을 하나로 묶어서 처리)
# -------------------
# Begin tran
# Update
# Insert
# Commit tran
# -------------------

import sqlite3
print()
# 연결 객체
con = sqlite3.connect(":memory:")
# 커서 객체
cur = con.cursor()
# table 생성
cur.execute("create table PhoneBook (name text, phoneNum text);")
# 한 건 입력
cur.execute("insert into PhoneBook values ('길동쓰', '010-2222-4444');")
# 입력 파라미터 처리
name = "전우치"
phone_num = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phone_num))

# 여러 정보를 동시에 입력
data_sets = (("순신장군님", "02-984"), ("장보고", "010-8080"))
cur.executemany("insert into PhoneBook values (?, ?);", data_sets)

# 검색
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)

# fetch 명령어들
print(cur.fetchone())
print(cur.fetchmany(2))
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
print()
# 주의! 구문을 실행하고 commit을 하지 않으면 다 날아감!!

