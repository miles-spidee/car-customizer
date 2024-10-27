import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Londrina+Sketch&family=Rubik+Wet+Paint&display=swap');

    body {
        background-color: #2c3e50;
        color: #ecf0f1;
        font-family: 'Arial', sans-serif;
    }

    .title-font {
        font-family: "Rubik Wet Paint", cursive;
        font-weight: 500;
        text-align: center;
        color: #e67e22;
        margin-bottom: 20px;
    }

    .subheader-font {
        font-family: "Arial", sans-serif;
        font-weight: 600;
        color: #e74c3c;
    }

    .summary {
        background-color: #34495e;
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }

    .total-cost {
        font-weight: bold;
        font-size: 1.5em;
        color: #f39c12;
    }

    .purchase-button {
        background-color: #1abc9c;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
        text-align: center;
        margin-top: 20px;
        display: inline-block;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .purchase-button:hover {
        background-color: #16a085;
        cursor: pointer;
        transform: scale(1.05);
    }

    .card {
        background-color: #2c3e50;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }

    .card select {
        background-color: #34495e;
        color: #ecf0f1;
        border: none;
        border-radius: 4px;
        padding: 10px;
        width: 100%;
    }

    .card select:focus {
        outline: none;
        border: 1px solid #e67e22;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title-font'>Rusteeze Car Customizers</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar for selection
st.sidebar.header("Customize Your Car")

# Car parts and their prices
car_parts = {
    "Wheels": {
        "Basic Wheels": 100,
        "Sport Wheels": 200,
        "Off-road Wheels": 300
    },
    "Color": {
        "Red": 50,
        "Blue": 50,
        "Black": 50,
        "White": 50
    },
    "Interior": {
        "Leather Seats": 400,
        "Fabric Seats": 200,
        "Custom Seats": 600
    },
    "Engine": {
        "Standard Engine": 500,
        "Turbo Engine": 800,
        "Electric Engine": 1000
    }
}

user_choices = {}
total_cost = 0

# Selection for car parts in the sidebar
for part, options in car_parts.items():
    user_choice = st.sidebar.selectbox(f"Select {part}", options.keys(), key=part)
    user_choices[part] = user_choice
    total_cost += options[user_choice]

# Display customization summary
st.markdown("<div class='summary'>", unsafe_allow_html=True)
st.write("### Your Customization Summary")
for part, choice in user_choices.items():
    st.write(f"{part}: {choice} - ${car_parts[part][choice]}")
st.markdown("</div>", unsafe_allow_html=True)

# Display total cost
st.write("### Total Cost: ", f"<span class='total-cost'>${total_cost}</span>", unsafe_allow_html=True)

# Purchase button
if st.button("Purchase"):
    st.markdown("<div class='purchase-button'>Thank you for your purchase! Your car will be ready soon.</div>", unsafe_allow_html=True)
