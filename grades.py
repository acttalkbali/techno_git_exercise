# grades.py
# Developer B — Grade calculations
# Branch: feature/grades

# The grades database is a nested dictionary with this structure:
# {
#   "S001": {"Math": 85, "English": 90, "Science": 78},
#   "S002": {"Math": 60, "English": 55},
# }

def add_grade(grades: dict, student_id: str, subject: str, score: int) -> dict:
    """
    add_grade(grades, "S001", "Math",    92)
    Add or update a grade for a student in a given subject.

    - Score must be between 0 and 100 (inclusive).
      If not, print a warning and do NOT add the grade:
      "Invalid score: 110. Score must be between 0 and 100."
    - If student_id does not exist in grades yet, create their entry.
    - Overwrite the score if the subject already exists for that student.

    Args:
        grades (dict): the current grades database
        student_id (str): the student's ID
        subject (str): the subject name (e.g. "Math")
        score (int): the score between 0 and 100

    Returns:
        dict: the updated grades dictionary

    Example:
        >>> db = {}
        >>> add_grade(db, "S001", "Math", 85)
        >>> db
        {"S001": {"Math": 85}}
    """
    if 0 <= score <=100:
        grade={}
        grade[subject]=score                        # Creating a dictionary subject,score
        try:
            grades[student_id].update(grade)        # Update the student's grades dictionary if exists
        except KeyError:
            grades[student_id]=grade                # Create an entry for the new student
    else:
        print("Invalid score:",score,". Score must range from 0 to 100.",sep="")
    return grades

def get_average(grades: dict, student_id: str) -> float:
    """
    Calculate the average score of a student across all their subjects.

    - Returns 0.0 if the student has no grades or does not exist.
    - Round the result to 2 decimal places.

    Args:
        grades (dict): the current grades database
        student_id (str): the student's ID

    Returns:
        float: the average score, rounded to 2 decimal places

    Example:
        >>> db = {"S001": {"Math": 80, "English": 90}}
        >>> get_average(db, "S001")
        85.0
        >>> get_average(db, "S999")
        0.0
    """
    scores = list(grades.get(student_id,{}).values())
    return round(sum(scores) / len(scores), 2) if scores else 0.0

def get_subjects(grades: dict) -> set:
    """
    Return the set of ALL unique subjects that appear across all students.

    - Uses a set to avoid duplicates.
    - Returns an empty set if grades is empty.

    Args:
        grades (dict): the current grades database

    Returns:
        set: a set of subject name strings

    Example:
        >>> db = {
                "S001": {"Math": 80, "English": 90},
                "S002": {"Math": 70, "Science": 65},
            }
        >>> get_subjects(db)
        {"Math", "English", "Science"}
    """
    for key in grades:
        matter = []
        cnt1=0
        for key in grades:
            subjects=(list(grades.values())[cnt1])
            for k in subjects:
                matter.append(k)
            cnt1+=1
        return set(matter)

def get_failing_students(students: dict, grades: dict, threshold: int = 50) -> list:
    """
    Return a list of (student_id, name, average) tuples for students
    whose average score is strictly below the threshold.

    - Tuples must be sorted by average score in ascending order (lowest first).
    - Students with no grades at all should be included with average 0.0.
    - Use get_average() to compute each student's average.

    Args:
        students (dict): the students database
        grades (dict): the grades database
        threshold (int): the minimum passing average (default 50)

    Returns:
        list[tuple]: list of (student_id, name, average) sorted by average

    Example:
        >>> students = {"S001": {"name": "Alice", "id": "S001"},
                        "S002": {"name": "Bob",   "id": "S002"}}
        >>> grades   = {"S001": {"Math": 40}, "S002": {"Math": 80}}
        >>> get_failing_students(students, grades)
        [("S001", "Alice", 40.0)]
    """
    failed_students_list = []
    for key in grades:
        average = get_average(grades,key)
        if average<threshold:                                           # Process only if stricky < threshold
            failed_student=key,list(students[key].values())[0],average  # Create a tuple for each failed student
            failed_students_list.append(failed_student)                 # Make a list of tuple(s)
    failed_students_list.sort(key=lambda x:x[2],reverse=False)          # Sort the list in ascending order of scores
    return failed_students_list

if __name__ == '__main__':

    grades = {
        "S001": {"Math": 70, "English": 60, "Chemistry": 75},
        "S002": {"Math": 60, "Science": 55, "Physics": 65},
        "S003": {"Biology": 55, "French": 65, "Spanish": 75},
    }

    students = {"S001": {"name": "Alice", "id": "S001"},
                "S002": {"name": "Bob", "id": "S002"},
                "S003": {"name": "Rita", "id": "S003"}}


    print("Average score of 'S001' is",get_average(grades, "S001"))
    print("Average score of 'S002' is",get_average(grades, "S002"))
    print("Average score of 'S003' is",get_average(grades, "S003"))

    print("Student who failed to get 65%",get_failing_students(students, grades,65))
    print("All the subjects covered",get_subjects(grades))
    print(grades)
    print("Adding a Math score of 92% to student S004")
    add_grade(grades, "S004", "Math",    92)
    print(grades)
    print("Updating the Math score of student S002 to 75%")
    add_grade(grades, "S002", "Math",    75)
    print(grades)
