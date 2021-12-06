for i in range(80):
    number = len(fish)
    for j in range(number):
        if fish[j] == 0 :
            fish[j] = 6
            fish.append(8)
        else:
            fish[j]-=1
print(len(fish))
'''

counts = [0,0,0,0,0,0,0,0,0]
for num in fish:
    counts[num]+=1
for i in range(257):
    print(i, counts, sum(counts))
    zero_count = counts[0]
    for j in range(8):
        counts[j] = counts[j+1]
    counts[8] = zero_count
    counts[6]+= zero_count