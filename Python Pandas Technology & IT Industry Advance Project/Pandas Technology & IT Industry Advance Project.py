import pandas as pd 
import os

# Import all files
customers = pd.read_csv(r"C:\Users\chait\OneDrive\Documents\30 Days Python Micro Course\Python Pandas Technology & IT Industry Advance Project\Customers.csv")
data_dict = pd.read_csv(r"C:\Users\chait\OneDrive\Documents\30 Days Python Micro Course\Python Pandas Technology & IT Industry Advance Project\Data_Dictionary.csv")
products = pd.read_csv(r"C:\Users\chait\OneDrive\Documents\30 Days Python Micro Course\Python Pandas Technology & IT Industry Advance Project\Products.csv")
subscriptions = pd.read_csv(r"C:\Users\chait\OneDrive\Documents\30 Days Python Micro Course\Python Pandas Technology & IT Industry Advance Project\Subscriptions.csv")
support_tickets = pd.read_csv(r"C:\Users\chait\OneDrive\Documents\30 Days Python Micro Course\Python Pandas Technology & IT Industry Advance Project\Support Tickets.csv")
transactions = pd.read_csv(r"C:\Users\chait\OneDrive\Documents\30 Days Python Micro Course\Python Pandas Technology & IT Industry Advance Project\Transactions.csv")

# # Exploratory Data Analysis

# EDA1. Load and Explore the Data

# print all datasets
datasets = {
    "Customers" : customers,
    "Data Dictionary" : data_dict,
    "Products" : products,
    "Subscriptions" : subscriptions,
    "Support Tickets" : support_tickets,
    "Transactions" : transactions
}

for name, df in datasets.items():
    print(f"\n{name}:")
    print(df)

# information about all datasets
for name, df in datasets.items():
    print(f"\n===={name} Dataset====")
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nHead:\n", df.head())
    print("\nInfo:")
    print(df.info())


# EDA.2 — Missing Values
# Find the number and percentage of missing values in every column for all 5 datasets 
def missing_values_report(df):
    missing_count = df.isnull().sum()
    missing_percentage = (missing_count / len(df)) * 100

    # Create a DataFrame to display the missing values report
    missing_report = pd.DataFrame({
        "Missing Count": missing_count,
        "Missing Percentage": missing_percentage
    })
    return missing_report[missing_report["Missing Count"] > 0]

print("\nCustomers missing report:\n", missing_values_report(customers).round(2))
print("\nData Dictionary missing report:\n", missing_values_report(data_dict).round(2))
print("\nProducts missing report:\n", missing_values_report(products).round(2))
print("\nSubscriptions missing report:\n", missing_values_report(subscriptions).round(2))
print("\nSupport Tickets missing report:\n", missing_values_report(support_tickets).round(2))
print("\nTransactions missing report:\n", missing_values_report(transactions).round(2))


# EDA.3 — Duplicate Analysis
def duplicate_report(df, id_column):
    total_duplicates = df.duplicated().sum()
    duplicate_percentage = (total_duplicates / len(df)) * 100
    id_duplicates = df[id_column].duplicated().sum()
    
    return{
        "Total_Duplicates": total_duplicates,
        "Duplicate_Percentage": duplicate_percentage,
        "ID_Duplicates": id_duplicates
    }
    

print("\nCustomers duplicate report:", duplicate_report(customers, "Customer_ID"))
print("\nProducts duplicate report:", duplicate_report(products, "Product_ID"))
print("\nSubscriptions duplicate report:", duplicate_report(subscriptions, "Subscription_ID"))
print("\nSupport Tickets duplicate report:", duplicate_report(support_tickets, "Ticket_ID"))
print("\nTransactions duplicate report:", duplicate_report(transactions, "Transaction_ID"))


# EDA.4 — Unique Values & Category Exploration
# For each dataset, find the number of unique values in every column
def unique_value_report(df):
    report = pd.DataFrame({
        "Unique_Values" : df.nunique(),
        "Missing_Values" : df.isnull().sum()
    })
    return report.sort_values("Unique_Values", ascending=True)

print("\nCustomers unique value report:\n", unique_value_report(customers))
print("\nProducts unique value report:\n", unique_value_report(products))
print("\nSubscriptions unique value report:\n", unique_value_report(subscriptions)) 
print("\nSupport Tickets unique value report:\n", unique_value_report(support_tickets))
print("\nTransactions unique value report:\n", unique_value_report(transactions))


# EDA.5 — Category Inconsistency Detection
# Find the actual categories and their frequencies
print("\n====Customers category inconsistency reprort====")
print("\n",customers["Industry"].value_counts())
print("\n",customers["State"].value_counts())
print("\n",customers["City"].value_counts())
print("\n",customers["Acquisition_Channel"].value_counts(dropna=False))

print("\n====Products category inconsistency reprort====")
print("\n",products["Product_Category"].value_counts())
print("\n",products["Product_Type"].value_counts())
print("\n",products["Pricing_Model"].value_counts())

print("\n====Subscriptions category inconsistency reprort====")
print("\n",subscriptions["Plan"].value_counts())
print("\n",subscriptions["Billing_Cycle"].value_counts())
print("\n",subscriptions["Status"].value_counts())
print("\n",subscriptions["Auto_Renewal"].value_counts())

print("\n====Transactions category inconsistency reprort====")
print("\n",transactions["Transaction_Type"].value_counts())
print("\n",transactions["Payment_Method"].value_counts())
print("\n",transactions["Payment_Status"].value_counts())
print("\n",transactions["Sales_Channel"].value_counts())

print("\n====Support Tickets category inconsistency reprort====")
print("\n",support_tickets["Issue_Category"].value_counts())
print("\n",support_tickets["Priority"].value_counts())
print("\n",support_tickets["Ticket_Status"].value_counts())


# EDA.6 — Numeric Data Analysis
print("\n====Products====")
print(products[["Unit_Price"]].describe())
print("\n====Subscriptions====")
print(subscriptions[["Monthly_Fee", "Discount"]].describe())
print("\n====Transactions====")
print(transactions[["Amount"]].describe())
print("\n====Support Tickets=====")
print(support_tickets[["Resolution_Time_Hours", "Satisfaction_Score"]].describe())

# 6.1 Investigate Suspicious Numeric Values
# A. Suspicious subscription discounts
print("\n====Suspicious Subscription Discounts====")
print(subscriptions[subscriptions["Discount"] > 100][["Subscription_ID", "Customer_ID", "Plan", "Monthly_Fee", "Discount", "Status"]])
print("\nDiscount > 100:", (subscriptions["Discount"]>100).sum())

# B. Negative transaction amounts
print("\n====Negative transaction amounts====")
negative_transactions = transactions[transactions["Amount"] < 0]
print(negative_transactions[["Transaction_ID", "Transaction_Type", "Amount", "Payment_Status"]])
print("\n",negative_transactions["Transaction_Type"].value_counts())

# C. Negative support resolution time
print("\n====Negative support resolution time====")
negative_resolution = support_tickets[support_tickets["Resolution_Time_Hours"] < 0]
print(negative_resolution[["Ticket_ID", "Issue_Category", "Priority", "Resolution_Time_Hours", "Ticket_Status"]])
print("\nNegative Resolution Time : ", (support_tickets["Resolution_Time_Hours"]<0).sum()) 


# EDA.7 — Negative Resolution Time Analysis
print("\n====Negative Resolution Time Analysis====")
negative_resolution = support_tickets[support_tickets["Resolution_Time_Hours"] < 0]
print("\nTotal Negative Resolution Tickets:", len(negative_resolution))

print("\nNegative Resolution by Ticket Status:")
print(negative_resolution["Ticket_Status"].value_counts())

print("\nNegative Resolution by Priority:")
print(negative_resolution["Priority"].value_counts())

print("\nNegative Resolution by Issue Category:")
print(negative_resolution["Issue_Category"].value_counts())

print("\nOverall Ticket Status:")
print(support_tickets["Ticket_Status"].value_counts())

print("\n",negative_resolution[["Ticket_ID", "Ticket_Status", "Priority", "Issue_Category", "Resolution_Time_Hours"]])


# EDA.8 — Date & Time Analysis
# Step 1 — Check date ranges
print("\n====Date Ranges====")
print("\nCustomers:")
print("Min:", customers["Signup_Date"].min())
print("Max:", customers["Signup_Date"].max())

print("\nProducts:")
print("Min:", products["Launch_Date"].min())
print("Max:", products["Launch_Date"].max())

print("\nSubscriptions:")
print("Start Date Min:", subscriptions["Subscription_Start_Date"].min())
print("Start Date Max:", subscriptions["Subscription_Start_Date"].max())

print("\nSupport Tickets:")
print("Min:", support_tickets["Ticket_Date"].min())
print("Max:", support_tickets["Ticket_Date"].max())

print("\nTransactions:")
print("Min:", transactions["Transaction_Date"].min())
print("Max:", transactions["Transaction_Date"].max())

# Step 2 — Check missing transaction dates
missing_transaction_dates = transactions[transactions["Transaction_Date"].isna()]
print("\nMissing Transaction Dates:\n", missing_transaction_dates[["Transaction_ID", "Customer_ID", "Subscription_ID", "Transaction_Type", "Amount", "Payment_Status"]])


# EDA.9 — Convert Dates & Check Date Logic
# 9.1 Convert date columns
customers["Signup_Date"] = pd.to_datetime(customers["Signup_Date"], format="%d-%m-%Y", errors="coerce")
products["Launch_Date"] = pd.to_datetime(products["Launch_Date"], format="%d-%m-%Y", errors="coerce")
subscriptions["Subscription_Start_Date"] = pd.to_datetime(subscriptions["Subscription_Start_Date"], format="%d-%m-%Y", errors="coerce")
subscriptions["Subscription_End_Date"] = pd.to_datetime(subscriptions["Subscription_End_Date"], format="%d-%m-%Y", errors="coerce")
support_tickets["Ticket_Date"] = pd.to_datetime(support_tickets["Ticket_Date"], format="%d-%m-%Y", errors="coerce")
transactions["Transaction_Date"] = pd.to_datetime(transactions["Transaction_Date"], format="%d-%m-%Y", errors="coerce")

# 9.2 Check invalid subscription dates
# Does any subscription have an End Date earlier than its Start Date?
invalid_subscription_dates = subscriptions[subscriptions["Subscription_End_Date"].notna() & (subscriptions["Subscription_End_Date"] < subscriptions["Subscription_Start_Date"])]
print("\n====Invalid Subscription Dates:====")
print(invalid_subscription_dates[["Subscription_ID", "Subscription_Start_Date", "Subscription_End_Date", "Status"]])
print("Count:",len(invalid_subscription_dates))

print("\n Subscription Start Date Before 01-01-2022:\n", subscriptions[subscriptions["Subscription_Start_Date"] < pd.Timestamp("2022-01-01")])


# EDA.10 — Analyze Subscription Duration
# 10.1 Analyze subscription duration in days
subscriptions["Subscription_Duration_Days"] = (subscriptions["Subscription_End_Date"] - subscriptions["Subscription_Start_Date"]).dt.days
print("\n====Subscription Duration:====")
print(subscriptions["Subscription_Duration_Days"].describe())

# 10.2 Investigate the shortest & longest completed subscription
short_subscriptions = subscriptions[subscriptions["Subscription_Duration_Days"].notna()].sort_values("Subscription_Duration_Days")
print("\nShorted Completed Subscriptions:")
print(short_subscriptions[["Subscription_ID", "Customer_ID", "Plan", "Status", "Subscription_Start_Date", "Subscription_End_Date", "Subscription_Duration_Days"]].head(10))

print("\nLongest Completed Subscription:")
print(short_subscriptions[["Subscription_ID", "Customer_ID", "Plan", "Status", "Subscription_Start_Date", "Subscription_End_Date", "Subscription_Duration_Days"]].tail(10))

# 10.2.1 Investigation of negative days in short duration
print("\nShort Negative Durations:") 
print(subscriptions.loc[subscriptions["Subscription_Duration_Days"] < 0, ["Subscription_ID", "Subscription_Start_Date", "Subscription_End_Date", "Subscription_Duration_Days"]].head(20))

# 10.2.2 Investigation of extended days in long durations
print("\nLong Entended Durations:")
print(subscriptions.loc[subscriptions["Subscription_End_Date"] > pd.Timestamp("2025-12-31"), ["Subscription_ID", "Subscription_Start_Date", "Subscription_End_Date", "Status", "Subscription_Duration_Days"]].head(20))

# 10.2.3 Percentage wise durations
print("\nPercentage wise durations:")
negative_duration = subscriptions[subscriptions["Subscription_Duration_Days"] < 0]
long_duration = subscriptions[subscriptions["Subscription_Duration_Days"] > 365]
print("Negative Duration Records:", len(negative_duration))
print("Duration > 1 year:", len(long_duration))

print("\nNegative Duration Percentage:", round(len(negative_duration)/len(subscriptions)*100,2))
print("Duration > 1 Year Percentage:", round(len(long_duration)/len(subscriptions)*100,2))


# EDA.11 — Subscription Status Analysis
print("\n====Subscription Status Analysis====")
print("Subscription Status Counts:")
print(subscriptions["Status"].value_counts())

print("\nStatus Percentage:")
print(subscriptions["Status"].value_counts(normalize=True).mul(100).round(2))


# EDA.12 — Plan-wise Subscription Analysis
print("\n====Plan-wise Subscription Analysis====")
plan_count = subscriptions["Plan"].value_counts()
print("Plan-wise Counts:")
print(plan_count)

print("\nPlan Percentage:")
print(subscriptions["Plan"].value_counts(normalize=True).mul(100).round(2))


# EDA.13 — Billing Cycle Analysis
print("\n====Billing Cycle Analysis====")
billing_count = subscriptions["Billing_Cycle"].value_counts()
print("Billing Cycle Counts:")
print(billing_count)

print("\nBilling Cycle Percentage:")
print(subscriptions["Billing_Cycle"].value_counts(normalize=True).mul(100).round(2))


# EDA.14 — Auto-Renewal Analysis
print("\n====Auto-Renewal Analysis====")
auto_renewal_counts = subscriptions["Auto_Renewal"].value_counts()
print("Auto-Renewal Counts:")
print(auto_renewal_counts)

auto_renewal_percentage = subscriptions["Auto_Renewal"].value_counts(normalize=True).mul(100).round(2)
print("\nAuto-Renewal Percentage:")
print(auto_renewal_percentage)


# EDA.15 — Subscription Status vs Auto-Renewal
# Are cancelled/expired subscriptions more common among customers who do not have auto-renewal?
print("\n====Subscription Status vs Auto-Renewal=====")
status_auto = pd.crosstab(subscriptions["Status"],subscriptions["Auto_Renewal"])
print("Status-Auto Counts:")
print(status_auto)

status_wise_percentage = pd.crosstab(subscriptions["Status"],subscriptions["Auto_Renewal"],normalize="index").mul(100).round(2)
print("\nStatus Wise Percentage:")
print(status_wise_percentage)


# EDA.16 — Subscription Status by Plan
# Does subscription status vary across different plans?
print("\n====Subscription Status vs Plan====")
status_plan = pd.crosstab(subscriptions["Plan"], subscriptions["Status"])
print("Status-Plan Counts:")
print(status_plan)

status_plan_percentage = pd.crosstab(subscriptions["Plan"], subscriptions["Status"], normalize="index").mul(100).round(2)
print("\nStatus-Plan Percentage:")
print(status_plan_percentage)


# EDA.17 — Billing Cycle vs Subscription Status
print("\n====Subscription Status vs Billing Cycle====")
status_billing = pd.crosstab(subscriptions["Billing_Cycle"],subscriptions["Status"])
print("Status-billing Counts:")
print(status_billing)

status_billing_percentage = pd.crosstab(subscriptions["Billing_Cycle"], subscriptions["Status"], normalize="index").mul(100).round(2)
print("\nStatus-billing Percentage:")
print(status_billing_percentage)


# EDA.18 — Monthly Subscription Start Trend
# How has the number of new subscriptions changed over time?
print("\n====Monthly Subscription Start Trend====")
monthly_subscription = (subscriptions.set_index("Subscription_Start_Date").resample("ME").size())
print(monthly_subscription)


# EDA.19 — Product Category Distribution
print("\n====Product Category Distribution====")
product_category_counts = products["Product_Category"].value_counts()
print("Product Category Counts:")
print(product_category_counts)

product_category_percentage = (products["Product_Category"].value_counts(normalize=True).mul(100).round(2))
print("\nProduct Category Percentage:")
print(product_category_percentage)


# EDA.20 — Product Pricing Analysis
print("\n====Product Pricing Analysis====")
print(products["Unit_Price"].describe())

print("\nProduct With Missing Prices:")
missing_price = products[products["Unit_Price"].isna()]
print(missing_price[["Product_ID", "Product_Name", "Product_Category", "Unit_Price"]])


# EDA.21 — Product Type Distribution
print("\n====Product Type Distribution====")
product_type_counts = products["Product_Type"].value_counts()
print("Product Type Counts:")
print(product_type_counts)

product_type_percentage = (products["Product_Type"].value_counts(normalize=True).mul(100).round(2))
print("\nProduct Type Percentage:")
print(product_type_percentage)


# EDA.22 — Pricing Model Distribution
print("\n====Pricing Model Distribution====")
pricing_model_counts = products["Pricing_Model"].value_counts()
print("Pricing Model Counts:")
print(pricing_model_counts)

pricing_model_percentage = (products["Pricing_Model"].value_counts(normalize=True).mul(100).round(2))
print("\nPricing Model Percentage:")
print(pricing_model_percentage)


# EDA.23 — Product Category Distribution
print("\n====Product Category Distribution====")
product_category_counts = products["Product_Category"].str.strip().str.title().value_counts()
print("Product Category Counts:")
print(product_category_counts)

product_category_percentage = products["Product_Category"].str.strip().str.title().value_counts(normalize=True).mul(100).round(2)
print("\nProduct Category Percentage:")
print(product_category_percentage)


# EDA.24 — Product Category × Product Type
# Which product types are offered within each product category?
print("\n====Product Category vs Product Type====")
category_type = pd.crosstab(products["Product_Category"].str.strip().str.lower(), products["Product_Type"].str.strip())
print("Category-Type Counts:")
print(category_type)


# EDA.25 — Product Category × Pricing Model
# Which pricing models are used within each product category?
print("\n====Product Category vs Pricing Model====")
category_model = pd.crosstab(products["Product_Category"].str.strip().str.lower(), products["Pricing_Model"].str.strip())
print("Category-Model Counts:")
print(category_model)




# # 1 — Data Cleaning & Validation
# 1.1 — Clean Customers Dataset
print("\n===== Customers ======")
print("\nBefore removing duplicates:", customers.shape)
customers = customers.drop_duplicates()
print("After removing duplicates:", customers.shape)


# 1.2 — Clean Customer Text Columns
print("\nCleaning Customers Text Columns:")
customers["Customer_Name"] = customers["Customer_Name"].str.strip().str.title()
customers["Company_Name"] = customers["Company_Name"].str.strip().str.title()
customers["Industry"] = customers["Industry"].str.strip().str.title()
customers["Company_Size"] = customers["Company_Size"].str.strip().str.title()
customers["Country"] = customers["Country"].str.strip().str.title()
customers["State"] = customers["State"].str.strip().str.title()
customers["City"] = customers["City"].str.strip().str.title()
customers["Customer_Segment"] = customers["Customer_Segment"].str.strip().str.title()
customers["Acquisition_Channel"] = customers["Acquisition_Channel"].str.strip().str.title()

print("Customer text columns cleaned successfully.")


# 1.3 — Handle Missing Customer Values
print("\nCustomer Missing Values:")
customer_missing = customers.isnull().sum()
print(customer_missing[customer_missing > 0])


# 1.4 — Inspect Records with Missing Values
print("\nCustomers With Missing State:")
missing_state = customers[customers["State"].isna()]
print(missing_state[["Customer_ID", "Customer_Name", "Country", "City", "State"]])
print("Total Missing State Records:", len(missing_state))

print("\nCustomers With Missing Acquisition Channel:")
missing_channel = customers[customers["Acquisition_Channel"].isna()]
print(missing_channel[["Customer_ID", "Customer_Name", "Industry", "Customer_Segment", "Acquisition_Channel"]])
print("Total Missing Acquisition_Channel Records:", len(missing_channel))


# 1.5 — Handle Missing Customer Values
print("\nHandling Customer Missing Values:")
customers["State"] = customers["State"].fillna("Unknown")
customers["Acquisition_Channel"] = customers["Acquisition_Channel"].fillna("Unknown")
print(customers[["State", "Acquisition_Channel"]].isnull().sum())


# 1.6 — Convert and Validate Signup_Date
print("\nConverting Signup Date:")
customers["Signup_Date"] = pd.to_datetime(customers["Signup_Date"], errors="coerce", dayfirst=True)
print("Data Type:", customers["Signup_Date"].dtype)
print("\nMissing Dates:", customers["Signup_Date"].isnull().sum())
print("\nMinimum Signup Date:", customers["Signup_Date"].min())
print("Maximum Signup Date:", customers["Signup_Date"].max())


# 1.7 — Validate Customer IDs
print("\nValidating Customer IDs:")
print("Missing Customer ID Values:", customers["Customer_ID"].isnull().sum())
print("Duplicate Customer ID Values:", customers["Customer_ID"].duplicated().sum())

print("\nTotal Customer Records:", len(customers))
print("Unique Customer ID Values:", customers["Customer_ID"].nunique())


# 1.8 — Final Customers Dataset Validation
print("\nFinal Customers Dataset Validation:")
print("Shape:", customers.shape)
print("\nMissing Values:\n", customers.isnull().sum())
print("\nData Types:\n", customers.dtypes)
print("\nDuplicate rows:", customers.duplicated().sum())



# 1.9 — Start Products Dataset Cleaning
print("\n===== Products =====")
print("\nProduct Duplicate Check:")
print("Before removing duplicates:", products.shape)

products = products.drop_duplicates()
print("After removing duplicates:", products.shape)

print("\nDuplicate Product ID Values:", products["Product_ID"].duplicated().sum())


# 1.10 — Clean Product Text Columns
print("\nCleaning Product Text Columns:")
products["Product_ID"] = products["Product_ID"].str.strip()
products["Product_Name"] = products["Product_Name"].str.strip().str.title()
products["Product_Category"] = products["Product_Category"].str.strip().str.lower()
products["Product_Type"] = products["Product_Type"].str.strip().str.title()
products["Pricing_Model"] = products["Pricing_Model"].str.strip()
products["Target_Segment"] = products["Target_Segment"].str.strip().str.title()

print("Product text columns cleaned successfully.")


# 1.11 — Convert Product Data Types
print("\nConverting Product Data Types:")
products["Unit_Price"] = pd.to_numeric(products["Unit_Price"], errors="coerce")
products["Launch_Date"] = pd.to_datetime(products["Launch_Date"], errors="coerce", dayfirst="True")

print("Unit Price Data Type:", products["Unit_Price"].dtypes)
print("Launch Date Data Type:", products["Launch_Date"].dtypes)

print("\nMissing Unit Price values:", products["Unit_Price"].isnull().sum())
print("Missing Launch Date Values:", products["Launch_Date"].isnull().sum())


# 1.12 — Inspect Products with Missing Prices
print("\nProducts with missing unit price:")
missing_prices = products[products["Unit_Price"].isna()]
print(missing_prices[["Product_ID", "Product_Name", "Product_Category", "Product_Type", "Pricing_Model", "Unit_Price"]])
print("\nTotal Products With Missing Prices:", len(missing_prices))


# 1.13 — Handle Missing Product Prices
print("\nCalculating Median Product Price:")
median_product_price = products["Unit_Price"].median()
print("Median Product Price:", median_product_price)

products["Unit_Price"] = products["Unit_Price"].fillna(median_product_price)
print("\nMissing Unit Price Values After Treatment:", products["Unit_Price"].isnull().sum())


# 1.14 — Validate Product IDs and Product Names
print("\nValidating Product Identifiers:")
print("Missing Product ID Values:", products["Product_ID"].isnull().sum())
print("Duplicate Product ID Values:", products["Product_ID"].duplicated().sum())
print("Missing Product Name Values:", products["Product_Name"].isnull().sum())

print("\nTotal Product Records:", len(products))
print("Unique Product ID Values:", products["Product_ID"].nunique())


# 1.15 — Final Products Dataset Validation
print("\nFinal Products Validation:")
print("Shape:", products.shape)

print("\nMissing Values:\n", products.isnull().sum())

print("\nData Types:\n", products.dtypes)

print("\nDuplicate rows:", products.duplicated().sum())



# 1.16 — Start Subscriptions Dataset Cleaning
print("\n===== Subscriptions =====")
print("\nSubscription Duplicate Check:")
print("Before removing duplicates:", subscriptions.shape)
subscriptions = subscriptions.drop_duplicates()
print("After removing duplicates:", subscriptions.shape)

print("\nDuplicate Subscription ID Values:", subscriptions["Subscription_ID"].duplicated().sum())


# 1.17 — Clean Subscription Text Columns
subscriptions["Subscription_ID"] = subscriptions["Subscription_ID"].str.strip()
subscriptions["Customer_ID"] = subscriptions["Customer_ID"].str.strip()
subscriptions["Product_ID"] = subscriptions["Product_ID"].str.strip()
subscriptions["Plan"] = subscriptions["Plan"].str.strip().str.title()
subscriptions["Billing_Cycle"] = subscriptions["Billing_Cycle"].str.strip().str.title()
subscriptions["Status"] = subscriptions["Status"].str.strip().str.title()
subscriptions["Auto_Renewal"] = subscriptions["Auto_Renewal"].str.strip().str.title()

print("\n", subscriptions.head())


# 1.18 — Check Missing Values in Subscriptions
print("\nSubscription Missing Values:")
print(subscriptions.isnull().sum())


# 1.19 — Analyze Missing End Dates by Status
print("\nMissing End Dates By Status:")
print(subscriptions.groupby("Status")["Subscription_End_Date"].apply(lambda x: x.isnull().sum()))


# 1.20 — Convert Subscription Date Columns
print("\nConverting Subscription Date Columns:")
subscriptions["Subscription_Start_Date"] = pd.to_datetime(subscriptions["Subscription_Start_Date"], errors="coerce", dayfirst=True)
subscriptions["Subscription_End_Date"] = pd.to_datetime(subscriptions["Subscription_End_Date"], errors="coerce", dayfirst=True)

print(subscriptions[["Subscription_Start_Date", "Subscription_End_Date"]].dtypes)

print("\nMissing Dates:")
print(subscriptions[["Subscription_Start_Date", "Subscription_End_Date"]].isnull().sum())


# 1.21 — Convert Numeric Columns
print("\nConverting Numeric Columns:")
numeric_columns = ["Monthly_Fee", "Discount", "Subscription_Duration_Days"]

for column in numeric_columns:
    subscriptions[column] = pd.to_numeric(subscriptions[column], errors="coerce")

print("Data Type:")
print(subscriptions[numeric_columns].dtypes)

print("\nMissing Numeric Values:")
print(subscriptions[numeric_columns].isnull().sum())


# 1.22 — Validate Subscription Financial Values
print("\nSubscription Financial Validation:")
print("Monthly Fee - Minimum:", subscriptions["Monthly_Fee"].min())
print("Monthly Fee - Maximum:", subscriptions["Monthly_Fee"].max())

print("\nDiscount - Minimum:", subscriptions["Discount"].min())
print("Discount - Maximum:", subscriptions["Discount"].max())

print("\nDiscount values greater than 100:", (subscriptions["Discount"] > 100).sum())


# 1.23 — Inspect Invalid Discount Records
print("\nInspect Invalid Discount Records:")

invalid_discounts = subscriptions[subscriptions["Discount"] > 100]

print(invalid_discounts[["Subscription_ID", "Monthly_Fee", "Discount", "Plan", "Billing_Cycle", "Status"]])


# 1.24 — Check Discount Distribution
print("\nDiscount Distribution:")
print(subscriptions["Discount"].value_counts().sort_index())


# 1.25 — Create Discount Validation Flag
print("\nCreate Invalid Discount Flag:")
subscriptions["Invalid_Discount_Flag"] = subscriptions["Discount"] > 100
print(subscriptions["Invalid_Discount_Flag"].value_counts())


# 1.26 — Validate Subscription Duration
print("\nSubscription Duration Validation:")
print("Minimum Duration:", subscriptions["Subscription_Duration_Days"].min())
print("Maximum Duration:", subscriptions["Subscription_Duration_Days"].max())

print("\nNegative Duration Count:", (subscriptions["Subscription_Duration_Days"] < 0).sum())


# 1.27 — Inspect Negative Subscription Durations
print("\nNegative Subscription Durations:")
negative_duration_records = subscriptions[subscriptions["Subscription_Duration_Days"] < 0]
print(negative_duration_records[["Subscription_ID", "Subscription_Start_Date", "Subscription_End_Date", "Subscription_Duration_Days", "Status", "Plan"]])


# 1.28 — Create Duration Validation Flag
print("\nCreate Invalid Duration Flag:")
subscriptions["Invalid_Duration_Flag"] = subscriptions["Subscription_Duration_Days"] < 0
print(subscriptions["Invalid_Duration_Flag"].value_counts())


# 1.29 — Check Subscription Date Consistency
print("\nSubscription Date Consistency:")
date_issue_count = (subscriptions["Subscription_End_Date"] < subscriptions["Subscription_Start_Date"]).sum()
print("End Date Before Start Date:", date_issue_count)


# 1.30 — Check Subscription Status Distribution
print("\nSubscription Status Distribution:")
print(subscriptions["Status"].value_counts())


# 1.31 — Compare Invalid Durations by Status
print("\nInvalid Durations By Status:")
print(subscriptions[subscriptions["Invalid_Duration_Flag"]]["Status"].value_counts())


# 1.32 — Create a Corrected Duration Column
subscriptions["Corrected_Duration_Days"] = (subscriptions["Subscription_End_Date"] - subscriptions["Subscription_Start_Date"]).dt.days
subscriptions.loc[subscriptions["Invalid_Duration_Flag"],"Corrected_Duration_Days"] = pd.NA

print("\nCorrected Duration Validation:")
print(subscriptions["Corrected_Duration_Days"].describe())

print("\nMissing corrected durations:")
print(subscriptions["Corrected_Duration_Days"].isnull().sum())


# 1.33 — Validate Corrected Duration Against Original Duration
print("\nValidate Corrected Duration:")
valid_duration_check = subscriptions[~subscriptions["Invalid_Duration_Flag"] & subscriptions["Subscription_Duration_Days"].notna()]
duration_difference = (valid_duration_check["Subscription_Duration_Days"] - valid_duration_check["Corrected_Duration_Days"])

print("Valid records checked:", len(valid_duration_check))
print("Records with duration differences:", (duration_difference != 0).sum())
print("Maximum absolute difference:", duration_difference.abs().max())


# 1.34 — Create the Final Duration Column
subscriptions["Final_Duration_Days"] = subscriptions["Corrected_Duration_Days"]
print("\nFinal Duration Validation:")
print("Missing Final Duration Values:", subscriptions["Final_Duration_Days"].isnull().sum())
print("Negative Final Duration Values:", (subscriptions["Final_Duration_Days"] < 0).sum())


# 1.35 — Validate Subscription ID and Customer/Product Relationships
print("\nSubscription ID Validation:")
print("Missing Subscription ID:", subscriptions["Subscription_ID"].isnull().sum())
print("Missing Customer ID:", subscriptions["Customer_ID"].isnull().sum())
print("Missing Product ID:", subscriptions["Product_ID"].isnull().sum())

print("\nUnique Subscription ID:", subscriptions["Subscription_ID"].nunique())
print("Unique Customer ID:", subscriptions["Customer_ID"].nunique())
print("Unique Product ID:", subscriptions["Customer_ID"].nunique())

print("\nsubscription ID format check:")
print(subscriptions["Subscription_ID"].str.startswith("S").value_counts())

print("\nCustomer ID format check:")
print(subscriptions["Customer_ID"].str.startswith("C").value_counts())

print("\nProduct ID format check:")
print(subscriptions["Product_ID"].str.startswith("P").value_counts())


# 1.36 — Check Referential Integrity
print("\nReferential Integrity Check:")
missing_customer_ids = set(subscriptions["Customer_ID"]) - set(customers["Customer_ID"])
missing_product_ids = set(subscriptions["Product_ID"]) - set(products["Product_ID"])

print("Customer ID not found in customers dataset:")
print(len(missing_customer_ids))
print("Product ID not found in products dataset:")
print(len(missing_product_ids))


# 1.37 — Display Missing Customer and Product IDs
print("\nMissing Customer And Product IDs:")
print("Missing Customer IDs:", missing_customer_ids)
print("Missing Product IDs:", missing_product_ids)


# 1.38 — Create Referential Integrity Flags
subscriptions["Missing_Customer_Flag"] = subscriptions["Customer_ID"].isin(missing_customer_ids)
subscriptions["Missing_Product_Flag"] = subscriptions["Product_ID"].isin(missing_product_ids)

print("\nReferential Integrity Flags:")
print("Subscriptions with missing customers:", subscriptions["Missing_Customer_Flag"].sum())
print("Subscriptions with missing products:", subscriptions["Missing_Product_Flag"].sum())


# 1.39 — Inspect Affected Subscription Records
print("\nMissing Customer Records:")
print(subscriptions[subscriptions["Missing_Customer_Flag"]][["Subscription_ID", "Customer_ID", "Product_ID", "Plan", "Status"]].head(10))

print("\nMissing Product Records:")
print(subscriptions[subscriptions["Missing_Product_Flag"]][["Subscription_ID", "Customer_ID", "Product_ID", "Plan", "Status"]].head(10))


# 1.40 — Count Records Affected by Either Missing Reference
print("\nUnmatched reference summary:")
subscriptions["Missing_Reference_Flag"] = subscriptions["Missing_Customer_Flag"] | subscriptions["Missing_Product_Flag"]
print("Subscriptions with either missing reference:", subscriptions["Missing_Reference_Flag"].sum())
print("Subscriptions with valid customer and product reference:", (~subscriptions["Missing_Reference_Flag"]).sum())


# 1.41 — Final Subscriptions Dataset Validation
print("\nFinal Subscription Validation:")
print("Shape:", subscriptions.shape)

print("\nMissing Values:")
print(subscriptions.isnull().sum())

print("\nDuplicate Rows:", subscriptions.duplicated().sum())

print("\nDuplicate Subscription ID Values:", subscriptions["Subscription_ID"].duplicated().sum())

print("\nInvalid Discount Records:", subscriptions["Invalid_Discount_Flag"].sum())

print("\nInvalid Duration Records:", subscriptions["Invalid_Duration_Flag"].sum())

print("\nUnmatched Reference Records:", subscriptions["Missing_Reference_Flag"].sum())



# 1.42 — Start Transactions Dataset Cleaning
print("\n===== Transactions =====")
print("\nTransaction Duplicate Check:")
print("Before removing duplicates:", transactions.shape)
transactions = transactions.drop_duplicates()
print("After removing duplicates:", transactions.shape)

print("\nDuplicate Transaction ID Values:", transactions["Transaction_ID"].duplicated().sum())


# 1.43 — Clean Transaction Text Columns
print("\nClean Transaction Text Columns:")
transactions["Transaction_ID"] = transactions["Transaction_ID"].str.strip()
transactions["Customer_ID"] = transactions["Customer_ID"].str.strip()
transactions["Subscription_ID"] = transactions["Subscription_ID"].str.strip()
transactions["Payment_Method"] = transactions["Payment_Method"].str.strip().str.title()
transactions["Transaction_Type"] = transactions["Transaction_Type"].str.strip().str.title()
transactions["Payment_Status"] = transactions["Payment_Status"].str.strip().str.title()
transactions["Sales_Channel"] = transactions["Sales_Channel"].str.strip().str.title()

print(transactions.head())


# 1.44 — Convert Transaction Date
print("\nConvert Transaction Date:")
transactions["Transaction_Date"] = pd.to_datetime(transactions["Transaction_Date"], errors="coerce", dayfirst=True)

print("\nTransaction Date Validation:")
print("Data Type:", transactions["Transaction_Date"].dtypes)
print("Missing Transaction Date:", transactions["Transaction_Date"].isnull().sum())
print("Minimum Transaction Date:", transactions["Transaction_Date"].min())
print("Maximum Transaction Date:", transactions["Transaction_Date"].max())


# 1.45 — Convert Numeric Columns
print("\nConvert Numeric Columns:")
numeric_columns = ["Amount", "Discount"]

for column in numeric_columns:
    transactions[column] = pd.to_numeric(transactions[column], errors="coerce")

print("\nTransaction Numeric Validation:")
print("Data Type:")
print(transactions[["Amount", "Discount"]].dtypes)
print("\nMissing Value:")
print(transactions[["Amount", "Discount"]].isnull().sum())
print("\nMinimum:")
print(transactions[["Amount", "Discount"]].min())
print("\nMaximum:")
print(transactions[["Amount", "Discount"]].max())


# 1.46 — Inspect Negative Transaction Amounts
print("\nNegative Transaction Amount Analysis:")
negative_amounts = transactions[transactions["Amount"] < 0]

print("Total Negative Amount Records:", len(negative_amounts))

print("\nNegative Amount By Transaction Type:")
print(negative_amounts["Transaction_Type"].value_counts())

print("\nNegative Amount By Payment Status:")
print(negative_amounts["Payment_Status"].value_counts())

print("\nSample Negative Amount Records:")
print(negative_amounts[["Transaction_ID", "Customer_ID", "Subscription_ID", "Transaction_Type", "Amount", "Payment_Status"]].head(10))


# 1.47 — Create Suspicious Negative Amount Flag
print("\nCreate Suspicious Negative Amount Flag:")
transactions["Suspicious_Negative_Amount_Flag"] = (transactions["Amount"] < 0) & (transactions["Transaction_Type"] != "Refund")

print("\nSuspicious Negative Amount Flag:")
print(transactions["Suspicious_Negative_Amount_Flag"].value_counts())

print("\nSuspicious Negative Transactions:", transactions["Suspicious_Negative_Amount_Flag"].sum())


# 1.48 — Standardize Payment_Method
print("\nPayment Method Standardization")
print("Payment Method Before Standardization:")
print(transactions["Payment_Method"].value_counts())


# 1.49 — Standardize UPI
transactions["Payment_Method"] = transactions["Payment_Method"].replace({"Upi" : "UPI"})

print("\nPayment Method After Standardization:")
print(transactions["Payment_Method"].value_counts())


# 1.50 — Validate Transaction IDs
print("\nTransaction ID Validation:")
print("Missing Transaction IDs:", transactions["Transaction_ID"].isnull().sum())

print("Duplicate Transaction IDs:", transactions["Transaction_ID"].duplicated().sum())

print("Total Transactions:", len(transactions))

print("Unique Transaction IDs:", transactions["Transaction_ID"].nunique())

print("\nMissing Customer IDs:", transactions["Customer_ID"].isnull().sum())

print("Missing Subscription IDs:", transactions["Subscription_ID"].isnull().sum())


# 1.51 — Check Transaction References
print("\nTransaction Referential Integrity:")
missing_transaction_customers = set(transactions["Customer_ID"]) - set(customers["Customer_ID"])
missing_transaction_subscriptions = set(transactions["Subscription_ID"]) - set(transactions["Subscription_ID"])

print("Missing Customer IDs:", len(missing_transaction_customers))
print("Missing Subscription IDs:", len(missing_transaction_subscriptions))

print("\nMissing Customer ID Values:", missing_transaction_customers)

print("Missing Subscription ID Value:", missing_transaction_subscriptions)


# 1.52 — Create Missing Customer Reference Flag
transactions["Missing_Customer_Flag"] = (~ transactions["Customer_ID"].isin(customers["Customer_ID"]))
print("\n", transactions["Missing_Customer_Flag"].value_counts())

print("\nTransaction with Missing Customer Reference:", transactions["Missing_Customer_Flag"].sum())


# 1.53 — Inspect the Unmatched Customer Transactions
print("\nUnmatched Customer Transactions")
unmatched_customer_transactions = transactions[transactions["Missing_Customer_Flag"]==True]

print("Total Unmatched Transactions:", len(unmatched_customer_transactions))

print("\nTransaction Types:")
print(unmatched_customer_transactions["Transaction_Type"].value_counts())

print("\nPayment Status:")
print(unmatched_customer_transactions["Payment_Status"].value_counts())

print("\nSample Records:")
print(unmatched_customer_transactions[["Transaction_ID", "Customer_ID", "Subscription_ID", "Transaction_Type", "Amount", "Payment_Status", "Sales_Channel"]].head(10))


# 1.54 — Create a Transaction Data-Quality Summary
print("\nTransaction Data Quality Summary")
print("Total Transactions:", len(transactions))

print("Missing Transaction Dates:", transactions["Transaction_Date"].isnull().sum())

print("Suspicious Negative Amounts:", transactions["Suspicious_Negative_Amount_Flag"].sum())

print("Missing Customer Reference:", transactions["Missing_Customer_Flag"].sum())

print("Missing Subscription References:", (~transactions["Subscription_ID"].isin(subscriptions["Subscription_ID"])).sum())


# 1.55 — Inspect Unmatched Subscription Transactions
print("\nUnmatched Subscription Transactions")
unmatched_subscription_transactions = transactions[~transactions["Subscription_ID"].isin(subscriptions["Subscription_ID"])]

print("Total Unmatched Subscription Transactions:", len(unmatched_subscription_transactions))

print("\nUnmatched Subscription IDs:")
print(unmatched_subscription_transactions["Subscription_ID"].value_counts())

print("\nSample Records:")
print(unmatched_subscription_transactions[["Transaction_ID", "Customer_ID", "Subscription_ID", "Transaction_Type", "Amount", "Payment_Status", "Sales_Channel"]].head(10))


# 1.56 — Create Missing Subscription Reference Flag
print("\nMissing Subscription Reference Flag")
transactions["Missing_Subscription_Flag"] = (~transactions["Subscription_ID"].isin(subscriptions["Subscription_ID"]))

print("\n", transactions["Missing_Subscription_Flag"].value_counts())

print("\nTransaction With Missing Subscription Reference:", transactions["Missing_Subscription_Flag"].sum())


# 1.57 — Create Overall Transaction Data-Quality Flag
print("\nOverall Transaction Data Quality Flag")
transactions["Data_Quality_Issue_Flag"] = (transactions["Transaction_Date"].isnull() | transactions["Suspicious_Negative_Amount_Flag"] | transactions["Missing_Customer_Flag"] | transactions["Missing_Subscription_Flag"])

print("\n", transactions["Data_Quality_Issue_Flag"].value_counts())

print("\nTransactions With at least one data-quality issue:", transactions["Data_Quality_Issue_Flag"].sum())


# 1.58 — Final Transaction Validation
print("\nFINAL TRANSACTION VALIDATION")

print("Shape:", transactions.shape)

print("\nMissing Values:")
print(transactions.isnull().sum())

print("\nDuplicate Rows:", transactions.duplicated().sum())

print("\nDuplicate Transaction_ID:", transactions["Transaction_ID"].duplicated().sum())

print("\nData Quality Issues:", transactions["Data_Quality_Issue_Flag"].sum())

print("\nSuspicious Negative Amounts:", transactions["Suspicious_Negative_Amount_Flag"].sum())

print("\nMissing Customer References:", transactions["Missing_Customer_Flag"].sum())

print("\nMissing Subscription References:", transactions["Missing_Subscription_Flag"].sum())



# 1.59 Start Support Tickets Dataset Cleaning
print("\n===== Support Ticket Duplicate Check =====")
print("Before removing duplicates", support_tickets.shape)
support_tickets = support_tickets.drop_duplicates()
print("After removing duplicates:", support_tickets.shape)

print("\nDuplicate Ticket ID Values:", support_tickets.duplicated().sum())


# 1.60 — Inspect Support Ticket Columns
print("\nSupport Ticket Columns:")
print(support_tickets.columns.tolist())

print("\nSample Support Tickets:")
print(support_tickets.head())


# 1.61 — Clean Support Ticket Text Columns
support_tickets["Ticket_ID"] = support_tickets["Ticket_ID"].str.strip()
support_tickets["Customer_ID"] = support_tickets["Customer_ID"].str.strip()
support_tickets["Subscription_ID"] = support_tickets["Subscription_ID"].str.strip()
support_tickets["Issue_Category"] = support_tickets["Issue_Category"].str.strip().str.title()
support_tickets["Priority"] = support_tickets["Priority"].str.strip().str.title()
support_tickets["Ticket_Status"] = support_tickets["Ticket_Status"].str.strip().str.title()
support_tickets["Agent_ID"] = support_tickets["Agent_ID"].str.strip().str.title()

print("\nCleaned Support Ticket Text Columns:")
print(support_tickets[["Ticket_ID", "Customer_ID", "Subscription_ID", "Issue_Category", "Priority", "Ticket_Status", "Agent_ID"]].head())


# 1.62 — Convert Ticket_Date to Datetime
print("\nConvert Ticket Date to Datetime")
support_tickets["Ticket_Date"] = pd.to_datetime(support_tickets["Ticket_Date"], errors="coerce", dayfirst=True)

print("\nSupport Ticket Date Validation:")
print("Data Type:", support_tickets["Ticket_Date"].dtypes)
print("Missing Ticket Date:", support_tickets["Ticket_Date"].isnull().sum())
print("Minimum Ticket Date:", support_tickets["Ticket_Date"].min())
print("Maximum Ticket Date:", support_tickets["Ticket_Date"].max())


# 1.63 — Convert Numeric Columns
numeric_columns = ["Resolution_Time_Hours", "Satisfaction_Score"]

for columns in numeric_columns:
    support_tickets[columns] = pd.to_numeric(support_tickets[columns], errors="coerce")

print("\nSupport Ticket Numeric Validation:")
for columns in numeric_columns:
    print(f"\n{columns}")
    print("Data Type:", support_tickets[columns].dtypes)
    print("Missing Values:", support_tickets[columns].isnull().sum())
    print("Minimum:", support_tickets[columns].min())
    print("Maximum:", support_tickets[columns].max())


# 1.64 — Analyze Negative Resolution Times
print("\nNegative Resolution Time Analysis")
negative_resolution = support_tickets[support_tickets["Resolution_Time_Hours"] < 0]

print("Negative Resolution Time Records:", len(negative_resolution))

print("\nNegative Resolution Time by Ticket Status:")
print(negative_resolution["Ticket_Status"].value_counts())

print("\nNegative Resolution Time by Priority:")
print(negative_resolution["Priority"].value_counts())

print("\nSample Negative Resolution Records:")
print(negative_resolution[["Ticket_ID", "Customer_ID", "Subscription_ID", "Issue_Category", "Priority", "Resolution_Time_Hours", "Satisfaction_Score", "Ticket_Status"]].head(10))


# 1.65 — Create Invalid Resolution Time Flag
print("\nCreate Invalid Resolution Time Flag")
support_tickets["Invalid_Resolution_Time_Flag"] = support_tickets["Resolution_Time_Hours"] < 0

print("\n", support_tickets["Invalid_Resolution_Time_Flag"].value_counts())

print("\nInvalid Resolution Time Records:", support_tickets["Invalid_Resolution_Time_Flag"].sum())


# 1.66 — Analyze Missing Satisfaction Scores
print("\nMissing Satisfaction Score Analysis")
missing_satisfaction = support_tickets[support_tickets["Satisfaction_Score"].isnull()]

print("Missing Satisfaction Scores:", len(missing_satisfaction))

print("\nMissing Satisfaction Scores by Ticket Status:")
print(missing_satisfaction["Ticket_Status"].value_counts())

print("\nMissing Satisfaction Scores by Priority:")
print(missing_satisfaction["Priority"].value_counts())

print("\nSample Records:")
print(missing_satisfaction[["Ticket_ID", "Customer_ID", "Issue_Category", "Priority", "Resolution_Time_Hours", "Satisfaction_Score", "Ticket_Status"]].head(10))


# 1.67 — Create Missing Satisfaction Flag
print("\nCreate Missing Satisfaction Flag")
support_tickets["Missing_Satisfaction_Flag"] = support_tickets["Satisfaction_Score"].isnull()

print("\nMissing Satisfaction Flag:")
print(support_tickets["Missing_Satisfaction_Flag"].value_counts())

print("\nMissing Satisfaction Records:", support_tickets["Missing_Satisfaction_Flag"].sum())


# 1.68 — Validate Satisfaction Score Range
print("Satisfaction Score Range Validation")
invalid_satisfaction = support_tickets[(support_tickets["Satisfaction_Score"] < 1) | (support_tickets["Satisfaction_Score"] > 5)]

print("\nInvalid Satisfaction Score Records:", len(invalid_satisfaction))

print("\nInvalid Satisfaction Scores:")
print(invalid_satisfaction.value_counts())

print("\nValid Satisfaction Score Distribution:")
print(support_tickets["Satisfaction_Score"].value_counts().sort_index())


# 1.69 — Validate Ticket IDs
print("\nSupport Ticket ID Validation")
print("Missing Ticket ID:", support_tickets["Ticket_ID"].isnull().sum())

print("Duplicate Ticket ID:", support_tickets["Ticket_ID"].duplicated().sum())

print("Total Ticket ID:", len(support_tickets))

print("Unique Ticket IDs:", support_tickets["Ticket_ID"].nunique())


# 1.70 — Check Customer & Subscription References
print("\nSupport Ticket Reference Validation")
missing_ticket_customers = set(support_tickets["Customer_ID"]) - (set(customers["Customer_ID"]))
missing_ticket_subscriptions = set(support_tickets["Subscription_ID"]) - set(subscriptions["Subscription_ID"])

print("Missing Customer IDs:", len(missing_ticket_customers))
print("Missing Subscription IDs:", len(missing_ticket_subscriptions))

print("\nMissing Customer IDs:")
print(missing_ticket_customers)
print("Missing Subscription IDs:")
print(missing_ticket_subscriptions)


# 1.71 — Create Reference Quality Flags
print("\nSupport Ticket Reference Flag")
support_tickets["Missing_Customer_Flag"] = (~support_tickets["Customer_ID"].isin(customers["Customer_ID"]))
support_tickets["Missing_Subscription_Flag"] = (~support_tickets["Subscription_ID"].isin(subscriptions["Subscription_ID"]))

print("Missing Customer Reference Records:", support_tickets["Missing_Customer_Flag"].sum())
print("Missing Subscription Reference Records:", support_tickets["Missing_Subscription_Flag"].sum())


# 1.72 — Create Overall Reference Issue Flag
print("\nSupport Ticket Reference Quality")
support_tickets["Reference_Quality_Issue_Flag"] = (support_tickets["Missing_Customer_Flag"] | support_tickets["Missing_Subscription_Flag"])

print(support_tickets["Reference_Quality_Issue_Flag"].value_counts())
print("\n",support_tickets["Reference_Quality_Issue_Flag"].sum())


# 1.73 — Analyze Reference Issues
print("\nReference Issue Analysis:")
both_invalid = support_tickets[(support_tickets["Missing_Customer_Flag"]) & (support_tickets["Missing_Subscription_Flag"])]

customer_only = support_tickets[(support_tickets["Missing_Customer_Flag"]) & (~support_tickets["Missing_Subscription_Flag"])]

subscription_only = support_tickets[(~support_tickets["Missing_Customer_Flag"]) & (support_tickets["Missing_Subscription_Flag"])]

print("Both Customer & Subscription Invalid:", len(both_invalid))
print("Customer Reference Only:", len(customer_only))
print("Subscription Reference Only:", len(subscription_only))
print("Total Reference-Issue Tickets:", len(both_invalid) + len(customer_only) + len(subscription_only))


# 1.74 — Create Overall Support Ticket Data-Quality Flag
print("\nSupport Ticket Data Quality")
support_tickets["Data_Quality_Issue_Flag"] = support_tickets["Invalid_Resolution_Time_Flag"] | support_tickets["Missing_Satisfaction_Flag"] | support_tickets["Missing_Customer_Flag"] | support_tickets["Missing_Subscription_Flag"]

print(support_tickets["Data_Quality_Issue_Flag"].value_counts())

print("\nTotal Tickets With Data Quality Issue:", support_tickets["Data_Quality_Issue_Flag"].sum())

print("\nTotal Clean Tickets:", (~support_tickets["Data_Quality_Issue_Flag"]).sum())


# 1.75 — Final Support Ticket Validation
print("\nFinal Support Ticket Validation")
print("Shape:", support_tickets.shape)

print("\nMissing Values:")
print(support_tickets.isnull().sum())

print("\nDuplicate Rows:", support_tickets.duplicated().sum())

print("Duplicate Ticket ID:", support_tickets["Ticket_ID"].duplicated().sum())

print("\nData Quality Issues:", support_tickets["Data_Quality_Issue_Flag"].sum())

print("Invalid Resolution Time:", support_tickets["Invalid_Resolution_Time_Flag"].sum())

print("Missing Satisfaction Scores:", support_tickets["Missing_Satisfaction_Flag"].sum())

print("Missing Customer References:", support_tickets["Missing_Customer_Flag"].sum())

print("Missing Subscription References:", support_tickets["Missing_Subscription_Flag"].sum())




# # 2 — Create Customer Subscription Summary
# 2.1 - Calculate subscription counts
print("\n===== Customer Subscription Summary =====")
customer_subscription_summary = (subscriptions.groupby("Customer_ID").agg(
                                                                            Total_Subscriptions=("Subscription_ID", "count"), 
                                                                            Active_Subscriptions=("Status", lambda x: (x == "Active").sum()), 
                                                                            Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()), 
                                                                            Expired_Subscriptions=("Status", lambda x: (x == "Expired").sum()),
                                                                            Paused_Subscriptions=("Status", lambda x: (x == "Paused").sum())
                                                                            ).reset_index())

print(customer_subscription_summary.head(10))
print("\nShape:", customer_subscription_summary.shape)


# 2.2 — Add Subscription Financial Metrics
print("\n===== Customer Subscription Financial Summary =====")
financial_summary = (subscriptions.groupby("Customer_ID").agg(Total_Subscription_Fee=("Monthly_Fee", "sum"),
                                                            Average_Monthly_Fee=("Monthly_Fee", "mean"),
                                                            Total_Discount=("Discount", "sum"),
                                                            Average_Discount=("Discount", "mean")
).reset_index())

customer_subscription_summary = customer_subscription_summary.merge(financial_summary, on="Customer_ID", how="left")

print(customer_subscription_summary.head(10))

print("\nShape:", customer_subscription_summary.shape)


# 2.3 — Validate Customer Subscription Summary
print("\n===== Customer Subscription Summary Validation =====")
print("Shape:", customer_subscription_summary.shape)

print("\nColumns:")
print(customer_subscription_summary.columns.tolist())

print("\nMissing Values:")
print(customer_subscription_summary.isnull().sum())

print("\nDuplicate Customer IDs:", customer_subscription_summary.duplicated().sum())


# 2.4 — Add Subscription Duration Metrics
print("\n===== Customer Subscription Duration Summary =====")
duration_summary = (subscriptions.groupby("Customer_ID").agg(
                                                           Average_Subscription_Days=("Final_Duration_Days", "mean"),
                                                           Maximum_Subscription_Days=("Final_Duration_Days", "max"),
                                                           Minimum_Subscription_Days=("Final_Duration_Days", "min")
).reset_index())

customer_subscription_summary = customer_subscription_summary.merge(duration_summary, on="Customer_ID", how="left")

print(customer_subscription_summary.head(10))

print("\nShape:", customer_subscription_summary.shape)


# 2.5 — Calculate Customer Cancellation Rate
print("\n===== Customer Cancellation Rate =====")
customer_subscription_summary["Cancellation_Rate"] = (customer_subscription_summary["Cancelled_Subscriptions"] / customer_subscription_summary["Total_Subscriptions"] * 100)

print(customer_subscription_summary[["Customer_ID", "Total_Subscriptions", "Cancelled_Subscriptions", "Cancellation_Rate"]].head(10))

print("\nShape:", customer_subscription_summary.shape)


# 2.6 — Create Customer Subscription Active Rate
print("\n===== Customer Active Rate =====")
customer_subscription_summary["Active_Rate"] = customer_subscription_summary["Active_Subscriptions"] / customer_subscription_summary["Total_Subscriptions"] * 100

print(customer_subscription_summary[["Customer_ID", "Total_Subscriptions", "Active_Subscriptions", "Active_Rate"]].head(10))

print("\nShape:", customer_subscription_summary.shape)


# 2.7 — Create Subscription Revenue Estimate
print("\n===== Net Monthly Subscription Fee =====")
subscriptions["Net_Monthly_Fee"] = subscriptions["Monthly_Fee"] * (1 - subscriptions["Discount"] / 100)

subscriptions.loc[subscriptions["Invalid_Discount_Flag"],"Net_Monthly_Fee"] = pd.NA

print(subscriptions[["Subscription_ID", "Monthly_Fee", "Discount", "Net_Monthly_Fee"]].head(10))

print("\nMissing Net Monthly Fees:", subscriptions["Net_Monthly_Fee"].isnull().sum())

print("\nNegative Net Monthly Fees:", (subscriptions["Net_Monthly_Fee"] < 0).sum())


# 2.8 — Add Net Subscription Fee to Customer Summary
print("\n===== Customer Net Subscription Fee Summary =====")
net_fee_summary = subscriptions.groupby("Customer_ID").agg(Total_Net_Monthly_Fee=("Net_Monthly_Fee", "sum"),
                                                           Average_Net_Monthly_Fee=("Net_Monthly_Fee", "mean")).reset_index()

customer_subscription_summary = customer_subscription_summary.merge(net_fee_summary, on="Customer_ID", how="left")

print(customer_subscription_summary[["Customer_ID", "Total_Subscriptions", "Total_Subscription_Fee", "Total_Net_Monthly_Fee", "Average_Net_Monthly_Fee"]].head(10))

print("\nShape:", customer_subscription_summary.shape)


# 2.9 — Create Customer Subscription Value
print("\n===== Customer Subscription Value =====")
customer_subscription_summary["Subscription_Value_Percentage"] = customer_subscription_summary["Total_Net_Monthly_Fee"] / customer_subscription_summary["Total_Subscription_Fee"] * 100

print(customer_subscription_summary[["Customer_ID", "Total_Subscription_Fee", "Total_Net_Monthly_Fee", "Subscription_Value_Percentage"]].head(10))

print("\nShape:", customer_subscription_summary.shape)


# 2.10 — Validate Subscription Value Percentage
print("\n===== Subscription Value Validation =====")
invalid_value_percentage = customer_subscription_summary[(customer_subscription_summary["Subscription_Value_Percentage"] < 0) | (customer_subscription_summary["Subscription_Value_Percentage"] > 100)]

print("Invalid Subscription Value Records:", len(invalid_value_percentage))

print("Missing Subscription Value Records:", customer_subscription_summary["Subscription_Value_Percentage"].isna().sum())

print("Minimum Value:", customer_subscription_summary["Subscription_Value_Percentage"].min())

print("Maximum Value:", customer_subscription_summary["Subscription_Value_Percentage"].max())


# 2.11 — Merge Customer Information
print("\n===== Customer Subscription + Customer Profile =====")
customer_subscription_summary = customer_subscription_summary.merge(customers[[
                                                                    "Customer_ID",
                                                                    "Customer_Name", 
                                                                    "Company_Name",
                                                                    "Industry",
                                                                    "Company_Size",
                                                                    "Country", 
                                                                    "State",
                                                                    "City",
                                                                    "Customer_Segment",
                                                                    "Acquisition_Channel"
                                                                    ]],
                                                                    on="Customer_ID",
                                                                    how="left")

print(customer_subscription_summary.head(10))

print("\nShape:", customer_subscription_summary.shape)

print("\nMissing Values:")
print(customer_subscription_summary.isnull().sum())


# 2.12 — Investigate missing customer profile
print("\n===== Missing Customer Profile =====")
missing_profile = customer_subscription_summary[customer_subscription_summary["Customer_Name"].isnull()]

print(missing_profile[["Customer_ID", "Total_Subscriptions", "Total_Subscription_Fee", "Total_Net_Monthly_Fee"]])
print("\nCount:", len(missing_profile))


print("\n===== Missing Net Monthly Fee =====")
missing_net_fee = customer_subscription_summary[customer_subscription_summary["Average_Net_Monthly_Fee"].isnull()]

print(missing_net_fee[["Customer_ID", "Total_Subscriptions", "Total_Subscription_Fee", "Total_Net_Monthly_Fee", "Average_Net_Monthly_Fee"]])
print("\nCount:", len(missing_net_fee))


# 2.13 — Correct the all-invalid net-fee aggregation
net_fee_summary = (subscriptions.groupby("Customer_ID").agg(Total_Net_Monthly_Fee=("Net_Monthly_Fee", "sum"),
                                                           Average_Net_Monthly_Fee=("Net_Monthly_Fee", "mean")).reset_index())

# Keep Total_Net_Monthly_Fee as NaN when all subscription fees are invalid
valid_net_fee_count = (subscriptions.groupby("Customer_ID")["Net_Monthly_Fee"].count().reset_index(name="Valid_Net_Fee_Count"))

net_fee_summary = net_fee_summary.merge(valid_net_fee_count, on="Customer_ID", how="left")

net_fee_summary.loc[net_fee_summary["Valid_Net_Fee_Count"] == 0, "Total_Net_Monthly_Fee"] = pd.NA

net_fee_summary = net_fee_summary.drop(columns="Valid_Net_Fee_Count")


# Update customer summary
customer_subscription_summary = customer_subscription_summary.drop(columns=["Total_Net_Monthly_Fee", "Average_Net_Monthly_Fee"])

customer_subscription_summary = customer_subscription_summary.merge(net_fee_summary, on="Customer_ID", how="left")

print("\n===== Net Fee Validation =====")
print(customer_subscription_summary[customer_subscription_summary["Average_Net_Monthly_Fee"].isnull()][["Customer_ID",
                                                                                                        "Total_Subscriptions",
                                                                                                        "Total_Subscription_Fee",
                                                                                                        "Total_Net_Monthly_Fee",
                                                                                                        "Average_Net_Monthly_Fee"]])

print("\nMissing Total Net Monthly Fee:", customer_subscription_summary["Total_Net_Monthly_Fee"].isnull().sum())

print("\nMissing Average Net Monthly Fee:", customer_subscription_summary["Average_Net_Monthly_Fee"].isnull().sum())


# 2.14 — Final validation of Customer Subscription Summary
print("\n===== Customer Subscription Summary Validation =====")
print("\nShape:", customer_subscription_summary.shape)

print("\nDuplicate Customer IDs:", customer_subscription_summary.duplicated().sum())

print("\nMissing Values:")
print(customer_subscription_summary.isnull().sum())

print("\nCancellation Rate Range:", customer_subscription_summary["Cancellation_Rate"].min(), "to", customer_subscription_summary["Cancellation_Rate"].max())

print("\nActive Rate Range:", customer_subscription_summary["Active_Rate"].min(), "to", customer_subscription_summary["Active_Rate"].max())

print("\nSubscription Value Percentage Range:", customer_subscription_summary["Subscription_Value_Percentage"].min(), "to", customer_subscription_summary["Subscription_Value_Percentage"].max())


# 2.15 — Customer Transaction Summary
print("\n===== Customer Transaction Summary =====")
customer_transaction_summary = (transactions.groupby("Customer_ID").agg(Total_Transactions=("Transaction_ID", "count"),
                                                                        Paid_Transactions=("Payment_Status", lambda x: (x == "Paid").sum()),
                                                                        Failed_Transactions=("Payment_Status", lambda x: (x == "Failed").sum()),
                                                                        Pending_Transactions=("Payment_Status", lambda x: (x == "Pending").sum()),
                                                                        Refunded_Transactions=("Payment_Status", lambda x: (x == "Refunded").sum()),
                                                                        Total_Transaction_Amount=("Amount", "sum"),
                                                                        Average_Transaction_Amount=("Amount", "mean"),
                                                                        Total_Transaction_Discount=("Discount", "sum"),
                                                                        Refund_Count=("Transaction_Type", lambda x: (x == "Refund").sum()),
                                                                        Suspicious_Negative_Count = ("Suspicious_Negative_Amount_Flag", "sum"))).reset_index()

print(customer_transaction_summary.head(10))

print("\nShape:", customer_transaction_summary.shape)


# 2.16 — Validate Customer Transaction Summary
print("\n===== Customer Transaction Summary Validation =====")
print("\n Shape:", customer_transaction_summary.shape)

print("\nDuplicate Customer IDs:", customer_transaction_summary["Customer_ID"].duplicated().sum())

print("\nMissing_Values:")
print(customer_transaction_summary.isnull().sum())

print("\nTotal Transactions Range:", customer_transaction_summary["Total_Transactions"].min(), "to", customer_transaction_summary["Total_Transactions"].max())

print("\nTotal Transaction Amount Range:", customer_transaction_summary["Total_Transaction_Amount"].min(), "to", customer_transaction_summary["Total_Transaction_Amount"].max())

print("\nRefund Count Range:", customer_transaction_summary["Refund_Count"].min(), "to", customer_transaction_summary["Refund_Count"].max())

print("\nSuspicious Negative Count:", customer_transaction_summary["Suspicious_Negative_Count"].sum())


# 2.17 — Merge Transaction Metrics
print("\n===== Customer Subscription + Transaction Summary =====")
customer_subscription_summary = customer_subscription_summary.merge(customer_transaction_summary, on="Customer_ID", how="left")
print(customer_subscription_summary.head(10))

print("\nshape:", customer_subscription_summary.shape)

print("\nMissing Values:")
print(customer_subscription_summary.isnull().sum())


# 2.18 — Handle Customers With No Transactions
print("\n===== Customers Without Transactions =====")
customers_without_transactions = customer_subscription_summary[customer_subscription_summary["Total_Transactions"].isnull()]
print(customers_without_transactions[["Customer_ID", "Total_Subscriptions", "Active_Subscriptions", "Cancelled_Subscriptions", "Total_Subscription_Fee"]])

print("\nCount:", len(customers_without_transactions))


# 2.19 — Fill Transaction Metrics for No-Transaction Customers
transaction_columns = ["Total_Transactions", "Paid_Transactions", "Failed_Transactions", "Pending_Transactions", "Refunded_Transactions", "Total_Transaction_Amount", "Average_Transaction_Amount", "Total_Transaction_Discount", "Refund_Count", "Suspicious_Negative_Count"]

customer_subscription_summary[transaction_columns] = customer_subscription_summary[transaction_columns].fillna(0)

print("\n===== Transaction Metrics After Filling =====")
print(customer_subscription_summary[transaction_columns].isnull().sum())

print("\nCustomers with zero transactions:", (customer_subscription_summary["Total_Transactions"] == 0).sum())


# 2.20 — Create Transaction Performance Metrics
print("\n===== Transaction Performance Metrics =====")
customer_subscription_summary["Transaction_Success_Rate"] = (customer_subscription_summary["Paid_Transactions"] / customer_subscription_summary["Total_Transactions"] * 100).fillna(0)

customer_subscription_summary["Refund_Rate"] = (customer_subscription_summary["Refund_Count"] / customer_subscription_summary["Total_Transactions"] * 100).fillna(0)

customer_subscription_summary["Average_Paid_Transaction_Amount"] = (customer_subscription_summary["Total_Transaction_Amount"] / customer_transaction_summary["Paid_Transactions"]).replace([float("inf"), -float("inf")],pd.NA)

customer_subscription_summary["Suspicious_Transaction_Rate"] = (customer_subscription_summary["Suspicious_Negative_Count"] / customer_subscription_summary["Total_Transactions"] * 100).fillna(0)

print(customer_subscription_summary[["Customer_ID", "Total_Transactions", "Paid_Transactions", "Transaction_Success_Rate", "Refund_Count", "Refund_Rate", "Average_Paid_Transaction_Amount", "Suspicious_Transaction_Rate"]].head(10))


# 2.21 — Validate Transaction Performance Metrics
print("\n===== Transaction Performance Validation =====")
print(customer_subscription_summary[["Transaction_Success_Rate", "Refund_Rate", "Average_Paid_Transaction_Amount", "Suspicious_Transaction_Rate"]].describe())

print("\nMissing Values:")
print(customer_subscription_summary[["Transaction_Success_Rate", "Refund_Rate", "Average_Paid_Transaction_Amount", "Suspicious_Transaction_Rate"]].isnull().sum())

print("\nRate Ranges:")
print("Transaction Success Rate:", customer_subscription_summary["Transaction_Success_Rate"].min(), "to", customer_subscription_summary["Transaction_Success_Rate"].max())
print("Refund Rate:", customer_subscription_summary["Refund_Rate"].min(), "to", customer_subscription_summary["Refund_Rate"].max())
print("Suspicious Transaction Rate:", customer_subscription_summary["Suspicious_Transaction_Rate"].min(), "to", customer_subscription_summary["Suspicious_Transaction_Rate"].max())


# 2.22 — Customer Support Ticket Summary
print("\n===== Customer Support Summary =====")
customer_support_summary = (support_tickets.groupby("Customer_ID").agg(Total_Tickets=("Ticket_ID", "count"),
                                                                       Resolved_Tickets=("Ticket_Status", lambda x: (x =="Resolved").sum()),
                                                                       Closed_Tickets=("Ticket_Status", lambda x: (x =="Closed").sum()),
                                                                       Open_Tickets=("Ticket_Status", lambda x: (x =="Open").sum()),
                                                                       In_Progress_Tickets=("Ticket_Status", lambda x: (x =="In Progress").sum()),
                                                                       Average_Resolution_Time_Hours=("Resolution_Time_Hours", lambda x: x[x >= 0].mean()),
                                                                       Average_Satisfaction_Score=("Satisfaction_Score", "mean"),
                                                                       High_Critical_Tickets=("Priority", lambda x: ((x=="High") | (x=="Critical")).sum()),
                                                                       Invalid_Resolution_Count=("Invalid_Resolution_Time_Flag", "sum"),
                                                                       Missing_Satisfaction_Count=("Missing_Satisfaction_Flag", "sum")).reset_index())

print(customer_support_summary.head(10))

print("\nShape:", customer_support_summary.shape)


# 2.23 — Validate Customer Support Summary
print("\n===== Customer Support Summary Validation =====")
print("\nShape:", customer_support_summary.shape)

print("\nDuplicate Customer IDs:", customer_support_summary["Customer_ID"].duplicated().sum())

print("\nMissing Values:")
print(customer_support_summary.isnull().sum())

print("\nTotal Tickets Range:", customer_support_summary["Total_Tickets"].min(), "to", customer_support_summary["Total_Tickets"].max())

print("\nAverage Satisfaction Score Range:", customer_support_summary["Average_Satisfaction_Score"].min(), "to", customer_support_summary["Average_Satisfaction_Score"].max())

print("\nInvalid Resolution Count:", customer_support_summary["Invalid_Resolution_Count"].sum())

print("\nMissing Satisfaction Count:", customer_support_summary["Missing_Satisfaction_Count"].sum())


# 2.24 — Merge support metrics into the main customer dataset
print("\n===== Merge Support Metrics =====")
customer_subscription_summary = customer_subscription_summary.merge(customer_support_summary, on="Customer_ID", how="left")

print("\nShape:", customer_subscription_summary.shape)

print("\nMissing Values:")
print(customer_subscription_summary[["Total_Tickets", "Resolved_Tickets", "Closed_Tickets", "Open_Tickets", "In_Progress_Tickets", "Average_Resolution_Time_Hours", "Average_Satisfaction_Score", "High_Critical_Tickets", "Invalid_Resolution_Count", "Missing_Satisfaction_Count"]].isnull().sum())


# 2.25 — Handle customers with no support tickets
support_count_columns = ["Total_Tickets", "Resolved_Tickets", "Closed_Tickets", "Open_Tickets", "In_Progress_Tickets", "High_Critical_Tickets", "Invalid_Resolution_Count", "Missing_Satisfaction_Count"]

customer_subscription_summary[support_count_columns] = customer_subscription_summary[support_count_columns].fillna(0)

print("\nMissing Values after filling support counts:")
print(customer_subscription_summary[support_count_columns + ["Average_Resolution_Time_Hours", "Average_Satisfaction_Score"]].isnull().sum())

print("\nCustomers With Zero Tickets:", (customer_subscription_summary["Total_Tickets"] == 0).sum())


# 2.26 — Create Support Performance Metrics
customer_subscription_summary["Ticket_Resolution_Rate"] = ((customer_subscription_summary["Resolved_Tickets"] + customer_subscription_summary["Closed_Tickets"]) / customer_subscription_summary["Total_Tickets"] * 100).fillna(0)

customer_subscription_summary["High_Critical_Ticket_Rate"] = (customer_subscription_summary["High_Critical_Tickets"] / customer_subscription_summary["Total_Tickets"] * 100).fillna(0)

customer_subscription_summary["Invalid_Resolution_Rate"] = (customer_subscription_summary["Invalid_Resolution_Count"] / customer_subscription_summary["Total_Tickets"] * 100).fillna(0)

customer_subscription_summary["Average_Ticket_Per_Subscription"] = (customer_subscription_summary["Total_Tickets"] / customer_subscription_summary["Total_Subscriptions"]).fillna(0)


# 2.27 — Validate Support Performance Metrics
print("\n===== Support Performance Validation =====")

print("\nTicket Resolution Rate:")
print(customer_subscription_summary["Ticket_Resolution_Rate"].describe())

print("\nHigh/Critical Ticket Rate:")
print(customer_subscription_summary["High_Critical_Ticket_Rate"].describe())

print("\nInvalid Resolution Rate:")
print(customer_subscription_summary["Invalid_Resolution_Rate"].describe())

print("\nAverage Ticket Per Subscription:")
print(customer_subscription_summary["Average_Ticket_Per_Subscription"].describe())

print("\nMissing Values:")
print(customer_subscription_summary[["Ticket_Resolution_Rate", "High_Critical_Ticket_Rate", "Invalid_Resolution_Rate", "Average_Ticket_Per_Subscription"]].isnull().sum())

print("\nInvalid Resolution Rate > 100%:", (customer_subscription_summary["Invalid_Resolution_Rate"] > 100).sum())

print("\nHigh\Critical Ticket Rate > 100%:", (customer_subscription_summary["High_Critical_Ticket_Rate"] > 100).sum())

print("\nTicket Resolution Rate > 100%:", (customer_subscription_summary["Ticket_Resolution_Rate"] > 100).sum())


# 2.28 — Final Customer Intelligence Dataset Validation
print("\n===== Final Customer Intelligence Dataset =====")
print("\nShape:", customer_subscription_summary.shape)

print("\nDuplicate Customer IDs:", customer_subscription_summary["Customer_ID"].isnull().sum())

print("\nTotal Missing Values:")
print(customer_subscription_summary.isnull().sum())

print("\nTotal Customers:", customer_subscription_summary["Customer_ID"].nunique())

print("\nTotal Subscriptions:", customer_subscription_summary["Total_Subscriptions"].sum())

print("\nTotal Transactions:", customer_subscription_summary["Total_Transactions"].sum())

print("\nTotal Support Tickets:", customer_subscription_summary["Total_Tickets"].sum())



# # 3 — Business Analysis & KPI Analysis.

# 3.1 — Overall Business KPI Summary
print("\n===== Overall Business KPI Summary =====")

total_customers = customers["Customer_ID"].nunique()

total_subscriptions = subscriptions["Subscription_ID"].nunique()

active_subscriptions = (subscriptions["Status"] == "Active").sum()

cancelled_subscriptions = (subscriptions["Status"] == "Cancelled").sum()

cancellation_rate = (cancelled_subscriptions / total_subscriptions * 100)

total_transaction_amount = transactions["Amount"].sum()

total_refund_amount = transactions.loc[transactions["Transaction_Type"] == "Refund", "Amount"].sum()

total_transactions = transactions["Transaction_ID"].nunique()

paid_transactions = (transactions["Payment_Status"] == "Paid").sum()

transaction_success_rate = (paid_transactions / total_transactions * 100)

total_support_tickets = support_tickets["Ticket_ID"].nunique()

resolved_support_tickets = (support_tickets["Ticket_Status"] == "Resolved").sum()

closed_support_tickets = (support_tickets["Ticket_Status"] == "Closed").sum()

ticket_resolution_rate = (resolved_support_tickets + closed_support_tickets) / total_support_tickets * 100

average_satisfaction = support_tickets["Satisfaction_Score"].mean()


print("\nTotal Customers:", total_customers)

print("\nTotal Subscriptions:", total_subscriptions)

print("\nActive Subscriptions:", active_subscriptions)

print("\nCancelled Subscriptions:", cancelled_subscriptions)

print("\nCancellation Rate:", round(cancellation_rate, 2), "%")

print("\nTotal Transaction Amount:", round(total_transaction_amount, 2))

print("\nTotal_Refund_Amount:", round(total_refund_amount, 2))

print("\nTotal_Transactions:", total_transactions)

print("\nPaid_Transactions:", paid_transactions)

print("\nTransaction Success Rate:", round(transaction_success_rate, 2), "%")

print("\nTotal Support Tickets:", total_support_tickets)

print("\nTicket Resolution Rate:", round(ticket_resolution_rate, 2), "%")

print("\nAverage Satisfaction Score:", round(average_satisfaction, 2))


# 3.2 — Subscription & Customer KPI Analysis
print("\n===== Subscription & Customer KPI Analysis =====")
status_counts = subscriptions["Status"].value_counts()

print("\nSubscription Status:")
print(status_counts)

print("\nSubscription Status Percentage:")
print(round(subscriptions["Status"].value_counts(normalize=True) * 100, 2))

print("\nAverage Monthly Fee:", round(subscriptions["Monthly_Fee"].mean(), 2))

print("\nAverage Discount:", round(subscriptions["Discount"].mean(), 2))

print("\nTotal Subscription Fees:", round(subscriptions["Monthly_Fee"].sum(), 2))

print("\nTotal Discounts:", round(subscriptions["Discount"].sum(), 2))

print("\nAverage Net Monthly Fee:", round(subscriptions["Net_Monthly_Fee"].mean(), 2))


# 3.3 — Analyze Subscription Plans
print("\n===== Subscription Plan Analysis =====")
plan_summary = (subscriptions.groupby("Plan").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                Active_Subscriptions=("Status", lambda x: (x == "Active").sum()),
                                                Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                Average_Monthly_Fee=("Monthly_Fee", "mean"),
                                                Average_Discount=("Discount", "mean"),
                                                Total_Subscription_Fee=("Monthly_Fee", "sum"),
                                                Average_Net_Monthly_Fee=("Net_Monthly_Fee", "mean")).reset_index())

plan_summary["Active_Rate"] = (plan_summary["Active_Subscriptions"] / plan_summary["Total_Subscriptions"] * 100)

plan_summary["Cancellation_Rate"] = (plan_summary["Cancelled_Subscriptions"] / plan_summary["Total_Subscriptions"] * 100)

plan_summary = plan_summary.sort_values("Total_Subscriptions", ascending=False)


pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
print("\n", round(plan_summary, 2))


# 3.4 Billing Cycle Analysis
print("\n===== Billing Cycle Analysis =====")

billing_summary=(subscriptions.groupby("Billing_Cycle").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                            Active_Subscriptions=("Status", lambda x: (x == "Active").sum()),
                                                            Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                            Average_Monthly_Fee=("Monthly_Fee", "mean"),
                                                            Average_Discount=("Discount", "mean"),
                                                            Total_Subscription_Fee=("Monthly_Fee", "sum"),
                                                            Average_Net_Monthly_Fee=("Net_Monthly_Fee", "mean")).reset_index())

billing_summary["Active_Rate"] = (billing_summary["Active_Subscriptions"] / billing_summary["Total_Subscriptions"] * 100)

billing_summary["Cancellation_Rate"] = (billing_summary["Cancelled_Subscriptions"] / billing_summary["Total_Subscriptions"] * 100)

billing_summary = billing_summary.sort_values("Total_Subscriptions", ascending=False)

pd.set_option = ("display.max_rows", None)
pd.set_option = ("display.max_columns", None)
print("\n", round(billing_summary, 2))


# 3.5 Auto-Renewal Analysis
print("\n===== Auto-Renewal Analysis =====")

auto_renewal_summary = (subscriptions.groupby("Auto_Renewal").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                                  Active_Subscriptions=("Status", lambda x: (x == "Active").sum()),
                                                                  Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                                  Expired_Subscriptions=("Status", lambda x: (x == "Expired").sum()),
                                                                  Average_Monthly_Fee=("Monthly_Fee", "mean"),
                                                                  Average_Discount=("Discount", "mean"),
                                                                  Average_Net_Monthly_Fee=("Net_Monthly_Fee", "mean")).reset_index())

auto_renewal_summary["Active_Rate"] = auto_renewal_summary["Active_Subscriptions"] / auto_renewal_summary["Total_Subscriptions"] * 100

auto_renewal_summary["Cancellation_Rate"] = auto_renewal_summary["Cancelled_Subscriptions"] / auto_renewal_summary["Total_Subscriptions"] * 100

auto_renewal_summary["Expiration_Rate"] = auto_renewal_summary["Expired_Subscriptions"] / auto_renewal_summary["Total_Subscriptions"] * 100

auto_renewal_summary = auto_renewal_summary.sort_values("Total_Subscriptions", ascending=False)

pd.set_option = ("display.max_rows", None)
pd.set_option = ("display.max_columns", None)
print("\n", round(auto_renewal_summary, 2))


# 3.6 Product Performance Analysis
print("\n===== Product Performance Analysis =====")
product_summary = (subscriptions.groupby("Product_ID").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                           Active_Subscriptions=("Status", lambda x: (x == "Active").sum()),
                                                           Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                           Average_Monthly_Fee=("Monthly_Fee", "mean"),
                                                           Average_Discount=("Discount", "mean"),
                                                           Average_Net_Monthly_Fee=("Net_Monthly_Fee", "mean")).reset_index())

product_summary["Active_Rate"] = product_summary["Active_Subscriptions"] / product_summary["Total_Subscriptions"] * 100

product_summary["Cancellation_Rate"] = product_summary["Cancelled_Subscriptions"] / product_summary["Total_Subscriptions"] * 100

product_summary = product_summary.merge(products[["Product_ID", "Product_Name", "Product_Category", "Product_Type", "Pricing_Model", "Target_Segment"]], on="Product_ID", how="left")

product_summary = product_summary.sort_values("Total_Subscriptions", ascending=False)

pd.set_option = ("delay.max_rows", None)
pd.set_option = ("delay.max_columns", None)
print("\n", round(product_summary, 2))


# 3.7 validation step
top_products = (product_summary[["Product_ID", "Product_Name", "Product_Category", "Product_Type", "Pricing_Model",
                                 "Total_Subscriptions", "Active_Subscriptions", "Cancelled_Subscriptions", "Average_Monthly_Fee",
                                 "Average_Net_Monthly_Fee", "Active_Rate", "Cancellation_Rate"]].sort_values("Total_Subscriptions", ascending=False).head(10))

print("\nValidation:")
print(top_products.to_string(index=False))


# 3.8 Product Category Analysis
print("\n===== Product Category Analysis =====")
category_summary = (product_summary.groupby("Product_Category").agg(Total_Subscriptions=("Total_Subscriptions", "sum"),
                                                             Active_Subscriptions=("Active_Subscriptions", "sum"),
                                                             Cancelled_Subscriptions=("Cancelled_Subscriptions", "sum"),
                                                             Average_Monthly_Fee=("Average_Monthly_Fee", "mean"),
                                                             Average_Discount=("Average_Discount", "mean"),
                                                             Average_Net_Monthly_Fee=("Average_Net_Monthly_Fee", "mean")).reset_index())

category_summary["Active_Rate"] = category_summary["Active_Subscriptions"] / category_summary["Total_Subscriptions"] * 100

category_summary["Cancellation_Rate"] = category_summary["Cancelled_Subscriptions"] / category_summary["Total_Subscriptions"] * 100

category_summary = category_summary.sort_values("Total_Subscriptions", ascending=False)

print("\n", category_summary.to_string(index=False))


# 3.9 Customer Segment Analysis
print("\n===== Customer Segment Analysis =====")
segment_summary = (customer_subscription_summary.groupby("Customer_Segment").agg(Total_Customers=("Customer_ID", "count"),
                                                                                 Total_Subscriptions=("Total_Subscriptions", "sum"),
                                                                                 Active_Subscriptions=("Active_Subscriptions", "sum"),
                                                                                 Cancelled_Subscriptions=("Cancelled_Subscriptions", "sum"),
                                                                                 Total_Transaction_Amount=("Total_Transaction_Amount", "sum"),
                                                                                 Total_Transactions=("Total_Transactions", "sum"),
                                                                                 Total_Tickets=("Total_Tickets", "sum"),
                                                                                 Average_Satisfaction_Score=("Average_Satisfaction_Score", "mean"),
                                                                                 Average_Monthly_Fee=("Average_Monthly_Fee", "mean"),
                                                                                 Average_Net_Monthly_Fee=("Average_Net_Monthly_Fee", "mean")).reset_index())

segment_summary["Active_Rate"] = segment_summary["Active_Subscriptions"] / segment_summary["Total_Subscriptions"] * 100

segment_summary["Cancellation_Rate"] = segment_summary["Cancelled_Subscriptions"] / segment_summary["Total_Subscriptions"] * 100

segment_summary["Average_Transaction_Per_Customer"] = segment_summary["Total_Transactions"] / segment_summary["Total_Customers"]

segment_summary["Average_Ticket_Per_Customer"] = segment_summary["Total_Tickets"] / segment_summary["Total_Customers"] 

segment_summary = segment_summary.sort_values("Total_Customers", ascending=False)

print("\n", segment_summary.to_string(index=False))


# 3.10 Transaction & Payment Analysis
print("\n===== Transaction & Payment Analysis =====")
transaction_summary = (transactions.groupby("Transaction_Type").agg(Total_Transactions=("Transaction_ID", "count"),
                                                                    Total_Amount=("Amount", "sum"),
                                                                    Average_Amount=("Amount", "mean"),
                                                                    Paid_Transactions=("Payment_Status", lambda x: (x == "Paid").sum()),
                                                                    Failed_Transactions=("Payment_Status", lambda x: (x == "Failed").sum()),
                                                                    Pending_Transactions=("Payment_Status", lambda x: (x == "Pending").sum()),
                                                                    Refunded_Transactions=("Payment_Status", lambda x: (x == "Refunded").sum()),
                                                                    Suspicious_Negative_Transactions=("Suspicious_Negative_Amount_Flag", "sum")).reset_index())

transaction_summary["Payment_Success_Rate"] = transaction_summary["Paid_Transactions"] / transaction_summary["Total_Transactions"] * 100

transaction_summary["Failure_Rate"] = transaction_summary["Failed_Transactions"] / transaction_summary["Total_Transactions"] * 100

transaction_summary["Refund_Rate"] = transaction_summary["Refunded_Transactions"] / transaction_summary["Total_Transactions"] * 100

transaction_summary = transaction_summary.sort_values("Total_Transactions", ascending=False)

print("\n", transaction_summary.to_string(index=False))


# 3.11 Payment Method Analysis
print("\n===== Payment Method Analysis =====")
payment_method_summary = (transactions.groupby("Payment_Method").agg(Total_Transactions=("Transaction_ID", "count"),
                                                                    Total_Amount=("Amount", "sum"),
                                                                    Average_Amount=("Amount", "mean"),
                                                                    Paid_Transactions=("Payment_Status", lambda x: (x == "Paid").sum()),
                                                                    Failed_Transactions=("Payment_Status", lambda x: (x == "Failed").sum()),
                                                                    Pending_Transactions=("Payment_Status", lambda x: (x == "Pending").sum()),
                                                                    Refunded_Transactions=("Payment_Status", lambda x: (x == "Refunded").sum())).reset_index())

payment_method_summary["Payment_Success_Rate"] = payment_method_summary["Paid_Transactions"] / payment_method_summary["Total_Transactions"] * 100

payment_method_summary["Failure_Rate"] = payment_method_summary["Failed_Transactions"] / payment_method_summary["Total_Transactions"] * 100

payment_method_summary["Refund_Rate"] = payment_method_summary["Refunded_Transactions"] / payment_method_summary["Total_Transactions"] * 100

payment_method_summary = payment_method_summary.sort_values("Total_Transactions",  ascending=False)

print("\n", payment_method_summary.to_string(index=False))


# 3.12 Sales Channel Analysis
print("\n===== Sales Channel Analysis =====")
sales_channel_summary = (transactions.groupby("Sales_Channel").agg(Total_Transactions=("Transaction_ID", "count"),
                                                                   Total_Amount=("Amount", "sum"),
                                                                   Average_Amount=("Amount", "mean"),
                                                                   Paid_Transactions=("Payment_Status", lambda x: (x == "Paid").sum()),
                                                                   Failed_Transactions=("Payment_Status", lambda x: (x == "Failed").sum()),
                                                                   Pending_Transactions=("Payment_Status", lambda x: (x == "Pending").sum()),
                                                                   Refunded_Transactions=("Payment_Status", lambda x: (x == "Refunded").sum())).reset_index())

sales_channel_summary["Payment_Success_Rate"] = sales_channel_summary["Paid_Transactions"] / sales_channel_summary["Total_Transactions"] * 100

sales_channel_summary["Failure_Rate"] = sales_channel_summary["Failed_Transactions"] / sales_channel_summary["Total_Transactions"] * 100

sales_channel_summary["Refund_Rate"] = sales_channel_summary["Refunded_Transactions"] / sales_channel_summary["Total_Transactions"] * 100

sales_channel_summary = sales_channel_summary.sort_values("Total_Transactions", ascending=False)

print("\n", sales_channel_summary.to_string(index=False))


# 3.13 Industry Analysis
print("\n===== Industry Analysis =====")
industry_summary = (customer_subscription_summary.groupby("Industry").agg(Total_Customers=("Customer_ID", "nunique"),
                                                                          Total_Subscriptions=("Total_Subscriptions", "sum"),
                                                                          Active_Subscriptions=("Active_Subscriptions", "sum"),
                                                                          Cancelled_Subscriptions=("Cancelled_Subscriptions", "sum"),
                                                                          Total_Transaction_Amount=("Total_Transaction_Amount", "sum"),
                                                                          Total_Transactions=("Total_Transactions", "sum"),
                                                                          Total_Tickets=("Total_Tickets", "sum"),
                                                                          Average_Satisfaction_Score=("Average_Satisfaction_Score", "mean"),
                                                                          Average_Monthly_Fee=("Average_Monthly_Fee", "mean"),
                                                                          Average_Net_Monthly_Fee=("Average_Net_Monthly_Fee", "mean")).reset_index())

industry_summary["Active_Rate"] = industry_summary["Active_Subscriptions"] / industry_summary["Total_Subscriptions"] * 100

industry_summary["Cancellation_Rate"] = industry_summary["Cancelled_Subscriptions"] / industry_summary["Total_Subscriptions"] * 100

industry_summary["Average_Transaction_Per_Customer"] = industry_summary["Total_Transaction_Amount"] / industry_summary["Total_Customers"] 

industry_summary["Average_Ticket_Per_Customer"] = industry_summary["Total_Tickets"] / industry_summary["Total_Customers"]

industry_summary = industry_summary.sort_values("Total_Customers", ascending=False)

print("\n", industry_summary.to_string(index=False))


# 3.14 Support Ticket / Issue Category Analysis
print("\n===== Support Issue Category Analysis =====")
issue_category_summary = (support_tickets.groupby("Issue_Category").agg(Total_Tickets=("Ticket_ID", "count"),
                                                                        Resolved_Tickets=("Ticket_Status", lambda x: (x == "Resolved").sum()),
                                                                        Closed_Tickets=("Ticket_Status", lambda x: (x == "Closed").sum()),
                                                                        Open_Tickets=("Ticket_Status", lambda x: (x == "Open").sum()),
                                                                        In_Progress_Tickets=("Ticket_Status", lambda x: (x == "In Progress").sum()),
                                                                        Average_Resolution_Time_Hours=("Resolution_Time_Hours", lambda x: x[x >= 0].mean()),
                                                                        Average_Satisfaction_Score=("Satisfaction_Score", "mean"),
                                                                        High_Critical_Tickets=("Priority", lambda x: ((x == "High") | (x == "Critical")).sum()),
                                                                        Invalid_Resolution_Count=("Invalid_Resolution_Time_Flag", "sum"),
                                                                        Missing_Satisfaction_Count=("Missing_Satisfaction_Flag", "sum")).reset_index())

issue_category_summary["Ticket_Resolution_Rate"] = (issue_category_summary["Resolved_Tickets"] + issue_category_summary["Closed_Tickets"]) / issue_category_summary["Total_Tickets"] * 100

issue_category_summary["High_Critical_Ticket_Rate"] = issue_category_summary["High_Critical_Tickets"] / issue_category_summary["Total_Tickets"] * 100

issue_category_summary["Invalid_Resolution_Rate"] = issue_category_summary["Invalid_Resolution_Count"] / issue_category_summary["Total_Tickets"] * 100

issue_category_summary = issue_category_summary.sort_values("Total_Tickets", ascending=False)

print("\n", issue_category_summary.to_string(index=False))


# 3.15 Priority Analysis  
print("\n===== Support Priority Analysis =====")
priority_summary = (support_tickets.groupby("Priority").agg(Total_Tickets=("Ticket_ID", "count"),
                                                            Resolved_Tickets=("Ticket_Status", lambda x: (x == "Resolved").sum()),
                                                            Closed_Tickets=("Ticket_Status", lambda x: (x == "Closed").sum()),
                                                            Open_Tickets=("Ticket_Status", lambda x: (x == "Open").sum()),
                                                            In_Progress_Tickets=("Ticket_Status", lambda x: (x == "In Progress").sum()),
                                                            Average_Resolution_Time_Hours=("Resolution_Time_Hours", lambda x: x[x >= 0].mean()),
                                                            Average_Satisfaction_Score=("Satisfaction_Score", "mean"),
                                                            Invalid_Resolution_Count=("Invalid_Resolution_Time_Flag", "sum"),
                                                            Missing_Satisfaction_Count=("Missing_Satisfaction_Flag", "sum")).reset_index())

priority_summary["Ticket_Resolution_Rate"] = (priority_summary["Resolved_Tickets"] + priority_summary["Closed_Tickets"]) / priority_summary["Total_Tickets"] * 100

priority_summary["Invalid_Resolution_Rate"] = priority_summary["Invalid_Resolution_Count"] / priority_summary["Total_Tickets"] * 100

priority_summary["Missing_Satisfaction_Rate"] = priority_summary["Missing_Satisfaction_Count"] / priority_summary["Total_Tickets"] * 100

priority_summary = priority_summary.sort_values("Total_Tickets", ascending=False)

print("\n", priority_summary.to_string(index=False))


# 3.16 Support Channel Analysis
print("\n===== Support Agent Analysis =====")
agent_summary = (support_tickets.groupby("Agent_ID").agg(Total_Tickets=("Ticket_ID", "count"),
                                                                  Resolved_Tickets=("Ticket_Status", lambda x: (x == "Resolved").sum()),
                                                                  Closed_Tickets=("Ticket_Status", lambda x: (x == "Closed").sum()),
                                                                  Open_Tickets=("Ticket_Status", lambda x: (x == "Open").sum()),
                                                                  In_Progress_Tickets=("Ticket_Status", lambda x: (x == "In Progress").sum()),
                                                                  Average_Resolution_Time_Hours=("Resolution_Time_Hours", lambda x: x[x >= 0].mean()),
                                                                  Average_Satisfaction_Score=("Satisfaction_Score", "mean")).reset_index())

agent_summary["Ticket_Completion_Rate"] = (agent_summary["Resolved_Tickets"] + agent_summary["Closed_Tickets"]) / agent_summary["Total_Tickets"] * 100

agent_summary = agent_summary.sort_values("Total_Tickets", ascending=False)

print("\n",agent_summary.to_string(index=False))


# 3.17 Customer Satisfaction Analysis
print("\n===== Customer Satisfaction Analysis =====")
satisfaction_priority = support_tickets.groupby("Priority").agg(Total_Tickets=("Ticket_ID", "count"),
                                                                Average_Satisfaction=("Satisfaction_Score", "mean"),
                                                                Satisfaction_Responses=("Satisfaction_Score", "count"),
                                                                Missing_Satisfaction=("Satisfaction_Score", lambda x: x.isnull().sum()),
                                                                Average_Resolution_Time_Hours=("Resolution_Time_Hours", lambda x: x[x >= 0].mean())).reset_index()

satisfaction_priority = satisfaction_priority.sort_values("Average_Satisfaction", ascending=False)

print("\n", satisfaction_priority.to_string(index=False))


# 3.18 Resolution Time Analysis by Priority
print("\n===== Resolution Time by Priority =====")
resolution_priority = support_tickets.groupby("Priority").agg(Total_Tickets=("Ticket_ID", "count"),
                                                              Average_Resolution_Hours=("Resolution_Time_Hours", lambda x: x[x >= 0].mean()),
                                                              Median_Resolution_Hours=("Resolution_Time_Hours", lambda x: x[x >= 0].median()),
                                                              Invalid_Resolution_Count=("Invalid_Resolution_Time_Flag", "sum")).reset_index()

resolution_priority = resolution_priority.sort_values("Average_Resolution_Hours", ascending=False)
print("\n", resolution_priority.to_string(index=False))


# 3.19 Calculate monthly subscription counts
print("\n===== Monthly Subscription Counts =====")
subscriptions["Subscription_Month"] = subscriptions["Subscription_Start_Date"].dt.to_period("M")
print("\n",subscriptions["Subscription_Month"].head())

monthly_subscriptions = subscriptions.groupby("Subscription_Month").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                                        Active_Subscriptions=("Status", lambda x: (x == "Active").sum()),
                                                                        Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                                        Expired_Subscriptions=("Status", lambda x: (x == "Expired").sum()),
                                                                        Paused_Subscriptions=("Status", lambda x: (x == "Paused").sum())).reset_index()

print("\n", monthly_subscriptions)

print("\nValidation:")
print("Total Monthly Subscriptions:", monthly_subscriptions["Total_Subscriptions"].sum())

highest_month = monthly_subscriptions["Total_Subscriptions"].idxmax()
print("\nHighest Month in Subscriptions:")
print(monthly_subscriptions.loc[highest_month, ["Subscription_Month", "Total_Subscriptions"]])

lowest_month = monthly_subscriptions["Total_Subscriptions"].idxmin()
print("\nLowest Month in Subscription:")
print(monthly_subscriptions.loc[lowest_month, ["Subscription_Month", "Total_Subscriptions"]])


# 3.20 Monthly Transaction Trend
# step 1 - Validate the transaction date
print("\nValidation :")  
print(transactions["Transaction_Date"].dtype)
print("\n",transactions.isnull().sum())
print("\n",transactions["Transaction_Date"].max())
print("\n",transactions["Transaction_Date"].min())

# Create Monthly Transaction Trend
print("\nCreate Monthly Transaction Trend:")
transactions["Transaction_Month"] = transactions["Transaction_Date"].dt.to_period("M")
print("\n",transactions["Transaction_Month"])

monthly_transactions = transactions.dropna(subset=["Transaction_Month"]).groupby("Transaction_Month").agg(Total_Transactions=("Transaction_ID", "count"),
                                                                                                          Total_Transaction_Amount=("Amount", "sum"),
                                                                                                          Average_Transaction_Amount=("Amount", "mean"),
                                                                                                          Paid_Transactions=("Payment_Status", lambda x: (x == "Paid").sum()),
                                                                                                          Failed_Transactions=("Payment_Status", lambda x: (x == "Failed").sum()),
                                                                                                          Pending_Transactions=("Payment_Status", lambda x: (x == "Pending").sum()),
                                                                                                          Refunded_Transactions=("Payment_Status", lambda x: (x == "Refunded").sum())).reset_index()

print("\n", monthly_transactions)

# Validation
print("\nValidation:")
print("Total Transactions in Monthly Summary:", monthly_transactions["Total_Transactions"].sum())
print("Transaction with valid dates:", transactions["Transaction_Date"].notna().sum())
print("Transaction with missing dates:", transactions["Transaction_Date"].isna().sum())
print("Original Total Transactions:", len(transactions))

# identify the most important monthly transaction findings.
highest_transaction_month = monthly_transactions.loc[monthly_transactions["Total_Transactions"].idxmax()]

lowest_transaction_month = monthly_transactions.loc[monthly_transactions["Total_Transactions"].idxmin()]

highest_amount_month = monthly_transactions.loc[monthly_transactions["Total_Transaction_Amount"].idxmax()]

lowest_amount_month = monthly_transactions.loc[monthly_transactions["Total_Transaction_Amount"].idxmin()]

print("\nHighest Transaction Count Month:") 
print(highest_transaction_month[["Transaction_Month", "Total_Transactions"]])

print("\nLowest Transaction Count Month:")
print(lowest_transaction_month[["Transaction_Month", "Total_Transactions"]])

print("\nHighest Transaction Amount Month:")
print(highest_amount_month[["Transaction_Month", "Total_Transaction_Amount"]])

print("\nLowest Transaction Amount Month:")
print(lowest_amount_month[["Transaction_Month", "Total_Transaction_Amount"]])

# Step 3.20 — Customer Retention Analysis
customer_subscription_status = subscriptions.groupby("Customer_ID")["Status"].value_counts().unstack(fill_value=0) 

print("\n",customer_subscription_status.head())

print("\nShape:", customer_subscription_status.shape)

# Step 3.20.1 — Create customer retention metrics
customer_retention = customer_subscription_status.copy()

customer_retention["Total_Subscriptions"] = customer_retention.sum(axis=1)

customer_retention["Has_Active_Subscriptions"] = customer_retention["Active"] > 0

customer_retention["Has_Cancelled_Subscriptions"] = customer_retention["Cancelled"] > 0

customer_retention["Has_Active_and_Cancelled"] = (customer_retention["Active"] > 0) & (customer_retention["Cancelled"] > 0)

print("\n",customer_retention.head())

print("\nShape:", customer_retention.shape)

# 3.20.2 — Calculate the retention KPIs
total_subscription_customers = len(customer_retention)

active_customers = customer_retention["Has_Active_Subscriptions"].sum()

cancelled_customers = customer_retention["Has_Cancelled_Subscriptions"].sum()

active_and_cancelled_customers = customer_retention["Has_Active_and_Cancelled"].sum()

retention_rate = (active_customers / total_subscription_customers) * 100

cancellation_customer_rate = (cancelled_customers / total_subscription_customers) * 100

both_rate = (active_and_cancelled_customers / total_subscription_customers) * 100


print("\nTotal Customers with Subscriptions:", total_subscription_customers)

print("Customers with Active Subscriptions:", active_customers)

print("Customers with Cancellation History:", cancelled_customers)

print("Customers with Active + Cancelled:", active_and_cancelled_customers)

print("Customer Retention Rate:", retention_rate)

print("Customer Cancellation History Rate:", cancellation_customer_rate)

print("Active + Cancelled Customer Rate:", both_rate)

# 3.20.4 — Check customer retention segments
customer_retention["Retention_Segment"] = "Other"

customer_retention.loc[(customer_retention["Has_Active_Subscriptions"]) & (~customer_retention["Has_Cancelled_Subscriptions"]), "Retention_Segment"] = "Active Only"

customer_retention.loc[(customer_retention["Has_Active_Subscriptions"]) & (customer_retention["Has_Cancelled_Subscriptions"]), "Retention_Segment"] = "Active + Cancelled"

customer_retention.loc[(~customer_retention["Has_Active_Subscriptions"]) & (customer_retention["Has_Cancelled_Subscriptions"]), "Retention_Segment"] = "Cancelled_Only"


print("\n", customer_retention["Retention_Segment"].value_counts())

print("\nPercentage:")
print(customer_retention["Retention_Segment"].value_counts(normalize=True) * 100)


# 3.21 — Subscription Cancellation Analysis
# 3.21.1 — Cancellation by Plan
cancellation_by_plan = subscriptions.groupby("Plan").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                         Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                         Active_Subscriptions=("Status", lambda x: (x == "Active").sum())).reset_index()

cancellation_by_plan["Cancellation_Rate_%"] = cancellation_by_plan["Cancelled_Subscriptions"] / cancellation_by_plan["Total_Subscriptions"] * 100

cancellation_by_plan = cancellation_by_plan.sort_values("Cancellation_Rate_%", ascending=False)
print("\nCancellation By Plan:")
print(cancellation_by_plan)

# 3.21.2 — Cancellation by Billing Cycle
cancellation_by_billing = subscriptions.groupby("Billing_Cycle").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                                     Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                                     Active_Subscriptions=("Status", lambda x: (x == "Active").sum())).sort_index()

cancellation_by_billing["Cancellation_Rate_%"] = cancellation_by_billing["Cancelled_Subscriptions"] / cancellation_by_billing["Total_Subscriptions"] * 100

cancellation_by_billing = cancellation_by_billing.sort_values("Cancellation_Rate_%", ascending=False)

print("\nCancellation By Billing:")
print(cancellation_by_billing)

# 3.21.3 — Cancellation by Auto-Renewal
cancellation_by_autorenewal = subscriptions.groupby("Auto_Renewal").agg(Total_Subscriptions=("Subscription_ID","count"),
                                                                        Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                                        Active_Subscriptions=("Status", lambda x: (x == "Active").sum())).reset_index()

cancellation_by_autorenewal["Cancellation_Rate_%"] = cancellation_by_autorenewal["Cancelled_Subscriptions"] / cancellation_by_autorenewal["Total_Subscriptions"] * 100

cancellation_by_autorenewal = cancellation_by_autorenewal.sort_values("Cancellation_Rate_%", ascending=False)

print("\nCancellation By Auto-Renewal:")
print(cancellation_by_autorenewal)

# 3.21.4 — Cancellation by Product Category
subscription_product = subscriptions.merge(products[["Product_ID", "Product_Category"]], on="Product_ID", how="left")

print("\nsubscription_product:")
print(subscription_product[["Product_ID", "Product_Category"]].head())
print("\nShape:", subscription_product.shape)

cancellation_by_category = subscription_product.groupby("Product_Category").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                                          Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                                          Active_Subscriptions=("Status", lambda x: (x == "Active").sum())).reset_index()

cancellation_by_category["Cancellation_Rate_%"] = cancellation_by_category["Cancelled_Subscriptions"] / cancellation_by_category["Total_Subscriptions"] * 100

cancellation_by_category = cancellation_by_category.sort_values("Cancellation_Rate_%", ascending=False)

print("\nCancellation By Category:")
print(cancellation_by_category)

# 3.21.5 — Cancellation by Customer Segment
subscription_customer = subscriptions.merge(customers[["Customer_ID", "Customer_Segment"]], on="Customer_ID", how="left")

print("\nsubscription_customer:")
print(subscription_customer[["Customer_ID", "Customer_Segment"]].head())
print("\nShape:", subscription_customer.shape)

cancellation_by_segment = subscription_customer.groupby("Customer_Segment").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                                                Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                                                Active_Subscriptions=("Status", lambda x: (x == "Active").sum())).reset_index()

cancellation_by_segment["Cancellation_Rate_%"] = cancellation_by_segment["Cancelled_Subscriptions"] / cancellation_by_segment["Total_Subscriptions"] * 100

cancellation_by_segment = cancellation_by_segment.sort_values("Cancellation_Rate_%", ascending=False)

print("\nCancellation By Segment:")
print(cancellation_by_segment)

# 3.21.6 — Cancellation by Industry
subscription_industry = subscriptions.merge(customers[["Customer_ID", "Industry"]], on="Customer_ID", how="left")

print("\nSubscription_Industry:")
print(subscription_industry[["Customer_ID", "Industry"]].head())
print("\nShape:", subscription_industry.shape)

cancellation_by_industry = subscription_industry.groupby("Industry").agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                                         Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                                         Active_Subscriptions=("Status", lambda x: (x == "Active").sum())).reset_index()

cancellation_by_industry["Cancellation_Rate_%"] = cancellation_by_industry["Cancelled_Subscriptions"] / cancellation_by_industry["Total_Subscriptions"] * 100

cancellation_by_industry = cancellation_by_industry.sort_values("Cancellation_Rate_%", ascending=False)

print("\nCancellation By Industry:")
print(cancellation_by_industry)

# 3.21.7 — Identify Products with the Highest Cancellation Rates
cancellation_by_product = subscription_product.groupby(["Product_ID", "Product_Category"]).agg(Total_Subscriptions=("Subscription_ID", "count"),
                                                                                             Cancelled_Subscriptions=("Status", lambda x: (x == "Cancelled").sum()),
                                                                                             Active_Subscriptions=("Status", lambda x: (x == "Active").sum())).reset_index()

cancellation_by_product["Cancellation_Rate_%"] = cancellation_by_product["Cancelled_Subscriptions"] / cancellation_by_product["Total_Subscriptions"] * 100

# Focus on products with at least 30 subscriptions
cancellation_by_product = cancellation_by_product[cancellation_by_product["Total_Subscriptions"] >= 30].sort_values("Cancellation_Rate_%", ascending=False)

print("\nTop 10 Product by Cancellation Rate:")
print(cancellation_by_product.head(10))

# 3.21.8 — Cancellation Analysis Summary
print("\nOVERALL CANCELLATION SUMMARY")
print("-" * 40)

print("\nTotal Subscriptions:", len(subscriptions))
print("Total Cancelled:", (subscriptions["Status"] == "Cancelled").sum())
print("Overall Cancellation Rate (%):", (subscriptions["Status"] == "Cancelled").mean() * 100)

print("\nHighest Cancellation Rate By Plan:")
print(cancellation_by_plan.head(1))

print("\nHighest Cancellation Rate By Billing Cycle:")
print(cancellation_by_billing.head(1))

print("\nHighest Cancellation Rate By Product Category:")
print(cancellation_by_category.head(1))

print("\nHighest Cancellation Rate By Customer Segment:")
print(cancellation_by_segment.head(1))

print("\nHighest Cancellation Rate By Industry:")
print(cancellation_by_industry.head(1))

print("\nHighest Cancellation Rate By Product:")
print(cancellation_by_product.head(1))


# 3.22 — Revenue and Refund Analysis
# 3.22.1 — Overall Revenue and Refund KPIs
print("\nREVENUE AND REFUND ANALYSIS:")
print("-" * 40)

print("\nTotal Transactions:", len(transactions))
print("Total Transaction Amount:", round(transactions["Amount"].sum(),2))
print("Total Refund Amount:", round(transactions.loc[transactions["Transaction_Type"] == "Refund", "Amount"].sum(), 2))
print("Number of Refund Transactions:", (transactions["Transaction_Type"] == "Refund").sum())
print("Paid Transaction Amount:", transactions.loc[transactions["Payment_Status"] == "Paid", "Amount"].sum().round(2))
print("Failed Transaction Amount:", transactions.loc[transactions["Payment_Status"] == "Failed", "Amount"].sum().round(2))

# 3.22.2 — Refund Analysis by Transaction Type
refund_by_type = transactions.groupby("Transaction_Type").agg(Total_Transactions=("Transaction_ID", "count"),
                                                              Total_Amount=("Amount", "sum"),
                                                              Average_Amount=("Amount", "mean"),
                                                              Refund_Status_Count=("Payment_Status", lambda x: (x == "Refunded").sum())).reset_index()

print("\nTransaction Analysis By Type:")
print(refund_by_type)

# 3.22.3 — Refunds by Payment Method
refund_by_payment_method = transactions.groupby("Payment_Method").agg(Total_Transactions=("Transaction_ID", "count"),
                                                                      Total_Amount=("Amount", "sum"),
                                                                      Refund_Transactions=("Transaction_Type", lambda x: (x == "Refund").sum()),
                                                                      Refund_Status_Count=("Payment_Status", lambda x: (x == "Refunded").sum())).reset_index()

print("\nRefund Analysis by Payment Method:")
print(refund_by_payment_method)

# 3.22.4 — Calculate Refund Rates by Payment Method
refund_by_payment_method["Refund_Rate_%"] = refund_by_payment_method["Refund_Transactions"] / refund_by_payment_method["Total_Transactions"] * 100

refund_by_payment_method["Refund_Rate_%"] = refund_by_payment_method["Refund_Status_Count"] / refund_by_payment_method["Total_Transactions"] * 100

refund_by_payment_method = refund_by_payment_method.sort_values("Refund_Rate_%", ascending=False)

print("\nRefund Rates by Payment Method:")
print(refund_by_payment_method)

# 3.22.5 — Refund Analysis by Sales Channel
refund_by_channel = transactions.groupby("Sales_Channel").agg(Total_Transactions=("Transaction_ID", "count"),
                                                              Total_Amount=("Amount", "sum"),
                                                              Refund_Transactions=("Transaction_Type", lambda x: (x == "Refund").sum()),
                                                              Refund_Status_Count=("Payment_Status", lambda x: (x == "Refunded").sum())).reset_index()

refund_by_channel["Refund_Rate_%"] = refund_by_channel["Refund_Transactions"] / refund_by_channel["Total_Transactions"] * 100

refund_by_channel = refund_by_channel.sort_values("Refund_Rate_%", ascending=False)

print("\nRefund Analysis by Sales Channel:")
print(refund_by_channel)

# 3.22.6 — Refund Analysis by Transaction Status
refund_by_status = transactions.groupby("Payment_Status").agg(Total_Transactions=("Transaction_ID", "count"),
                                                              Total_Amount=("Amount", "sum"),
                                                              Average_Amount=("Amount", "mean"),
                                                              Refund_Type_Count=("Transaction_Type", lambda x: (x == "Refund").sum())).reset_index()

refund_by_status["Transaction_Percentage_%"] = refund_by_status["Total_Transactions"] / len(transactions) * 100

print("\nTransaction Analysis by Payment Status:")
print(refund_by_status)

# 3.22.7 — Compare Transaction Type with Payment Status
transaction_status_check = pd.crosstab(transactions["Transaction_Type"], transactions["Payment_Status"], margins=True)

print("\nTransaction Type VS Payment Status:")
print(transaction_status_check)

# 3.22.8 — Calculate the Refund-Type Status Breakdown
transaction_status_percentage = pd.crosstab(transactions["Transaction_Type"], transactions["Payment_Status"], normalize="index") * 100

print("\nPayment Status Percentage Within Each Transaction Type:")
print(transaction_status_percentage.round(2))

# 3.22.9: Monthly Transaction and Refund Trend
#  Create a monthly period from Transaction_Date
transactions["Transaction_Month"] = pd.to_datetime(transactions["Transaction_Date"], errors="coerce").dt.to_period("M")

# Calculate monthly transaction and refund metrics
monthly_refund_analysis = transactions.groupby("Transaction_Month").agg(Total_Transactions=("Transaction_ID", "count"),
                                                                        Total_Amount=("Amount", "sum"),
                                                                        Refund_Transactions=("Transaction_Type", lambda x: (x == "Refund").sum()))

# Calculate refund rate
monthly_refund_analysis["Refund_Rate_%"] = monthly_refund_analysis["Refund_Transactions"] / monthly_refund_analysis["Total_Transactions"] * 100

print("\nMonthly Transaction and Refund Analysis:")
print(monthly_refund_analysis.round(2))

# 3.22.10: Validate monthly totals
print("\nValidate Monthly Totals:")
print("Total Transaction in original dataset:", len(transactions))
print("Total Transaction in monthly summary:", monthly_refund_analysis["Total_Transactions"].sum())
print("Refund Transaction in original dataset:", (transactions["Transaction_Type"] == "Refund").sum())
print("Refund Transaction in monthly summary:", monthly_refund_analysis["Refund_Transactions"].sum())
print("Missing Transaction dates:", transactions["Transaction_Date"].isna().sum())

# 3.22.11 — Inspect transactions with missing dates
missing_date_transactions = transactions[transactions["Transaction_Date"].isna()]

print("\nMissing-date Transaction Records:")
print(missing_date_transactions.head(10))

print("\nTransaction Type Among Missing-date Records:")
print(missing_date_transactions["Transaction_Type"].value_counts())

print("\nPayment Statuses Among Missing-date Records:")
print(missing_date_transactions["Payment_Status"].value_counts())

print("\nRefund-type Transaction With Missing Dates:", (missing_date_transactions["Transaction_Type"] == "Refund").sum())

# 3.22.12: Analyze refunds by customer segment
# Merge customer segment information into transactions
transaction_customer = transactions.merge(customers[["Customer_ID", "Customer_Segment"]], on="Customer_ID", how="left")

# Analyze transactions and refund-type transactions by segment
refund_by_segment = transaction_customer.groupby("Customer_Segment", dropna=False).agg(Total_Transactions   =("Transaction_ID", "count"),
                                                                                       Total_Amount=("Amount", "sum"),
                                                                                       Refund_Transactions=("Transaction_Type", lambda x: (x == "Refund").sum()))

# Calculate refund rate
refund_by_segment["Refund_Rate_%"] = refund_by_segment["Refund_Transactions"] / refund_by_segment["Total_Transactions"] * 100

print("\nRefund Analysis by Customer Segment:")
print(refund_by_segment)

# 3.22.13: Validate transaction totals after the merge
print("\nValidation:")
print("Original transaction rows:", len(transactions))
print("Merge transaction rows:", len(transaction_customer))
print("Unique transaction IDs after merge:", transaction_customer["Transaction_ID"].nunique())
print("Missing Customer Segments:", transaction_customer["Customer_Segment"].isna().sum())
print("Refund-type transaction after merge:", (transaction_customer["Transaction_Type"] == "Refund").sum())

# 3.22.14: Refund Analysis by Product Category
# Connect transactions to subscription product IDs
transaction_subscription = transactions.merge(subscriptions[["Subscription_ID", "Product_ID"]], on="Subscription_ID", how="left")

# Add product category
transaction_product = transaction_subscription.merge(products[["Product_ID", "Product_Category"]], on="Product_ID", how="left")

# Analyze refunds by product category
refund_by_category = transaction_product.groupby("Product_Category").agg(Total_Transactions=("Transaction_ID", "count"),
                                                                        Total_Amount=("Amount", "sum"),
                                                                        Refund_Transactions=("Transaction_Type", lambda x: (x == "Refund").sum()))

refund_by_category["Refund_Rate_%"] = refund_by_category["Refund_Transactions"] / refund_by_category["Total_Transactions"] * 100

print("\nRefund Analysis by Product Category:")
print(refund_by_category.round(2))

print("\nMerged Dataset Shape:", transaction_product.shape)
print("Unique Transaction IDs:", transaction_product["Transaction_ID"].nunique())

# 3.22.15 — Validate the product-category merge
print("\nValidation:")
print("Original Transaction Rows:", len(transactions))
print("Merged Transaction Rows:", len(transaction_product))
print("Unique Transaction IDs:", transaction_product["Transaction_ID"].nunique())
print("Missing Product Categories:", transaction_product["Product_Category"].isna().sum())
print("Original Refund-type transactions:", (transactions["Transaction_Type"] == "Refund").sum())
print("Refund-type transaction after merge:", (transaction_product["Transaction_Type"] == "Refund").sum())

missing_category_records = transaction_product[transaction_product["Product_Category"].isna()]

print("\nMissing Product-Category Records:")
print(missing_category_records[["Transaction_ID", "Customer_ID", "Subscription_ID", "Product_ID", "Transaction_Type", "Amount", "Payment_Status"]].head(10))

print("\nMissing Category Records:", len(missing_category_records))

print("\nMissing Product_ID Count:", missing_category_records["Product_ID"].isna().sum())

print("\nUnmatched Product_IDs:")
print(missing_category_records["Product_ID"].value_counts(dropna=False))

print("\nDoes P9999 exist in products?")
print(products["Product_ID"].eq("P9999").any())

print("\nMissing Product_ID records:")
print(missing_category_records.loc[missing_category_records["Product_ID"].isna(),["Transaction_ID", "Subscription_ID"]].head(10))

print("\nMissing Product_ID records with S999999:",(missing_category_records["Subscription_ID"] == "S999999").sum())

print("Total unmatched subscription references in transactions:",(transactions["Subscription_ID"] == "S999999").sum())

# 3.22.18: Analyze refund rates by transaction year
# Extract year from transaction date
transactions["Transaction_Year"] = (pd.to_datetime(transactions["Transaction_Date"],errors="coerce").dt.year)

# Analyze transactions by year
yearly_refund_analysis = transactions.groupby("Transaction_Year",dropna=False).agg(Total_Transactions=("Transaction_ID", "count"),
                                                                                   Total_Amount=("Amount", "sum"),
                                                                                   Refund_Transactions=("Transaction_Type", lambda x: (x == "Refund").sum()))

# Calculate yearly refund rate
yearly_refund_analysis["Refund_Rate_%"] = (yearly_refund_analysis["Refund_Transactions"] / yearly_refund_analysis["Total_Transactions"] * 100)

print("\nYearly Transaction and Refund Analysis:")
print(yearly_refund_analysis.round(2))

print("\nTotal transactions across yearly groups:", yearly_refund_analysis["Total_Transactions"].sum())

# 3.22.19: Calculate the overall refund rate
total_transactions = len(transactions)

refund_transactions = (transactions["Transaction_Type"] == "Refund").sum()

overall_refund_rate = (refund_transactions / total_transactions) * 100

print("\nTotal Transactions:", total_transactions)
print("Refund-Type Transactions:", refund_transactions)
print("Overall Refund Rate (%):", round(overall_refund_rate, 2))

print("\nValidation:")
print("Total transaction records:", len(transactions))

print("Total transaction amount:", round(transactions["Amount"].sum(), 2))

print("Refund-type transaction count:", (transactions["Transaction_Type"] == "Refund").sum())

print("Refund-type transaction amount:", round(transactions.loc[transactions["Transaction_Type"] == "Refund", "Amount"].sum(),2))

print("Refunded payment-status count:", (transactions["Payment_Status"] == "Refunded").sum())



# # 4. Export Final Reports
print("\nExporting Final Reports...")

# 4.1 Create an Output Folder 
os.makedirs("Python Pandas Technology & IT Industry Advance Project/final_reports", exist_ok=True)

# 4.2 Export Cleaned Datasets
customers.to_csv("Python Pandas Technology & IT Industry Advance Project/final_reports/customers_cleaned.csv", index=False)

subscriptions.to_csv("Python Pandas Technology & IT Industry Advance Project/final_reports/subscriptions_cleaned.csv", index=False)

transactions.to_csv("Python Pandas Technology & IT Industry Advance Project/final_reports/transactions_cleaned.csv", index=False)

support_tickets.to_csv("Python Pandas Technology & IT Industry Advance Project/final_reports/support_tickets_cleaned.csv", index=False)

products.to_csv("Python Pandas Technology & IT Industry Advance Project/final_reports/products_cleaned.csv", index=False)


