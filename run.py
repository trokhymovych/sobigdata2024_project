import numpy as np
import pandas as pd
import requests
import streamlit as st
from pydantic import BaseModel
import altair as alt
import json


QUESTIONS = {
    "question 1": "What is the size of the company?",
    "question 2": "What is the industry of the company?",
    "question 3": "What is the location of the company?",
    "question 4": "What is the revenue of the company?"
}
ANSWERS = dict()
document_link = "imgs/logo.png"
DOCUMENTS_MOCK = [
    ("Document 1 Title", "Document 1 text 1", document_link),
    ("Document 1 Title", "Document 1 text 2", document_link),
    ("Document 2 Title", "Document 2 text 2", document_link),
    ("Document 2 Title", "Document 2 text 1", document_link),
    ("Document 3 Title", "Document 3 text 2", document_link),
    ("Document 3 Title", "Document 3 text 1", document_link),
    ("Document 4 Title", "Document 4 text 2", document_link),
    ("Document 4 Title", "Document 4 text 1", document_link),
    ("Document 5 Title", "Document 5 text 2", document_link),
    ("Document 5 Title", "Document 5 text 1", document_link),
]

# Header organisation
st.set_page_config(page_title="ReSearch: Regulation documents search", layout="wide", page_icon="🔭")

# Create a spaces for the first line:
row0_spacer1, row0_1, row0_spacer2, row0_2 = st.columns(
    (0.7, 5, 0.5, 3)
)

with row0_spacer1:
    st.image('imgs/logo.png')
row0_1.title(" ReSearch: Regulation documents search")


# reassigning rows
_, row0_1, _, row0_2, _ = st.columns(
    (0.5, 3, 0.5, 3, 0.5)
)

# Add the form information:
with row0_1:
    # displaying the information regarding generated question
    row0_1.markdown("---")
    row0_1.markdown('### Self-reflective control checklist')
    row0_1.markdown('**Some legal info**')
    form = st.form(key="annotation", clear_on_submit=False)
    with form:
        # self-reflective form:
        for i, (question_id, question_text) in enumerate(QUESTIONS.items()):
            ANSWERS[question_id] = st.text_input(f"**{i+1}. {question_text}**", key=question_id)
        submitted = st.form_submit_button(label="Process my form")


with row0_2:
    row0_2.markdown("---")
    row0_2.markdown('### Documents to check:')
    if submitted and any([ANSWERS.get(q) == "" for q in QUESTIONS.keys()]):
        row0_2.error('**Please check if all the fields are filled.**')
    elif not submitted:
        row0_2.warning('**Please submit the form first.**')
    else:
        row0_2.success("**Please check the documents needed to check.**")
        row0_2.balloons()
        row0_2.container()

        unique_documents = set([d[0] for d in DOCUMENTS_MOCK])
        for doc_name in unique_documents:
            with row0_2.expander(doc_name):
                local_docs = [d for d in DOCUMENTS_MOCK if d[0] == doc_name]
                # Showing all snipets for the found document: 
                for j, snippet_docs in enumerate(local_docs):
                    st.markdown(f"Document snipet {j+1}: {snippet_docs[1]}")
                # Downloading the whole document: 
                with open(local_docs[0][2], "rb") as file:
                    btn = st.download_button(
                            label=f"Download {doc_name}",
                            data=file,
                            file_name=local_docs[0][2],
                            key=doc_name
                        )
                

