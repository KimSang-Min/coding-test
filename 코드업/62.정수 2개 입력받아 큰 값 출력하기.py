# 입력
# 두 정수가 공백을 두고 입력된다.

# 출력
# 두 정수 중 큰 값을 10진수로 출력한다.

n1, n2 = map(int, input().split())

print(n1 if n1 > n2 else n2)