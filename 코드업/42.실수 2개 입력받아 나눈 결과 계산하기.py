# 입력
# 2개의 실수(f1, f2)가 공백으로 구분되어 입력된다.

# 출력
# f1을 f2로 나눈 결과를 소숫점 이하 넷째 자리에서 반올림하여 소숫점 세 번째 자리까지 출력한다.

f1, f2 = map(float, input().split())

print(format(f1/f2, ".3f"))