import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return "".join(tempList)

# uppercase characters
character1 = chr(random.randint(65,90))
character2 = chr(random.randint(65,90))

#lowercase characters
character3 = chr(random.randint(97,122))
character4 = chr(random.randint(97,122))

#symbol characters
character5 = chr(random.randint(32,47))
character6 = chr(random.randint(32,47))

#digit characters
character7 = chr(random.randint(48,57))
character8 = chr(random.randint(48,57))

password = ""

for i in range(1, 9):
  temp = "character" + str(i)
  temp = locals()[temp]
  password += temp
  print (temp)

password = shuffle(password)
print (password)