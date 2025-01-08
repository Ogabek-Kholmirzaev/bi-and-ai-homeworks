import csv

def calculate_average_grades(input_file, output_file):
    grades = {}
    counts = {}

    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            subject = row["Subject"]
            grade = int(row["Grade"])
            grades[subject] = grades.get(subject, 0) + grade
            counts[subject] = counts.get(subject, 0) + 1

    averages = {subject: grades[subject] / counts[subject] for subject in grades}

    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, average in averages.items():
            writer.writerow([subject, average])

input_file = "grades.csv"
output_file = "average_grades.csv"
calculate_average_grades(input_file, output_file)
print(f"Average grades written to {output_file}.")