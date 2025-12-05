filename = 'list_presents.csv'

total_surface = 0
ribbon_perimeter = 0
total_ribbon = 0

## surface of the box ##




with open(filename) as f:      #open csv
	for ligne in f:
		ligne = ligne.strip()
		fields = ligne.split('x') #clean the data : from aaxbbxcc to 'aa' 'bb' 'cc', for each line
		numbers = [int(i) for i in fields] # str -> int
		
		
		l = numbers[0] #assigne position à chaque int
		w = numbers[1]
		h = numbers[2]

## extra ##
		
		side1 = l*w 
		side2 = w*h 
		side3 = h*l
		extra = min(side1, side2, side3) #extra face = shortest side
			
		surface_box = 2*side1 + 2*side2 + 2*side3 + extra

		total_surface = total_surface + surface_box


### ribon
		
		perimeter1 = 2*(l+w)
		perimeter2 = 2*(h+w)
		perimeter3 = 2*(l+h)

		ribbon_bow = l*w*h

		ribbon_perimeter = min(perimeter1, perimeter2,  perimeter3) + ribbon_bow
		

		total_ribbon += ribbon_perimeter
		print(ribbon_perimeter)

#print(total_surface)
print(total_ribbon)


