import time

start_time = time.time() # 측정 시작

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# # N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수를 정렬하기
first = data[n - 1]
second = data[n - 2]

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
      if m == 0: #M이 0이라면 반복문 탈출
        break
      result += first
      m -= 1 # 더할 때마다 1씩 빼기
    if m == 0:
      break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1 # 더할 때마다 1씩 빼기

end_time = time.time() # 측정 종료
print(result)
print("time :", end_time - start_time) # 수행 시간 출력
