import streamlit as st
import calculate_temperature


def main() -> None:
    st.set_page_config(page_title="Beerfection")
    st.title("The perfect drinking temperature for your beer")
    st.image("pictures/beer-10.gif")

    options = ["lager", "IPA", "NEIPA"]
    choice = st.selectbox("Choose your beer:", options)

    if st.button("Fetch optimal drinking temperature"):
        result = calculate_temperature.lookup_temp(choice)
        st.success(f"The optimal temperature for {choice} is: {result}")


    cooling_options = ["Fridge (6°C)", "Freezer (-18°C)", "Ice bath"]
    cooling_choice = st.radio("Choose your cooling method:", cooling_options, index=None)

    container_options = ["Glass bottle", "Plastic bottle", "Can"]
    container_choice = st.radio("Choose your container type:", container_options, index=None)


    # Size

    container_size = st.radio(
        "Container size:",
        ["330 ml", "500 ml", "other"],
        index=None,
    )

    if container_size == "other":
        container_size = st.text_input("Container size (in ml):")


    if st.button("Calculate the cooling time"):
        st.success(f"The optimal cooling time for your {choice} in a {container_size} {container_choice} in the {cooling_choice} is 5 minutes.")

    

if __name__ == "__main__":
    main()
