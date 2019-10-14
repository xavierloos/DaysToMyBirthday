import datetime

currentDate = datetime.date.today()
print("\n**************************")
print("*** BIRTHDAY COUNTDOWN ***")
print("**************************")
userInput = input("\nPlease enter your birthday \n(Month/Day/Year)\n")

birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
#Options if the user wants to try another date
def options():
  print('\nDo you want to try another date? \n0 = NO, 1 = YES')
  choice = int(input())
  if choice == 1:
    userInput = input("\nPlease enter your birthday \n(Month/Day/Year)\n")

    birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()
    if birthday < currentDate: 
      print("\n======================================")
      print("Happy Birthday, Your birthday has over")
      print("======================================\n")
      options()
    else:
      days = birthday - currentDate
      print("\n===============================")
      print("Days to your birthday: {} days".format(days.days))
      print("===============================\n")
      options()
  else:
    print("Bye")
    exit()


if birthday < currentDate: 
  print("\n======================================")
  print("Happy Birthday, Your birthday has over")
  print("======================================\n")
  options()
else:
  days = birthday - currentDate
  print("\n===============================")
  print("Days to your birthday: {} days".format(days.days))
  print("===============================\n")
  options()