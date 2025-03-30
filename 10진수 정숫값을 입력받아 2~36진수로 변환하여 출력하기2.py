#10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기2

def card_conv(x: int, r: int) -> str:
    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = len(str(x))
    
