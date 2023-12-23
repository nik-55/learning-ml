import streamlit as st
from answer import getAnswer, uploadedFile

st.title("PDF Q&A")

file = st.file_uploader("Upload a PDF file", type="pdf")

process_btn = st.button("Process")

if process_btn:
    if file is None:
        st.write("Please upload a file")
    else:
        uploadedFile(file)

question = st.text_area("Question", placeholder="write your question here", max_chars=1000)

btn = st.button("Submit")

if btn:
    if None in (question, file) or question == "":
        st.write("Please process file and write a question")
    else:
        st.title("Answer")
        st.write(getAnswer(question, file))