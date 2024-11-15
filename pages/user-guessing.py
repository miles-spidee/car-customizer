import streamlit as st
import random

st.set_page_config(
    page_title="Guess Game",
    page_icon=":question:",
)

if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'guessed_numbers' not in st.session_state:
    st.session_state.guessed_numbers = []

st.title("Guess the Number Game")

st.write("I'm thinking of a number between 1 and 100. You have 15 attempts!")

user_guess = st.number_input("Enter your guess (whole number):", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):

    st.session_state.attempts += 1
    st.session_state.guessed_numbers.append(user_guess)

    if user_guess < st.session_state.number_to_guess:
        st.write("Too low! Try again.")
    elif user_guess > st.session_state.number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write("Congratulations! You've guessed the number! Reload the site to play again!")
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.guessed_numbers = []

    attempts_left = 15 - st.session_state.attempts
    if attempts_left > 0:
        st.write(f"You have {attempts_left} attempts left.")
    else:
        st.write(f"Game over! The number was {st.session_state.number_to_guess}.")
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.guessed_numbers = []

if st.session_state.guessed_numbers:
    st.write("Your guesses:", st.session_state.guessed_numbers)

def binary_search_guess(low, high, guess_count):
    return (low + high) // 2

    