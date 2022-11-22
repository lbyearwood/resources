daysOftheWeek = ['mon','tue','wed','thu','fri','sat','sun']
i = 0
while i <= 7:
  try:
   print(daysOftheWeek[i])
   i +=1
  except Exception as e:
    print(e)