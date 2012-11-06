import re

ip = open('southwest-tokens.txt', 'r')
tokens = ip.read()
ip.close()
airport = re.compile('[(][A-Z][A-Z][A-Z][)]')
l = airport.findall(tokens)
l = list(set(l))
op = open('southwest-airports.txt', 'w')
op.write('\n'.join(l))
op.close()
