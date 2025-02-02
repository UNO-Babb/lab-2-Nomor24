#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute



  #TODO:
  #Ask user for hours
  addHours = int(input("Enter the number of hours to add:"))

  #Ask user for minutes
  addMinutes = int(input("enter the number of minutes to add:"))

  #Calculate the time after the user-supplied time has passed.
  totalMinutes = currentMinute + addMinutes
  newMinute = totalMinutes % 60
  extraHour = totalMinutes // 60
  totalHours = currentHour + addHours + extraHour
  newhour24 = totalHours % 24
#Do not use any if statements in calculating the time.
  
  newhour12 = ((newhour24-1) % 12) + 1
#Output the future time in standard format "HH:MM"
  print("The time will be: " + f"{newhour12:02}:{newMinute:02}")

if __name__ == '__main__':
  main()
