import re

ip = open('us-airways-schedules.txt')
schedule = ip.read()
ip.close()

sources = []
destinations = []
pages = schedule.split('')
for page in pages[1:2]:    
    lines = page.split('\n')
    lines = [line for line in lines if line != '']    
    src = 
