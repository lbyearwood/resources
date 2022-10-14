try:
    file = open("test2.txt","r")
    x = file.read()
    print(x)
except Exception as e:
    print(e)

print("Proof")

