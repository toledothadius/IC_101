name = input('Enter your name:')
print('Hello, ' + name + ' please answer each question below')
science = input("Enter your Science grade: ")
math = input("Enter your Math grade: ")
english = input("Enter your English grade: ")

print("Hi " + name + " your grades are \n" + science + "% in Science \n" + math + "% in Math \n" + english + "% in Eglish")

total = float(science) + float(math) + float(english)
average = float(total) / 3
print("your average grade is: " + str(average) + "%")
if average < 75:
    print("sorry " + name + " you failed!")
if average > 75:
    print("Congratulations " + name + " you passed!")