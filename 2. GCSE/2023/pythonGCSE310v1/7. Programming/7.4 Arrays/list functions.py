register = [] #
register = ["Yusuf","Ayo","Aaron"] # declare a list with values
register.append("Mehdi")
register.append("Sami")
register.append("Wyn")
register[0] = "Hussein" # update index 0
register.pop(0)
index = register.index("Wyn")
print(index)
print(register)