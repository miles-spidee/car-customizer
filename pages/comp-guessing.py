import streamlit as st

def binary_search_guess(low, high, guess_count):
    """ Binary search algorithm to guess the number """
    return (low + high) // 2

def main():
    st.title("Computer Guesses Your Number Using Binary Search")
    
    # Get user input for the range of numbers
    st.sidebar.header("Set Range for Guessing")
    low = st.sidebar.number_input("Enter the lower bound", value=1, min_value=1)
    high = st.sidebar.number_input("Enter the upper bound", value=100, min_value=low + 1)
    
    # Ensure low is less than high
    if low >= high:
        st.sidebar.error("Lower bound must be less than upper bound.")
        return
    
    # Start guessing
    st.header("Think of a number between {} and {}!".format(low, high))
    st.subheader("Then, help the computer by answering its guesses!")

    guess_count = 0
    guess = binary_search_guess(low, high, guess_count)

    # Keep track of the guess count
    while True:
        guess_count += 1
        # Display the current guess
        st.write(f"Guess #{guess_count}: Is your number {guess}?")
        
        # Let the user provide feedback
        feedback = st.radio(
            "Is the guess correct?",
            ('Correct', 'Too High', 'Too Low'),
            key=f"guess_{guess_count}"
        )
        
        # Adjust the search range based on the feedback
        if feedback == 'Correct':
            st.success(f"Yay! The computer guessed your number, {guess}, in {guess_count} guesses!")
            break
        elif feedback == 'Too High':
            high = guess - 1
        elif feedback == 'Too Low':
            low = guess + 1
        
        # Make a new guess based on the updated range
        guess = binary_search_guess(low, high, guess_count)

if __name__ == "__main__":
    main()
