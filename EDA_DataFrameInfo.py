from sklearn.impute import SimpleImputer
import pandas as pd 
import numpy as np
import seaborn as sns
import missingno as msno
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

df = pd.read_csv('transformed_loan_payments.csv') 

class DataFrameInfo:
    """
    The DataFrameInfo class provides methods to retrieve information about a DataFrame, such as data
    types, summary statistics, distinct values for categorical columns, shape of the DataFrame, and
    count of null values.

    Paramaters: 
    df: the dataframe coverted to pandas fromat from csv

    Atributes: 
    self.df: This is the pandas dataframe

    Methods:
    __init__(): Initialises the class
    
    df_shape(): Gives the shape of the dataframe rows/columns
      
    df_information(): Gives us information about the dataframe, data types etc

    Extract_stats(): Gives the mean, median and standard deviation of the dataset 
   
    distinct_values_categories(): Finds the unique values in each columns 

    null_count(): Finds the amount of null values in the dataframe


    """ 
    def __init__(self, df):
        """
        The function initializes an object with a dataframe as an attribute.
        
        :param df: The parameter "df" is a variable that represents a pandas DataFrame object. It is
        used to store and manipulate tabular data in a structured format
        """
        self.df = df

    @staticmethod
    def df_shape():
        """
        The function "df_shape" prints the shape of a DataFrame and returns the shape as a tuple.
        :return: The shape of the DataFrame.
        """
        print('The shape of the DataFrame: ')
        return df.shape 

    @staticmethod   
    def df_information():
        """
        The function "df_information" prints information about the data types of a DataFrame.
        :return: The `df.info()` method returns information about the DataFrame, including the number of
        non-null values, data types of each column, and memory usage.
        """
        #check data types changed from DataTransform 
        print("Information about data types")
        return df.info()
    
    @staticmethod
    def Extract_stats():
        """
        The function "Extract_stats" prints the description of a dataframe, including the median,
        standard deviation, and mean.
        """
       
        print('Description of the dataframe:')
        describe = df.describe()
        print(f'The median is: {describe.loc["50%"]}')
        print(f'The standard deviation is: {describe.loc["std"]}')
        print(f'The mean is: {describe.loc["mean"]}')
    
    @staticmethod
    def distinct_values_categories():
        """
        The function `distinct_values_cat` returns the number of distinct values for each categorical
        column in a DataFrame.
        :return: the number of distinct values for each category column in the DataFrame.
        """
        categories = df.select_dtypes(include="category").columns
        distinct_values = {col: df[col].unique() for col in categories}
        return distinct_values
    
    
    @staticmethod
    def null_count():
        """
        The function calculates the total number and percentage of null values in a DataFrame.
        """
        total_nulls = df.isnull().sum()
        percentage_of_nulls = total_nulls * 100 / len(df)
        print(f'Total of null values is {total_nulls}')
        print(f'Percentage of nulls is {percentage_of_nulls}') 

class plotter: 
    """
    The `plotter` class provides methods for creating various plots for the loan
    payments data.

    Paramaters: 
    df: the dataframe coverted to pandas fromat from csv
    table: the dataset
    coloumn_1: variable for grapth
    column_2: variable for graph
    data: dataframe for graph
    num_col: numeric columns in the dataframe


    Atributes: 
    self.df: This is the pandas dataframe

    Methods:
    __init__(): Initialises the class
     
    msno_matrix(): Plots a missingno matrix to highlight the missing values in the dataset 

    scatter_plot(): Plots a scatter plot
     
    histogram(): Plots a histogram 
    
    box_plot(): Plots a boxplot 
   
    pair_plot(): Plots a pair plot for the dataframe 
      
    heat_map(): Plots a heatmap to highlight the correlated values 
    
    """
    def __init__(self, df):
        """
        The function initializes an object with a dataframe attribute.
        """
        self.df = df
    
    @staticmethod
    def msno_matrix():
        """
        The function `msno_matrix` creates a matrix plot to visualize missing values in a dataframe.
        """
        plt.figure(figsize=(10,5))
        msno.matrix(df)
        gray_patch = mpatches.Patch(color='gray', label='Data present')
        white_patch = mpatches.Patch(color='white', label='Data absent ')
        plt.xticks(rotation=45)
        plt.title("Loan Payments Missingno Matrix")
        plt.legend(handles=[gray_patch, white_patch])
        plt.show()
    
    def scatter_plot(self, data, column_1, column_2):
        """
        The scatter_plot function creates a scatter plot of two columns from a table, with points
        colored and sized based on loan status and loan amount respectively.
        
        """
        plt.figure(figsize=(10,5))
        sns.scatterplot(x= column_1, y= column_2, data=data, hue="loan_status", size="loan_amount")
        plt.xticks(rotation=45)
        plt.title("Loan Payments Scatter Plot")
        plt.show()

    def histogram(Self, data, column_1):
        """
        The function `histogram` creates a histogram plot of a specified column in a given table.
        
        """
        plt.figure(figsize=(10,5))
        sns.histplot(data=data, x=column_1, kde=True)
        plt.xticks(rotation=45)
        plt.title("Loan Payments Histogram")
        plt.show()
    

    def box_plot(self, column_1, column_2):
        """
        The function `box_plot` creates a box plot of loan payments using the `sns.boxplot` function
        from the seaborn library.
        """
        plt.figure(figsize=(15,10))
        sns.boxplot(x= column_1 , y= column_2, data=self.df)
        plt.xticks(rotation=45)
        plt.title("Loan Payments Box Plot")
        plt.show()


    @staticmethod
    def pair_plot():
        """
        The function `pair_plot` generates a pair plot of numerical columns in a dataframe, with
        different colors representing different grades.
        """
        plt.figure(figsize=(5,5))
        sns.pairplot(df.select_dtypes(['number']), hue="loan_amount")
        plt.title("Loan Payments Box Plot")
        plt.show()
    
  
    def heat_map(self, num_col):
        """
        The function `heat_map` generates a correlation heat map for the loan payments data.
        """
        plt.figure(figsize=(15,10))
        sns.heatmap(df[num_col].corr(), annot=True, cmap="coolwarm")
        plt.title("Loan Payments Correlation Heat Map")
        plt.show()



class DataFrameTransform:
    """
    The `DataFrameTransform` class provides methods for finding null values, dropping columns, imputing
    null values with mode or mean, finding skewed columns, performing log transformation, and removing
    outliers in a pandas DataFrame.

    The `plotter` class provides methods for creating various plots for the loan
    payments data.

    Paramaters: 
    df: the dataframe coverted to pandas fromat from csv
    median_impute: List of columns to be imputed with the median 
    mode_impute: List of columns to be imputed with the mode
    cols_for_drop: List of columns to drop
    num_col: numeric columns in the dataframe
    skewed_cols: skewed columns in the dataframe 

    Atributes: 
    self.df: This is the pandas dataframe

    Methods:
    __init__(): Initialises the class
     
    find_nulls():nFinds the null values 
  
    columns_to_drop(): Drops the columns from the dataframe
  
    impute_nulls_with_mode(): Imputes mssing values with the mode

    impute_nulls_with_median(): Imputes missing values with the median
     
    find_skewed_cols(): Finds the skewed columns greater or less than 1 or -1 

    log_transformation(): Performs a log transformation on skewed columns 

    remove_outliers(): Removes outliers greater than or less than Q1/Q3 -/+ (1.5 * IQR)
    

    """
    def __init__(self, df):
        """
        The function initializes an object with a dataframe as an attribute.
        
        :param df: The parameter "df" is a variable that represents a pandas DataFrame object. It is
        used to store and manipulate tabular data in a structured format
        """
        self.df = df

    
    @staticmethod
    def find_nulls():
        """
        The function "find_nulls" returns the number of null values in each column of a dataframe.
        :return: the number of null values in each column of the dataframe.
        """
        nulls_in_each_col = df.isnull().sum()
        return nulls_in_each_col
    

    def columns_to_drop(self, cols_for_drop):
        """
        The function drops specified columns from a DataFrame and returns the name of the column that
        was dropped.
        """
        
      
        self.df = self.df.drop([cols_for_drop], axis=1)
            

    def impute_nulls_with_mode(self, mode_impute):
        """
        The function imputes null values in a specified column of a dataframe using the mode value.
      
        """
        mode_imputer = SimpleImputer(strategy="most_frequent")
        self.df[mode_impute] =mode_imputer.fit_transform(self.df[mode_impute])

           
    def impute_nulls_with_median(self,  median_impute):
        """
        The function imputes null values in a specified column with the mean value.
        
    
        """
        
        median_imputer = SimpleImputer(strategy="median")
        self.df[median_impute] = median_imputer.fit_transform(self.df[median_impute])
            

    def find_skewed_cols(self, num_col):
        """
        The function "find_skewed_cols" identifies columns in a DataFrame that have a skewness value
        greater than 1 or less than -1.
        """
        list_of_skew = self.df[num_col].skew()
        skew_cols = [col for col in list_of_skew if col <-1 or col >1]
        return skew_cols

    def log_transformation(self, skewed_cols):
        for col in skewed_cols: 
            self.df[col].map(lambda i: np.log(i) if i > 0 else 0)


    def remove_outliers(self, num_col):
        """
        The function removes outliers from numerical columns in a DataFrame using the interquartile
        range method.
        """
        Q1 = self.df[num_col].quantile(0.25)
        Q3 = self.df[num_col].quantile(0.75)
        IQR = Q3 - Q1
        threshold = 1.5
        outliers = self.df[(self.df[num_col] < Q1 - threshold * IQR) | (self.df[num_col] > Q3 + threshold * IQR)]
        self.df = self.df.drop(outliers.index)
        


if __name__ == '__main__':
    information = DataFrameInfo(df)
    plot = plotter(df)
    transform = DataFrameTransform(df)

    mode_impute = ['last_credit_pull_date', 'next_payment_date', 'last_payment_date', 'employment_length','term']
    
    median_impute = ['collections_12_mths_ex_med','mths_since_last_delinq', 'int_rate', 'funded_amount']
    
    skewed_cols = ['annual_inc', 'delinq_2yrs', 'inq_last_6mths','open_accounts',\
                                         'out_prncp','out_prncp_inv','total_payment','total_payment_inv',\
                                            'total_rec_prncp','total_rec_int','total_rec_late_fee','recoveries',\
                                                'collection_recovery_fee','last_payment_amount','collections_12_mths_ex_med']
    
    cols_for_drop = ['mths_since_last_record', 'mths_since_last_major_derog']

    num_col = df.select_dtypes(include='number').columns.tolist()   
    
    information.df_shape()
    information.df_information()
    information.Extract_stats()
    information.distinct_values_categories()
    information.null_count() 

    plot.msno_matrix()
    plot.scatter_plot(df, 'total_payment_inv', 'last_payment_amount')
    plot.histogram(df, 'total_payment')
    plot.box_plot('instalment','int_rate')
    plot.pair_plot()
    plot.heat_map(num_col)

    transform.find_nulls()
    transform.columns_to_drop(cols_for_drop)
    transform.impute_nulls_with_mode(mode_impute)
    transform.impute_nulls_with_median(median_impute)
    transform.find_skewed_cols(num_col)
    transform.log_transformation(skewed_cols)
    transform.remove_outliers(num_col)

df.to_csv('EDA_Frameinfo_loan_payments.csv')