# cs135_calc.py

def average(scores):
    """Return the average of a list of numbers, or 0 if the list is empty."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def compute_course_grade(A, M, F, P):
    """
    A, M, F, P are percentages (0–100).
    Returns overall course grade as a percentage.
    """
    return 0.20 * A + 0.25 * M + 0.45 * F + 0.10 * P


def assignment_requirement_met(A):
    """
    Assignment requirement: at least half the assignment points.
    20 points total, so need 10 points => A >= 50%.
    """
    return A >= 50.0


def exam_requirement_met(M, F):
    """
    Exam requirement: midterm(25) + final(45) >= 35 points out of 70.
    0.25*M + 0.45*F >= 35
    """
    return 0.25 * M + 0.45 * F >= 35.0


def overall_pass(A, M, F):
    """
    Overall pass just looking at the two hard requirements:
    - assignment requirement
    - exam requirement
    (ignores the actual overall grade threshold for now).
    """
    return assignment_requirement_met(A) and exam_requirement_met(M, F)
