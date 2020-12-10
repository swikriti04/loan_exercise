# Data Transformation Excercise - PYTHON

## How to submit your code assignment

1. Fork the project from GitHub.
2. Make your forked project to **private** 
3. Add **ibmq2c** as member via **Manage Access**. From 'Settings' tab -> 'Manage access' -> 'Invite teams or people' -> Search for **ibmq2c** -> add  **ibmq2c** to this repository.
4. Complete your code and documentation in the forked project.
5. Create a new plain text file in the root folder of the forked project. And make the file name in the format of "your full name", e.g. **Mark Leon**.
6. Notify the code assignment is done or you can contact your employer to notify the same (we would be regularly checking the repo for any checkins).

OR

1. Send the file/s to the interviewer or recruiter and you may ask them to share the file to the concerned point of contact/hiring team. 

## Database Details: MySql
```
Database type : MySql
host: sl-aus-syd-1-portal.5.dblayer.com
port: 22243
dbname: q2c
Username : q2c
password : passw0rd
```

## Code assignment instruction
* Create a Python application/file/script(s) (e.g test.py).
* Using Python, create a connection to the MySQL database using the datanase connection details as provided above.
* Load the data from the q2c database and perform the following operation to generate your result:
  * Update the values inside column **term** by adding extra 12 months across all entries having **id** with **term** is equal to = '36 months' and **loan_status** is not equal to 'Fully Paid'
  * Create a new colum **int_rates_add_2pct**. Across each entry, the values inside the new column is equal to the value in **int_rate** plus and addition of 2% point.
  * For each entry, replace and recalculate the corresponding value in the **installament** by using the new interest rate in **int_rates_add_2pct**.
* Ouput the result into a csv file and submit the file.
* Please also submit the Python script(s) used in the coding assignment. 
* Create a requirement.txt file with all dependencies used. 
