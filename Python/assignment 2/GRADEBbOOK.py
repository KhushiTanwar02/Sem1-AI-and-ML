#=========================================
# Name=khushi
# date=26-11-25
# batch=b.tech CSE(AI/ML)
# title=GRADEBOOK
#=========================================
# ---------------- Task 2: Manual Data Entry ---------------- #
def input_student_data():
    marks = {}
    n = int(input("Enter number of students: "))
    for _ in range(n):
        student_name = input("Enter student name: ")
        Marks = int(input(f"Enter the marks of {student_name}: "))
        marks[student_name] = Marks
    return marks
# ---------------- Task 3: Statistical Analysis Functions ---------------- #
def calculate_average(marks_dict):
    return sum(marks_dict.values()) / len(marks_dict) if marks_dict else 0 
def calculate_median(marks_dict):
    sorted_marks = sorted(marks_dict.values())
    n = len(sorted_marks)
    if n == 0:
        return None
    mid = n // 2
    if n % 2 == 0:
        return (sorted_marks[mid - 1] + sorted_marks[mid]) / 2
    else:
        return sorted_marks[mid]
def find_max_score(marks_dict):
    return max(marks_dict.values()) if marks_dict else None
def find_min_score(marks_dict):
    return min(marks_dict.values()) if marks_dict else None 
# ---------------- Task 4: Grade Assignment ---------------- #
def assign_grades(marks_dict):
    grades = {}
    for name, mark in marks_dict.items():
        if mark >= 90:
            grades[name] = 'A'
        elif mark >= 80:
            grades[name] = 'B'
        elif mark >= 70:
            grades[name] = 'C'
        elif mark >= 60:
            grades[name] = 'D'
        else:
            grades[name] = 'F'
    return grades
def count_grades(grades):
    summary = {}
    for grade in grades.values():
        summary[grade] = summary.get(grade, 0) + 1
    return summary
# ---------------- Task 5: Pass/Fail Lists ---------------- #
def get_pass_fail_lists(marks_dict):    
    passed_students = [name for name, m in marks_dict.items() if m >= 40]
    failed_students = [name for name, m in marks_dict.items() if m < 40]
    return passed_students, failed_students
# ---------------- Task 6: Results Table ---------------- #
def print_results_table(marks_dict, grades):
    print("\n-----------------------------------")
    print(f"{'Name':<10} {'Marks':<10} {'Grade':<10}")
    print("-----------------------------------")
    for name in marks_dict:
        print(f"{name:<10} {marks_dict[name]:<10} {grades[name]:<10}")
    print("-----------------------------------")


def main():   
    print("Welcome to the Gradebook Analyzer!")
while True:
        print("\nMenu:")
        print("1. Manual Data Entry")
        print("2. Exit")
        choice = input("Choose an option (1-2): ")
        if choice == '1':
            marks = input_student_data()
            avg = calculate_average(marks)
            med = calculate_median(marks)
            max_score = find_max_score(marks)
            min_score = find_min_score(marks)
            print(f"\nStatistical Analysis:\nAverage: {avg}\nMedian: {med}\nMax Score: {max_score}\nMin Score: {min_score}")
            grades = assign_grades(marks)
            grade_summary = count_grades(grades)
            print(f"\nGrade Distribution: {grade_summary}")
            passed_students, failed_students = get_pass_fail_lists(marks)
            print(f"\nPassed Students: {passed_students}\nFailed Students: {failed_students}")
            print_results_table(marks, grades)
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    print("Welcome to the Gradebook Analyzer!")































