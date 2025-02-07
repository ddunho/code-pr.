#시퀀스 원소의 최대값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any: #시퀀스형 a원소의 최대값을 반환
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
        return maximum
    
