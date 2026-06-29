import streamlit as st
import csv
import os
import pandas as pd
from groq_helper import get_ai_analysis

def calculate_burnout(sleep_hours, screen_time, breaks_taken):

    burnout_score = 0

    if sleep_hours < 5:
        burnout_score += 40
    elif sleep_hours < 7:
        burnout_score += 20

    if screen_time > 8:
        burnout_score += 30
    elif screen_time >= 5:
        burnout_score += 15
    if breaks_taken <= 1:
        burnout_score += 20
    elif breaks_taken <= 3:
        burnout_score += 10

    if burnout_score >= 60:
        burnout_risk = "HIGH"
    elif burnout_score >= 30:
        burnout_risk = "MODERATE"
    else:
        burnout_risk = "LOW"

    return burnout_score, burnout_risk

def calculate_productivity(
    study_hours,
    sleep_hours,
    screen_time,
    breaks_taken
):

    score = 0

    score += study_hours * 10
    score += sleep_hours * 5
    score -= screen_time * 3
    score += breaks_taken * 2

    if score > 100:
        score = 100

    if score < 0:
        score = 0

    return score

def calculate_fake_productivity(
    study_hours,
    planning_hours,
    study_video_hours
):

    if study_hours == 0:
        return "HIGH"

    fake_ratio = (
        planning_hours + study_video_hours
    ) / study_hours

    if fake_ratio >= 1:
        return "HIGH"

    elif fake_ratio >= 0.5:
        return "MODERATE"

    else:
        return "LOW"
    
st.title("🎓 Student Burnout Detection System")

study_hours = st.number_input(
    "Study Hours Per Day",
    min_value=0,
    max_value=24
)

sleep_hours = st.number_input(
    "Sleep Hours Per Day",
    min_value=0,
    max_value=24
)

screen_time = st.number_input(
    "Screen Time Per Day",
    min_value=0,
    max_value=24
)

breaks_taken = st.number_input(
    "Breaks Taken",
    min_value=0
)

planning_hours = st.number_input(
    "Planning Hours",
    min_value=0,
    max_value=24
)

study_video_hours = st.number_input(
    "Study Video Hours",
    min_value=0,
    max_value=24
)

if st.button("Analyze"):

    burnout_score, burnout_risk = calculate_burnout(
        sleep_hours,
        screen_time,
        breaks_taken
    )

    productivity_score = calculate_productivity(
        study_hours,
        sleep_hours,
        screen_time,
        breaks_taken
    )

    fake_productivity = calculate_fake_productivity(
        study_hours,
        planning_hours,
        study_video_hours
    )

    st.success("Analysis Complete")

    st.subheader("📊 Analysis Results")

    col1, col2 = st.columns(2)

    with col1:
      st.metric("🔥 Burnout Score", burnout_score)
      st.metric("🎭 Fake Productivity", fake_productivity)

    with col2:
      st.metric("📈 Productivity Score", productivity_score)
      st.metric("⚠️ Burnout Risk", burnout_risk)

    st.write("Burnout score progress")
    st.progress(burnout_score / 100)
    st.write("Productivity score progress")
    st.progress(productivity_score / 100)
    file_exists = os.path.isfile("student_history.csv")
    with open("student_history.csv", "a", newline="") as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow([
                "StudyHours",
                "SleepHours",
                "ScreenTime",
                "BreaksTaken",
                "BurnoutScore",
                "ProductivityScore",
                "FakeProductivity"
            ])

        writer.writerow([
            study_hours,
            sleep_hours,
            screen_time,
            breaks_taken,
            burnout_score,
            productivity_score,
            fake_productivity
        ])


    if burnout_risk == "HIGH":
     st.error("High Burnout Risk Detected")

    elif burnout_risk == "MODERATE":
     st.warning("Moderate Burnout Risk")

    else:
     st.success("Low Burnout Risk")
     
    st.divider()
    st.header("🤖 AI Wellness Report")
    st.subheader("🤖 AI Analysis")

    with st.spinner("Generating AI insights..."):

       ai_response = get_ai_analysis(
        study_hours,
        sleep_hours,
        screen_time,
        breaks_taken,
        burnout_score,
        productivity_score,
        fake_productivity
    )

    st.markdown(ai_response)
    

    st.divider()

st.header("📈 Student History Dashboard")

try:
    df = pd.read_csv("student_history.csv")

    st.dataframe(df)

    st.subheader("🔥 Burnout Score Trend")
    st.line_chart(df["BurnoutScore"])

    st.subheader("📈 Productivity Score Trend")
    st.line_chart(df["ProductivityScore"])

except:
    st.info("No history available yet.")

    st.subheader("🔥 Burnout Score Trend")
st.write(df.columns)
st.line_chart(df["BurnoutScore"])
st.subheader("📈 Productivity Score Trend")

st.line_chart(df["ProductivityScore"])