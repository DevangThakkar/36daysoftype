# the point of this script is to draw random lines and get multiple layers
# for the letter P

from random import random

n_low = 15000
n_high = 30000

lines_low = []
lines_high = []

h = 800
w = 800

perturb = 10

def rand(a, b):
	return a+(b-a)*random()

for i in range(n_low):
	randx = rand(0, w)
	randy = rand(0, h)
	x1 = randx + rand(-perturb, perturb)
	x2 = randx + rand(-perturb, perturb)
	y1 = randy + rand(-perturb, perturb)
	y2 = randy + rand(-perturb, perturb)
	lines_low.append("<line class=\"st0\" x1=\""+str(x1)+"\" y1=\""+str(y1)+"\" x2=\""+str(x2)+"\" y2=\""+str(y2)+"\"/>")

for i in range(n_high):
	randx = rand(0, w)
	randy = rand(0, h)
	x1 = randx + rand(-perturb, perturb)
	x2 = randx + rand(-perturb, perturb)
	y1 = randy + rand(-perturb, perturb)
	y2 = randy + rand(-perturb, perturb)
	lines_high.append("<line class=\"st1\" x1=\""+str(x1)+"\" y1=\""+str(y1)+"\" x2=\""+str(x2)+"\" y2=\""+str(y2)+"\"/>")

print("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
print("<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->")
print("<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"")
print("\t viewBox=\"0 0 800 800\" style=\"enable-background:new 0 0 800 800;\" xml:space=\"preserve\">")
print("<style type=\"text/css\">\n\t.st0{fill:none;stroke:#555555;stroke-width:2;stroke-miterlimit:10;}")
print("\t.st1{fill:none;stroke:#000000;stroke-width:2;stroke-miterlimit:10;}\n</style>")
print("<g id=\"Layer_1\">")

for i in range(n_low):
	print(lines_low[i])

print("</g>")

print("<g id=\"Layer_2\">")

for i in range(n_high):
	print(lines_high[i])

print("</g>\n</svg>")