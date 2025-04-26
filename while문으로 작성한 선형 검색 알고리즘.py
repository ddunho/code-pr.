#while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int: """시퀀스 a에서 key와 값이 같은 원소를 선형검색(while문)"""
    i = 0


    while True:
        if i == len(a):
            return -1 #검색에 실패하여 -1을 반환
        if a[i] == key:
            return 1
        i += 1

        
