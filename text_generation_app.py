from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv


load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-lite',temperature=0.7)


def main():
    st.title('SIMPLE TEXT GENERATION')
    st.subheader('User:')
    input_text = st.text_input('')

    submit = st.button('Click Here')
    if submit:
        response = model.invoke(input_text)
        st.subheader('Output:')
        st.write(response.content)

if  __name__=='__main__':
    main()





