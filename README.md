# Local Food Wastage Management System

A data-driven project focused on reducing food waste by analyzing surplus food availability, connecting food providers with potential receivers, and improving food redistribution through Python and SQL.

## Project Overview

Food wastage is a major challenge, while many individuals and communities face food insecurity. Restaurants, grocery stores, and other food providers often have surplus food that could be redistributed instead of being discarded.

The **Local Food Wastage Management System** aims to address this problem by organizing food donation records, managing provider and receiver information, tracking food claims, and analyzing distribution patterns.

The project uses Python for data cleaning and processing and SQL for database management and analytical queries. Streamlit is part of the proposed interactive application interface.

## 🎯 Project Objectives

- Organize food provider, receiver, food listing, and claim records.
- Clean and prepare datasets for reliable analysis.
- Analyze food availability across different cities and provider categories.
- Track food claims and their completion status.
- Identify food distribution patterns and provider contributions.
- Generate insights that can support better food redistribution decisions.
- Promote efficient use of surplus food and reduce avoidable wastage.

## 🛠️ Technologies Used

- **Python:** Data cleaning, processing, and analysis.
- **Pandas:** Dataset manipulation and preparation.
- **SQL:** Database management, joins, aggregations, and analytical queries.
- **Streamlit:** Intended interactive interface for exploring food records and analysis.

## 📂 Dataset Description

The project uses four main datasets:

| Dataset | Description |
|---|---|
| Providers | Provider IDs, names, types, addresses, cities, and contact details. |
| Receivers | Receiver IDs, names, organization types, cities, and contact details. |
| Food Listings | Food names, quantities, expiry dates, provider details, locations, food types, and meal types. |
| Claims | Claim IDs, food IDs, receiver IDs, claim statuses, and timestamps. |

These datasets form the foundation for studying food availability, provider contributions, and food distribution activity.

## 🔍 Data Analysis and SQL Questions

The analysis focuses on the following areas:

### 1. Providers and Receivers
- Count food providers and receivers by city.
- Identify provider categories contributing the most food.
- Retrieve provider contact information for a selected city.
- Identify receivers with the highest number of claims.

### 2. Food Availability
- Calculate the total quantity of available food.
- Identify cities with the highest number of food listings.
- Analyze the most frequently available food types.
- Compare food availability across providers and locations.

### 3. Claims and Distribution
- Count claims associated with individual food items.
- Identify providers associated with the highest number of successful claims.
- Analyze completed, pending, and cancelled claims.
- Compare claim activity across receivers and meal categories.

### 4. Insights and Trends
- Examine average quantities claimed per receiver.
- Identify the most frequently claimed meal types.
- Calculate food contributions by provider.
- Explore patterns that may help improve food redistribution.

## ⚙️ Project Workflow

1. **Data Preparation:** Load the available datasets and inspect their structure and consistency.
2. **Data Cleaning:** Use Python scripts to prepare the data for analysis.
3. **Database Management:** Organize relevant records for SQL-based querying.
4. **SQL Analysis:** Use analytical queries to investigate food availability, providers, receivers, and claims.
5. **Visualization and Interface:** Use Streamlit as the planned interface for presenting results and interacting with records.

## 💡 Potential Applications

- Helping food providers identify available donation opportunities.
- Supporting NGOs and receivers in finding surplus food.
- Understanding differences in food availability across locations.
- Monitoring food claim activity and distribution trends.
- Supporting decisions aimed at reducing food waste.

## 📁 Repository Structure

```text
food-waste-management-analysis/
│
├── README.md
├── Data_cleaning.py
├── db.py
├── query.py
├── data/
│   ├── providers_data.csv
│   ├── receivers_data.csv
│   ├── food_listings_data.csv
│   ├── claims_data.csv
│   
├── sql/
├── images/

```


## Project Domain

Food Management | Data Analysis | Waste Reduction | Social Good

## Author

**Aditya Raj**
A license can be added to specify how others may use, modify, and distribute this project.

