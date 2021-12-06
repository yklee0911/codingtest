import time

start_time = time.time() # 측정 시작

# N 입력 받기
n = int(input())
# N 보다 작은 자연수를 공백으로 구분하여 입력 받기
data = list(map(int, input().split()))

# 오름차순으로 정렬
data.sort()

sum = 0 # 최대 그룹 수
count = 0 # 그룹에 포함된 인원

for i in data:
  count += 1
  if count >= i:
    sum += 1
    count = 0

# 최대 그룹수 출력
print(sum)

end_time = time.time() # 측정 종료

print("time :", format(end_time - start_time))# 수행 시간 출력