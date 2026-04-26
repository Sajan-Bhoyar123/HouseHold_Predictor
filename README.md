# FWI Prediction Flask Application

## Description
This Flask application predicts Fire Weather Index (FWI) using machine learning models.

## Files Structure
- `application.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `templates/` - HTML templates
- `models/` - Trained ML models (ridge.pkl, scaler.pkl)
- `.ebextensions/` - AWS Elastic Beanstalk configuration

## Deployment Instructions

### Local Development
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application: `python application.py`
3. Open http://localhost:5000

### AWS Elastic Beanstalk Deployment
1. Create a ZIP file of all project files
2. Upload to Elastic Beanstalk
3. The application will be automatically deployed

## Features
- FWI prediction using Ridge Regression model
- Web interface for data input
- Real-time prediction results

## Requirements
- Python 3.7+
- Flask 2.3.3
- scikit-learn 1.3.0
- pandas 2.0.3
- numpy 1.24.3
