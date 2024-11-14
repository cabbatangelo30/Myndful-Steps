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
    st.header("Educational Module: Exercise & Behavior Change")

    st.write("""
    **World Health Organization for Adult Physical Activity (per week)**:
    - Engage in either:
        - Moderate exercise for 150-300 minutes; OR,
        - Virgorous exercise for 75-150 minutes.
        - Ideally, the exercise is spread throughout the week
    
    **Benefits of Exercise**:
    - Improves cardiovascular health, strength, and flexibility
    - Boosts mood and reduces symptoms of depression and anxiety
    - Enhances cognitive function and reduces risks of chronic diseases

    **Consequences of Physical Inactivity**:
    Increase risk of:
﻿﻿        - Early death
﻿﻿        - Coronary heart disease
﻿﻿        - Stroke
﻿﻿        - High BP
﻿﻿        - Adverse blood lipid profile
﻿﻿        - Type 2 diabetes
﻿﻿        - Metabolic syndrome
﻿﻿        - Colon cancer
﻿﻿        - Breast cancer
﻿﻿        - Cancer recurrence/secondary cancers

    **Theories of Health Behavior Change**:
    - **Self-Efficacy**:
        - The belief in one's ability to accomplish a task
        - People will adhere to behaviors if they:
            - Believe they can initiate and carry out this behavior (self-efficacy),
            - Believe that the behavior will produce valuable outcomes (outcome expectations)
            
        - Sources of self-efficacy:
﻿﻿            - Mastery Experiences (successes/failures): personal successes and failures that shape a person’s confidence in their abilities.
              - Successes reinforce self-efficacy,
              - Failures—if interpreted as a learning experience—can also build resilience and determination.
              
﻿﻿            - Vicarious Experience (modeling): observing others (role models) successfully perform a behavior, which can enhance self-efficacy in those who feel similar to the model.
              - If users see someone else succeed, especially someone they identify with, it increases their belief that they, too, can succeed.
              
﻿﻿            - Social or Verbal Persuasion: encouragement or feedback from others that builds confidence.
              - Positive reinforcement from friends, coaches, or even virtual sources can strengthen self-efficacy by helping people believe they have the skills to succeed.
              
﻿﻿            - Physiological Responses: Physical and emotional reactions (e.g., fatigue, stress, or excitement) can influence self-efficacy.
              - When individuals feel relaxed and positive, they tend to have stronger self-efficacy beliefs.
              - Conversely, if they experience negative physical symptoms like exhaustion or anxiety, they may doubt their ability to succeed.

    - **Stages of Change**:
        - Pre-contemplation
            - Individuals in this stage have no immediate intention to change their behavior and may be unaware of the problem or its consequences. Often, people in this stage underestimate the benefits of change or see the downsides of change as too significant. Health interventions at this stage aim to raise awareness and encourage self-reflection, helping individuals recognize why the change might be beneficial in the future.
        
        - Contemplation
            - At this stage, individuals acknowledge the need for change and start weighing the pros and cons but have not committed to action. This period can involve ambivalence and may last for extended periods as individuals assess their motivations. Effective interventions in the contemplation stage often provide information on the benefits of change and work to reduce perceived obstacles, helping individuals develop a stronger desire to take action.
        
        - Preparation
            - In the preparation stage, individuals make concrete plans to begin the desired behavior change, such as gathering information, setting goals, or preparing resources. The decision to act is made, and short-term steps are initiated to build momentum toward change. Supportive strategies here can include setting a start date, creating a plan, and finding resources or support systems to help maintain motivation.
        
        - Action
            This stage involves direct efforts to change behavior, such as actively engaging in exercise routines if the goal is physical activity. It is often the most visible stage, where individuals start adopting new, healthier behaviors. Support during this phase is essential to reinforce motivation, celebrate successes, and provide tools to overcome challenges, ensuring that the change can be sustained.

        - Maintenance
            - Individuals in the maintenance stage continue the behavior consistently, typically for six months or more, and work to prevent relapse. This phase focuses on reinforcing progress and finding strategies to deal with potential triggers that could lead to reverting to old habits. Maintenance often involves a continuous commitment to the behavior, adjusting strategies as necessary, and may include reminders of the initial motivations to help sustain progress.

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
