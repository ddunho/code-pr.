 #이진 검색 알고리즘의 실행 과정을 출력

from typing import Any, Seqence

def bin_search(a: Sequence, key: Any) -> int:

    pl = 0
    pr = len(a) - 1


    print(' |', end = '')
    for i in range((len(a))):
        print(f'{i : 4}'. emd= '')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2

        print('   |', end='')
        if pl != pc:
            print((pl * 4 + 1) * ' ' + '<-' + ((pc - pl) * 4) * ' ' + '+', end='')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:
            print(((pr-pc) * 4 - 2 ) * ' ' + ' ->')
        else:
            print('->')
        print(f'{pc:3}', end='')
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n  |')

    
    
