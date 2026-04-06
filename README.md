# 🌾 AgriQual: Agricultural Compliance Assessment Tool

An AI-powered decision-support system for farmers, cooperatives, and export regulators to assess agricultural product compliance with international standards.

![AgriQual Logo](https://via.placeholder.com/800x200?text=AgriQual+Logo)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Compliance Standards](#compliance-standards)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

AgriQual is a Streamlit-based web application that uses machine learning to predict whether agricultural batches comply with Codex Alimentarius and EU food safety standards. The system helps stakeholders make informed decisions about product quality and export readiness.

### Key Benefits
- **Real-time Assessment**: Instant compliance predictions
- **AI-Powered**: Machine learning model trained on historical data
- **User-Friendly**: Intuitive web interface with mobile responsiveness
- **Standards-Based**: Checks against international food safety regulations
- **Data-Driven**: Provides insights and recommendations

## ✨ Features

### 🔍 Compliance Assessment
- Input quality parameters for agricultural batches
- Real-time ML prediction of compliance status
- Detailed reasoning for non-compliant predictions
- Threshold checking against Codex/EU standards

### 📊 Regulator Dashboard
- Historical compliance data visualization
- Interactive charts and statistics
- Compliance rate tracking
- Data insights for regulatory monitoring

### 🏠 Home Page
- Application overview and benefits
- How-to guide for users
- Visual demonstrations

### 📋 Policy & Terms
- Terms of use and service conditions
- Compliance standards reference
- Contact information

### 🔒 Data Protection
- Privacy policy and data handling practices
- Security measures explanation
- User rights and data control

## 🛠 Technology Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn (Random Forest)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Styling**: Custom CSS with responsive design
- **Model Serialization**: Joblib

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/agricqual.git
   cd agricqual
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install streamlit pandas joblib plotly scikit-learn
   ```

4. **Ensure model and data files are in place**
   - `rf_agricqual_model.joblib` (trained model)
   - `dataset/agricqual_dataset.csv` (historical data)

## 🚀 Usage

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app/app.py
   ```

2. **Access the application**
   - Open your browser to `http://localhost:8501`

### Using the App

1. **Navigate to Compliance Assessment tab**
2. **Enter batch parameters**:
   - Moisture Content (%)
   - Pesticide Residue (mg/kg)
   - Aflatoxin B1 (µg/kg)
   - Microbial Load (CFU/g)
   - Heavy Metals (mg/kg)
   - Storage Duration (Days)
   - Storage Temperature (°C)
   - Packaging Integrity

3. **Click "Assess Compliance"**
4. **Review results**:
   - Compliance prediction
   - Detailed reasons for non-compliance
   - Warnings for marginal values

### Mobile Usage
The app is fully responsive and works on mobile devices and tablets.

## 📁 Project Structure

```
AgriQual/
│
├── app/
│   └── app.py                 # Main Streamlit application
│
├── model/
│   ├── train_model.py         # Model training script
│   └── trained_model.py       # Model evaluation utilities
│
├── dataset/
│   ├── agricqual_dataset.csv  # Historical compliance data
│   ├── generate_dataset.py    # Data generation script
│   └── generate_dataset1.py   # Alternative data generation
│
├── asset/                     # Static assets (logo, favicon, etc.)
│
└── README.md                  # Project documentation
```

## 📊 Data Model

### Input Features
- `moisture_content`: Moisture percentage (0-100%)
- `pesticide_residue`: Pesticide levels in mg/kg
- `aflatoxin_b1`: Aflatoxin concentration in µg/kg
- `microbial_load`: Microbial count in CFU/g
- `heavy_metals`: Heavy metal concentration in mg/kg
- `storage_duration`: Days in storage
- `temperature`: Storage temperature in °C
- `packaging_integrity`: Categorical (Good/Fair/Poor)

### Target Variable
- `compliant`: Binary classification (0 = Non-compliant, 1 = Compliant)

## ⚖️ Compliance Standards

The system checks against the following international standards:

### Codex Alimentarius
- **Aflatoxin B1**: Maximum 5.0 µg/kg
- **Microbial Load**: Maximum 25,000 CFU/g

### EU Regulations
- **Pesticide Residue**: Maximum 0.05 mg/kg
- **Heavy Metals**: Maximum 0.1 mg/kg

### General Standards
- **Moisture Content**: Maximum 12.0%
- **Packaging Integrity**: Must be Good or Fair

## 🤝 Contributing

We welcome contributions to AgriQual! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add tests for new features
- Update documentation as needed
- Ensure mobile responsiveness

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**AgriQual Development Team**

- **Email**: agricqual.support@example.com
- **GitHub**: [https://github.com/your-username/agricqual](https://github.com/your-username/agricqual)
- **Documentation**: [Wiki](https://github.com/your-username/agricqual/wiki)

---

**Version**: 1.0  
**Last Updated**: April 2026  
**Model**: Random Forest Classifier