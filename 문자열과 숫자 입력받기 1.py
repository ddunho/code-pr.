#이름을 입력받아 인사하기

print('이름을 입력하세요.: ', end='')
name = input()
print(f'안녕하세요? {name}님.')

#input 함수는 키보드로 문자열을 입력받아 반환.
#이름을 입력한 후 ENTER를 눌러야 입력이 완료된다.

name = input('이름을 입력하세요. : ')
print(f'안녕하세요? {name}님.')

"""두 코드의 차이점
첫번째 코드 : print()함수는 기본적으로 출력 후 줄을 바꾸는 특성이 있는데, 
end=''를 사용하여 줄바꿈을 없애고, 그 자리에 빈 문자열('')을 추가하여 커서를 같은줄에 남겨둔다.
print() input()이 분리되어 있어서 두줄로 작성됨.
두번째와 코드 : input()함수가 메시지를 직접 받아 화면에 출력 > 코드가 간결해 보임"""


