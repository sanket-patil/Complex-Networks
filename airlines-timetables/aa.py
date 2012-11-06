import re

ip = open('aa-schedules.txt')
schedule = ip.read()
ip.close()

routes = {}
flights = schedule.split('From')
print flights[0]
print flights[1]
print flights[2]
#print flights[0].splitlines()
#print flights[1].splitlines()

