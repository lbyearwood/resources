alarm = False
lights = False
movementGround = True
movementFirst = True
system = "on"
## 5a
if system == "on":
	print("System on. Security system activated")
	if movementGround == True:
		alarm = True
		lights = True
		print("Intruder on the ground floor")
	if movementFirst == True:
		alarm = True
		lights = True
		print("Intruder on the first floor")
## 5b
if system == "on" and (movementGround == True or movementFirst == True):
	alarm = True
	lights = True
	print("Intruder alert")
