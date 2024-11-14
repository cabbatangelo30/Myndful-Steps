import streamlit as st 
import pandas as pd
import datetime

# Set the page title and layout
st.set_page_config(page_title="Myndful Steps", layout="wide")

# Title of the app
st.title("Myndful Steps")

# Sidebar navigation
st.sidebar.header("Navigation")
app_mode = st.sidebar.radio("Select Mode", ["Home", "Self-Efficacy", "Stages of Change", "Physical Activity", "Barriers to Physical Activity", "Educational Module", "Activity Log", "Results"])

# Home Page
if app_mode == "Home":
    st.header("Welcome to Myndful Steps")
    st.write("""
    This app helps you measure your health behavior change using theories of self-efficacy and stages of change. 
    It also assesses your physical activity using the **Exercise Vital Sign (EVS)**. The app will provide personalized recommendations based on your responses.
    """)

# Self-Efficacy Assessment
elif app_mode == "Self-Efficacy":
    st.header("Self-Efficacy Assessment")
    
    st.write("""
    Self-efficacy refers to an individual's belief in their ability to succeed in specific situations or accomplish a task. 
    This assessment will help measure your confidence in making health behavior changes.
    """)

    # Self-Efficacy scale (1-10)
    confidence = st.slider("On a scale from 1 to 10, how confident are you in your ability to make a lasting change in your health behaviors?", 1, 10, 5)
    
    if st.button("Submit Self-Efficacy Score"):
        st.session_state.confidence = confidence
        st.success(f"Your self-efficacy score is: {confidence}. Higher scores indicate greater confidence in making health changes.")

# Stages of Change Assessment
elif app_mode == "Stages of Change":
    st.header("Stages of Change Assessment")

    st.write("""
    Behavior change occurs in stages. This assessment will help identify your current stage of change for health behaviors.
    """)

    # Stages of Change options
    stage = st.radio("Which of the following best describes your current stage of behavior change?", 
                     ("Precontemplation", "Contemplation", "Preparation", "Action", "Maintenance"))
    
    if st.button("Submit Stage of Change"):
        st.session_state.stage = stage
        st.success(f"Your current stage of change is: {stage}.")

# Physical Activity Assessment (Exercise Vital Sign, EVS)
elif app_mode == "Physical Activity":
    st.header("Physical Activity Assessment (Exercise Vital Sign)")

    st.write("""
    The Exercise Vital Sign (EVS) is a set of questions that help assess the frequency and duration of moderate to strenuous exercise you engage in each week.
    """)

    # Frequency of Exercise (How often per week)
    exercise_frequency = st.slider("How many days per week do you engage in moderate or strenuous exercise?", 0, 7, 3)

    # Duration of Exercise (How many minutes per session)
    exercise_duration = st.slider("On average, how many minutes per session do you engage in moderate or strenuous exercise?", 0, 120, 30)

    # Cardio and weight training minutes
    cardio_minutes = st.slider("How many minutes per week do you engage in cardio-respiratory training?", 0, 300, 60)
    weight_minutes = st.slider("How many minutes per week do you engage in weight-based training?", 0, 300, 60)

    if st.button("Submit Exercise Data"):
        st.session_state.exercise_frequency = exercise_frequency
        st.session_state.exercise_duration = exercise_duration
        st.session_state.cardio_minutes = cardio_minutes
        st.session_state.weight_minutes = weight_minutes
        st.success(f"You engage in exercise {exercise_frequency} days per week for an average of {exercise_duration} minutes per session. Cardio: {cardio_minutes} minutes/week, Weight training: {weight_minutes} minutes/week.")

# Barriers to Physical Activity
elif app_mode == "Barriers to Physical Activity":
    st.header("Identify Barriers to Physical Activity")
    
    st.write("""
    Understanding barriers can help us address obstacles to engaging in regular physical activity.
    """)
    barriers = st.text_area("Please list any personal barriers you feel may prevent you from engaging in physical activity.")
    
    if st.button("Submit Barriers"):
        st.session_state.barriers = barriers
        st.success("Thank you for sharing your barriers to physical activity.")

# Educational Module
elif app_mode == "Educational Module":
    st.header("Educational Module: Benefits of Exercise & Behavior Change")

    st.write("""
    **Benefits of Exercise**:
    - Improves cardiovascular health, strength, and flexibility
    - Boosts mood and reduces symptoms of depression and anxiety
    - Enhances cognitive function and reduces risks of chronic diseases

    **Theories of Health Behavior Change**:
    - **Self-Efficacy**: Belief in one's ability to initiate and persist in behaviors that lead to desired outcomes.
    - **Stages of Change**: Understand where you are in the behavior change process, from precontemplation to maintenance.

    **Counseling Services**:
    - **The Counseling Center** is available for all students and offers mental health support.
    - **Contact Information**:
        - Phone: 781-891-2274
        - Location: Callahan Building, 2nd Floor
        - Hours: Mon-Fri, 9am-12pm & 1pm-4pm (Closed 12-1pm for lunch)
    """)

# Activity Log (Journaling)
elif app_mode == "Activity Log":
    st.header("Weekly Activity Log")

    st.write("Log your daily physical activities and experiences here.")
    
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    activity_log = {}
    
    for day in days:
        activity_log[day] = st.text_area(f"{day} - Type of Activity & Minutes", key=day)
    
    if st.button("Submit Activity Log"):
        st.session_state.activity_log = activity_log
        st.success("Your weekly activity log has been saved.")

# Results Page
elif app_mode == "Results":
    st.header("Myndful Steps Results")

    if 'confidence' in st.session_state:
        st.write(f"**Self-Efficacy Score**: {st.session_state.confidence}")
    else:
        st.write("Please complete the Self-Efficacy assessment first.")
    
    if 'stage' in st.session_state:
        st.write(f"**Stage of Change**: {st.session_state.stage}")
    else:
        st.write("Please complete the Stages of Change assessment first.")
    
    if 'exercise_frequency' in st.session_state and 'exercise_duration' in st.session_state:
        st.write(f"**Physical Activity**: {st.session_state.exercise_frequency} days per week, {st.session_state.exercise_duration} minutes per session. Cardio: {st.session_state.cardio_minutes} min/week, Weight training: {st.session_state.weight_minutes} min/week.")
    else:
        st.write("Please complete the Physical Activity assessment first.")
    
    if 'barriers' in st.session_state:
        st.write(f"**Barriers to Physical Activity**: {st.session_state.barriers}")
    
    if 'activity_log' in st.session_state:
        st.write("**Weekly Activity Log**:")
        for day, log in st.session_state.activity_log.items():
            st.write(f"{day}: {log}")
    
    # Tailored recommendations based on WHO guidelines
    st.write("\n### Recommendations:")
    if st.session_state.exercise_frequency < 3:
        st.write("- Aim to exercise 3-5 days per week to meet minimum health guidelines.")
    if st.session_state.exercise_duration < 30:
        st.write("- Consider increasing sessions to at least 30 minutes for optimal benefits.")
    if st.session_state.cardio_minutes + st.session_state.weight_minutes < 150:
        st.write("- WHO recommends at least 150-300 minutes of moderate exercise per week or 75-150 minutes of vigorous exercise per week.")

    st.write("\n**Remember:** Counseling Center is available to support your mental well-being. Reach out if needed!")
