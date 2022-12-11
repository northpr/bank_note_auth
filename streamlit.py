import streamlit as st
import pickle

# Save and load model
pickle_model = open("model/rfc.pkl","rb")
rfc = pickle.load(pickle_model)

# To predict the value
def predict_note_authentication(variance, skewness, curtosis, entropy):
    predict = rfc.predict([[variance, skewness, curtosis, entropy]])
    return predict

# Test the random forest model
# print(predict_note_authentication(1,2,3,4))

def main():
    st.title("Bank Note Authenticator")
    st.markdown("""
    ## ** Dataset Information: **
    **Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.**
                """,True)
    html_temp = """<div style="background-color:tomato;padding:10px">
                <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
                </div>"""
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Variance")
    skewness = st.text_input("skewness", "skewness")
    curtosis = st.text_input("curtosis", "curtosis")
    entropy = st.text_input("entropy", "entropy")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(variance, skewness, curtosis, entropy)
        if result == 0:
            st.success("The Banknotes are Genuine ✅")
        else:
            st.error("The Banknotes are Fake ❌")

    if st.button("About:"):
        st.markdown("""
                    **Source: https://github.com/DARK-art108**""")
        
if __name__ == "__main__":
    main()

