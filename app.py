import streamlit as st

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Londrina+Sketch&family=Rubik+Wet+Paint&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Londrina+Sketch&family=Rubik+Wet+Paint&display=swap');

    .title-font {
        font-family: "Rubik Wet Paint", system-ui;
        font-weight: 400;
        font-style: normal;
    }

    .intro-font {
        font-family: "Josefin Sans", sans-serif;
        font-optical-sizing: auto;
        font-weight: <weight>;
        font-style: normal;
}
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;' class='title-font'>Rusteeze Car Customizers</h1>", unsafe_allow_html=True)
st.markdown("---")

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

for part, options in car_parts.items():
    st.subheader(part)
    user_choice = st.selectbox(f"Select {part}", options.keys())
    user_choices[part] = user_choice
    total_cost += options[user_choice]

st.write("### Your Customization Summary")
for part, choice in user_choices.items():
    st.write(f"{part}: {choice} - ${car_parts[part][choice]}")

st.write("### Total Cost: $", total_cost)

if st.button("Purchase"):
    st.success("Thank you for your purchase! Your car will be ready soon.")
