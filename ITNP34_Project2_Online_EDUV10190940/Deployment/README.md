ITNPA34 Deployment Guide
This folder contains the Streamlit application for the Researchly
research abstract classifier.
What the application does
The application accepts a research abstract and predicts whether it
belongs to one of the categories represented in the training dataset
(for example, `ai` or `classical`).
The current prototype uses:
Text cleaning based on the preprocessing workflow in the project.
TF-IDF text features.
A Random Forest classifier.
The application trains the model from `research_abstracts.json` when it
starts. It therefore needs the dataset file to be available at the
location expected by `app.py`.
Folder contents
``` text
Deployment/
├── app.py
├── README.md
└── research_abstracts.json
```
Make sure the actual files are present. If the dataset is stored
elsewhere, update the dataset path in `app.py`.
Requirements
Python 3.9 or later (use a version compatible with the installed
scikit-learn and Streamlit releases).
pip.
The `research_abstracts.json` dataset.
Install and run locally
1. Open a terminal in this folder
Change directory to the `Deployment` folder:
``` bash
cd path/to/Researchly-Research-Analytics/Deployment
```
2. (Recommended) Create a virtual environment
``` bash
python -m venv .venv
```
Windows:
``` bash
.venv\Scripts\activate
```

3. Start the application
``` bash
streamlit run app.py
```
Streamlit will print a local URL, usually:
`http://localhost:8501`
Open that address in a web browser.
Using the application
Paste or type a research abstract into the text input area.
Select Classify Abstract.
Read the predicted research category.
Review the displayed prediction probability, if enabled in the
application.
The probability is the model's estimated score for its prediction, not a
guarantee that the classification is correct.
Troubleshooting
`ModuleNotFoundError: No module named 'streamlit'`
Install the dependencies using:
``` bash
pip install -r requirements.txt
```
If using Jupyter Notebook, ensure that the terminal and notebook use the
intended Python environment.
Dataset file not found
Confirm that `research_abstracts.json` is in the `Deployment/` folder,
or edit the path used in `app.py`.
Streamlit command not found
Try launching Streamlit through Python:
``` bash
python -m streamlit run app.py
```
NLTK resource errors
The application downloads the required NLTK resources when it starts. If
the environment has no internet access, download the required NLTK data
in advance or configure the application to use locally available
resources.
Notes
The application is a prototype for academic demonstration.
Its predictive performance depends on the training data and model
configuration.
Retraining on the full dataset at application startup is convenient
for a prototype, but a production deployment would normally save and
load a validated model pipeline.
Do not expose private or restricted datasets through a public
deployment.
