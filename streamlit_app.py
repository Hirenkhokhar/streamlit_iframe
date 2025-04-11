import streamlit as st

st.set_page_config(page_title="Embedded Streamlit", layout="centered")

st.title("Hello from Streamlit!")
st.write("This Streamlit app is embedded inside a React website.")
if "budget" not in st.session_state:
    st.session_state["budget"] = None

# Selectbox for budget selection
select = st.selectbox("Select your budget:", ("low", "medium", "high"))

# Update session state with selected budget
st.session_state["budget"] = select

# Show success message
st.success(f"Your selected budget is: {select}")
      


