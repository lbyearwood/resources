l = list(i for i in range(1,11))
head = l[0:1]
tail = l[1:]
print(head)
print(tail)

while True:
    if len(tail) == 0:
        break
    head = tail[0:1]
    tail = tail[1:]
    print(f"Head:{head}")
    print(f"Tail:{tail}")