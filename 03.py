import copy
raw = raw.splitlines()
most_common = []
least_common = []
for i in range(len(raw[0])):
    total = 0
    for j in range(len(raw)):
        if raw[j][i] == '1':
            total +=1
        else:
            total -=1
    if total > 0:
        most_common.append('1')
        least_common.append('0')
    else:
        most_common.append('0')
        least_common.append('1')
print(int(''.join(most_common),2)*int(''.join(least_common),2))
mc = copy.deepcopy(raw)
lc = copy.deepcopy(raw)
for i in range(len(mc[0])):
    total = 0
    mc_one = []
    mc_zero = []
    for j in range(len(mc)):
        if mc[j][i] == '1':
            total +=1
            mc_one.append(mc[j])
        else:
            total -=1
            mc_zero.append(mc[j])
    if total >= 0:
        mc = copy.deepcopy(mc_one)
    else:
        mc = copy.deepcopy(mc_zero)
    if len(mc) == 1:
        print(mc)
        break
   
for i in range(len(lc[0])):
    total = 0
    lc_one = []
    lc_zero = []
    for j in range(len(lc)):
        if lc[j][i] == '1':
            total +=1
            lc_one.append(lc[j])
        else:
            total -=1
            lc_zero.append(lc[j])
    if total >= 0:
        lc = copy.deepcopy(lc_zero)
    else:
        lc = copy.deepcopy(lc_one)
    if len(lc) == 1:
        print(lc)
        break

print(int(mc[0],2)*int(lc[0],2))
