import streamlit as st

from cs135_calc import *

st.title("CS 135 Grade Calculator")

st.markdown("**Weights:** Assignments 20% | Midterm 25% | Final 45% | Participation 10%")
st.markdown("**Pass if:** Assignments ≥ 50% AND (Midterm + Final) ≥ 35/70 points")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    assign_str = st.text_input(
        "Assignment scores (%)",
        value="",
        help="Comma-separated (e.g. 82, 95, 100)",
    )

with col2:
    iclicker_str = st.text_input(
        "Participation scores (%)",
        value="",
        help="Comma-separated (e.g. 100, 80, 90)",
    )

with col3:
    M = st.number_input("Midterm (%)", min_value=0.0, max_value=100.0, value=90.0)

# Helper to parse comma-separated numbers safely
def parse_scores(s):
    if not s.strip():
        return []
    parts = s.split(",")
    scores = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        try:
            scores.append(float(p))
        except ValueError:
            # ignore invalid entries silently
            pass
    return scores

assign_scores = parse_scores(assign_str)
iclicker_scores = parse_scores(iclicker_str)

A_avg = average(assign_scores)
P_avg = average(iclicker_scores) if iclicker_scores else 100.0  # assume 100 if none given

st.write(f"Detected {len(assign_scores)} assignment scores. Assignment average: **{A_avg:.2f}%**.")
if iclicker_scores:
    st.write(f"Detected {len(iclicker_scores)} participation scores. Participation average: **{P_avg:.2f}%**.")
else:
    st.write("No participation scores entered. Assuming **100%** for now (you can change this later).")

# Slider for final exam
F_slider = st.slider("What final exam mark do you expect?", 0.0, 100.0, 80.0, step=1.0)

st.divider()

grade_with_slider = compute_course_grade(A_avg, M, F_slider, P_avg)
assign_ok = assignment_requirement_met(A_avg)
exam_ok = exam_requirement_met(M, F_slider)
pass_overall = overall_pass(A_avg, M, F_slider)

col1, col2 = st.columns(2)

with col1:
    st.metric("Assignment Average", f"{A_avg:.1f}%")
    st.metric("Midterm", f"{M:.1f}%")
    st.metric("Participation Average", f"{P_avg:.1f}%")

with col2:
    st.metric("Final Exam (Expected)", f"{F_slider:.0f}%")
    st.metric("Course Grade", f"{grade_with_slider:.2f}%")
    if pass_overall:
        st.success("✓ Meets all requirements")
    else:
        missing = []
        if not assign_ok:
            missing.append("Assignments < 50%")
        if not exam_ok:
            missing.append("Exams < 35/70")
        st.info(f"Missing: {', '.join(missing)}")
