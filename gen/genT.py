# the point of this script is to create non intersecting circles

from random import random

h = 800
w = 800

n_in = 300
n_out = 7500

size_in = 8
size_out = 3

perturb_in = 5
perturb_out = 2

circles = []
circles1 = []

hor_bar11 = [150, 100]
hor_bar12 = [650, 100]
hor_bar21 = [150, 200]
hor_bar22 = [650, 200]

ver_bar11 = [350, 200]
ver_bar12 = [450, 200]
ver_bar21 = [350, 700]
ver_bar22 = [450, 700]

def rand(a, b):
	return a+(b-a)*random()

def checkIntersect(circ1, circ2):
	# circ<i> is an array with centreX, centreY, radius
	x1 = circ1[0]
	y1 = circ1[1]
	r1 = circ1[2]

	x2 = circ2[0]
	y2 = circ2[1]
	r2 = circ2[2]

	if ((r1+r2)*(r1+r2) <= (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)):
		return False
	# if ((r1-r2)*(r1-r2) <= (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)):
		# return True
	return True

#hor_bar
count = n_in
while True:
	
	x = rand(hor_bar11[0], hor_bar22[0])
	y = rand(hor_bar12[1], hor_bar21[1])
	r = rand(size_in-perturb_in, size_in+perturb_in)
	# print([x, y, r])
	
	if len(circles) == 0:
		circles.append([x, y, r])
		# print([x, y, r])
		# print(count)
		count -= 1
	else:
		flag = True
		for circle in circles:
			if checkIntersect(circle, [x, y, r]):
				flag = False
		if flag:
			circles.append([x, y, r])
			# print([x, y, r])
			# print(count)
			count -= 1

	if count == 0:
		break

#ver_bar
count = n_in
while True:
	
	x = rand(ver_bar11[0], ver_bar22[0])
	y = rand(ver_bar12[1], ver_bar21[1])
	r = rand(size_in-perturb_in, size_in+perturb_in)
	# print([x, y, r])
	
	if len(circles) == 0:
		circles.append([x, y, r])
		# print([x, y, r])
		# print(count)
		count -= 1
	else:
		flag = True
		for circle in circles:
			if checkIntersect(circle, [x, y, r]):
				flag = False
		if flag:
			circles.append([x, y, r])
			# print([x, y, r])
			# print(count)
			count -= 1

	if count == 0:
		break

#outside
count = n_out
while True:
	
	x = rand(0, w)
	y = rand(0, h)
	r = rand(size_out-perturb_out, size_out+perturb_out)
	# print([x, y, r])
	
	if len(circles) == 0:
		circles.append([x, y, r])
		circles1.append([x, y, r])
		# print([x, y, r])
		# print(count)
		count -= 1
	else:
		flag = True
		for circle in circles:
			if checkIntersect(circle, [x, y, r]):
				flag = False
		if flag:
			circles.append([x, y, r])
			circles1.append([x, y, r])
			# print([x, y, r])
			# print(count)
			count -= 1

	if count == 0:
		break


print("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
print("<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->")
print("<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"")
print("\t viewBox=\"0 0 800 800\" style=\"enable-background:new 0 0 800 800;\" xml:space=\"preserve\">")
print("<style type=\"text/css\">\n\t.st0{fill:#AA467F;}\n.st1{fill:#B5396D;}\n</style>\n<g>")

for circle in circles:
	if circle in circles1:
		continue
	print(
		"<circle class=\"st0\" cx=\""+
		str(circle[0])+"\" cy=\""+
		str(circle[1])+"\" r=\""+
		str(circle[2])+"\"/>")

for circle in circles1:
	print(
		"<circle class=\"st1\" cx=\""+
		str(circle[0])+"\" cy=\""+
		str(circle[1])+"\" r=\""+
		str(circle[2])+"\"/>")

print("</g>\n</svg>\n")