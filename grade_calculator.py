from statistics import mean
import statistics
def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input("What is your name:")

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = float(input("What is your Math score:"))

    science_score = float(input("What is your Science score:"))
    english_score = float(input("What is your English score:"))

    # Calculate the average grade
    # mean method from the statistics module takes the average from all the variables in the list by adding them up and dividing by the length of the list
    average_grade = float(statistics.mean([math_score,science_score,english_score]))

    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"{student_name} got an average grade of {average_grade:.2f}%")