import pickle
# 객체를 직렬화하여 파일에 저장하기
# data = {"name": "곰돌이사육사", "age": 22, "addr": "서울시 강남구 역삼동"}
# with open("data.pickle", "wb") as file:
#     pickle.dump(data, file)

# 파일에서 객체를 역직렬화 하여 복원하기
with open("data.pickle", "rb") as file:
    restored_data = pickle.load(file)

print(restored_data)
