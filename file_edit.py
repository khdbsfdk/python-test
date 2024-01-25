# read() : 파일 전체를 읽어서 문자열로 반환
# readline(): 한 줄씩 읽은 문자열을 반환
# readlines(): 파일의 모든 내용을 줄 단위로 잘라서 반환(리스크 형태)
# 근데 1GB 넘는 파일은 read로 읽으면 컴터 느려진다
# write() : 파일에 쓰기 작업을 한다
# tell() : 어디까지 읽고 썼는지 위치 반환

# 파일 쓰기
f = open("demo.txt", 'wt', encoding="utf-8")
f.write("첫 번째\n두 번째\n세 번째") # 줄바꿈은 수동!
f.close() # 항상 종료해야해!

# 파일 읽기
f = open("demo.txt", 'rt', encoding="utf-8")
result = f.read()
print(result)
print()

# 다시 처음으로 파일 포인터 이동
f.seek(0)
# 한번에 한줄을 읽어서 처리
print(f.readline(), end='') # readine은 줄 바꿈이 기본이라 \n이 있으면 end=''로 해결 가능
print(f.readline())

# 전체를 리스트로 반환
f.seek(0)
list_f = f.readlines()
print(list_f)

f.close()

