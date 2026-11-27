num_list = list(range(1, 101))
# 1부터 100까지의 숫자에서 홀수만 출력 하세요
# 홀수들의 합을 구해서 출력하시오
odd_sum = 0
even_sum = 0

for num in num_list:
    if num % 2 == 1:
        odd_sum = odd_sum + num
    if num % 2 == 0:
        even_sum = even_sum + num

print(odd_sum)
print(even_sum)