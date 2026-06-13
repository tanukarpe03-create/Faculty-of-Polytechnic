def calculate(l, b, h):
    if (h>0):
        volume = l*b*h
        perimeter = 4 * (l+b+h)
        return ( volume , perimeter)
    
    else:
        area = l*b
        perimeter = 2 * (l+b)
        return ( area, perimeter)

print("Cuboid:", calculate(5, 3, 4))
print("Rectangle:", calculate(5, 3,0))

#problem2
info="name surname age"
a=info.split(" ") 
print(a)

#problem3
def about_me():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter your city: ")
    fav_lang = input("Enter your favourite programming language: ")
    years = int(input("How many years have you been coding? "))

    bio = f"""--------------------------
**About Me**
Name: {name}
Age: {age}
City: {city}
Favourite Language: {fav_lang}
Years Coding: {years}
--------------------------"""
    
    print(bio)

about_me()

#problem4
def classify_grade(score):
    if(score>=90):
        print("A")
    elif(score>=80 and score<90):
         print("B")
    elif(score>=70 and score<=80):
         print("C")
    elif(score>=60 and score<70):
         print("D")
    else:
          print("E")
score=int(input("enter a num:")) 
classify_grade(score)
