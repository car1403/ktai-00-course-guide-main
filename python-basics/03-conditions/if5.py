num = int(input("정수 입력> "))

if num == 0:
    print("잘못된 값입니다.")
    exit()

if num == 1:
    print("캐쉬카드 입니다.")
elif num == 2:
    print("신용카드 입니다.")
elif num == 3:
    print("타은행 카드 입니다.")
else:
    print("카드가 아닙니다.")