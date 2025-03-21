#뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None;
#뮤터블 시퀀스 a의 원소를 역순으로 정렬
    n = len(a)
    for i in range(n //2):
        ai], a[n - i - 1] = a[n - i - 1], a[i]
