raw = '''xx-xh
vx-qc
cu-wf
ny-LO
cu-DR
start-xx
LO-vx
cu-LO
xx-cu
cu-ny
xh-start
qc-DR
vx-AP
end-LO
ny-DR
vx-end
DR-xx
start-DR
end-ny
ny-xx
xh-DR
cu-xh
'''
raw = raw.splitlines()
raw = [r.split('-') for r in raw]
Nodes = {}
print(raw)
others = []
lower = []
for r in raw:
    if r[0] != "start":
        others.append([r[1],r[0]])
    if r[0].islower() == True:
        lower.append(r[0])
    if r[1].islower() == True:
        lower.append(r[1])
for o in others:
    raw.append(o)
print(raw)

for r in raw:
    Nodes[r[0]] = []
for r in raw:
    Nodes[r[0]].append(r[1])

print(Nodes)

def find_all_paths(graph, start, end, path=[]): #part 1
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node.lower() not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

all_paths = find_all_paths(Nodes,'start', 'end')
#for p in all_paths:
    #print(p)
print(len(find_all_paths(Nodes,'start', 'end')))

def find_all_paths(graph, start, end, path=[]): #part 2
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node != 'start' and sum(el in lower for el in path) <= len(set(path).intersection(set(lower)))+1:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

all_paths = find_all_paths(Nodes,'start', 'end')
#for p in all_paths:
    #print(p)
print(len(find_all_paths(Nodes,'start', 'end')))
lower = list(set(lower))
lower.remove('start')
lower.remove('end')
print(lower)
final = []
from collections import Counter
for p in all_paths:
    c = Counter(p)
    good = True
    for l in lower:
        if c[l] > 2:
            good = False
    if sum(el in lower for el in p) > len(set(p).intersection(set(lower)))+1:
        good = False
    if p.count('start') > 1:
        good = False
    if good == True:
        final.append(p)
#for f in final:
    #print(f)
print(len(final))
                
'''xx-xh
vx-qc
cu-wf
ny-LO
cu-DR
start-xx
LO-vx
cu-LO
xx-cu
cu-ny
xh-start
qc-DR
vx-AP
end-LO
ny-DR
vx-end
DR-xx
start-DR
end-ny
ny-xx
xh-DR
cu-xh
'''
    
            
