ITNPA34 Research Analytics System
Project Overview
Researchly is a research analytics prototype developed using Python,
Natural Language Processing (NLP), and machine learning. It demonstrates
two related capabilities:
Research abstract classification --- classifies research
abstracts into the dataset's available categories (AI and
Classical).
Research trend exploration --- preprocesses a small corpus of
research articles, summarises article content, and applies Latent
Dirichlet Allocation (LDA) to explore recurring themes.
The project was developed as an academic proof of concept using the
datasets supplied for the assignment.
Project Objectives
Load and preprocess research abstracts and research article
documents.
Apply text-denoising techniques such as lowercasing, removal of
unwanted markup and symbols, stop-word filtering, and lemmatisation.
Extract text features using TF-IDF.
Train and evaluate machine-learning classifiers.
Compare model performance against a Multinomial Naive Bayes
baseline.
Provide a Streamlit interface for classifying a user-entered
research abstract.
Explore research themes using LDA and visualise topic relationships
using pyLDAvis.
Technologies
Python
Jupyter Notebook
pandas
scikit-learn
NLTK
Matplotlib
Streamlit
pyLDAvis
NetworkX
pypdf and python-docx (for reading supported document formats)
Repository Structure
``` text
Researchly-Research-Analytics/
├── Documentation/
│   ├── Question_1_Documentation.pdf
│   ├── Question_2_Documentation.pdf
│   ├── Question_3_Documentation.pdf
│   └── Question_4_Documentation.pdf
├── Datasets/
│   ├── research_abstracts.json
│   ├── research_corpus.zip
├── Notebooks/
│   ├── Question_1.ipynb
│   ├── Question_2.ipynb
│   ├── Question_3.ipynb
│   └── Question_4.ipynb
├── Deployment/
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   └── research_abstracts.json
└── README.md
```
Update the filenames and folders to match the files actually committed
to the repository. Do not add generated files that are not included.
Getting Started
1. Clone the repository
``` bash
git clone https://github.com/Mosky27/ITNPA34_Online_Project2_Eduv10190940.git
cd Researchly-Research-Analytics
```
2. Create and activate a virtual environment (recommended)
``` bash
python -m venv .venv
```
Windows:
``` bash
.venv\Scripts\activate
```
3. Install dependencies
``` bash
pip install -r Deployment/requirements.txt
```
4. Run the web application
``` bash
cd Deployment
streamlit run app.py
```
Then open the local address printed by Streamlit, usually:
`http://localhost:8501`
The application requires `research_abstracts.json` to be available at
the path expected by `app.py`. The simplest arrangement is to keep the
dataset in the `Deployment/` folder alongside the application, as shown
above.
Reproducing the Analysis
Open the relevant notebook in the `Notebooks/` folder.
Ensure the required dataset is in the location referenced by the
notebook, or update the path in the notebook.
Install the required packages.
Run the notebook cells in order, from data loading and preprocessing
through model evaluation or topic modelling.
The notebooks are the primary record of the analytical workflow and
should include the code, outputs, evaluation results, and visualisations
for the corresponding questions.
Model Evaluation Note
The baseline Multinomial Naive Bayes model and the alternative
classifiers were evaluated using a held-out test set. In the recorded
experiment, Random Forest achieved the highest accuracy among the four
models tested (91.52%), compared with 89.29% for the baseline. A
subsequent hyperparameter-tuning experiment produced 91.07% test
accuracy, so it did not improve overall accuracy over the original
Random Forest configuration. These figures describe the particular
dataset split and experiment; they are not a guarantee of performance on
new data.
Data and Reproducibility
Keep the original supplied datasets unchanged where possible.
Clearly distinguish original data from processed outputs.
Record any changes to file paths or preprocessing steps.
Do not commit confidential, licensed, or personally identifiable
data unless you have permission.
Large datasets may need Git Large File Storage (Git LFS), depending
on GitHub's file-size limits.
Limitations
The research trend corpus used for topic modelling is small. Therefore,
LDA topics should be treated as exploratory themes within the supplied
documents, not as definitive evidence of trends across the entire AI
research field. Topic labels are interpretations of the words grouped by
the model and should be checked against the original articles.
Project Source
Source: MATANGA NY (2026), assignment brief and supplied datasets.
License
Add the licence required by your institution or project owner before
redistributing this repository. If no redistribution permission has been
granted for the datasets or source materials, do not add a licence that
implies permission to reuse them.
