import re
import os

# Do you want a quote yes or no?
while True:
	yn = input("Hello, Need a quote? Yes or No : ").lower()
	if yn == "yes":
		break
	elif yn == "no":
		print("Thank you, come again!")
		quit()
	elif yn != "yes" or "no":
		print("You Entered: " + yn)
		print("Please Enter Yes or No.")
		continue
		
		
os.system('cls')

#What type of material...

#list of material choices and their stored prices
material_kind = ['rock', 'sand'] 
mat_type = {'rock' : 13.50,'sand' : 12.00}	

#Create material_choice variable	
while True:
	material_choice = input(material_kind[0].capitalize() + " or " + material_kind[1].capitalize() + "?").lower()
	if material_choice == "rock":
		os.system('cls')
		print(material_choice.capitalize() + " is " + '${:.2f}'.format((mat_type[material_choice])) + " per ton.")
		break
	elif material_choice == "sand":
		os.system('cls')
		print(material_choice.capitalize() + " is " + '${:.2f}'.format((mat_type[material_choice])) + " per ton.")
		break
	elif material_choice != material_kind:
		print("You Entered: " + material_choice)
		print("Wrong Material. Please choose Rock or Sand only.")
		continue
		
print(" ")

#Check price of material choice on file and allow to change it for this quote only
while True:
	yn2 = input("Is this the correct price? Yes or No?").lower()
	print(" ")
	if yn2 == "yes":
		break
	elif yn2 == "no":
		new_price = input("What's the correct price? Example: '$13.50 per ton' is '13.5'.  ")
		print(" ")
		if len(new_price) > 5 and re.match('^[0-9]*[.,]{0,1}[0-9]*$', new_price):
			print("Too Many Entries. No more than 5 digits")
			continue
		elif len(new_price) > 0 and re.match('^[0-9]*[.,]{0,1}[0-9]*$', new_price):
			mat_type[material_choice] = new_price
			break
		elif not re.match('^[0-9]*[.,]{0,1}[0-9]*$', new_price):
			print("Incorrect entry. Try Again.")
			continue
	elif yn2 != "yes" or "no":
		print("You Entered: " + yn2)
		print("Please enter Yes or No.")
		print(" ")
		continue


os.system('cls')

print("The " + material_choice + " price for this quote will be " + '${:.2f}'.format(float(mat_type[material_choice])) + " per ton.")
print(' ')


#Measurement of the hole...


#lists for gathering measurements 
measur_list = ['length', 'width', 'height']
measur_result = {}
hole_meas_comp = []
inches_list = []
tot_inches = sum(inches_list)

#3 While loops for gathering L,W,H of hole
while True:
	meas_length = input("What is the length of the hole in feet? Please enter numbers only. Example: '16 Feet' is 16. 3 digit max.  ").strip()
	if  len(meas_length) > 3 and re.match("^[-+]?([1-9]\d*|0)$", meas_length):
		print("You Entered: " + meas_length)
		print("Please enter 3 numbers only.")
		continue
	elif not re.match("^[-+]?([1-9]\d*|0)$", meas_length):
		print("You Entered: " + meas_length)
		print("Please enter numbers only.")
		continue
	elif len(meas_length) > 0 and re.match("^[-+]?([1-9]\d*|0)$", meas_length):
		measur_result['Length'] = meas_length
		break

print(" ")
		
while True:
	meas_width = input("What is the width of the hole in feet? Please enter numbers only. Example: '16 Feet' is 16. 3 digit max.  ").strip()
	if  len(meas_width) > 3 and re.match("^[-+]?([1-9]\d*|0)$", meas_width):
		print("You Entered: " + meas_width)
		print("Please enter 3 numbers only.")
		continue
	elif not re.match("^[-+]?([1-9]\d*|0)$", meas_width):
		print("You Entered: " + meas_width)
		print("Please enter 3 numbers only.")
		continue
	elif len(meas_width) > 0 and re.match("^[-+]?([1-9]\d*|0)$", meas_width):
		measur_result['Width'] = meas_width
		break


print(" ")
		
while True:
	meas_height = input("What is the height of the hole in feet? Please enter numbers only. Example: '16 Feet' is 16. 3 digit max.  ").strip()
	if  len(meas_height) > 3 and re.match("^[-+]?([1-9]\d*|0)$", meas_height):
		print("You Entered: " + meas_height)
		print("Please enter 3 numbers only.")
		continue
	elif not re.match("^[-+]?([1-9]\d*|0)$", meas_height):
		print("You Entered: " + meas_height)
		print("Please enter 3 numbers only.")
		continue
	elif len(meas_height) > 0 and re.match("^[-+]?([1-9]\d*|0)$", meas_height):
		measur_result['Height'] = meas_height
		break		


print(" ")

#add measuements to one list named hole_meas_comp
hole_meas_comp.append(meas_length)
hole_meas_comp.append(meas_width)
hole_meas_comp.append(meas_height)

#turns feet into inches and creates new list containg inches values for conversion into cubic feet
for x in hole_meas_comp:
	sum_inches = int(x)*12
	inches_list.append(sum_inches)

#converts inches list into a total cubic feet needed for quote
cub_feet = (int(inches_list[0]) * int(inches_list[1]) * int(inches_list[2]))/1728
#converts cubic feet to cubic yards for conversion into tonage
cub_yard = cub_feet * .037
#turns cubic yards into tonage
tot_tonage = cub_yard * 1.4

os.system('cls') 
#Select a delivery zone...


deliv_kind = ['Foothills', 'In Town', '32nd and B','foothills', 'in town', '32nd and b']
deliv_type = {'foothills' : 3.70, 'in town' : 5.50, '32nd and b' : 6.70}

#list choices of zones

print("Delivery Zone Choices")
print(" ")
print(deliv_kind[0])
print(deliv_kind[1])
print(deliv_kind[2])
print(" ")




while True:
	deliv_choice = input("Which delivery zone will apply?")
	print(" ")
	if deliv_choice in deliv_kind:
		deliv_pric_conf = input("Is " + '${:.2f}'.format(float(deliv_type[deliv_choice])) + " the correct price for " + deliv_choice.capitalize() + "?" )
		print(" ")
		if deliv_pric_conf == "yes":
			print('${:.2f}'.format(float(deliv_type[deliv_choice]))) 
			break
		elif deliv_pric_conf == "no":
			correct_deliv_price = input("What's the correct price? Example: '$13.50 per ton' is '13.5'.  ")
			if len(correct_deliv_price) > 5 and re.match('^[0-9]*[.,]{0,1}[0-9]*$', correct_deliv_price):
				print("Too many entires. 5 digit max.")
				continue
			elif len(correct_deliv_price) > 0 and re.match('^[0-9]*[.,]{0,1}[0-9]*$', correct_deliv_price):
				deliv_type[deliv_choice] = correct_deliv_price
				break
			elif not re.match('^[0-9]*[.,]{0,1}[0-9]*$', correct_deliv_price):
				print("You Entered: " + correct_deliv_price)
				print("Numbers only please.")
				continue
		elif deliv_pric_conf is not "yes" or "no":
			print("Please enter 'Yes' or 'No' only.")
			print(" ")
			continue
	elif deliv_choice != deliv_kind:
		print(" ")
		print("You Entered: " + deliv_choice)
		print(" ")
		print(deliv_kind[0])
		print(deliv_kind[1])
		print(deliv_kind[2])
		print(" ")
		continue
		
os.system('cls')

#build quote
		
print(' ')		
tot_cost_notax = tot_tonage * float(mat_type[material_choice])


print("..." + material_choice.capitalize() + "...")
print(" ")
print("The " + str(material_choice.capitalize()) + " price for this quote will be " + '${:,.2f}'.format(float(mat_type[material_choice])) + " per ton.")
print(" ")
print("The delivery zone for this quote is " + deliv_choice.capitalize() + ".")
print(" ")
print("The delivery zone fee for this quote will be " + '${:.2f}'.format(float(deliv_type[deliv_choice])) + " per ton.")
print(" ")
print("The total cubic yards is " + '{:.2f}'.format(float(cub_yard)) + ". The L, W, H entered is " + str(meas_length) + ", " + str(meas_height) + ", " + str(meas_width) + ".")
print(" ")
print("The total tonage of material needed is " + '{:.2f}'.format(float(tot_tonage)) + " tons.")
print(" ")

print("<<<Here is your quote!!!>>>")
print(" ")

print("   " + '${:,.2f}'.format(tot_cost_notax))

end = input() #to analyze output
