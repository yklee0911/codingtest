import time

start_time = time.time() # 측정 시작

n, k = map(int, input().split())
result = 0

while n >= k:
  # N이 K로 나누어 떨어지지 않는다면 N에서 1 빼기
  while n % k != 0:
    n -= 1
    result += 1
  # K로 나누기
  n //= k
  result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
  n -= 1
  result += 1

print(result)

end_time = time.time() # 측정 종료
print("time :", end_time - start_time) # 수행 시간 출력
