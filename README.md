# Intelligent-Procurement-Invoice-Analytics

### AI-Powered Vendor Invoice Risk Detection and Procurement Analytics

**Intelligent Procurement Invoice Analytics** is a data-driven and machine-learning-based system designed to analyze vendor invoices and procurement data, identify invoice discrepancies, detect potentially risky invoices, and provide actionable insights into vendor and invoice performance.

The system integrates **invoice, purchase order, item-level, and receiving data** to automatically identify anomalies such as invoice amount mismatches, quantity discrepancies, and abnormal receiving delays. A machine learning classification model is then used to predict invoice risk and support faster and more accurate invoice verification.

---

## 🚀 Project Overview

Manual invoice verification can be time-consuming and prone to human error, especially when organizations process a large number of vendor invoices.

This project aims to automate the invoice analysis process by combining:

* Data preprocessing
* Procurement data integration
* Feature engineering
* Exploratory Data Analysis
* Rule-based risk identification
* Machine learning classification
* Vendor risk analysis
* Invoice risk scoring
* Interactive dashboards

The system helps organizations identify invoices that require additional verification and provides insights into vendor-related risks and procurement performance.

---

## 🎯 Objectives

The main objectives of the project are:

* Analyze vendor invoice and procurement data.
* Integrate invoice, purchase order, receiving, and item-level information.
* Identify invoice amount and quantity mismatches.
* Detect abnormal receiving and processing delays.
* Generate invoice risk labels using predefined business rules.
* Build machine learning models for invoice risk classification.
* Evaluate models using **Accuracy, Precision, Recall, F1-Score, and Support**.
* Generate risk scores for individual invoices.
* Analyze vendor-wise invoice risk and performance.
* Provide an easy-to-understand dashboard for decision-making.
* Explain why an invoice has been classified as risky.

---

## 🔄 System Workflow

```text
                Procurement Data
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
     Invoices      Purchase Orders   Receiving
        │              │              │
        └──────────────┼──────────────┘
                       ↓
              Data Integration
                       ↓
               Data Preprocessing
                       ↓
              Feature Engineering
                       ↓
        ┌──────────────┴──────────────┐
        ↓                             ↓
   Exploratory Data             Risk Label Creation
      Analysis                         │
                                      ↓
                            Machine Learning Model
                                      │
                                      ↓
                              Risk Classification
                                      │
                 ┌────────────────────┼───────────────────┐
                 ↓                    ↓                   ↓
          Invoice Risk          Vendor Analysis      Risk Reasons
                 │                    │                   │
                 └────────────────────┼───────────────────┘
                                      ↓
                               Analytics Dashboard
```

---

## 🔍 Key Features

### 1. Invoice Data Analysis

The system analyzes important invoice attributes such as:

* Invoice amount
* Invoice quantity
* Vendor
* Invoice date
* Purchase order information
* Item-level information
* Receiving information

### 2. Invoice-Purchase Order Matching

The system compares invoice information with purchase order data to identify discrepancies in:

* Quantity
* Price
* Total amount
* Ordered vs. invoiced items

### 3. Item-Level Validation

Invoice totals are compared with item-level calculated totals to identify potential inconsistencies.

For example:

```text
Invoice Amount       = ₹10,000
Item-Level Amount    = ₹8,500
Difference           = ₹1,500
```

Such a difference can be used as an important risk indicator.

### 4. Receiving Delay Detection

The system analyzes receiving-related information to identify unusually high delays.

For example:

```text
Normal Receiving Delay  →  2–5 days
Abnormal Delay          →  10+ days
```

Abnormally high delays can contribute to an invoice's overall risk.

### 5. Invoice Risk Classification

Business rules are used to create initial invoice risk labels based on factors such as:

* Invoice amount mismatch
* Item-level amount mismatch
* Abnormally high receiving delay
* Other engineered risk indicators

The generated labels are then used to train classification models.

### 6. Machine Learning

The project uses supervised machine learning algorithms to classify invoices into risk categories.

The model learns patterns from historical invoice data and predicts whether a new invoice should be considered:

```text
0 → Low/Normal Risk
1 → High Risk
```

### 7. Model Evaluation

The classification models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Support
* Classification Report

Special attention is given to **Precision, Recall, and F1-Score** because correctly identifying risky invoices is an important part of the system.

### 8. Vendor Risk Analysis

The system analyzes invoice behavior at the vendor level to identify:

* High-risk vendors
* Number of invoices processed
* Risky invoice frequency
* Invoice mismatch patterns
* Vendor performance indicators

### 9. Risk Explanation

Instead of simply showing that an invoice is risky, the system can provide the reason behind the classification.

Example:

```text
Invoice Risk: HIGH

Reasons:
✓ Invoice amount mismatch
✓ Quantity discrepancy
✓ Receiving delay > 10 days
```

### 10. Interactive Dashboard

The final analytics dashboard can provide:

* Total invoices
* Risky invoices
* Normal invoices
* Risk percentage
* Vendor-wise risk
* Invoice mismatch trends
* Receiving delay analysis
* High-risk invoice details
* Filters for date, vendor, and risk level

---

## 🛠️ Technology Stack

### Programming Language

* **Python**

### Data Processing

* **Pandas**
* **NumPy**

### Data Visualization

* **Matplotlib**
* **Seaborn**

### Machine Learning

* **Scikit-learn**

### Dashboard / Application

* **Power BI**
* **Streamlit** *(if used in the final implementation)*

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## 📊 Important Features Used

Some of the important engineered features include:

```text
invoice_quantity
invoice_dollars
total_item_quantity
total_item_dollars
total_brands
day_po_to_invoice
avg_receiving_delay
```

Additional features can be added depending on the available procurement data.

---

## 🤖 Machine Learning Pipeline

```text
Raw Data
   ↓
Data Cleaning
   ↓
Data Integration
   ↓
Feature Engineering
   ↓
Risk Label Creation
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation
   ↓
Invoice Risk Classification
```

---

## 📈 Model Evaluation

The classification models are evaluated using a classification report.

Example:

```text
              precision    recall    f1-score    support

Low Risk        0.XX       0.XX       0.XX        XXX
High Risk       0.XX       0.XX       0.XX        XXX

accuracy                              0.XX        XXX
macro avg       0.XX       0.XX       0.XX        XXX
weighted avg    0.XX       0.XX       0.XX        XXX
```

> The actual values depend on the final dataset and trained model.

---

## 📁 Project Structure

```text
Intelligent-Procurement-Invoice-Analytics/
│
├── data/
│   ├── invoices.csv
│   ├── purchase_orders.csv
│   ├── receiving.csv
│   └── item_details.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── eda.ipynb
│   ├── feature_engineering.ipynb
│   └── model_training.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── risk_detection.py
│   └── model.py
│
├── dashboard/
│   └── app.py
│
├── models/
│   └── invoice_risk_model.pkl
│
├── reports/
│   └── model_results/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/intelligent-procurement-invoice-analytics.git
```

Navigate to the project directory:

```bash
cd intelligent-procurement-invoice-analytics
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

### Windows

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

If the project uses Streamlit:

```bash
streamlit run dashboard/app.py
```

For Jupyter Notebook:

```bash
jupyter notebook
```

Then open the notebooks inside the `notebooks/` directory.

---

## 💡 Example Use Case

Consider a vendor invoice containing:

```text
Invoice Quantity       = 120
PO Quantity            = 100

Invoice Amount         = ₹60,000
Expected Amount        = ₹50,000

Receiving Delay        = 15 days
```

The system identifies:

```text
Quantity Mismatch       → YES
Amount Mismatch         → YES
Abnormal Delay          → YES
```

The invoice can therefore be classified as:

```text
HIGH RISK
```

The system can then flag the invoice for manual verification.

---

## 🌟 Benefits

The proposed system can help organizations:

* Reduce manual invoice verification effort.
* Detect invoice discrepancies automatically.
* Identify potentially risky invoices.
* Improve procurement visibility.
* Monitor vendor performance.
* Reduce financial errors.
* Prioritize invoices for manual review.
* Support data-driven procurement decisions.

---

## 🔮 Future Scope

The project can be further enhanced with:

* OCR-based invoice data extraction.
* Real-time invoice processing.
* Automated email alerts for high-risk invoices.
* Explainable AI using SHAP/LIME.
* Deep learning-based anomaly detection.
* Fraud detection using unsupervised learning.
* Integration with ERP systems.
* Automated three-way matching.
* Natural language querying of procurement data.
* Role-based access control.
* Cloud deployment.
* Real-time monitoring dashboards.

---

## 👨‍💻 Project Team

**Project:** Intelligent Procurement Invoice Analytics

**Domain:** Data Science | Machine Learning | Procurement Analytics

**Technologies:** Python, Pandas, NumPy, Scikit-learn, Power BI, Streamlit

---

## 📜 License

This project is developed for educational and academic purposes.
