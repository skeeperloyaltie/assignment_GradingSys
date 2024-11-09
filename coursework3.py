from datetime import datetime
from tabulate import tabulate
import os

# Define grade boundaries and their corresponding categories
grade_categories = [
    (100, "Aurum Standard"),
    (92, "Upper First"), (85, "Upper First"), (82, "Upper First"),
    (78, "First"), (75, "First"), (72, "First"),
    (68, "2:1 Upper Second"), (65, "2:1 Upper Second"), (62, "2:1 Upper Second"),
    (58, "2:2 Lower Second"), (55, "2:2 Lower Second"), (52, "2:2 Lower Second"),
    (48, "Third"), (45, "Third"), (42, "Third"),
    (38, "Condonable Fail"), (35, "Condonable Fail"), (32, "Condonable Fail"),
    (25, "Fail"), (15, "Fail"), (5, "Fail"),
    (0, "Defecit Opus")
]

# Function to calculate the overall score based on weighted components
def calculate_overall_score(coursework1, coursework2, coursework3, final_exam):
    overall_score = (coursework1 * 0.10) + (coursework2 * 0.20) + (coursework3 * 0.30) + (final_exam * 0.40)
    return overall_score  # Keep as float for precise rounding

# Function to round the score to the nearest category boundary and determine the category
def round_to_nearest_category(score):
    closest_boundary = min(grade_categories, key=lambda x: abs(x[0] - score))
    rounded_score, category = closest_boundary
    return rounded_score, category

# Function to calculate age based on D.o.B
def calculate_age(dob):
    birth_date = datetime.strptime(dob, "%Y-%m-%d")
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

# Function to load existing data from students.txt, excluding headers
def load_existing_data():
    students_data = []
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if "|" in line and not line.strip().startswith("ID"):  # Exclude header rows
                    columns = [col.strip() for col in line.split("|") if col.strip()]
                    if len(columns) == 7:  # Ensure we have exactly 7 columns
                        students_data.append(columns)
    return students_data

# Function to process each student's data
def process_student_data():
    students_data = []
    while True:
        student_id = input("Enter student ID (2-digit number, or 'end' to finish): ")
        if student_id.lower() == "end":
            break
        if not student_id.isdigit() or len(student_id) != 2:
            print("Invalid ID. Please enter a 2-digit number.")
            continue

        name = input("Enter student's name: ")
        dob = input("Enter student's Date of Birth (YYYY-MM-DD): ")

        try:
            age = calculate_age(dob)
        except ValueError:
            print("Invalid Date of Birth format. Please enter in YYYY-MM-DD.")
            continue

        try:
            coursework1 = float(input("Enter the score for Coursework 1 (0-100): "))
            coursework2 = float(input("Enter the score for Coursework 2 (0-100): "))
            coursework3 = float(input("Enter the score for Coursework 3 (0-100): "))
            final_exam = float(input("Enter the score for the Final Exam (0-100): "))

            if not all(0 <= score <= 100 for score in [coursework1, coursework2, coursework3, final_exam]):
                print("Error: Each score must be between 0 and 100.")
                continue

            overall_score = calculate_overall_score(coursework1, coursework2, coursework3, final_exam)
            rounded_score, category = round_to_nearest_category(overall_score)

            students_data.append([student_id, name, dob, age, round(overall_score, 1), rounded_score, category])

        except ValueError:
            print("Error: Invalid input. Please enter numeric values for scores.")
            continue

    return students_data

# Function to display all data (existing + new) in a table format with a single header
def display_all_data(existing_data, new_data):
    all_data = existing_data + new_data
    headers = ["ID", "Name", "D.o.B", "Age", "Raw Score", "Rounded Score", "Category"]
    print(tabulate(all_data, headers, tablefmt="grid"))

# Function to save only the new data rows to students.txt in a consistent format without headers
def save_to_file(new_data):
    with open("students.txt", "a") as file:
        for row in new_data:
            file.write("| " + " | ".join(map(str, row)) + " |\n")  # Write each row as a line

# Main function to run the program
def main():
    print("Welcome to the Student Grading System")

    # Load existing data from the file
    existing_data = load_existing_data()

    # Process new student data
    new_data = process_student_data()

    # Display all data (existing and new) in one table
    display_all_data(existing_data, new_data)

    # Save new data to file
    save_to_file(new_data)
    print("Student data has been saved to 'students.txt'.")

# Run the program
if __name__ == "__main__":
    main()
