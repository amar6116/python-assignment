# python-assignment
## Code2Xplore – 60 Days Challenge (Day‑1)
Problem Statement
The program asks for four things:
- Full Name
- Email ID
- Mobile Number
- Age 
  It checks each one based on certain rules. If everything’s good, you get “User Profile is VALID.” If not, you get “User Profile is INVALID.

   
Validation Rules
  
   - Full Name: Has to have at least two words. Can’t start or end with a space.
   - Email ID: Needs at least one @ and one . Can’t start with @.
  -  Mobile Number: Exactly 10 digits, only numbers, and shouldn’t start with 0.
  -  Age: Must be over 18 and no more than 60.


  
Algorithm
- Ask for your full name, email, mobile number, and age.
- Check the full name for the right number of spaces and no leading or trailing spaces.
- Check the email for @ and . and make sure it’s not starting with @.
- Check the mobile number for length, digits, and starting digit.
- Make sure the age is in the right range.
- Print out if the profile is valid or not.

 Code Snippets
 
  <img width="800" height="500" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/6ae20adb-b1f7-4f6a-84a5-a9570009dc68" />

## Code2Xplore – 60 Days Challenge (Day‑2)
The goal is to create a program that checks student details before approving their account.
The program uses only:
- Strings
- Conditional statements
Problem Statement
The program takes four inputs:
- Student ID
- Email ID
- Password
- Referral Code
It checks if these inputs follow the university rules.
If all are valid → it prints APPROVED
If any rule fails → it prints REJECTED

Validation Rules
Student ID
- Format: CSE-XXX
- Must start with "CSE"
- 4th character must be "-"
- Last 3 characters must be digits
- Example: CSE-245 → Valid, cse-245 → Invalid
Email ID
- Must contain @ and .
- @ cannot be the first or last character
- Must end with .edu
- Example: student@univ.edu → Valid, student@gmail.com → Invalid
Password
- Must be at least 8 characters long
- First character must be uppercase
- Must contain at least one digit
- Example: Aman1234 → Valid, amanabcd → Invalid
Referral Code
- Format: REF##@
- Must start with "REF"
- Next 2 characters must be digits
- Last character must be @
- Example: REF45@ → Valid, RE45@ → Invalid

Code snippets
<img width="800" height="500" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/a55bf82d-3f3d-4567-b418-4b854788a830" />

## Code2Xplore – 60 Days Challenge (Day‑3)
  Goal
    The goal is to create a program that checks student marks and classifies them into grades, while also counting valid and failed students.
    Inputs
The program takes:
  - Number of students (m)
  - Marks of each student
  - A fixed username ("amar")

Logic
  - If the username length is ≥ 6, each student’s mark is increased by 2.
  - If the username length is < 6, each student’s mark is decreased by 2.
Since "amar" has only 4 characters, all marks are reduced by 2.
  
Validation Rules (Grading)

  - 91–100 → Excellent
  - 76–89 → Very Good
  - 61–74 → Good
  - 41–59 → Average
  - 0–39 → Fail
  - Marks outside 0–100 → Invalid

Counters
  - valid → counts all students whose marks fall into valid ranges (0–100).
  - fail → counts students who fall into the Fail category.

Output
  - Prints each student’s adjusted mark with its grade.
  - Prints total valid students.
  - Prints total failed students.

<img width="1306" height="907" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/f17beb52-31e0-4f5f-aa67-ddd772bfdae6" />

## Code2Xplore – 60 Days Challenge (Day‑4)

# Activity Score Risk Categorization Program

## Goal

* The goal is to create a program that checks a student’s activity scores and classifies them into risk categories, while also counting valid, ignored, and filtered scores.

## Inputs

The program takes:

* Number of activity scores (`m`)
* Activity scores (one score at a time)
* A registration number (used for personalized filtering)

## Logic

* For each score:

  * If the score is negative, it is ignored.
  * Scores are classified as follows:

    * 0–30 → Low Risk
    * 31–60 → Medium Risk
    * 61–100 → High Risk
    * > 100 → Critical Risk
* Personalized filtering based on the last digit (`D`) of the registration number:

  * If `D` is **even**, all Low Risk scores are removed.
  * If `D` is **odd**, all Critical Risk scores are removed.

## Counters

* `valid` → counts all scores in the valid range (≥0)
* `ignored` → counts all negative scores
* `removed` → counts the scores removed due to the personalized filtering

## Output

* Prints the last digit of the registration number (`D`)
* Shows risk categories **before and after filtering**
* Prints total valid scores, total ignored scores, and total removed scores
  <img width="1437" height="958" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/9afcad43-0ed4-4ffd-a090-491501e320a4" />

## Code2Xplore – 60 Days Challenge (Day-5)

# Demand Classification and Personalized Filtering Program

## Goal

- Create a program to analyze demand requests.
- Classify requests into demand categories.
- Apply personalized filtering based on a computed index.

- Count valid and removed requests.

## Inputs

- Number of requests (m).
- Demand values entered one by one.
- A predefined name used to calculate the personalization index.

## Logic

- For each demand value:
  - If the value is negative, it is treated as an invalid request.
  - If the value is zero, it is counted as no demand.
  - Requests are classified as:
    - 1 to 20 → Low Demand
    - 21 to 50 → Moderate Demand
    - Greater than 50 → High Demand

## Personalization Rule (PLI)

- Count the number of characters in the name excluding spaces.
- Compute:
  - PLI = length mod 3
- Apply filtering as follows:
  - If PLI equals 0, remove all Low Demand requests.
  - If PLI equals 1, remove all High Demand requests.
  - If PLI equals 2, remove both Low and High Demand requests.

## Counters

- valid: counts all non-negative requests.
- removed: counts requests removed due to filtering.
- invalid requests are tracked separately.

## Output

- Length of the name.
- Personalization index (PLI).
- Total valid requests.
- Number of removed requests.
- Demand categories after filtering:
  - Low Demand
  - Moderate Demand
  - High Demand

<img width="1589" height="968" alt="Screenshot (9)" src="https://github.com/user-attachments/assets/7e022808-92de-4b09-9bc6-b63e54d29807" />

## Code2Xplore – 60 Days Challenge (Day-6)

# Transaction Risk Analysis Program

## Problem Overview
- This program analyzes transaction amounts entered by the user.
- It identifies risky spending patterns based on frequency and total amount.
- Transactions are grouped into categories for better analysis.

## Objective
- Accept multiple transaction values
- Classify transactions into categories
- Detect spending patterns
- Calculate total and frequency
- Assign a final risk level
- Provide a summary using a tuple

## How the Program Works
- The user enters the number of transactions and their values.
- All values are stored in a list.
- Using list comprehension, transactions are classified into:
  - invalid (≤ 0)
  - normal (1–500)
  - large (501–2000)
  - high risk (> 2000)
- A separate list is created for valid transactions (greater than 0).
- A loop is used to calculate total spending.
- Conditions are used to detect:
  - frequent transactions
  - large spending
  - suspicious patterns

## Risk Classification Logic
- The program uses three factors:
  - number of valid transactions (freq)
  - total transaction value (total)
  - number of high-risk transactions

### Decision Rules
- High Risk
  - freq > 4 AND total > 3000

- Moderate Risk
  - freq > 3 OR total > 2500 OR high-risk transactions ≥ 3

- Low Risk
  - when none of the above conditions are satisfied

## Output
- Categorized transactions:
  - Invalid
  - Normal
  - Large
  - High Risk
- Pattern detection:
  - Frequent Transactions
  - Large Spending
  - Suspicious Pattern
- Total transaction value
- Number of transactions
- Final Risk Classification
- Summary tuple:
  - (total transactions, valid transactions, total amount, risk)

## My Approach / Logic Decisions
- I separated classification and analysis to keep the code simple.
- I considered only positive values as valid transactions.
- I used both frequency and total amount to determine risk level.
- I used list comprehension for cleaner classification.

## Reflection
- This program helped me understand how multiple conditions affect decision making.
- Combining frequency and amount gives better results than using a single factor.
- The logic can be extended for real-world fraud detection systems.

## Concepts Used
- Lists
- Loops (for)
- Conditional statements (if-elif)
- List comprehension
- Dictionary
- Tuple

  <img width="1163" height="910" alt="Screenshot (23)" src="https://github.com/user-attachments/assets/b0a33bc3-eff9-4412-8e93-a0c33943b963" />



  ## Code2Xplore – 60 Days Challenge (Day-8)

# Multi-Dimensional Academic Intelligence System

## Problem Overview
- This program analyzes student performance.
- It uses marks, attendance, and assignment scores.
- It classifies students into categories.
- It gives overall class performance.

## Objective
- Generate student data using random values
- Store data using list, tuple, and dictionary
- Convert data into DataFrame using Pandas
- Use NumPy for calculations
- Classify students into categories
- Detect patterns in data
- Provide final system result
- Return summary using a tuple

## How the Program Works
- The program generates n students based on roll number.
- Each student has:
  - marks (0–100)
  - attendance (0–100)
  - assignment (0–50)
- Data is stored in a list as tuples.
- Data is converted into a DataFrame.
- Classification is done using conditions.
- Analysis is done using NumPy and manual calculation.

## Student Classification Logic
- At Risk
  - marks < 40 OR attendance < 50
- Average
  - marks between 40 and 70
- Good
  - marks between 71 and 90
- Top Performer
  - marks > 90 AND attendance > 80

## Analysis Performed
- Mean (calculated manually)
- Median (NumPy)
- Standard Deviation (NumPy)
- Correlation (Marks vs Attendance)
- Normalization of marks

## Pattern Detection
- Consistency
  - standard deviation < 15
- Attendance Risk
  - more than 3 students with attendance < 50
- High Achievement
  - at least 2 top performers

## Performance Index Formula
performance_index = (marks * 0.6 + assignment * 0.4) * log(attendance + 1)

## Output
- DataFrame (table format)
- Student category dictionary
- Unique categories (set)
- Statistical values:
  - mean
  - median
  - standard deviation
  - correlation
- Final system insight:
  - Stable Academic System
  - Moderate Performance
  - Critical Attention Required
- Summary tuple:
  - (mean, std_dev, max_marks)

## Personalization Applied
- Last digit of Register Number = 6
- Hence, n = 6 students generated

## My Approach / Logic Decisions
- I used three functions:
  - generate_data()
  - classify_students()
  - analyze_data()
- I used random values to simulate data.
- I used conditions to classify students.
- I calculated mean manually.

## Concepts Used
- Lists
- Tuples
- Dictionary
- Set
- Functions
- List comprehension
- NumPy
- Pandas
- Random module
- Math module

## Reflection
- I learned how to use NumPy and Pandas.
- I understood how to analyze data step by step.
- I learned classification using conditions.
- I learned manual calculation of mean.

## Output Screenshot
<img width="1444" height="890" alt="Screenshot (54)" src="https://github.com/user-attachments/assets/9a0bfb50-0322-4017-962a-fa323a7d3523" />


## Code2Xplore – 60 Days Challenge (Day-9)

# Smart Inventory Mutation Tracker

## Problem Overview
- This program analyzes how inventory data behaves when copied and modified.
- It focuses on shallow copy and deep copy behavior.
- It detects unintended changes in original data due to improper copying.
- It helps understand nested data mutation.

## Objective
- Create inventory using nested dictionaries  
- Apply changes based on roll number logic  
- Perform shallow copy and deep copy  
- Modify copied data selectively  
- Compare original and modified data  
- Identify changed and unchanged items  
- Return summary using tuples  

## How the Program Works
- The program creates an inventory list.
- Each item contains:
  - price  
  - stock  
  - supplier rating  
- Two copies are created:
  - shallow copy  
  - deep copy  
- A specific item is selected using:
  - index = roll_number % length_of_inventory  
- Selected item is modified:
  - price reduced by 10%  
  - stock increased by 5  
- Results are compared with original data.

## Mutation Logic
```
index = roll_number % len(inventory)
price = price * 0.9
stock = stock + 5
```

## Copy Behavior
### Shallow Copy
- Shares nested objects  
- Changes affect original data  

### Deep Copy
- Fully independent copy  
- Changes do not affect original  

## Analysis Performed
- Compared original vs shallow copy  
- Compared original vs deep copy  
- Identified:
  - changed items  
  - unchanged items  

## Output
- Original inventory  
- Shallow copy result  
- Deep copy result  
- Changed items  
- Unchanged items  
- Tuple summary:
  - (changed_count, unchanged_count)  

## Personalization Applied
- Roll Number: 24110011606  
- Logic applied using:
  index = roll_number % number_of_items  

## My Approach / Logic Decisions
- Used modular functions:
  - create_inventory()  
  - update_items()  
  - check_diff()  
- Used nested dictionaries  
- Used conditional logic for mutation  
- Compared data using loops  

## Concepts Used
- Lists  
- Dictionaries  
- Nested structures  
- Shallow copy  
- Deep copy  
- Functions  
- Loops  
- Tuple  

## Reflection
- Learned difference between shallow and deep copy  
- Understood mutation in nested data  
- Practiced comparing complex structures  
- Improved logical thinking  


## Code2Xplore – 60 Days Challenge (Day-10)

# Academic Data Drift & Copy Behavior Analyzer

## Problem Overview
- This program analyzes how student data changes when copied and modified.
- It focuses on detecting data drift.
- It compares shallow copy and deep copy behavior.
- It uses statistical analysis to evaluate changes.

## Objective
- Generate student data using random values  
- Store data using list of dictionaries  
- Perform shallow copy and deep copy  
- Apply mutation based on roll number logic  
- Analyze data using NumPy and manual calculation  
- Detect data drift  
- Classify system behavior  
- Return summary using tuple  

## How the Program Works
- The program generates n student records.
- Each student contains:
  - marks  
  - attendance  
  - scores (list)  
- Data is copied using:
  - shallow copy  
  - deep copy  
- Mutation is applied:
  - marks increased using square root  
  - attendance decreased  
  - scores updated  
- Data is converted into DataFrame using Pandas.
- Statistical analysis is performed.

## Mutation Logic
```
r = roll_number % 3
if r == 0:
    r = 1

if index % r == 0:
    marks = marks + sqrt(marks)
    attendance = attendance - 5
    scores[0] = scores[0] + 2
```

## Copy Behavior
### Shallow Copy
- Shares nested data  
- Changes affect original data  

### Deep Copy
- Fully independent  
- Changes do not affect original  

## Analysis Performed
- Mean (NumPy)  
- Standard Deviation (NumPy)  
- Manual Mean Calculation  
- Data Drift Calculation:
```
drift = abs(mean(original_marks) - mean(modified_marks))
```

## Normalization
```
normalized_marks = (marks - min) / (max - min)
```

## Classification Logic
- Copy Failure Detected  
  - if original data is modified due to shallow copy  
- Stable Data  
  - if drift < threshold  
- Minor Drift  
  - if drift < 2 × threshold  
- Critical Drift  
  - otherwise  

## Output
- Original DataFrame  
- Shallow Copy DataFrame  
- Deep Copy DataFrame  
- Drift Value  
- Tuple:
  - (mean, drift, std_dev)  
- Final Classification  

## Personalization Applied
- Roll Number: 24110011606  
- Logic applied using:
  r = roll_number % 3  

## My Approach / Logic Decisions
- Used modular functions:
  - create()  
  - change()  
  - stats()  
  - result_check()  
- Used random data for simulation  
- Applied mathematical transformation  
- Compared original and modified datasets  

## Concepts Used
- Lists  
- Dictionaries  
- Nested structures  
- Shallow copy  
- Deep copy  
- NumPy  
- Pandas  
- Functions  
- Mathematical operations  
- Data analysis  

## Reflection
- Learned data drift concept  
- Understood shallow vs deep copy clearly  
- Practiced statistical analysis using NumPy  
- Improved understanding of data mutation  

