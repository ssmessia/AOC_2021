raw = '''5212166716
1567322581
2268461548
3481561744
6248342248
6526667368
5627335775
8124511754
4614137683
4724561156
'''
raw = raw.splitlines()
raw = [[int(x) for x in row] for row in raw]
for r in raw:
     r.append("X")
     r.insert(0,"X")
temp = ["X"] * 12
raw.append(temp)
raw.insert(0, temp)
print(raw)
