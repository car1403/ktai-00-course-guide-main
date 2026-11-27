# 1부터 100까지 숫자 중 랜덤하게 10개를 뽑아 리스트에 담습니다.
# 10개의 숫자를 출력 한다

# 10개의 숫자 중 3의 배수만 출력한다.

# 3의 배수의 합과 평균을 구하시오



# [1 34 2 4 5 6 7 3]
import random

num_list = random.sample(range(1, 101), 10)
print(num_list)

sum_num = 0
count_num = 0

for num in num_list:
    if num % 3 == 0:
        print(num)
        sum_num += num
        count_num += 1

print(f"3의 배수 합: {sum_num}")
print(f"3의 배수 평균: {sum_num / count_num}")


