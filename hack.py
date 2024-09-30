import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
import numpy as np

# Set page config
st.set_page_config(page_title="Insulin Tracker", layout="wide")

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Mock user database (in a real application, use a secure database)
USERS = {
    "TigerofChrompet": "joegabby",
    "hackathonuser": "datathon"
}


def login():
    st.title("Insulin Tracker - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in USERS and USERS[username] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Logged in successfully!")
            st.rerun()  # Changed from st.experimental_rerun()
        else:
            st.error("Invalid username or password")


def calculate_insulin(weight):
    # This is a simplified calculation and should be adjusted based on medical advice
    return weight * 0.55


def main():
    st.title(f"Welcome to your Insulin Tracker, {st.session_state.username}!")

    # User weight input
    weight = st.number_input("Enter your weight (in kg)", min_value=0.0, step=0.1)

    if weight > 0:
        recommended_insulin = calculate_insulin(weight)
        st.write(
            f"Based on your weight, your recommended daily insulin intake is approximately {recommended_insulin:.2f} units.")

    st.write("Enter your manual syringe measurements below:")

    # Initialize or get the existing dataframe
    if 'df' not in st.session_state:
        st.session_state.df = pd.DataFrame(columns=['Insulin Units'])  # Only 'Insulin Units' now

    # Input for milliliters
    ml_input = st.number_input("Enter milliliters (mL)", min_value=0.0, step=0.1)

    if st.button("Add Entry"):
        insulin_units = ml_input * 100
        # Get the next available day index
        next_day_index = len(st.session_state.df) + 1  # Add 1 for a human-friendly starting day
        # Create the new row
        new_row = pd.DataFrame({'Insulin Units': [insulin_units]})
        st.session_state.df = pd.concat([st.session_state.df, new_row], ignore_index=True)

        # Add the 'Days' column after the row is added
        st.session_state.df['Days'] = range(1, len(st.session_state.df) + 1)

    # Display the dataframe
    st.write(st.session_state.df)

    # Calculate total insulin intake
    total_insulin = st.session_state.df['Insulin Units'].sum()
    st.write(f"Total insulin intake: {total_insulin:.2f} units")

    # Warning message
    if total_insulin > 400:
        st.warning("Warning: Your total insulin intake exceeds the recommended 400 units per day!")

    if not st.session_state.df.empty:
        plt.figure(figsize=(10, 6))
        # Plot against 'Days' column
        plt.plot(st.session_state.df['Days'], st.session_state.df['Insulin Units'], marker='o')
        plt.title('Insulin Units vs Day')
        plt.xlabel('Day')  # Correct label to 'Day'
        plt.ylabel('Insulin Units')
        plt.grid(True)

        # Set x-axis ticks (1 to 7)
        plt.xticks(range(1, len(st.session_state.df) + 1))  # Ensure x-axis covers all days
        st.pyplot(plt)
 


# Main app logic
if not st.session_state.logged_in:
    login()
else:
    main()
