a = int(input())
b = list(map(int, input().split(" ")))
c = int(input())
d = []
for i in b:
  if i == c:
    d.append(0)
print(len(d))