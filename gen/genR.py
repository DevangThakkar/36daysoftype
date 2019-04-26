# the point of this script is to generate normal and rotated rectangles for
# the letter R

from random import random

w = 500
h = 500

size = 5

ratio = 0.5

print("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
print("<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->")
print("<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"")
print("\t viewBox=\"0 0 500 500\" style=\"enable-background:new 0 0 500 500;\" xml:space=\"preserve\">")
print("<style type=\"text/css\">\n\t.st0{fill:#000000;stroke:#000000;stroke-width:4;stroke-miterlimit:10;}\n</style>")

def print_norm(w_count, h_count):
	print("<rect x=\""+str(w_count*(size*2.5))+"\" y=\""+str(h_count*(size*2.5))+"\" class=\"st0\" width=\""+str(size)+"\" height=\""+str(size)+"\"/>")
	return

def print_rot(w_count, h_count):
	print("<rect x=\""+str(w_count*(size*2.5))+"\" y=\""+str(h_count*(size*2.5))+"\" transform=\"rotate(45 "+str(w_count*(size*2.5)+size/2)+" "+str(h_count*(size*2.5)+size/2)+")\" class=\"st0\" width=\""+str(size)+"\" height=\""+str(size)+"\"/>")
	return

h_count = 0
for i in range(int(h/(size*2.5))+1):
	w_count = 0
	for j in range(int(w/(size*2.5))+1):
		dec = random()
		if dec < ratio:
			print_norm(w_count, h_count)
		else:
			print_rot(w_count, h_count)
		w_count += 1
	h_count += 1

print("</svg>")