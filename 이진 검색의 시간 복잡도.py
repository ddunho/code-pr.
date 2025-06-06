#이진 검색의 시간 복잡도

def bin_search(a: Sequence, key: Any) -> int:

    pl = 0
    pr = len(a) - 1


    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
