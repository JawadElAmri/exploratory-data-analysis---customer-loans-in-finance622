from sqlalchemy import create_engine
import pandas as pd 
import psycopg2 
import yaml



def load_database_credentials(): 
    """
    The function `load_database_credentials` reads and returns the contents of a YAML file containing
    AWS RDS database credentials.
    :return: The function `load_database_credentials` is returning the `database_credentials` variable.
    """
    with open ('/Users/jawadelamri/exploratory-data-analysis---customer-loans-in-finance622/credentials.yaml', 'r') as r:
        database_credentials  = yaml.safe_load(r)
        return database_credentials 


class RDSDatabaseConnector: 
    """ The RDSDatabaseConnector class connects to the AWS RDS database, extracts the loan payments table, and saves the data to a CSV file.

    """
    def __init__(self, database_credentials_dict):
        """
        The function initializes an object with a dictionary of database credentials.
        
        :param database_credentials_dict: A dictionary containing the credentials needed to connect to a
        database. The dictionary should have the following keys:
        """
        self.database_credentials_dict = database_credentials_dict
    
    def initialise_sqlalchmey_engine(self):
        """
        The function `initialise_sqlalchemy_engine` initialises and returns a SQLAlchemy engine using
        the yaml credentials
        """
        login = self.database_credentials_dict
        engine = create_engine(f"{login['DATABASE_TYPE']}+{login['DBAPI']}://{login['USER']} :{login['PASSWORD']}@{login['HOST']}\:{login['PORT']}/{login['DATABASE']}")
        engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        engine.connect() 
        return engine 
   
    def database_extraction(self, table):
        """
        The function `database_extraction` extracts all data from the loan payments table in the AWS RDS database and
        returns it as a pandas DataFrame.
        """
        try:
            connect_to_database = self.initialise_sqlalchmey_engine()
            print("Connected to the database")
        except Exception as e:
            print(e, "failed to connect")

        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, connect_to_database)
        return df
   
    def save_data_to_csv(self, df):
        """
        The function saves a DataFrame to a CSV file without including the index.
        """
        df.to_csv('loan_payments.csv', index=False)
       
        
if __name__ == "__main__":
#code won't run unless file is executed as a script 
    database_credentials_dict = load_database_credentials()
    database_connection = RDSDatabaseConnector(database_credentials_dict)
    loan_payments_df = database_connection.database_extraction('loan_payments')
    database_connection.save_data_to_csv(df='loan_payments')
   
loan_payments_df.info()
loan_payments_df.describe()


    

 


