for number in range(100,999):
 hundreds = number // 100  # 465 int_divsion 100 = 4
 hund_remainder = number % 100  # 465 rem_divsion 100 = 65
 tens = hund_remainder // 10  # 65 int_divsion 10 = 6
 units = hund_remainder % 10  # 65 rem_divsion 10 = 5
 sumOfCubes = hundreds ** 3 + tens ** 3 + units ** 3
 if number == sumOfCubes:
    print("sum of cubes is ", hundreds, tens, units)