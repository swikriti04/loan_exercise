#!/usr/bin/env python
# coding: utf-8

# In[ ]:


DB_HOST= "f5fc7f6b-efd4-4ee7-a84b-332e38adf2a5.c9v3nfod0e3fgcbd1oug.databases.appdomain.cloud"
DB_NAME= "q2c"
DB_USER= "q2c_user"
DB_PASS= "passw0rd"
DB_PORT= "30835"

import psycopg2
import pandas as pd
import pyodbc 

## Setting up connection with database
conn = psycopg2.connect(dbname = DB_NAME, user= DB_USER, password= DB_PASS, host= DB_HOST, port= DB_PORT)

## Setting cursor 
curr = conn.cursor()

## checking all the values from term column
##curr.execute("SELECT * FROM information_schema.columns where table_schema = 'public' and table_name= 'loan_data';")
##print(curr.fetchall())

## COPY of TABLE because there was no access to alter table
curr.execute("create table mytable as select * from loan_data;")

##curr.execute("select * from mytable;")
##print(curr.fetchall())

## Adding new column - new_term to table
curr.execute("ALTER table mytable ADD new_term varchar(20) default 'NULL';")
curr.execute("select * from mytable;")
##print(curr.fetchall())


## Updating values of new_term with specified conditions
curr.execute("UPDATE mytable set new_term = '48 months' where loan_status != 'Fully Paid' and term = '36 months';")
curr.execute("select * from mytable;")
##print(curr.fetchall())


## Adding new column - int_rates_add_2pct to table
curr.execute("ALTER table mytable ADD int_rates_add_2pct float default 0.0;")

## Updating values of column
curr.execute("UPDATE mytable set int_rates_add_2pct = int_rate+2;")
curr.execute("select * from mytable;")


## Fetching all data
print(curr.fetchall())

## Adding data to a dataframe
df = pd.DataFrame(pd.read_sql_query('select * from mytable', conn))

## Converting output to csv file
df.to_csv('output.csv')

curr.close()

## Closing Connection
conn.close()

