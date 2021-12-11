data = list(map(int, input().split()))

data.sort()

target = 1

for i in data:
  if target < data[i]:
    break
  else:
    target += data[i]

print(target)
