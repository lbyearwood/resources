# this program will break (stop) the loop once count equals 100
count = 0
while True:
    if count > 99:
        break
    print(count)
    count = count + 1