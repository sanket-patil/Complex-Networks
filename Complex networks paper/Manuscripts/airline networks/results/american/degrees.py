ip = open('indegrees.txt', 'r')
indegrees = ip.read().split('\n')
ip.close()
print indegrees
ip = open('outdegrees.txt', 'r')
outdegrees = ip.read().split('\t')
ip.close()
print outdegrees
for i in range(len(indegrees)):
    if indegrees[i] != outdegrees[i]:
        print indegrees[i], outdegrees[i]
