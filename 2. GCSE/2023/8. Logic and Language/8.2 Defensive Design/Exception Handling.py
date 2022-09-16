list = [5,4,3,2,1,0,-1,-2,-3]

for i in range(0,len(list)):
    try:
        result = 10 / list[i]
        print(result)
    except Exception as e: # catch the error and place it in e
        print(e)