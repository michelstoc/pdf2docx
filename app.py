import streamlit as st
from docx import Document
import pdfplumber
import io

st.title('Convertisseur de PDF à DOCX')

uploaded_file = st.file_uploader("Choisissez un fichier PDF", type="pdf")
if uploaded_file is not None:
    pdf = pdfplumber.open(io.BytesIO(uploaded_file.read()))
    doc = Document()
    for page in pdf.pages:
        text = page.extract_text()
        doc.add_paragraph(text)

    # Sauvegarder le document DOCX dans un BytesIO object et le renvoyer
    docx_file = io.BytesIO()
    doc.save(docx_file)
    docx_file.seek(0)

    st.download_button(
        label="Télécharger le fichier DOCX",
        data=docx_file,
        file_name='output.docx',
        mime='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
