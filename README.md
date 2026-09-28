# VITyarthi_Project
E-Commerce Sales Analytics
-------------------------------------------------------------------------------------------
1. Project Overview

E-Commerce Sales Analytics is a simple Python project made to analyse e-commerce sales data.

It helps to check important info like total sales, profit, orders, customers, products, cities, categories and payment methods.

The project is console based, so it runs in the Command Prompt / Terminal. The user can select different options from the menu and get the required result.
-------------------------------------------------------------------------------------------
2. Features

The project has the following features:

Check total sales
Check total profit
Check total orders
Check total customers
View sales by category
Find top 10 products
View sales by city
View monthly sales
Analyse payment methods
View profit by category
View complete sales data
Filter data by category
Filter data by city
Reset filters
Show project/student credit
-------------------------------------------------------------------------------------------
3. Technologies Used
Python – Main programming language
Pandas – Used for handling and analysing data
StringIO – Used to read the data as CSV-style data
Command Prompt / Terminal – Used to run the project
-------------------------------------------------------------------------------------------
4. Requirements

To run this project, you need:

Python 
Pandas

-------------------------------------------------------------------------------------------

5. Installation
Step 1: Install Python

First, install Python 3.x on your system.

Check if Python is already installed:

python --version
Step 2: Open the project folder

Open Command Prompt / Terminal and go to the project folder.

Example:

cd ecommerce-sales-analytics
Step 3: Install Pandas

Run:

pip install pandas

Or, if you have requirements.txt:

pip install -r requirements.txt
-------------------------------------------------------------------------------------------
6. How to Run

Run this command:

python app.py

After running, the main menu will appear.

1. Show Key Performance Indicators
2. Sales by Category
3. Top 10 Products
4. Sales by City
5. Monthly Sales
6. Payment Method Analysis
7. Profit by Category
8. Show Sales Data
9. Filter Data
10. Reset Filters
0. Exit

Just enter the option number you want.
-------------------------------------------------------------------------------------------
7. How Filtering Works

Select:
Filter Data

The program will show the available categories.

You can select a category or choose all categories.

After that, it will show the available cities. You can select a city or choose all cities.

The selected filters will then be applied to the data.
-------------------------------------------------------------------------------------------
8. Reset Filters

If you want to remove the filters, select:

 Reset Filters

The complete data will be available again.
-------------------------------------------------------------------------------------------
9. Testing

The project can be tested by selecting different options from the main menu.

For eg.:

Test 1 – KPI

Select:

1

It should show:

Total Sales
Total Profit
Total Orders
Total Customers
Test 2 – Category

Select:

2

It should show sales for different categories.

Test 3 – Monthly Sales

Select:

5

It should show sales month-wise.

Test 4 – Filter

Select:

9

Choose a category and city and check the filtered records.

Test 5 – Reset

Select:

10

It should show:

Filters reset successfully.
Test 6 – Exit

Select:

0

The program will exit.
-------------------------------------------------------------------------------------------
10. Data Used

The project currently has 10 sample e-commerce records.

The data includes:

Order ID
Order Date
Customer ID
Product
Category
City
Sales
Profit
Payment Method

The sample data is stored directly in the Python file using StringIO.
-------------------------------------------------------------------------------------------
11. Student Credit

Name: Bhavya Chauhan
Reg. No.: 26BAI10579
Project: E-Commerce Sales Analytics
-------------------------------------------------------------------------------------------
13. Conclusion

This project is made to understand the basic use of Python and Pandas for data analysis.

It helps in analysing sales, profit, products, categories, cities, payment methods etc. in a simple way.

The project can be improved later by adding more data, charts, more filters and other analysis features.
 ------------------------------------------------------------------------------------------
