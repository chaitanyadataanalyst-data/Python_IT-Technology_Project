# 📊 Python Pandas Technology & IT Industry Advance Project

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Only%20Library-green?logo=pandas)
![GitHub stars](https://img.shields.io/github/stars/chaitanya/pandas-project?style=social)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Project Overview
This project demonstrates  end-to-end Exploratory Data Analysis (EDA) ,  data cleaning , and  validation  using  only Pandas  on multiple datasets from a simulated Technology & IT Industry environment.  
The goal is to uncover insights, detect anomalies, and prepare clean datasets for analytics and reporting.

---

## 📂 Datasets Used
-  Customers.csv  → Customer demographics, acquisition channels, industries, signup dates  
-  Products.csv  → Product categories, types, pricing models, launch dates  
-  Subscriptions.csv  → Subscription plans, billing cycles, fees, discounts, start/end dates  
-  Transactions.csv  → Transaction types, amounts, payment methods, sales channels  
-  Support Tickets.csv  → Customer support issues, priorities, resolution times, satisfaction scores  
-  Data_Dictionary.csv  → Metadata reference for all datasets  
---
## 🔎 Exploratory Data Analysis (EDA)
- Missing values detection and imputation  
- Duplicate analysis and ID validation  
- Category distribution and inconsistency checks  
- Numeric data anomaly detection (negative values, invalid discounts)  
- Date/time validation and subscription duration analysis  
- Trend analysis (monthly subscription starts, product category distribution)  

---

## 🧹 Data Cleaning & Validation
- Standardized text columns (title case, stripped spaces)  
- Filled missing values with `"Unknown"` or median values  
- Converted dates and numeric columns to correct formats  
- Created validation flags (`Invalid_Discount_Flag`, `Invalid_Duration_Flag`)  
- Corrected subscription duration calculations  

---

## 📈 Key Insights
- Discounts >100% flagged as invalid  
- Negative transaction amounts detected  
- Negative resolution times in support tickets  
- Auto-renewal strongly correlated with active subscriptions  
- Subscription durations revealed anomalies (negative days, unusually long durations)  

---

## 🎯 Business Recommendations
1. Audit discounts to prevent >100% values  
2. Investigate negative transactions in payment logs  
3. Fix support ticket logging errors  
4. Normalize categories across datasets  
5. Monitor subscription durations for anomalies  
6. Encourage auto-renewal for higher retention  

---

