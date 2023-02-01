import random 
lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
numbers = "0123456789"
symbols = "{}[]()'./,*&%@#-_"

together=lower+upper+numbers+symbols;
lenqth=20
for i in range (1,4):
    password="".join(random.sample(together,lenqth))
    print("Password #", i,": ",password)
    