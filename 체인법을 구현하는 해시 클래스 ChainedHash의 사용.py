#체인법을 구현하는 해시 클래스 ChainedHash의 사용

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])


def select_menu() -> Menu:
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '    ', end = '')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)
