# Breast Cancer Classification Web App

This project is a machine learning-based diagnostic tool that classifies breast tumors as **benign** or **malignant**. It aims to assist with early detection of breast cancer, supporting **Sustainable Development Goal (SDG) 3: Good Health and Well-being**.

---

## Project Overview

Breast cancer is one of the most prevalent cancers among women worldwide. Early detection is critical for improving survival rates. This tool uses machine learning algorithms trained on the Wisconsin Breast Cancer (Diagnostic) dataset to classify tumors based on biopsy features.

Each year, nearly 500,000 women globally are diagnosed with breast cancer ([source: nature.com](https://www.nature.com/)). A reliable predictive model can significantly aid healthcare professionals in early screening, thereby potentially reducing mortality.

---

## Dataset

- **Source**: Wisconsin Breast Cancer (Diagnostic) Dataset
- **Content**: 30 numerical features derived from digitized images of fine needle aspirates (FNA) of breast masses (e.g., radius, texture, perimeter, area, smoothness).
- **Target**: Diagnosis (Malignant `M` / Benign `B`)
- **Path**: `data/cleaned_breast_cancer.csv`

Data preprocessing steps included:

- Handling missing values
- Encoding target labels
- Normalizing/standardizing features where appropriate

---

## SDG 3 Alignment

This project contributes to **SDG 3: Good Health and Well-being** by:

- Promoting **early detection** through predictive analytics
- Assisting healthcare professionals with **decision support**
- Reducing risk of delayed diagnosis with rapid classification tools

> “Early diagnosis can provide medical staff with reliable and rapid responses to reduce the risk of death.” – [nature.com](https://www.nature.com/)

---

## Usage Instructions

### 1. Explore the Data & Model

# Launch the Jupyter notebook to explore data

jupyter notebook notebooks/breast_cancer_analysis.ipynb

### 2. Train the Model

Choose a model to train:

lr = Logistic Regression

svm = Support Vector Machine

rf = Random Forest

nn = Neural Network

python scripts/train.py --model rf

### 3. Evaluate the Model

python scripts/evaluate.py

Outputs:

Confusion Matrix

ROC Curve

Feature Importances (Gini + Permutation)

Metrics (accuracy, precision, recall, F1)

### 4. Run the Web App

streamlit run app/streamlit_app.py

The app provides an interactive interface to input features (e.g., radius, texture, perimeter, area, smoothness, etc.) and receive predictions (benign or malignant) from the trained model.

## Ethical Considerations

Medical AI carries important ethical responsibilities:

- Not a diagnostic tool: The app includes a disclaimer stating that predictions are for educational/demonstration purposes only.

- Bias in data: Historical datasets may reflect demographic or procedural biases.

- Model error: All models have false positive and false negative rates—human oversight is essential.

- Transparency: Code and instructions are open-source to promote trust and reproducibility.

- Explainability: Feature importance plots are included to support clinical interpretability.

Sample Outputs

- Confusion Matrix (Random Forest)
  Shows the number of correct and incorrect predictions. A good classifier has high values on the diagonal.

Example image placeholder:
figures/confusion_matrix_rf.png

- ROC Curve Comparison (SVM vs. RF)
  Visualizes model performance at different classification thresholds. Area Under Curve (AUC) is a key metric.

Example image placeholder:
figures/roc_curves.png

- Feature Importances
  Left: Gini importance (from Random Forest)

Right: Permutation importance (shows how model accuracy drops when a feature is shuffled)

Example image placeholder:
figures/feature_importance.png

## Project Structure

├── app/
│ └── streamlit_app.py # Streamlit web application
├── data/
│ └── cleaned_breast_cancer.csv # Preprocessed dataset
├── figures/
│ └── \*.png # Evaluation visualizations
├── models/
│ └── random_forest_model.pkl # Trained model
├── notebooks/
│ └── breast_cancer_analysis.ipynb
├── scripts/
│ ├── clean_data.py  
│ └── model_train.py
| |\_\_ utils.py  
├── requirements.txt
└── README.md

## Disclaimer

This tool is for educational and demonstrational use only. It should not be used for medical diagnosis. Always consult a licensed medical professional for health concerns.

## Contributors

## Author

👤 **Fred Kibutu**  
🌐 [Portfolio](https://kibutujr.github.io/Portfolio-KibutuJr/)  
💻 [GitHub Profile: KibutuJr](https://github.com/KibutuJr/)

## License

MIT License

Copyright (c) 2025 Fred Kibutu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
