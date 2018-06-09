print("a".ljust(3)+"bn".ljust(3))
print("as".ljust(3) + "n".ljust(3))
info =["sdfsf","sdf","dfgkjdgkfdjgndk"]
info2=["2fgf","sd","werwerwererewrewrwer"]
print(info[0].ljust(10) + info[1].ljust(5) + info[2].ljust(20))
print(info2[0].ljust(10) + info2[1].ljust(5) + info2[2])

print()
book = {"far":"arnulf","mor":["peder"],"barn1":["førstebarn"],"hund":["det var nok med barn","noe"]}
printlen = 0
for key,value in book.items():
    if len(key) > printlen:
        printlen = len(key)

for key,value in book.items():
    if type(value) == list:
        barn = ", ".join(value)
    else:
        barn = value
    print(key.rjust(printlen+2),":",barn)