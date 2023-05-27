# Project : Print ASCII
# Author : Seong-Hun Son
# St_ID : 21812371
# Major : Robotics engineering
# Date of last update : 2023.3.16.
# Major features : print,for
print('Homework 4.1 아스키 코드 출력')
print('로봇기계공학과, 학번 : 21812371, 이름 : 손성훈')

#리스트 생성
L_digits=[]
L_upper=[]
L_lower=[]

for i in range(48,58):  #리스트에 숫자 추가
    L_digits.append(chr(i))
for i in range(65,91):  #리스트에 대문자 추가
    L_upper.append(chr(i))
for i in range(97,123):  #리스트에 소문자 추가
    L_lower.append(chr(i))

print(f'L_digits (size : {len(L_digits)}) {L_digits}')
print(f'L_upper (size : {len(L_upper)}) {L_upper}')
print(f'L_lower (size : {len(L_lower)}) {L_lower}')
