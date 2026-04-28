def calculate_bmi (height,weight):
    print ("Height="+str(height)) #+joining two strings together
    print("Weight="+str(weight))
    bmi=weight/(height*height) 
    print(bmi)
    if bmi<18.5:
        print("Under Weight")
    elif bmi>25.0:
        print("Over Weight")
    else:
        print("Normal Weight")
calculate_bmi(weight=57,height=1.73)