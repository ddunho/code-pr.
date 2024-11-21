#세 정수를 입력받아 최대값 구하기

print('세 정수의 최대값을 구합니다.')

a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum: maximum = b #b > maximum이 참일때, maximum = b
if c > maximum: maximum = c

print(f'최대값은 {maximum}입니다.')
#{maximum}과 같이 문자열 안에 변수나 계산된 값을 삽입해야 할 때, f-string 사용
