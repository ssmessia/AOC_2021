raw = '''KBKPHKHHNBCVCHPSPNHF

OP -> H
CF -> C
BB -> V
KH -> O
CV -> S
FV -> O
FS -> K
KO -> C
PP -> S
SH -> K
FH -> O
NF -> H
PN -> P
BO -> H
OK -> K
PO -> P
SF -> K
BF -> P
HH -> S
KP -> H
HB -> N
NP -> V
KK -> P
PF -> P
BK -> V
OF -> H
FO -> S
VC -> P
FK -> B
NK -> S
CB -> B
PV -> C
CO -> N
BN -> C
HV -> H
OC -> N
NB -> O
CS -> S
HK -> C
VS -> F
BH -> C
PC -> S
KC -> O
VO -> P
FB -> K
BV -> V
VN -> N
ON -> F
VH -> H
CN -> O
HO -> O
SV -> O
SS -> H
KF -> N
SP -> C
NS -> V
SO -> F
BC -> P
HC -> C
FP -> H
OH -> S
OB -> S
HF -> V
SC -> B
SN -> N
VK -> C
NC -> V
VV -> S
SK -> K
PK -> K
PS -> N
KB -> S
KS -> C
NN -> C
OO -> C
BS -> B
NV -> H
FF -> P
FC -> N
OS -> H
KN -> N
VP -> B
PH -> N
NH -> S
OV -> O
FN -> V
CP -> B
NO -> V
CK -> C
VF -> B
HS -> B
KV -> K
VB -> H
SB -> S
BP -> S
CC -> F
HP -> B
PB -> P
HN -> P
CH -> O'''

test='''NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''
from collections import Counter

raw = raw.splitlines()
word, d = '',{}
d_map = {}

split = False
for r in raw:
    if r == '':
        split = True
        continue
    if split == True:
        tmp = r.split(' -> ')
        d[tmp[0]] = tmp[1] #part 1 dictionary
        #part 2 dictionary: pair => string 1, string 2, count, letter added
        d_map[tmp[0]] = [tmp[0][0]+tmp[1],tmp[1]+tmp[0][1],0,tmp[1]]
    else:
        word = r
word_copy = word
for i in range(10): #do this naively for part 1, just keep appending to the string
    pairs = []
    w = ''
    for j in range(len(word)-1):
        pairs.append(word[j:j+2])
    for p in pairs:
        try:
            p = p[:1]+d[p]+p[1:]
        except KeyError:
            continue
        w+=p[:-1]
    w+=p[2:]
    word = w

    counts = Counter(word)
    counts = counts.values()
    print(i, max(counts)-min(counts))
    max_c, min_c, diff = max(counts), min(counts), max(counts)-min(counts)
                
word = word_copy
counts = {}
for c in word: #set initial counts
    try:
        counts[c]+=1
    except KeyError:
        counts[c]=1
pairs = []
for j in range(len(word)-1):
    pairs.append(word[j:j+2])
for p in pairs:
    d_map[p][2] = 1
for i in range(40):
    pairs = []
    for key in d_map.items(): #pairs represent the current string
        k = key[0]
        if d_map[k][2] != 0:
            pairs.append([k,key[1][2]]) #pair, number of pairs in "string"
    for pair in pairs:
        p = pair[0]
        v = pair[1]
        d_map[d_map[p][0]][2]+=v
        d_map[d_map[p][1]][2]+=v
        try:
            counts[d_map[p][3]]+=v
        except KeyError:
            counts[d_map[p][3]] = 1
        d_map[p][2]-=v

    print(i, max(counts.values())-min(counts.values()))

    
        
    