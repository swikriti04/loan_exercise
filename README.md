# Data Transformation Excercise - PYTHON

## How to submit your code assignment

1. Fork the project from GitHub.
2. Make your forked project to **private** 
3. Add member of **ibmq2c** in **Manage Access**,  from Current Setting tab -> Manager access -> Invite a Collaborator -> lookup for **ibmq2c** -> add  **ibmq2c** to thi repository.
4. Complete your code and documentation in the forked project.
5. Create a new plain text file in the root folder of the forked project. And make the file name in the format of "your full name", e.g. **Mark Leon**.
6. Notify the code assignment is done or you can contact your employer to notify the same (we would be regularly checking the repo for any checkins).

## Database Details: MySql
```
Database type : MySql
host: sl-aus-syd-1-portal.5.dblayer.com
port: 22243
dbname: q2c
Username : q2c
password : passw0rd
```

## Code assignment details

* Create a python based application/file (e.g test.py)
* Create a connection to the database details provided above.
* Load the data and perform the following operation/result
  * For column **term** add extra 12 months to all **id** with **term 36 month**  and **loan_status** is not equal to _Fully Paid_
  * For column **int_rate** increase the intrest by 2% and recalculate the **installament** to be continued.
* Ouput the result to a csv file
* Create a requirment.txt file with all dependencies used. 
