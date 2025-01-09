import streamlit as st
import pandas as pd
import numpy as np

# App Title
st.title("Loan Calculator with Savings Insights")

# User Inputs
st.sidebar.header("Enter Loan Details")
loan_amount = st.sidebar.number_input("Loan Amount ($)", min_value=1000, step=1000, value=10000)
interest_rate = st.sidebar.number_input("Interest Rate (APR %)", min_value=0.1, max_value=30.0, step=0.1, value=5.0)
loan_term = st.sidebar.number_input("Loan Term (Years)", min_value=1, max_value=30, step=1, value=5)
monthly_income = st.sidebar.number_input("Monthly Income ($)", min_value=500, step=100, value=3000)

# Calculate EMI
monthly_rate = interest_rate / 100 / 12
n_payments = loan_term * 12
emi = loan_amount * monthly_rate * ((1 + monthly_rate)**n_payments) / (((1 + monthly_rate)**n_payments) - 1)

# Suggested Savings
savings_percentage = 20  # Suggest saving 20% of income
suggested_savings = monthly_income * (savings_percentage / 100)

# Display Results
st.header("Loan Details and Insights")
st.write(f"**Loan Amount:** ${loan_amount:,.2f}")
st.write(f"**Interest Rate (APR):** {interest_rate:.2f}%")
st.write(f"**Loan Term:** {loan_term} years")
st.write(f"**Monthly Installment (EMI):** ${emi:,.2f}")
st.write(f"**Suggested Monthly Savings (20% of Income):** ${suggested_savings:,.2f}")

# Example Dataset
if st.checkbox("Show Example Dataset"):
    data = {
        "Loan Amount": [10000, 20000, 30000],
        "Interest Rate (%)": [5.0, 7.0, 10.0],
        "Term (Years)": [5, 10, 15],
        "Monthly Income ($)": [3000, 4000, 5000],
    }
    df = pd.DataFrame(data)
    st.write("Example Scenarios:")
    st.dataframe(df)
