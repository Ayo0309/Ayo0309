print("Welcome to this python seconds calculator")
print("This app can convert the time to seconds")
hour = int(input("Enter the number of hours: "))
minute = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))
hours_to_seconds = (hour*60*60)
minutes_to_seconds = (minute*60)
print("The time in seconds is: ",hours_to_seconds + minutes_to_seconds + seconds)