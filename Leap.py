Year =int(input("Enter the year :"))
If year % 4 == 0:
  If year % 100 == 0:
    If year % 400 == 0:
      print("Leap year")
    else:
      print("Not a leap year")
  else:
    print("Leap year")
else:
  print("Not a leap year")