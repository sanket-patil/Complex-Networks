import re

ip = open('southwest-schedule.txt')
txt = ip.read().split()
ip.close()
op = open('southwest-tokens.txt', 'w')
op.write('\n'.join(txt))
op.close()
ip = open('southwest-tokens.txt', 'r')
tokens = ip.read().split('\n')
airport = re.compile('[(][A-Z][A-Z][A-Z][)]')
el = ''
src = ''
for t in range(len(tokens)):
    m = airport.match(tokens[t])
    if m:
        if t > 2:
            if tokens[t - 2] == 'To' or tokens[t - 3] == 'To' or tokens[t - 4] == 'To':
                dst = m.group()
                el = el + '\n' + src + ' ' + dst
            elif tokens[t - 2] == 'From' or tokens[t - 3] == 'From' or tokens[t - 4] == 'From':
                continue
            else:
                src = m.group()
ip.close()
op = open('southwest-flights.txt', 'w')
op.write(el)
op.close()
