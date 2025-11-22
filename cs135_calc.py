# cs135_calc.py

def average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def compute_course_grade(A, M, F, P):
    return 0.20 * A + 0.25 * M + 0.45 * F + 0.10 * P


def assignment_requirement_met(A):
    return A >= 50.0


def exam_requirement_met(M, F):
    return 0.25 * M + 0.45 * F >= 35.0


def overall_pass(A, M, F):
    return assignment_requirement_met(A) and exam_requirement_met(M, F)

def needed_score_on_final(Assignment, midterm):
    needed = ((35 - .25 * midterm) / .45)
    if Assignment < 50:
        return None
    elif needed > 100:
        return None
    else:
        return needed
    
    
