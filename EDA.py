import pandas as pd 
import numpy as np
from pandas.core.tools import numeric
import seaborn as sns

df = pd.read_csv('loan_payments.csv') 

categories = ['grade', 'term','sub_grade', 'home_ownership', 'verification_status', 'loan_status', 'purpose', 'application_type', 'employment_length']
dates = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']
excess_dp = ['funded_amount_inv', 'collection_recovery_fee']
floats = ['funded_amount', 'mths_since_last_delinq', 'mths_since_last_record', 'collections_12_mths_ex_med', 'mths_since_last_major_derog']


class DataTransform: 
    """The DataTransform class provides methods to transform different types of data in a pandas DataFrame,
    such as converting object columns to boolean, category, date, or integer types, rounding float
    values, and converting a specific column to integer by removing the "months" string.
    """
    def  __init__(self, df):
        """
        The function initialises the class with a dataframe as an attribute.
        
        :param df: The parameter "df" is a variable that represents a pandas DataFrame object. It is
        used to store and manipulate tabular data in a structured format
        """
        self.df = df 

    
    def object_to_category(self, categories):
        """
        The function converts the specified columns in a DataFrame to categorical data type.
        
        :param categories: The "categories" parameter is a list of column names in a dataframe. Each
        column contains text values that you want to convert to categorical data type
        """
        #Finite list of text values
        for col in categories:
            self.df[col] = self.df[col].astype('category')
    
    def object_to_date(self, dates):
        """
        The function converts date and time values in a specified column of a dataframe to a datetime
        format.
        
        :param dates: The "dates" parameter is a list of column names in a pandas DataFrame. These
        columns contain date and time values in the format "Dec 2018"
        """
        #Date and time values e.g Dec 2018
        for col in dates:
            self.df[col] = pd.to_datetime(self.df[col], format="%b-%Y") 
    
    def round_floats(self,excess_dp):
        """
        The function `round_floats` rounds the values in the specified columns of a DataFrame to 2
        decimal places.
        
        :param excess_dp: The parameter "excess_dp" is a list of column names in a DataFrame. These
        columns contain floating-point numbers that may have more than 2 decimal places. The purpose of
        the function is to round these numbers to 2 decimal places, as they represent monetary values
        """
        #entries should be to 2 decimal places as represent monetary values 
        for col in excess_dp:
            self.df[col] = self.df[col].round(2)
    
    def flaot_to_int(self, floats):
        """
        The function converts float numbers in a pandas DataFrame to integer numbers.
        
        :param floats: The "floats" parameter is a list of column names in a pandas DataFrame that
        contain floating-point numbers. The function converts these columns to integer data type by
        using the "astype" method with the 'int64' argument
        """
        #Integer numbers
        for col in floats:
            self.df[col] = self.df[col].astype('int64', errors="ignore")


    def object_to_bool(self, col):
        """
        The function converts a column in a dataframe to boolean values based on the presence of two
        unique values, "n" or "y".
        
        :param col: The "col" parameter is the name of the column in the dataframe that you want to
        convert to boolean values
        """
        #Boolean values (True/False) as column has 2 unique values n or y
        self.df[col] = self.df[col].astype("bool")


if __name__ == '__main__': 
    transform = DataTransform(df)
    transform.object_to_category(categories)
    transform.object_to_date(dates)
    transform.round_floats(excess_dp)
    transform.flaot_to_int(floats)
    transform.object_to_bool('payment_plan')
   

#funded_amount                   5.544799
#term                            8.799395 int/object mmode
#int_rate                        9.531449 float mean
#employment_length               3.905515 category mode
#mths_since_last_delinq         57.166565 float mean
#mths_since_last_record         88.602460 floa mean 
#last_payment_date               0.134609 date mode
#next_payment_date              60.127971 date mode
#last_credit_pull_date           0.012908 date mode
#collections_12_mths_ex_med      0.094042 float mean
#mths_since_last_major_derog    86.172116 float
#mode = ['last_credit_pull_date', 'next_payment_date', 'last_payment_date', 'employment_length','term']
#mean = ['collections_12_mths_ex_med', 'mths_since_last_record','mths_since_last_delinq', 'int_rate', 'funded_amount']
   #Cols_to_ drop = 
#mths_since_last_major_derog    86.172116
#mths_since_last_record         88.602460
#member_id
#id_

#Median-It is preferred if data is numeric and skewed.
#Mean-It is preferred if data is numeric and not skewed.
#Mode-It is preferred if the data is a string(object) or numeric.
   


#def find_skewed_cols():
#        num_col = df.select_dtypes(include='number').columns.tolist()        
#        list_of_skew = df[num_col].skew()
#        skew_cols = [col for col in list_of_skew if col <-1 or col >1]
#        print(skew_cols)
#find_skewed_cols()
print(df.info())