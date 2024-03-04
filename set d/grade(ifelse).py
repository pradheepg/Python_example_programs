def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

percentage = float(input("Enter the percentage score of the student: "))
grade = calculate_grade(percentage)
print("Grade obtained by the student:", grade)
