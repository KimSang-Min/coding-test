# 입력
# 영문자 1개가 입력된다.
# (a ~ z)

# 출력
# a부터 입력한 문자까지 순서대로 공백을 두고 한 줄로 출력한다.

inputVar = ord(input())
s = ord('a')

while s <= inputVar:
    print(chr(s), end=" ")
    s += 1