import time

start_time = time.time() # 측정 시작

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# # N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수를 정렬하기
first = data[n - 1]
second = data[n - 2]

count = int(m/(k + 1))
count += m % (k+1)

result = 0
result += (count * first) # 가장 큰 수 더하기
result += (m-count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력

end_time = time.time() # 측정 종료
print("time :", end_time - start_time) # 수행 시간 출력