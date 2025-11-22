import streamlit as st

st.set_page_config(layout="wide")

from cs135_calc import *

st.title("CS 135 Grade Calculator")

st.markdown("⚠️ **Disclaimer:** This calculator is unofficial, may contain errors, and is not affiliated with the University of Waterloo.")
st.markdown("**Weights:** Assignments 20% | Midterm 25% | Final 45% | Participation 10%")
st.markdown("**Pass if:** Assignments ≥ 50% AND (Midterm + Final) ≥ 35/70 points")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    assign_scores = st.number_input(
        "Assignment scores (%)",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=0.1,
        help="Average Assignment Score",
    )

with col2:
    iclicker_scores = st.number_input(
        "Participation scores (%)",
        min_value=0.,
        max_value=100.0,
        value=100.0,
        step=0.1,
        help="Top 75\% of Iclickr Marks",
    )

with col3:
    M = st.number_input("Midterm (%)", 
                        min_value=0., 
                        max_value=100., 
                        value=90., 
                        step=0.1)


st.write(f"Assignment average: ***{assign_scores:.2f}%***.")
st.write(f"Participation average: ***{iclicker_scores:.2f}%***.")

# Slider for final exam
F_slider = st.slider("What final exam mark do you expect?", 0.0, 100.0, 80.0, step=1.0)

st.divider()

grade_with_slider = compute_course_grade(assign_scores, M, F_slider, iclicker_scores)
assign_ok = assignment_requirement_met(assign_scores)
exam_ok = exam_requirement_met(M, F_slider)
pass_overall = overall_pass(assign_scores, M, F_slider)
needed_final_score = needed_score_on_final(assign_scores, M)

col1, col2 = st.columns(2)

with col1:
    st.metric("Assignment Average", f"{assign_scores:.1f}%")
    st.metric("Midterm", f"{M:.1f}%")
    st.metric("Participation Average", f"{iclicker_scores:.1f}%")

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

st.divider()

col1, = st.columns(1)

if needed_final_score is None:
    final_text = "Impossible"
else:
    final_text = f"{needed_final_score:.0f}%"

with col1:
    st.markdown(f"""
        <div style="
            background-color:#22ddca;
            padding:20px;
            border-radius:10px;
            text-align:center;
            font-size:40px;
            font-weight:800;
            color:#000;
            margin-top:10px;">
            Score Needed on Final: {final_text}
        </div>
        """, unsafe_allow_html=True)


