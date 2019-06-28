# Predicting_Hospital_Readmissions
### Claudio Staub


## Introduction
With estimated costs in the order of tens of billions per annum, hospital readmissions impose a significant financial burden on health care institutions across the nation. Up until more recent times, there was not a lot of incentive for Hospitals to reduce these readmissions. When Center for Medicares and Medicaid Services began public reporting hospital readmission rates, the ethical and professional incentive was there, but hospitals that aimed to reduce readmissions were losing revenue unless they could fill their beds. Enter the Hospital Readmissions Reduction Program (HRRP) circa 2013 which provided financial incentive for Hospitals to reduce readmissions. 

This has still proven to be a difficult task but hospitals are employing a number of strategies to reduce the preventable readmissions. Progress has been made since the implementation of the HRRP but estimates of readmissions that could have been prevented are still as high as 70%. It is therefore in their best interest to find ways to further reduce this undesirable outcome. 


## Strategy

- Data Preprocessing
- Exploratory Data Analysis
- Hypothesis Testing


## Data Overview

The data set was made available by the UCI Machine Learning Repository and can be found [here](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008).

- It contains 101766 observations with 50 different features. 
- Features are largely categorical variables

#### Main feature categories:
- Basic demographics: Encounter ID, Patient #, Race, Gender, Age, Weight
- Medical Hx: Medications, # of Procedures, # Medications, ************ to be continued


## Data Preprocessing

The metric of interest that labels whether a patient was readmitted or not has three possible values: 

- **<30** : Patients that were readmitted in less than thirty days. 
- **>30** : Paitents that were readmitted in greater than thirty days. 
- **NO** : Patients that were not readmitted

The metric of concern according to the HRRP is patients that were readmitted in less than thirty days. Therefore we will rename the column to 'readmitted_<30d' and combine the '>30' and 'NO'.

Below is the proportion of patients in the dataset that were readmitted. 

<img src="img/target.png">

## Exploratory Data Analysis
It is worth exploring if any of the numeric variables have any correlations. We will write a function to exract numeric columns from a data frame of choice and return a numeric data frame. This will be performed for both the 

<img src='img/pair_plot.png'>

Extraction of numeric columns and plotting in a pairplot did not yield any strong correlations. 

The columns with integer values did not provide a lot of insight. These int columns are largely nominal and interval variables which explains their lack of fruitful information in the pairplots generated above. A good next step would be to evaluate all the values that each feature contains. If the feature contains a large amount of values (i.e. Patient ID, encounter ID) we will just take a count of the unique values in the column.



## Hypothesis Testing


Since the columns in this dataset are largely categorical variables, we want to test some of these for indepence. 

As there are various mechanisms of action by which diabetes medication can treat the disease, there are many medications on the market. This can be seen by the 23 various diabetes medications that are included in this data set. Finding the optimal medication for each patient can often be an exercise of trial and error. Adverse side-effects secondary to a medication change often result in hospitalization as patients need to be monitored with serial blood glucose tests. 

I'd like to test the change in medication column and the readmission column for independence. Since these both only contain two possible values, this would be a fairly straight forward X^2 test

#### State Null and Alternative Hypothesis

>$H_0$:Change in Medicine and Readmission are independent variables

>$H_A$:They are not independent

#### Assumptions

- When testing the data, the cells should be counts of cases and not percentages. It is okay to convert to percentages after testing the data
- The levels (groups) of the variables being tested are mutually exclusive
- Each participant contributes to only one cell within the Chi-square table
- The groups being tested must be independent
- The value of expected cells should be greater than 5 for at least 20% of the cells

Credit to [this](https://pythonfordatascience.org/chi-square-test-of-independence-python/) medium article

