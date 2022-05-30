import pickle
import streamlit as st

model = pickle.load(open("spam.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


def main():
    st.title("Email Spam Classification.", )
    st.subheader("Build with Python and Streamlit.")
    msg = st.text_input("Input", placeholder = "Enter your mail content here.")
    st.write("Your mail : "+msg)
    if(st.button("Predict")):
        data = [msg]
        vector = vectorizer.transform(data).toarray()
        pred = model.predict(vector)[0]
        if(pred == 1):
            st.success("Your mail is not SPAM.")
        else: st.error("Your mail is a SPAM.")

main()