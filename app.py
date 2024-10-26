import streamlit as st

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Londrina+Sketch&family=Rubik+Wet+Paint&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Londrina+Sketch&family=Rubik+Wet+Paint&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Chokokutai&family=Josefin+Sans:ital,wght@0,100..700;1,100..700&family=Londrina+Sketch&family=Rubik+Wet+Paint&display=swap');

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

    .stylish {
        font-family: "Chokokutai", system-ui;
        font-weight: 400;
        font-style: normal;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;' class='title-font'>Rusteeze Car Customizers</h1>", unsafe_allow_html=True)
st.markdown("---")

gif_url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia2.giphy.com%2Fmedia%2FResMcS5XgohYRGeBOH%2Fgiphy.gif&f=1&nofb=1&ipt=da9bee520526161284f3587a49941201e729b57db65d0a97c8e47acd88399414&ipo=images"

st.markdown(
    f"<div style='text-align: center;'><img src='{gif_url}' style='max-width: 100%;'></div>",
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align: center;' class='intro-font'>We make your cars more powerful than just wrooooom!</h3>", unsafe_allow_html=True)

# customising section
st.markdown("<h3 style='text-align: center;' class='stylish'>...</h3>", unsafe_allow_html=True)

st.title("Lets start customizing ...")

st.markdown("<h4 style='text-align: center;'>Which Spoiler do you need?</h4>", unsafe_allow_html=True)
spoiler_image = "https://example.com/spoiler_image.jpg"  # Replace with actual image URL
st.markdown(f"<div style='text-align: center;'><img src='{spoiler_image}' style='width: 100px; height: auto;'></div>", unsafe_allow_html=True)
options = ["Lip Spoilers", "Wing Spoilers", "Active Spoilers", "None"]
selected_option = st.radio("", options)

# Wheel question with image
st.markdown("<h4 style='text-align: center;'>Which Wheels do you need?</h4>", unsafe_allow_html=True)
wheel_image = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.JbgXbQcNHO9EA5JVj3C0VAAAAA%26pid%3DApi&f=1&ipt=4e5d4f2bc91f46f2657c47f862ce42c89e257b30353d385879520a7e309d8a18&ipo=images"  # Replace with actual image URL
st.markdown(f"<div style='float: right;'><img src='{wheel_image}' style='width: 100px; height: auto;'></div>", unsafe_allow_html=True)
options = ["Steel Wheels", "Alloy Wheels", "Chrome Wheels", "Default"]
selected_option = st.radio("", options)

