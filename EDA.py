import pandas as pd 


df = pd.read_csv('loan_payments.csv') 

class DataTransform: 
    """
    The DataTransform class provides methods to transform different types of data in a pandas DataFrame,
    such as converting object columns to boolean, category, date, or integer types, rounding float
    values, and converting a specific column to integer by removing the "months" string.

    Paramaters: 
    df: The dataframe coverted to pandas fromat from csv
    categories: list of columns to change to category data type
    dates: list if columns to change to datetime64 data type
    excess_dp: Columns to round up becuase they have more than 2 decimal places
    floats: list of columns to change to float data type 
    col: Column to change ot boolean 

    Atributes: 
    self.df: This is the pandas dataframe

    Methods:
    __init__(): Initialises the class
    object_to_category(): Changes column to category data type
    object_to_date(): Changes column to datetime64 data type
    round_floats(): Rounds float columns to 2 decimal places
    flaot_to_int(): Changes float column to int data type
    object_to_bool: Changes column to boolean data type
    term_to_int(): Changes term to int data type and removes 'months'

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
    
    def float_to_int(self, floats):
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
    
    @staticmethod
    def term_to_int():
        df['term'] = df['term'].str.replace('months', '')
        df['term'] = df['term'].astype(int)
        


if __name__ == '__main__': 


    categories = ['grade','sub_grade', 'home_ownership', 'verification_status', 'loan_status', 'purpose', 'application_type', 'employment_length']
    dates = ['issue_date', 'earliest_credit_line', 'last_payment_date', 'next_payment_date', 'last_credit_pull_date']
    excess_dp = ['funded_amount_inv', 'collection_recovery_fee']
    floats = ['funded_amount', 'mths_since_last_delinq', 'mths_since_last_record', 'collections_12_mths_ex_med', 'mths_since_last_major_derog']

    transform = DataTransform(df)
    transform.object_to_category(categories)
    transform.object_to_date(dates)
    transform.round_floats(excess_dp)
    transform.float_to_int(floats)
    transform.object_to_bool('payment_plan')
    
print(df.info())

df.to_csv('transformed_loan_payments.csv')