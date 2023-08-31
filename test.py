import streamlit as st

def calculate_worth(income, profession, employment_status, location):
    # Your worth calculation logic here
    profession_weights = {
        "engineer": 0.3,
        "doctor": 0.4,
        "businessman": 0.5,
        "unemployed": 0.1
    }

    employment_weights = {
        "employed": 0.2,
        "unemployed": 0.1
    }

    location_weights = {
        "India": 0.2,
        "USA": 0.4,
        "Australia": 0.3
        # Add more locations and weights as needed
    }

    profession_worth = profession_weights.get(profession.lower(), 0)
    employment_worth = employment_weights.get(employment_status.lower(), 0)
    location_worth = location_weights.get(location, 0)

    total_worth = (
        0.2 * profession_worth +
        0.2 * employment_worth +
        0.2 * location_worth
    )

    if profession.lower() == "doctor":
        total_worth += 400000
    elif profession.lower() == "engineer":
        total_worth += 300000
    elif profession.lower() == "unemployed":
        total_worth += 100000

    final_worth = total_worth + income * 10
    return f"Your calculated Dowry in rupees: {final_worth:.2f}"

st.title("Dowry Calculator (by yours truly - A^2)")
st.write("Naughty hora k BKL")

income = st.number_input("Monthly Income (in rupees)")
profession = st.selectbox("Profession", ["Engineer", "Doctor", "Businessman", "Unemployed"])
employment_status = st.selectbox("Employment Status", ["Employed", "Unemployed"])
location = st.selectbox("Location", ["India", "USA", "Australia"])

if st.button("Calculate Dowry"):
    result = calculate_worth(income, profession, employment_status, location)
    st.write(result)
