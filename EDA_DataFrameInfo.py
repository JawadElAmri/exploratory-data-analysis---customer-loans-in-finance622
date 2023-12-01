from sklearn.impute import SimpleImputer
from scipy import stats
import pandas as pd 
import numpy as np
import seaborn as sns
import missingno as msno
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

df = pd.read_csv('loan_payments.csv') 

class DataFrameInfo:
    """
    The DataFrameInfo class provides methods to retrieve information about a DataFrame, such as data
    types, summary statistics, distinct values for categorical columns, shape of the DataFrame, and
    count of null values.
    """ 
    def __init__(self, df):
        """
        The function initializes an object with a dataframe as an attribute.
        
        :param df: The parameter "df" is a variable that represents a pandas DataFrame object. It is
        used to store and manipulate tabular data in a structured format
        """
        self.df = df
    
    def df_shape(self):
        """
        The function "df_shape" prints the shape of a DataFrame and returns the shape as a tuple.
        :return: The shape of the DataFrame.
        """
        print('The shape of the DataFrame: ')
        return self.df.shape() 
        
    def df_information(self):
        """
        The function "df_information" prints information about the data types of a DataFrame.
        :return: The `df.info()` method returns information about the DataFrame, including the number of
        non-null values, data types of each column, and memory usage.
        """
        #check data types changed from DataTransform 
        print("Information about data types")
        return self.df.info()
    
    def Exttract_stats(self):
        """
        The function "Extract_stats" calculates and prints the median, standard deviation, and mean of a
        given dataframe, and returns the descriptive statistics of the dataframe.
        :return: The method `Exttract_stats` is returning the result of `self.df.describe()`, which is a
        summary of the statistics of the DataFrame `self.df`.
        """
        median = self.df.describe().loc[['median']]
        standard_deviation = self.df.describe().loc[['standard deviation']]
        mean = self.df.describe().loc[['mean']]
        print(f'The median is: {median}')
        print(f'The standard deviation is: {standard_deviation}')
        print(f'The mean is: {mean}')
        return self.df.describe()
    
    def distinct_values_categories(self):
        """
        The function `distinct_values_cat` returns the number of distinct values for each categorical
        column in a DataFrame.
        :return: the number of distinct values for each category column in the DataFrame.
        """
        categories = self.df.select_dtypes(include="category").columns
        distinct_value = self.df[categories].unique()
        return distinct_value
    
    def null_count(self):
        """
        The function calculates the total number and percentage of null values in a DataFrame.
        """
        total_nulls = self.df.isnull().sum()
        percentage_of_nulls = total_nulls * 100 / len(self.df)
        print(f'Total of null values is {total_nulls}')
        print(f'Percentage of nulls is {percentage_of_nulls}') 

class plotter: 
    """
    The `plotter` class provides methods for creating various plots for the loan
    payments data.
    """
    def __init__(self):
        """
        The function initializes an object with a dataframe attribute.
        """
        self.df = df
    
    def msno_matrix(self):
        """
        The function `msno_matrix` creates a matrix plot to visualize missing values in a dataframe.
        """
        plt.figure(figsize=(10,5))
        msno.matrix(self.df)
        gray_patch = mpatches.Patch(color='gray', label='Data present')
        white_patch = mpatches.Patch(color='white', label='Data absent ')
        plt.xticks(rotation=45)
        plt.title("Loan Payments Missingno Matrix")
        plt.legend(handles=[gray_patch, white_patch])
        plt.show()
    
    def scatter_plot(self, table):
        """
        The scatter_plot function creates a scatter plot of two columns from a table, with points
        colored and sized based on loan status and loan amount respectively.
        
        """
        plt.figure(figsize=(10,5))
        sns.scatterplot(x="colum_1", y="colum_2", data=table, hue="loan_status", size="loan_amount")
        plt.xticks(rotation=45)
        plt.title("Loan Payments Scatter Plot")
        plt.legend()
        plt.show()

    def histogram(Self, table, column_1):
        """
        The function `histogram` creates a histogram plot of a specified column in a given table.
        
        """
        plt.figure(figsize=(10,5))
        sns.histplot(data=table, x=column_1, kde=True)
        plt.xticks(rotation=45)
        plt.title("Loan Payments Histogram")
        plt.legend()
        plt.show()
    

    def box_plot(self):
        """
        The function `box_plot` creates a box plot of loan payments using the `sns.boxplot` function
        from the seaborn library.
        """
        plt.figure(figsize=(10,5))
        sns.boxplot(x="variable", y="value", data=pd.melt(self.df))
        plt.xticks(rotation=45)
        plt.title("Loan Payments Box Plot")
        plt.legend()
        plt.show()
    
    def pair_plot(self):
        """
        The function `pair_plot` generates a pair plot of numerical columns in a dataframe, with
        different colors representing different grades.
        """
        plt.figure(figsize=(5,5))
        sns.pairplot(self.df.select_dtypes(['number']), hue="grade")
        plt.title("Loan Payments Box Plot")
        plt.legend()
        plt.show()
    
    def heat_map(self):
        """
        The function `heat_map` generates a correlation heat map for the loan payments data.
        """
        plt.figure(figsize=(10,5))
        sns.heatmap(self.df.corr(), annot=True, cmap="coolwarm")
        plt.title("Loan Payments Correlation Heat Map")
        plt.legend()
        plt.show()



class DataFrameTransform:
    """
    The `DataFrameTransform` class provides methods for finding null values, dropping columns, imputing
    null values with mode or mean, finding skewed columns, performing log transformation, and removing
    outliers in a pandas DataFrame.
    """
    def __init__(self, df):
        """
        The function initializes an object with a dataframe as an attribute.
        
        :param df: The parameter "df" is a variable that represents a pandas DataFrame object. It is
        used to store and manipulate tabular data in a structured format
        """
        self.df = df
        
    def find_nulls(self):
        """
        The function "find_nulls" returns the number of null values in each column of a dataframe.
        :return: the number of null values in each column of the dataframe.
        """
        nulls_in_each_col = self.df.isnull().sum()
        return nulls_in_each_col
    
    def columns_to_drop(self, cols_for_drop):
        """
        The function drops specified columns from a DataFrame and returns the name of the column that
        was dropped.
        
        :param cols_for_drop: The parameter "cols_for_drop" is a list of column names that you want to
        drop from the DataFrame
        :return: The variable "col" is being returned.
        """
        for col in cols_for_drop:
            self.df = self.df.drop([cols_for_drop], axis=1)
            return col

    def impute_nulls_mith_mode(self, col, mode):
        """
        The function imputes null values in a specified column of a dataframe using the mode value.
        
        :param col: The "col" parameter represents the column name or list of column names in the
        dataframe where you want to impute null values
        :param mode: The "mode" parameter is the value that will be used to impute the null values in
        the specified column. It should be a single value that represents the most frequent value in the
        column
        """
        mode = ['last_credit_pull_date', 'next_payment_date', 'last_payment_date', 'employment_length','term']
        for col in meidan:
           mode_imputer = SimpleImputer(strategy="most_frequent")
           df_mode_arr = mode_imputer.fit_transform(self.df)
           loans_df = pd.DataFrame(data=df_mode_arr, columns=loans_cols)
           print(loans_df)
    
    def impute_nulls_with_mean(self, col, mean):
        """
        The function imputes null values in a specified column with the mean value.
        
        :param col: The "col" parameter represents the column or columns in which you want to impute
        null values with the mean
        :param mean: The "mean" parameter in the code represents the mean value that will be used to
        impute null values in the specified column
        """
        mean = ['collections_12_mths_ex_med', 'mths_since_last_record','mths_since_last_delinq', 'int_rate', 'funded_amount']
        for col in mean:
            mean_imputer = SimpleImputer(strategy="median")
            df_mean_arr = mean_imputer.fit_transform(self.df)
            loans_df = pd.DataFrame(data=df_mean_arr, columns=loans_cols)
            loans_df

    def find_skewed_cols():
        """
        The function "find_skewed_cols" identifies columns in a DataFrame that have a skewness value
        greater than 1 or less than -1.
        """
        num_col = df.select_dtypes(include='number').columns.tolist()        
        list_of_skew = df[num_col].skew()
        skew_cols = [col for col in list_of_skew if col <-1 or col >1]
        return skew_cols

    def log_transformation(self):
        skewed_cols = ['annual_inc', 'delinq_2yrs', 'inq_last_6mths','open_accounts',\
                                         'out_prncp','out_prncp_inv','total_payment','total_payment_inv',\
                                            'total_rec_prncp','total_rec_int','total_rec_late_fee','recoveries',\
                                                'collection_recovery_fee','last_payment_amount','collections_12_mths_ex_med']
        for col in skewed_cols: 
            self.df[col].map(lambda i: np.log(i) if i > 0 else 0)
           
    
    def remove_outliers(self):
        """
        The function removes outliers from numerical columns in a DataFrame using the interquartile
        range method.
        """
        num_col = self.df.select_dtypes(include='number').columns.tolist()  
        Q1 = self.df[num_col].quantile(0.25)
        Q3 = self.df[num_col].quantile(0.75)
        IQR = Q3 - Q1
        threshold = 1.5
        outliers = self.df[(self.df[num_col] < Q1 - threshold * IQR) | (self.df[num_col] > Q3 + threshold * IQR)]
        self.df = self.df.drop(outliers.index)
        


if __name__ == '__main___':
    information = DataFrameInfo 
    plot = plotter 
    transform = DataFrameTransform
    transform.impute_nulls_mith_mode()