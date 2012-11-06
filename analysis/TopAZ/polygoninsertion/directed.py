def directed(n, l, orientation = 1):
    el = []
    for i in range(1, n):
        el.append(str(i) + ' ' + str(i + 1))
    el.append(str(n) + ' ' + str(1))
    k = int(n/l)
    if orientation == 1:
        for i in range(1, n, k):
            if i + k > n:
                el.append(str(i) + ' ' + str(1))
                break
            el.append(str(i) + ' ' + str(i + k))
    elif orientation == -1:
        for i in range(n - k + 1, 1, -1 * k):
            if i - k >= 1:
                el.append(str(i) + ' ' + str(i - k))
        if i > 1:
            el.append(str(i) + ' ' + str(1))
        el.append(str(1) + ' ' + str(n - k + 1))
    return el

if __name__ == "__main__":
    print directed(32, 4, -1)
