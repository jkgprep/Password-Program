#Jonas Kennedy, 11/16/21, allows the user to guess a password
pass1 = input("what's your first password? ")
pass2 = input("what's your second password? ")
if pass1=="Pizza" or pass1=="pizza" or pass1=="Arugula" or pass1=="arugula" and pass2=="Pizza" or pass2=="pizza" or pass2=="Arugula" or pass2=="arugula":
  print("The password is correct")
else:
  print("Wrong password, try harder")