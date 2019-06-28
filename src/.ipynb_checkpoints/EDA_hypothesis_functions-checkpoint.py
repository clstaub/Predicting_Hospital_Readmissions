import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
import researchpy as rp
from scipy import stats



#iterate through column names and check percentage of data missing/col
#if >= 5% of data missing, list below. 
def missing_data(df,percent):
    '''
    Description: Checks all columns of a df and returns percent of 
    missing data if it is above the defined threshold 'percent' 
    
    Input: df = Pandas DataFrame 
           percent threshold = integer
    Output: String of all columns missing more than the defined 
            threshold % of data. 
    '''
    stringlist = []
    for idx,col in enumerate(df.columns):
        if ((len(df) - df.count()[idx])/len(df) * 100) >= percent:
            stringlist.append(str(("Column '"+str(col)+"' is missing {:2.2f}% of data"
               .format((len(df) - df.count()[idx])/len(df) * 100))))
    return stringlist



# createa a data frame of int features.. 
def get_num_cols(df):
    '''
    Description: Takes a dataframe as it's input and returns a Pandas
    DataFrame of all columns that contain data of type 'int'
    of all continuous/numeric columns
    Input: Pandas DF
    Output: DF of numeric cols
    '''
    intlist=[]
    for col in df.columns:
        for val in df[col]:
            if type(val) == int:
                intlist.append(col)
                break
    return pd.DataFrame(df[intlist])



def get_cat_cols(df):
    '''
    Description: Takes a dataframe as it's input and returns a Pandas
    DataFrame of all columns that contain data of type 'str'
    of all continuous/numeric columns
    Input: Pandas DF
    Output: DF of categorical features
    '''
    intlist=[]
    for col in df.columns:
        for val in df[col]:
            if type(val) == str:
                intlist.append(col)
                break
    return pd.DataFrame(df[intlist])



def chisq(df,cols):
    '''
    Description: Performs Chi-Square test on the categorical columns vs target variable return Chi-squared test score, p-value, and degrees of freedom
    Input: Pandas Dataframe, list of categorical columns
    Output: Column_name, Chi_sq test score, p-value, degrees of freedom'''
    results = []
    for col in cols:
        crosstab = pd.crosstab(df[col],df['readmitted_<30d'])
        result = stats.chi2_contingency(crosstab)
        results.append(col, result[0], result[1], result[2])
    return results
