num = 0
tot = 0
while True:

    sval = range(int(input('Enter a number: ')))
    s = list(sval)
    print(s)
    x = len(s)
    s.append(x)
    print(s)
    for x in s[1:]:
        #print(type(x))
        for _ in range(x):
            print(x, end=' ')
        print('')
