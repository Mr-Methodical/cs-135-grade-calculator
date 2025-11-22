# cs135_calc.py
def compute_course_grade(A, M, F, P):
    return 0.20 * A + 0.25 * M + 0.45 * F + 0.10 * P


def assignment_requirement_met(A):
    return A >= 50.0


def exam_requirement_met(M, F):
    return 0.25 * M + 0.45 * F >= 35.0


def overall_pass(A, M, F, P):
    return assignment_requirement_met(A) and exam_requirement_met(M, F) and ((compute_course_grade(A, M, F, P)) >= 50)


def needed_score_on_final_to_pass(Assignment, midterm, partcipation):
    F_grade = (50 - 0.20 * Assignment - 0.25 * midterm - 0.10 * partcipation) / 0.45
    needed = max(((35 - .25 * midterm) / .45), F_grade)
    
    if Assignment < 50:
        return None
    elif needed > 100:
        return None
    elif needed < 0:
        return 0
    else:
        return needed

def needed_score_on_final_for_cs136(Assignment, midterm, participation):
    if Assignment < 50:
        return None

    F_exam = (35.0 - 0.25 * midterm) / 0.45
    F_grade60 = (60.0 - 0.20 * Assignment - 0.25 * midterm - 0.10 * participation) / 0.45

    needed = max(F_exam, F_grade60, 0.0)

    if needed > 100.0:
        return None

    return needed
