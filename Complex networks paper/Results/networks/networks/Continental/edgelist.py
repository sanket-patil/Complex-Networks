ip = open("continental.txt", 'r')
edges = ip.read()
edges = edges.split('\n')
el = []
for e in edges:
    el.append(str(e))
print el
ip.close()
