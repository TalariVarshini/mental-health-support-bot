import streamlit as st
import matplotlib.pyplot as plt
import datetime

# Save mood score in session state
def store_mood(score):
    if 'mood_history' not in st.session_state:
        st.session_state['mood_history'] = []

    timestamp = datetime.datetime.now().strftime("%d-%b %H:%M")
    st.session_state['mood_history'].append((timestamp, score))

# Plot mood history
def plot_mood_history():
    if 'mood_history' in st.session_state and len(st.session_state['mood_history']) > 1:
        timestamps = [item[0] for item in st.session_state['mood_history']]
        scores = [item[1] for item in st.session_state['mood_history']]

        fig, ax = plt.subplots()
        ax.plot(timestamps, scores, marker='o', color='blue')
        ax.set_xlabel('Time')
        ax.set_ylabel('Mood Score')
        ax.set_title('🧠 Mood Tracker')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.info("🕒 Not enough data to show mood trend yet.")
