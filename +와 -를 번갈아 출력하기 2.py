#+와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력합니다.')
n = int(input('몇개를 출력할까요?: '))

for _ in range(n // 2): #_는 변수이지만 변수의 값을 사용하지 않겠다는 관례적의미
    print('+-', end='')


if n % 2:
    print('+', end='')


print()
