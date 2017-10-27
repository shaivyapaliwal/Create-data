import random

#Format Date, Hour, ID, Traffic, Rate(Min)

file = open("traffic.data", "a")

for i in range(30):
	for j in range(24):
		Traffic_Val = random.randint(0, 40)/10
		if Traffic_Val < 0.1:
			Traffic_Val = 0.1
		if Traffic_Val > 1:
			if Traffic_Val > 2:
				if Traffic_Val > 3:
					if Traffic_Val == 4:
						Min_Rate = 500
					else:
						Min_Rate = 400 + (Traffic_Val-3)*100
				else:
					Min_Rate = 375 + (Traffic_Val-2)*25
			else:
	 			Min_Rate = 350 + (Traffic_Val-1)*25
		else:
			Min_Rate = 300 + (Traffic_Val)*50

		a = str(i+1) + ',' + str(j + 1) + ',' + str('dl_110085_h1') + ',' + str(Traffic_Val) + ',' + str(Min_Rate)
		file.write(a+'\n')