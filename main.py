import pandas as pd
from io import StringIO


# DATA

data = """
Order_ID,Order_Date,Customer_ID,Product,Category,City,Sales,Profit,Payment_Method
1001,2026-01-05,C001,Laptop,Electronics,Lucknow,55000,7000,UPI
1002,2026-01-08,C002,Mobile Phone,Electronics,Kanpur,25000,4000,Credit Card
1003,2026-01-12,C003,Headphones,Electronics,Agra,3000,800,UPI
1004,2026-02-03,C004,Office Chair,Furniture,Lucknow,8500,1500,Cash
1005,2026-02-10,C005,Table,Furniture,Varanasi,12000,2500,Credit Card
1006,2026-02-15,C006,Shoes,Fashion,Kanpur,4500,900,UPI
1007,2026-03-02,C007,T-Shirt,Fashion,Agra,1200,300,Cash
1008,2026-03-11,C008,Watch,Fashion,Lucknow,6000,1200,Credit Card
1009,2026-03-18,C009,Smart TV,Electronics,Varanasi,42000,6000,UPI
1010,2026-04-04,C010,Refrigerator,Electronics,Kanpur,38000,5500,Credit Card
"""


# Convert the data into a pandas DataFrame
df = pd.read_csv(StringIO(data))

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# CHECK ORDER DATES

print("\nCHECKING ORDER DATES:")
print(df["Order_Date"])


# FUNCTIONS

def show_summary(data):
    ttl_sales = data["Sales"].sum()
    ttl_profit = data["Profit"].sum()
    ttl_orders = data["Order_ID"].nunique()
    ttl_customers = data["Customer_ID"].nunique()

    print("\n" + "=" * 50)
    print("KEY PERFORMANCE INDICATORS")
    print("=" * 50)

    print(f"Total Sales     : ₹{ttl_sales:,.2f}")
    print(f"Total Profit    : ₹{ttl_profit:,.2f}")
    print(f"Total Orders    : {ttl_orders:,}")
    print(f"Total Customers : {ttl_customers:,}")


def sales_by_category(data):
    result = (data.groupby("Category")["Sales"].sum().sort_values(ascending=False))

    
    print("\n" + "=" * 50)
    
    print("SALES BY CATEGORY")
    
    print("=" * 50)

    print(result.to_string())


def top_products(data):
    result = ( data.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10))

    print("\n" + "=" * 50)
    
    print("TOP 10 PRODUCTS")
    
    print("=" * 50)

    print(result.to_string())


def sales_by_city(data):
    result = (data.groupby("City")["Sales"].sum().sort_values(ascending=False))

    print("\n" + "=" * 50)
    
    print("SALES BY CITY")
    
    print("=" * 50)

    print(result.to_string())


def monthly_sales(data):
    result = (data.groupby(data["Order_Date"].dt.to_period("M"))["Sales"].sum())

    print("\n" + "=" * 50)
    
    print("MONTHLY SALES")
    
    print("=" * 50)

    print(result.to_string())


def payment_analysis(data):
    result = (    data.groupby("Payment_Method")["Sales"].sum().sort_values(ascending=False))

    print("\n" + "=" * 50)
    
    print("PAYMENT METHOD ANALYSIS")
    
    print("=" * 50)

    print(result.to_string())


def profit_by_category(data):
    result = (    data.groupby("Category")["Profit"].sum().sort_values(ascending=False))

    print("\n" + "=" * 50)
    
    print("PROFIT BY CATEGORY")
    
    print("=" * 50)

    print(result.to_string())


def show_data(data):
    print("\n" + "=" * 50)
    print("SALES DATA")
    print("=" * 50)

    print(data.to_string(index=False))


def filter_data(data):

    filtered_data = data.copy()

    print("\n" + "=" * 50)
    print("FILTER DATA")
    print("=" * 50)

    # Category
    categories = sorted(data["Category"].dropna().unique())

    print("\nCategories:")

    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    print("0. All Categories")

    choice = input("\nSelect category: ")

    if choice.isdigit():

        choice = int(choice)

        if 1 <= choice <= len(categories):

            selected_category = categories[choice - 1]

            filtered_data = filtered_data[filtered_data["Category"] == selected_category]

    # City
    cities = sorted(data["City"].dropna().unique())

    print("\nCities:")

    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    print("0. All Cities")

    choice = input("\nSelect city: ")

    if choice.isdigit():

        choice = int(choice)

        if 1 <= choice <= len(cities):

            selected_city = cities[choice - 1]

            filtered_data = filtered_data[filtered_data["City"] == selected_city]

    return filtered_data


# MAIN PROGRAM

def main():

    print("\n" + "=" * 60)
    print("       E-COMMERCE SALES ANALYTICS")
    print("=" * 60)

    print(f"\nTotal records: {len(df)}")

    filtered_df = df.copy()

    while True:

        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)

        print("1. Show Key Performance Indicators")
        print("2. Sales by Category")
        print("3. Top 10 Products")
        print("4. Sales by City")
        print("5. Monthly Sales")
        print("6. Payment Method Analysis")
        print("7. Profit by Category")
        print("8. Show Sales Data")
        print("9. Filter Data")
        print("10. Reset Filters")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_summary(filtered_df)

        elif choice == "2":
            sales_by_category(filtered_df)

        elif choice == "3":
            top_products(filtered_df)

        elif choice == "4":
            sales_by_city(filtered_df)

        elif choice == "5":
            monthly_sales(filtered_df)

        elif choice == "6":
            payment_analysis(filtered_df)

        elif choice == "7":
            profit_by_category(filtered_df)

        elif choice == "8":
            show_data(filtered_df)

        elif choice == "9":
            filtered_df = filter_data(df)

            print(f"\nFiltered records: {len(filtered_df)}")

        elif choice == "10":
            filtered_df = df.copy()
            print("\nFilters reset successfully.")

        elif choice == "0":
            print("\nThank you for using E-Commerce Sales Analytics.")
            break

        else:
            print("\nInvalid choice. Please try again.")


# START PROGRAM

if __name__ == "__main__":
    main()

#PROJECT CREDIT

print("\n" + "=" * 60)
print("                    PROJECT CREDIT")
print("=" * 60)

print("Student Name     : BHAVYA CHAUHAN")
print("Registration No. : 26BAI10579")
print("Project Name     : E-Commerce Sales Analytics")

print("=" * 60)
print("                    THANK YOU")
print("=" * 60)