import random

file = open("traffic.data", "a")
for i in range(30):
    for j in range(24):
        a = str(i+1) + ',' + str(j + 1) + ',' + str(1) + ',' + str(random.randint(0, 40)/10)
        file.write(a+'\n')



