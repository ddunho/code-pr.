#배열 a의 원소중에서 최대값을 구하기

def max_of(a):
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
            
