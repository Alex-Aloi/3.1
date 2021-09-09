import turtle
def convert_height():
	height_in_inches=input("Enter your height in inches: ")
	final_height_feet=int(height_in_inches)/12
	final_height_inches=int(height_in_inches)%12
	print("You are ",final_height_feet,"' ",final_height_inches,"\" tall",sep="")
def convert_distance(kilometers):
	total_inches=kilometers*39370.1
	total_feet=total_inches/12
	final_inches=total_inches%12
	miles=total_feet/(63360/12)
	final_feet=total_feet%(63360/12)
	print(int(kilometers),"kilometers is",int(miles),"miles,",int(final_feet),"feet,",int(final_inches),"inches")
def snow_man(x,y,radius):
	turtle.bgcolor("cyan")
	turtle.up()
	turtle.goto(x,y)
	draw_circle(radius)
	draw_circle(radius*0.75)
	draw_circle(radius*0.75*0.75)
	input("press enter to close: ")

def draw_circle(radius):
	turtle.down()
	turtle.fillcolor("white")
	turtle.begin_fill()
	turtle.circle(radius)
	turtle.end_fill()
	turtle.up()
	turtle.left(90)
	turtle.forward(2*radius)
	turtle.right(90)
	
def main():
	#convert_height()
	#convert_distance(123.5)
	snow_man(0,-100,100)
	
main()
