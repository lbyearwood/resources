def answerYorN():
   while True:
       response = input('Please enter [Y]es or [N]o >>').upper()
       if response != 'Y' and response != 'N':
           print('You must enter [Y]es or [N]o')
       else:
           break
   return response
userResponse = answerYorN()