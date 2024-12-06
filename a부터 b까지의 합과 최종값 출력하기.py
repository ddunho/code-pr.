#a부터 b까지의 합과 최종값 출력하기

print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('정수 a를 입력하세요.: '))
b = int(input('정수 b를 입력하세요,: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end ='') #i < b면 합을 구하는 과정 출력
    else:
        print(f'{i} = ', end ='') #i >= b면 최종값 출력을 위해 i =을 출력
    sum += i

print(sum)
