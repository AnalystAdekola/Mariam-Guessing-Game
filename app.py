import streamlit as st
import random

# --- THEME & LOGO ---
st.set_page_config(page_title="Mariam Guessing Game", page_icon="🤖❤️")
st.title("🤖❤️ Mariam Guessing Game")

# --- GAME LOGIC (Using Session State) ---
# This ensures the number doesn't change every time you guess
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.write("I'm thinking of a number between **1 and 20**. Can you score?")

# --- USER INPUT ---
guess = st.number_input("Enter your guess:", min_value=1, max_value=20, step=1)
submit = st.button("Submit Guess")

if submit and not st.session_state.game_over:
    st.session_state.attempts += 1
    
    if guess < st.session_state.secret_number:
        st.warning("Too low! Aim higher.")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Drop your aim.")
    else:
        st.success(f"⚽ GOAL! Correct! You found it in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True
        st.balloons()

# --- RESET BUTTON ---
if st.session_state.game_over:
    if st.button("Play Again"):
        del st.session_state.secret_number
        st.rerun()
