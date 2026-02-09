import streamlit as st
import pickle
import nltk



# load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("📩 SMS Spam Classifier")

sms = st.text_area("Enter your message")

if st.button("Predict"):
    if sms.strip() == "":
        st.warning("Please enter a message")
    else:
        vector_sms = vectorizer.transform([sms])
        prediction = model.predict(vector_sms)[0]

        if prediction == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam")