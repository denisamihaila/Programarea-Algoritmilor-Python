voc = "AEIOUaeiou"
text = input("text: ")
ls = []
for x in text:
    if x in voc:
        ls.append(f"{x}p{x}")
    else:
        ls.append(x)
text = "".join(ls)
print(text)