#세 정수를 입력받아 중앙값 구하기 2
def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c #else를 추가하면 가독성과 협업성은 더 좋아짐. 기능적으론 동일

"""b >= a, b <= a / a > b, a < b와 같이 뒤집은 판단은,
if 문의 조건식이 성립하지 않으면 elif문은 이 판단을 수행할 필요가 없어지므로 효율x
(a와 b의 비교를 마친 상태에서 다시 비교하는것이 효율적이지 않다)"""
