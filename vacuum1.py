import random
n = int(input("Enter the room numbers:-"))
a = 1
b = n
room = [[0*a]*b]
x = 0
y = 0
while x < a :
        while y < b :
            room[x][y] = random.choice([0,1])
            y+=1
        x+= 1
x = 0
y = 0
count = 0
while x <= a: 
    while y < b:
        if room[x][y] == 1:
            print("Vacuum agent is in room :",y+1)
            count = count +1
            room[x][y] = 0
        y+=1
    x+=1
print("Efficiency of the agent is ",(count/n)*100, end =" %")    
