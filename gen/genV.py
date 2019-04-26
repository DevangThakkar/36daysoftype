# the point of this script is to create triangles of random orientation for a
# given square - the traingles are made using three of the four corners

from random import randint

w = 1000
h = 1000

size = 20

print("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
print("<!-- Generator: Adobe Illustrator 22.1.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->")
print("<svg version=\"1.1\" id=\"Layer_1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\" x=\"0px\" y=\"0px\"")
print("\t viewBox=\"0 0 "+str(w)+" "+str(h)+"\" style=\"enable-background:new 0 0 "+str(w)+" "+str(h)+";\" xml:space=\"preserve\">")
print("<style type=\"text/css\">\n\t.st0{fill:#000000;stroke:#000000;stroke-width:4;stroke-miterlimit:10;}\n</style>")

h_count = 0
for i in range(int(h/size)+1):
	w_count = 0
	for j in range(int(w/size)+1):
		pt = [[0,0], [0,0], [0,0], [0,0]]
		pt[0] = [w_count*size, h_count*size]
		pt[1] = [(w_count+1)*size, h_count*size]
		pt[2] = [w_count*size, (h_count+1)*size]
		pt[3] = [(w_count+1)*size, (h_count+1)*size]

		dec = randint(0, 3)
		# print(dec)
		arr = [0, 1, 2, 3]
		arr.remove(dec)
		# print(arr)
		print("<polygon class=\"st0\" points=\""+str(pt[arr[0]][0])+","+str(pt[arr[0]][1])+" "+str(pt[arr[1]][0])+","+str(pt[arr[1]][1])+" "+str(pt[arr[2]][0])+","+str(pt[arr[2]][1])+" \"/>")
		w_count += 1
	h_count += 1

print("</svg>")