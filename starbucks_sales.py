file_name = "starbucks_daily_sales.txt"
# with open(file_name, "r", encoding="utf-8") as file:
#     file_data = file.read()
# print(file_data)

f = open(file_name, "r", encoding="utf-8")
head = f.readline() # 파일의 첫 번째 줄을 읽음
head_list = head.split()    # 메뉴명을 공백 기준으로 잘라서 리스트로 변환

espresso = []
americano = []
cafelatte = []
cappuccino = []

for line in f: # f는 파일 객체이며 파일의 읽는 위치를 가리키는 식별자, 두번째 라인 부터 반복 처리
    data_list = line.split()    # 각각의 라인을 공백 기준으로 자름
    espresso.append(int(data_list[1]))
    americano.append(int(data_list[2]))
    cafelatte.append(int(data_list[3]))
    cappuccino.append(int(data_list[4]))
    print(data_list)
f.close()

print(f"{head_list[1]} 전체 판매량 : {sum(espresso)}, 일 평균 판매량 : {sum(espresso)/len(espresso)}")
print(f"{head_list[2]} 전체 판매량 : {sum(americano)}, 일 평균 판매량 : {sum(americano)/len(americano)}")
print(f"{head_list[3]} 전체 판매량 : {sum(cafelatte)}, 일 평균 판매량 : {sum(cafelatte)/len(cafelatte)}")
print(f"{head_list[4]} 전체 판매량 : {sum(cappuccino)}, 일 평균 판매량 : {sum(cappuccino)/len(cappuccino)}")