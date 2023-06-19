print("This program converts milliseconds into hours, minutes, and seconds")

while True:
    a = input("Enter a number to convert or type 'exit' to end the program: ")

    if a.lower() == "exit":
        print("The program is shutting down. Goodbye!")
        break

    try:
        a = int(a)
        if a < 1:
            print("Enter a value greater than 0.")
            continue
    except ValueError:
        print("Invalid input. Enter a numeric value or 'exit'.")
        continue
    else:
      if  1000 < a < 60000:
        b= a//1000
        print(f"{a} is {b} second")
        break
      elif 60000 < a < 3600000:           
        c=a // 60000   #dakika
        d= a % 60000
        e=d // 1000     #saniye
        print(f"{a} is {c} minutes and {e} seconds")
        break
      else:
        f = a//3600000    #saat                       
        g = a % 3600000     # saaaten  arta kalanlar
        x = g // 60000      #dakika     
        y = g % 60000       #dakikadan arta kalan 
        z = y // 1000       #saniye
        print(f"{a} is {f} hours , {x} minutes and {z} seconds ")
        break