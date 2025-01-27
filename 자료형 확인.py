#자료형 확인

x = 0

type(x + 17) #x + 17의 자료형 확인
>> <class 'int'>

type(x = 17) #x = 17의 자료형 확인 >> 오류 발생
Traceback (most recent call last):
    File "pyshell#9>", line 1, in <module>
    type(x = 17)
Type Error: type() takes 1 or 3 arguments

#x = 17은 식(expression)이 아니라 문(statement)이므로 자료형 확인 불가능
