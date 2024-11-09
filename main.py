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
    return overall_score  # Keep as float for more precise rounding

# Function to round the score to the nearest category boundary and determine the category
def round_to_nearest_category(score):
    # Find the closest category boundary
    closest_boundary = min(grade_categories, key=lambda x: abs(x[0] - score))
    rounded_score, category = closest_boundary
    return rounded_score, category

# Main program function
def main():
    # Get user input for the scores of each component
    try:
        coursework1 = float(input("Enter the score for Coursework 1 (0-100): "))
        coursework2 = float(input("Enter the score for Coursework 2 (0-100): "))
        coursework3 = float(input("Enter the score for Coursework 3 (0-100): "))
        final_exam = float(input("Enter the score for the Final Exam (0-100): "))

        # Ensure all scores are between 0 and 100
        if not all(0 <= score <= 100 for score in [coursework1, coursework2, coursework3, final_exam]):
            print("Error: Each score must be between 0 and 100.")
            return

        # Calculate the overall score
        overall_score = calculate_overall_score(coursework1, coursework2, coursework3, final_exam)

        # Round the score to the nearest category and determine the category
        rounded_score, category = round_to_nearest_category(overall_score)

        # Display the results
        print(f"Overall Score: {overall_score:.1f}")
        print(f"Rounded Score: {rounded_score}")
        print(f"Category: {category}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for scores.")

# Run the program
if __name__ == "__main__":
    main()
