# reports.py
# Developer C — Reporting & summaries
# Branch: feature/reports

from grades import get_average


def get_top_students(students: dict, grades: dict, n: int = 3) -> list:
    """
        Return the top n students with the highest average scores.

        - Returns a list of (student_id, name, average) tuples.
        - Sorted by average in descending order (highest first).
        - If n is greater than the number of students, return all of them.
        - Students with no grades have an average of 0.0.

        Args:
            students (dict): the students database
            grades (dict): the grades database
            n (int): number of top students to return (default 3)

        Returns:
            list[tuple]: list of (student_id, name, average) sorted descending

        Example:
            >>> students = {
            ...   "S001": {"name": "Alice", "id": "S001"},
            ...   "S002": {"name": "Bob",   "id": "S002"},
            ... }
            >>> grades = {"S001": {"Math": 90}, "S002": {"Math": 70}}
            >>> get_top_students(students, grades, n=1)
            [("S001", "Alice", 90.0)]
        """
    results = []

    for student_id, name in students.items():

        student_grades = grades.get(student_id, [])
        avg=get_average(grades,student_id)
        """if not student_grades:
            avg = 0.0
        else:
            list_grade=list(map(float,student_grades.values()))
            avg = sum(list_grade) / len(student_grades)"""
        results.append((student_id, name, avg))
        results.sort(key=lambda x: x[2], reverse=True)
    return results[:n]

    # TODO: implement this function
    raise NotImplementedError("get_top_students is not implemented yet.")

def summarize_class(students: dict, grades: dict) -> tuple:
    """
        Return a summary of the whole class as a single tuple.

        The tuple must contain exactly 4 values in this order:
            (total_students, class_average, highest_average, lowest_average)

        - total_students (int): number of students in the database
        - class_average (float): average of all students' averages, rounded to 2 decimals
        - highest_average (float): the best individual average in the class
        - lowest_average (float): the worst individual average in the class

        - If there are no students, return (0, 0.0, 0.0, 0.0).

        Args:
            students (dict): the students database
            grades (dict): the grades database

        Returns:
            tuple: (total_students, class_average, highest_average, lowest_average)

        Example:
            >>> students = {
            ...   "S001": {"name": "Alice", "id": "S001"},
            ...   "S002": {"name": "Bob",   "id": "S002"},
            ... }
            >>> grades = {"S001": {"Math": 80}, "S002": {"Math": 60}}
            >>> summarize_class(students, grades)
            (2, 70.0, 80.0, 60.0)
        """
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
    """
        Generate and return a formatted text report as a single string.

        The report must follow this exact format:
        ─────────────────────────────────
        GRADEBOOK REPORT
        Total students: 3
        Class average:  75.33

        STUDENT DETAILS
        S001 | Alice Smith     | Avg:  85.00 | Subjects: English, Math, Science
        S002 | Bob Martin      | Avg:  62.50 | Subjects: Math, Science
        S003 | Carol White     | Avg:   0.00 | Subjects: none
        ─────────────────────────────────

        Rules:
        - Student names are left-aligned in a field of 16 characters.
        - Averages are right-aligned with 2 decimal places.
        - Subjects are listed in alphabetical order, comma-separated.
        - If a student has no grades, show "none" for subjects.
        - Use summarize_class() to get total_students and class_average.
        - Students are listed in alphabetical order by name.

        Args:
            students (dict): the students database
            grades (dict): the grades database

        Returns:
            str: the complete formatted report
        """
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
        4: {},  # Average: 0.0 (Empty list)
        
    }

    print(get_top_students(students_database, grades_database, n=3))
    summary = summarize_class(students_database, grades_database)
    print(f"Total: {summary[0]}, Class Avg: {summary[1]}, Max: {summary[2]}, Min: {summary[3]}")
    print(export_report(students_database, grades_database))

