# 변수 (Variable)
# 정수, 실수, 문자
# 변수들의 집합
# List 

num1 = 10
num2 = 19.2
str = "Hello"
num_list = [1, 2, 3, 4, 5]

print(num_list)
print(num_list[3]) # 4
print(len(num_list)) # length
print(num_list[-3]) # 3
# 2 3 4
print(num_list[1:4]) # 1번째 부터 4번째 전까지

print(num_list[1:]) # 2 3 4 5

print(num_list[:3]) # 1 2 3

num2_list = [5,8,2,9,1]
print(num2_list)
print(sorted(num2_list)) # 정렬
print(sorted(num2_list, reverse=True)) # 내림차순 정렬
# 가장 큰수를 출력 하시오
print(max(num2_list)) # 9
