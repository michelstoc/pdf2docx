# PDF-to-Word Converter

## Description

This is a simple Python program using Streamlit which allows you to upload a PDF file, convert it into Word format, and then download the resulting Word file.

## Installation

Before you start using this program, ensure that you have installed Python 3.x on your machine. If not, download and install Python from [here](https://www.python.org/downloads/).

After installing Python, clone this repository to your local machine by running the following command in your terminal:

```
git clone https://github.com/michelstoc/pdf2docx.git
```

Next, navigate to the repository's directory:

```
cd pdf2docx
```

Create a virtual environment to isolate your project's dependencies. Run the following command:

```
python3 -m venv env
```

Activate the virtual environment:

- On Windows:
```
env\Scripts\activate
```
- On Unix or MacOS:
```
source env/bin/activate
```

Once your virtual environment is activated, install the required dependencies with the following command:

```
pip install -r requirements.txt
```

## Usage

To start the Streamlit app, run the following command in your terminal:

```
streamlit run app.py
```

This will open a new browser window or tab with the Streamlit interface. Here, you can upload a PDF file using the provided button. Once uploaded, the app will automatically convert the PDF file into a Word document which you can then download.

## Contribution

We welcome contributions! Please feel free to make a pull request or open an issue on GitHub. If you notice a bug or have a feature request, please use the issues page to let us know.


