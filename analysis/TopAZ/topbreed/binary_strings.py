import random

def create_rbs(num, length):
    rbs = []
    for i in range(num):        
        bs = ''.join([str(random.randint(0, 1)) for j in range(length)])
        rbs.append(bs)
    return rbs

if __name__ == '__main__':
    print create_rbs(5, 32)
