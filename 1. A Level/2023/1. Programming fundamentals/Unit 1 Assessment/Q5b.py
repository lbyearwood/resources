def openFile():
   fileName = input("Please enter filename to open:\n")
   fileName += ".txt"
   try:
      file = open(fileName,"r")
      content = file.read()
      print("Continue with the rest of the program")
   except  Exception as e:
      print(e)
openFile()
