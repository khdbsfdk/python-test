dict_dev = {"아이폰":5, "아이패드":10, "테블릿":15}
print(type(dict_dev))
print(len(dict_dev))
dict_dev["맥북"] = 20
print(dict_dev,"\n")

# 사전식 구조의 매서드
dict_dev["아이폰16"] = 5
print(dict_dev)
dict_copy = dict_dev
print("copy -> ", dict_copy)
del dict_dev["아이폰"]
print(dict_dev)
print(dict_copy,"\n")
# 둘 다 원래의 딕셔너리 값을 바라보기 때문에 원 데이터가 수정되면 다 바뀜

dict_num = {"kim":111, "kang":222, "park":333}
dict_num["lee"] = 545
print(dict_num)
print(id(dict_num),"\n")

