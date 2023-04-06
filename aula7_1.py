
fh = open('mbox-short.txt')
print(fh)
count = 0
soma = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    ipos = line.find(':')
    print(ipos)
    piece = line[ipos + 1:]
    print(piece)
    value = float(piece)
    print(value)
    lineWn = line.rstrip()
    print(lineWn.upper())
    soma += value
    count += 1

average = soma/count

print('Average spam confidence:', average)

