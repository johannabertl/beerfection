import streamlit as st
import calculate_temperature


def main() -> None:
    st.set_page_config(page_title="Beerfection")
    st.title("The perfect drinking temperature for your beer")
    st.image("pictures/beer-10.gif")

    options = ["lager", "IPA", "NEIPA"]
    choice = st.selectbox("Choose your beer:", options)

    if st.button("Calculate"):
        result = calculate_temperature.lookup_temp(choice)
        st.success(f"Result: {result}")
    else:
        st.write("Select an option and click Calculate.")


if __name__ == "__main__":
    main()
