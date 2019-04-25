# the point of this script is to generate random rectangles for the letter I

from random import randint

m = 20
n = 10
o = 20
pert = 2
dist = 35

x1 = 30
y1 = 30
y2 = 60
x2 = 60

count = 0

i_list = [
	90, 91,
	110, 111,
	130, 131,
	150, 151,
	170, 171,
	190, 191,
	210, 211,
	230, 231,
	250, 251,
	270, 271,
	290, 291,
	310, 311,
	]

for k in range(o):
	for j in range(m):
		count += 1
		print("<!-- "+str(count)+" -->")
		for i in range(n):
			if count in i_list:
				print(
					"<polygon class=\"st7\" points=\""+
					str(randint(x2+j*dist-i*2-(pert+2), x2+j*dist-i*2+(pert+2)))+","+
					str(randint(y2+k*dist-i*2-(pert+2), y2+k*dist-i*2+(pert+2)))+" "+
					str(randint(x1+j*dist+i*2-(pert+2), x1+j*dist+i*2+(pert+2)))+","+
					str(randint(y2+k*dist-i*2-(pert+2), y2+k*dist-i*2+(pert+2)))+" "+
					str(randint(x1+j*dist+i*2-(pert+2), x1+j*dist+i*2+(pert+2)))+","+
					str(randint(y1+k*dist+i*2-(pert+2), y1+k*dist+i*2+(pert+2)))+" "+
					str(randint(x2+j*dist-i*2-(pert+2), x2+j*dist-i*2+(pert+2)))+","+
					str(randint(y1+k*dist+i*2-(pert+2), y1+k*dist+i*2+(pert+2)))+" "+
					" \t\"/>")
			else:
				print(
					"<polygon class=\"st"+str(randint(2,6))+"\" points=\""+
					str(randint(x2+j*dist-i*2-pert, x2+j*dist-i*2+pert))+","+
					str(randint(y2+k*dist-i*2-pert, y2+k*dist-i*2+pert))+" "+
					str(randint(x1+j*dist+i*2-pert, x1+j*dist+i*2+pert))+","+
					str(randint(y2+k*dist-i*2-pert, y2+k*dist-i*2+pert))+" "+
					str(randint(x1+j*dist+i*2-pert, x1+j*dist+i*2+pert))+","+
					str(randint(y1+k*dist+i*2-pert, y1+k*dist+i*2+pert))+" "+
					str(randint(x2+j*dist-i*2-pert, x2+j*dist-i*2+pert))+","+
					str(randint(y1+k*dist+i*2-pert, y1+k*dist+i*2+pert))+" "+
					" \t\"/>")
		print("")