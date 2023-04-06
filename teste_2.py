count = 0
sh = input('Entre com uma Palavra:')
s = list(sh)
#print(s)
x = len(s)
s.append(x)
#print(s)
for y in sh:
    #print(sh[count])
    count += 1
    contador = 0
    for _ in range(count):
        print(s[contador], end=' ')
        contador += 1
    print('')
