# **Travel and Luggage Preferences Analysis Project**

This repository houses the scripts and datasets used for the analysis of travel and luggage preferences among a diverse demographic population. The project includes data cleaning, exploratory data analysis (EDA), and visualization to understand trends and insights from the collected survey data.

## **Project Overview**

This project aims to provide insights into travel habits, luggage preferences, and enhancements desired by travelers. The analysis focuses on various aspects such as age, nationality, current residence, travel frequency, and attitudes towards smart luggage and other travel enhancements.
Getting Started
Prerequisites

To run the scripts, you will need Python along with several libraries installed on your machine. Ensure you have the following:

    Python 3.x
    pandas
    numpy
    matplotlib

Use the following command to install the necessary libraries using pip:

  pip install pandas numpy matplotlib


## **Usage**

Navigate to the scripts/ directory and run the Python script to start the analysis:

  python data_analysis.py


## **Files and Directories**

    data/Blank Quiz.csv: Raw survey data collected from participants.
    data/demographics.csv: Additional demographic data for correlating with survey responses.
    scripts/data_analysis.py: Main script that performs data cleaning, EDA, visualization, and outputs processed data.

## **Data Cleaning and Analysis**

Data cleaning steps include:
- Removing unnecessary columns like timestamps.
- Renormalizing text entries to correct for typos and inconsistencies in nationality and current residence fields.
- Recategorizing data into more meaningful groups for analysis.

The exploratory data analysis includes:
- Distribution of age, nationality, and current residence.
- Analysis of travel frequency and preferences regarding luggage types.
- Exploration of attitudes towards smart luggage and potential enhancements that travelers find appealing.

## **Visualization**

This project utilizes matplotlib for generating various charts and graphs to visualize:
- Pie charts for distribution analysis.
- Bar graphs to show preferences and frequency counts.
- Scatter plots for correlations between different variables.
