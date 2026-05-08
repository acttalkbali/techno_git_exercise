# reports.py
# Developer C — Reporting & summaries
# Branch: feature/reports

from grades import get_average


def get_top_students(students: dict, grades: dict, n: int = 3) -> list:
    results = []

    for student_id, name in students.items():

        student_grades = grades.get(student_id, [])
        if not student_grades:
            avg = 0.0
        else:
            list_grade=list(map(float,student_grades.values()))
            avg = sum(list_grade) / len(student_grades)
        results.append((student_id, name, avg))
        results.sort(key=lambda x: x[2], reverse=True)
    return results[:n]

    # TODO: implement this function
    raise NotImplementedError("get_top_students is not implemented yet.")

def summarize_class(students: dict, grades: dict) -> tuple:
    if not students:
        return (0, 0.0, 0.0, 0.0)

    all_averages = []

    for student_id in students:
        student_grades = grades.get(student_id, [])

        if not student_grades:
            avg = 0.0
        else:
            list_grade = list(map(float, student_grades.values()))
            avg = sum(list_grade) / len(student_grades)

        all_averages.append(avg)

    total_students = len(students)
    class_average = round(sum(all_averages) / total_students, 2)
    highest_average = max(all_averages)
    lowest_average = min(all_averages)
    return (total_students, class_average, highest_average, lowest_average)
    # TODO: implement this function
    raise NotImplementedError("summarize_class is not implemented yet.")


def export_report(students: dict, grades: dict) -> str:
    total_students, class_avg, _, _ = summarize_class(students, grades)

    report = "─────────────────────────────────\n"
    report += "GRADEBOOK REPORT\n"
    report += f"Total students: {total_students}\n"
    report += f"Class average:  {class_avg:.2f}\n\n"
    report += "STUDENT DETAILS\n"
    sorted_students = sorted(students.items(), key=lambda item: item[1])
    for student_id, name in sorted_students:
        student_grades = grades.get(student_id, {})

        if not student_grades:
            avg = 0.0
            subject_list = "none"
        else:
            avg = sum(student_grades.values()) / len(student_grades)
            subject_list = ", ".join(sorted(student_grades.keys()))
        id_str = f"S{student_id:03}"
        report += f"{id_str} | {name:16} | Avg: {avg:6.2f} | Subjects: {subject_list}\n"

    report += "─────────────────────────────────"
    return report
    # TODO: implement this function
    raise NotImplementedError("export_report is not implemented yet.")

if __name__ == "__main__":
    students_database = {
        1: "Alice",
        2: "Bob",
        3: "Charlie",
        4: "David",
        5: "Eve"
    }
    grades_database = {
        1: {"Math": 90, "Science": 95, "History": 88},
        2: {"Math": 70, "Science": 80, "History": 75},
        3: {"Math": 60, "Science": 55, "History": 50},
        4: [],  # Average: 0.0 (Empty list)
        
    }

    print(get_top_students(students_database, grades_database, n=3))
    summary = summarize_class(students_database, grades_database)
    print(f"Total: {summary[0]}, Class Avg: {summary[1]}, Max: {summary[2]}, Min: {summary[3]}")
    print(export_report(students_database, grades_database))

