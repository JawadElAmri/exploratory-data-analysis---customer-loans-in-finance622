from sqlalchemy import create_engine
import pandas as pd 
import psycopg2 
import yaml


def load_database_credentials(): 
    with open ('/Users/jawadelamri/exploratory-data-analysis---customer-loans-in-finance622/credentials.yaml', 'r') as r:
        database_credentials  = yaml.safe_load(r)
        return database_credentials 


class RDSDatabaseConnector:  
    def __init__(self, database_credentials_dict):
        self.database_credentials_dict = database_credentials_dict
    
    def initialise_sqlalchmey_engine(self):
        login = self.database_credentials_dict
        engine = create_engine(f"{login['DATABASE_TYPE']}+{login['DBAPI']}://{login['USER']}:{login['PASSWORD']}@{login['HOST']}:{login['PORT']}/{login['DATABASE']}")
        engine.execution_options(isolation_level='AUTOCOMMIT').connect()
        engine.connect() 
        return engine 
   
    def database_extraction(self, table):
        connect_to_database = self.initialise_sqlalchmey_engine()
        query = f"SELECT * FROM {table}"
        df = pd.read_sql(query, connect_to_database)
        return df
   
    def save_data_to_csv(self, df):
       df.to_csv('loan_payments.csv', index=False)
       
        
if __name__ == "__main__":
    database_credentials_dict = load_database_credentials()
    database_connection = RDSDatabaseConnector(database_credentials_dict)
    loan_payments_df = database_connection.database_extraction('loan_payments')
    database_connection.save_data_to_csv(df='loan_payments')
   
loan_payments_df.info()
loan_payments_df.describe()


    

 


