# Cosmic-Classifer
# **Exoplanet Confirmation Prediction: This app predicts whether an exoplanet is confirmed, a candidate, or a false positive based on the features provided.")
**

## **Introduction**

The discovery of exoplanets—planets that orbit stars outside our solar system—has captivated astronomers and space enthusiasts alike. With thousands of candidates identified by the Kepler Space Telescope, confirming whether these celestial bodies are indeed exoplanets or false positives is a critical task. This repository contains two machine-learning-powered applications designed to classify exoplanets based on data from NASA's Exoplanet Archive.

These applications leverage machine learning techniques to predict whether an exoplanet is **Confirmed**, a **Candidate**, or a **False Positive**, providing valuable insights to researchers, students, and data scientists alike. Both applications feature a user-friendly interface built with Streamlit, offering a seamless experience for data input and real-time predictions.

## **Problem Statement**

Astronomical datasets, such as those from the Kepler mission, contain numerous observations of potential exoplanets. However, not all these observations are actual planets; some are false positives due to noise or other astrophysical phenomena. The challenge lies in distinguishing real exoplanets from false positives. This classification is critical in advancing our understanding of planetary systems beyond our solar system.

The primary **problem** this project addresses is simplifying the exoplanet classification process. By providing a machine learning-based application, we make it easier to predict the status of a potential exoplanet with high accuracy.

## **Purpose**

The **purpose** of this application is twofold:
1. To provide an accessible tool for classifying exoplanets using machine learning techniques.
2. To demonstrate how machine learning models can be applied to astronomical data, enabling faster and more accurate exoplanet detection.

This application is targeted at researchers in astronomy, data scientists exploring space data, and students/enthusiasts who want to experiment with machine learning and astronomy. The project aims to bridge the gap between complex astronomical datasets and easily understandable predictions.

## **Technical Overview**

### **Application 1: Random Forest Classifier**

- **Model**: The first application uses a **Random Forest Classifier** trained on NASA's exoplanet dataset. Random forests combine multiple decision trees to enhance classification accuracy by reducing overfitting.
- **Front-End**: The app is built using Streamlit, allowing users to input key exoplanet features and instantly receive predictions.

**Key Features:**
- Predicts whether an exoplanet is **Confirmed**, a **Candidate**, or a **False Positive**.
- Displays a confidence score alongside the prediction.
- Reset functionality to clear inputs.
  
### **Application 2: Stacked Ensemble Model**

- **Model**: The second app uses a **custom-built ensemble model** that stacks predictions from multiple classifiers—**Logistic Regression**, **SVM**, and **Random Forests**—using a meta-model for final predictions.
- **Front-End**: Similar to the first app, the interface is built using Streamlit for easy interaction and real-time predictions.

**Key Features:**
- Stacking ensemble model for improved classification accuracy.
- Predicts exoplanet classification with enhanced precision by combining multiple machine learning models.
- Confidence scores indicate the certainty of the classification.

## **Dataset**

Both applications are trained on data from NASA's **Kepler Space Telescope** available through the [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/). The dataset includes features such as the orbital period, planet radius, stellar properties, and signal-to-noise ratios, which are critical for making predictions.

### **Input Features Include:**
- **Orbital Period**: Time taken for the planet to complete one orbit.
- **Transit Depth**: Depth of the transit in parts per million.
- **Impact Parameter**: Measure of how central the planet's transit is across its star.
- **Planet Radius**: Radius of the planet relative to Earth.
- **Stellar Properties**: Effective temperature, surface gravity, and stellar radius.

## **Installation and Setup**

To run the applications locally, follow these steps:

### **1. Clone the repository:**
```bash
git clone https://github.com/yourusername/exoplanet-classification.git
```

### **2. Navigate to the project directory:**
```bash
cd exoplanet-classification
```

### **3. Install the required Python packages:**
```bash
pip install -r requirements.txt
```

### **4. Run the Streamlit app:**
```bash
streamlit run app.py
```

## **Technology Stack**

- **Streamlit**: Provides an interactive front-end for input and output.
- **scikit-learn**: Used for building and training machine learning models.
- **Python**: Main programming language.
- **XGBoost**: Integrated in ensemble models for robust performance.
  
## **Usage**

1. Open the app in your browser after running the `streamlit` command.
2. Input exoplanet features such as orbital period, planet radius, and stellar properties.
3. Click the "Predict" button to classify the exoplanet.
4. View the result (Confirmed, Candidate, or False Positive) along with a confidence score.
5. Use the "Reset" button to clear inputs and start over.

## **Who Is This For?**

- **Astronomy Researchers**: The app can be used to assist in validating potential exoplanets based on real data.
- **Data Scientists**: The app showcases how machine learning can be applied to space-related datasets, serving as a practical example for exploration.
- **Students and Enthusiasts**: Anyone interested in astronomy and machine learning can use this tool to learn more about the classification of exoplanets and machine learning models.

## **Future Work**

- **Model Optimization**: Further improve prediction accuracy by incorporating more advanced models or tuning existing models.
- **Visualization**: Add data visualizations to represent the dataset features more effectively.
- **Deployment**: Deploy the apps on cloud platforms like Heroku or AWS for public access.

