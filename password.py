import random
import string
letters = string.ascii_letters
x=''
y='Siria'
l=0
for i in range(1,(len(y)*2)+1):
    if i%2==0:
        x+=y[l]
        l+=1
    else:
        if random.randint(0,1)==0:
            x+=str(random.randint(0,9))
        else:
            x+=random.choice(letters)
print(x)