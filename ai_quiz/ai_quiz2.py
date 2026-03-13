numbers = [3,7,2,9,4,10,15,7,3,7] #7출력 max값 찾기
count = {}
for n in numbers:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1
print(max(count, key=count.get))
