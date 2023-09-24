import streamlit as st
import random

# Set the page title and icon
st.set_page_config(page_title="Number Guessing Game", page_icon="🎮")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 3

st.title("Number Guessing Game")
st.write("You have 3 attempts to guess the secret number.")

while attempts > 0:
    # Add an input field for the user to enter their guess
    user_guess = st.number_input("Enter your guess:", min_value=1, max_value=100)

    if st.button("Check"):
        attempts -= 1
        if user_guess == secret_number:
            st.success("Congratulations! You guessed the correct number.")
            break
        elif user_guess < secret_number:
            st.error("Try a higher number.")
        else:
            st.error("Try a lower number.")
        
        if attempts > 0:
            st.write(f"You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
        else:
            st.error("Sorry, you've run out of attempts. You failed.")
            break

    # Reset the game
    if st.button("New Game"):
        secret_number = random.randint(1, 100)
        attempts = 3
        st.success("New game started. You have 3 attempts to guess the new secret number.")

# Display the secret number (for testing purposes)
st.write(f"**Hint:** The secret number was {secret_number}")
