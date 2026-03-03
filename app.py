import streamlit as st

st.title("💰 Expense Behavior Intelligence")

income = st.number_input("Monthly Income", 0)
expense = st.number_input("Monthly Expense", 0)

if st.button("Analyze Behavior"):
    ratio = expense / max(income,1)

    if ratio > 0.8:
        st.error("Risky Spending Behavior")
    elif ratio > 0.5:
        st.warning("Moderate Spending Behavior")
    else:
        st.success("Healthy Spending Behavior")