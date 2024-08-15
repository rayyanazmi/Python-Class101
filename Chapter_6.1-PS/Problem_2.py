#Q. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = float(input("Enter marks 1: "))
marks2 = float(input("Enter marks 2: "))
marks3 = float(input("Enter marks 3: "))

#Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3)/300)

if(total_percentage>=40):
    print("You are pass", total_percentage)

else:
    print("You Failed, try again next year ;)", total_percentage)


#CGPA calculator
'''
total_number_of_semesters = float(input("Enter total number of semester: "))
sem1 = float(input("Semester 1 CGPA: "))
sem2 = float(input("Semester 2 CGPA: "))
sem3 = float(input("Semester 3 CGPA: "))
sem4 = float(input("Semester 4 CGPA: "))
sem5 = float(input("Semester 5 CGPA: "))
sem6 = float(input("Semester 6 CGPA: "))

Overall_CGPA = ((sem1 + sem2 + sem3 + sem4 + sem5 + sem6)/total_number_of_semesters)

print(Overall_CGPA)'''