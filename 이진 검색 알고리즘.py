#이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:

    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
