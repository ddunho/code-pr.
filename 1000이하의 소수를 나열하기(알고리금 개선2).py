# 1000이하의 소수를 나열하기(알고리금 개선2)

counter = 0  #곱셈과 나눗셈을 합한 횟수
ptr = 0      #이미 찾은 소수의 갯수
prime = [None] * 500   #소수를 저장하는 배열

prime[ptr] = 2
ptr += 1


prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
        else:
