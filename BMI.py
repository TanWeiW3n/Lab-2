

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight /(height*height)
    print("BMI is " + str(bmi))
    if bmi<18.5:
        print("You are skinny")
    elif 18.5 <= bmi <= 25.0:
        print("You are healthy")
    else:
        print("You fat af")



calculate_bmi(weight=57.1,height=1.73)