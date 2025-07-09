import streamlit as st
from emotion_model import get_emotion
from chatbot import get_chat_response
from mood_tracker import store_mood, plot_mood_history
from PIL import Image


# Page config
st.set_page_config(page_title="EmotiMate – Your AI Mood Companion", layout="centered", page_icon="🧠")

# Header Image
#img = Image.open("emoti_header.png")
#st.image(img, use_column_width=(60, 60))

# Inspiring quote
st.markdown(
    "<div style='background-color:#f0f4ff;padding:10px;border-radius:10px;text-align:center;'>"
    "<h3 style='color:#3b3c4f;'>“Your emotions are valid. Let’s talk it out, together 🤗”</h3>"
    "</div>", unsafe_allow_html=True
)

# Title
st.title("💬 EmotiMate – Your AI Mood Companion")

# User Input
user_text = st.text_area("📝 How are you feeling today?")

if user_text:
    emotion, score = get_emotion(user_text)
    mood_score = round(score * 10)

    st.markdown("---")
    st.markdown(f"### 🧠 Detected Emotion: **{emotion}**")
    st.progress(mood_score)
    st.write(f"📈 Mood Score: **{mood_score}/10**")

    # Track the mood
    store_mood(mood_score)

    # Self-care suggestions
    st.markdown("### 🌿 Self-Care Suggestion")
    if emotion.lower() in ["sadness", "fear", "anger", "anxiety"]:
        st.warning("🌧️ Try deep breathing or journaling. Want relaxing music? [Listen on YouTube](https://www.youtube.com/watch?v=2OEL4P1Rz04)")
        st.info("📞 Need to talk to someone? Reach out to [iCall India](https://icallhelpline.org/) or dial 9152987821")
    elif emotion.lower() == "joy":
        st.success("😄 Glad you're feeling good! Keep doing what works for you 🕺🎨")

# Chatbot
st.markdown("---")
st.markdown("### 🤖 Talk to EmotiMate")

chat_input = st.text_input("Type your message here:")

if chat_input:
    response = get_chat_response(chat_input)
    st.markdown(f"**EmotiMate:** {response}")

# Mood Tracker
st.markdown("---")
st.subheader("📊 Your Mood Tracker (This Session)")
plot_mood_history()

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center;color:gray'>Built with ❤️ using Streamlit + Hugging Face</p>", unsafe_allow_html=True)
