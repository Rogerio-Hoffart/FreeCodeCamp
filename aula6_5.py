text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
# print(ipos)
piece = text[ipos+1:]
# print(piece)
value = float(piece)
print(value)

word = "bananana"
i = word.find("b")
print(i)

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print(bob)