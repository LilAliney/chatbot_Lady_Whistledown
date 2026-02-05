import streamlit as st
from chatbot_functies import chatbot_response

st.set_page_config(
    page_title="Lady Whistledown",
    page_icon="",
    layout="centered"
)

# Titel en uitleg
st.markdown("<h1 style='text-align: center; color: #ff69b4;'>Lady Whistledown</h1>")
st.markdown("<p style='text-align: center; color: #ffb6c1; font-size:16px;'>")
st.markdown("Chat with the most mysterious writers of the ton")


# input
with st.form(key="ai_form"):
    AI_concept = st.text_input("Ask Lady Whistledown anything you would like to know:")
    role = st.selectbox("For which audience should it be explained?",
                        ("Colin Bridgerton, Her husband", "A kind reader"))
    submit = st.form_submit_button("Let Lady Whistledown explain")

# output
if submit and AI_concept.strip():
    with st.spinner("Lady Whistledown is writing..."):
        prompt = f"""
                    You are a society columnist from the Regency era (Lady Whistledown).
                    Explain what the asker wants but keep in mind who the reader is in '{role}'.
                    Write elegantly, dramatically, and a little sarcastically, just like Lady Whistledown in Bridgerton.
                    Answer in English.
                    """
        antwoord = chatbot_response(prompt)
    st.markdown(f"Dearest Gentle Reader")
    st.write(antwoord)
