import sys

if len(sys.argv) < 2:
    print 'Usage: python', sys.argv[0], '<airline_flight_list.txt>'
    exit()
ip = open(sys.argv[1])
flights = ip.read().split('\n')
print len(flights)
ip.close()
airports = []
for flight in flights:
    nodes = flight.split()
    for node in nodes:
        if not node in airports:            
            airports.append(node)
print len(airports)
opfile = sys.argv[1].split('.txt')[0] + '-airports.txt'
op = open(opfile, 'w')
op.write('\n'.join(airports))
op.close()
print 'Output file:', opfile