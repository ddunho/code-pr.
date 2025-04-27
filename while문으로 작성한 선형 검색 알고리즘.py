#while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1


  
