names = ["Ersin","James", "John", "Emma"]
surnames = ["Sari","Oliver", "Smith", "Brown"]
birth_days = [18,15, 22, 8]
birth_months = [1,3, 6, 12]
birth_years = [2007,1984, 1994, 2001]
string_number=0
a=input("Please enter your name:").capitalize()
if a in names:
  string_number=names.index(a)
  b=input("Enter your surname:").capitalize()
  if b in surnames and surnames.index(b) == string_number:
    c=input("Please enter your birthday (MM/DD/YYYY):").split("/")
    MM=int(c[0])
    DD=int(c[1])
    YYYY=int(c[2])
    if DD in birth_days and birth_days.index(DD) == string_number and MM in birth_months and birth_months.index(MM) == string_number and YYYY in birth_years and birth_years.index(YYYY) == string_number:
      print("You are a customer")
    else:
      print("You have entered an incorrect value!")
  else:
    print("You are not a customer")
else:
  print("You are not a customer")