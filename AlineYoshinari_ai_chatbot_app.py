import streamlit as st
from chatbot_functies import chatbot_response

# tab stijl
st.set_page_config(
    page_title="Lady Whistledown",
    page_icon="🖋️"
)

# titel
st.markdown("# 🕯️ Lady Whistledown")
st.markdown("💖 Come read what the most mysterious writes of the ton answer's to your questions 💖")
# de lijn die de titel met de form parts
st.markdown("---")

# form
with st.form(key="ai_form"):
    question = st.text_input("Ask our dearest writer anything")
    role = st.selectbox("For which audience should it be explained?",
                        ("A gentle reader", "Queen Charlotte", "Colin Bridgerton", "Sir Petillion", "Miss Aline"))
    submit = st.form_submit_button("Let Lady Whistledown explain")

#input
if submit and question.strip():
    with st.spinner("Lady Whistledown is writing... 🖋️"):
        prompt = f"""
                You are a society columnist from the Regency era (Lady Whistledown).
                Answer the questions '{question}' from the person with the role '{role}',
                with a gentle tone just like lady whistledown from bridgerton book series.
                Write elegantly, dramatically, and a little sarcastically.
                Answer in English, always end with yours truly.
                """
        answer = chatbot_response(prompt)

    # output
    with st.container():
        st.markdown("🌸🌸🌸")
        st.markdown("### Dearest Gentle Reader")
        st.markdown(f"💌 {answer}")
        st.markdown("🌸🌸🌸")
