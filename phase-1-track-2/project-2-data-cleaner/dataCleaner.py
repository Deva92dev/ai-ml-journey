import pandas as pd
import re

# keep using messy kaggle datasets for learning

data_file = "customerData.csv"

expected_types = {
    'CustomerID': "int",
    'CustomerName': "str",
    'Age': "int",
    'Gender': "text",               
    'Email': "text",                
    'Phone': "text",              
    'SignupDate': "datet",           
    'Country': "text",            
    'PurchaseAmount' : "int",       
    'MembershipStatus': "text"    
}

def load_csv(file):
    df = pd.read_csv(file, on_bad_lines="warn")
    return df

def display_data_structure(df):
    data_type = df.dtypes
    return data_type

def shape_of_data(df):
    rows = df.shape[0]
    cols = df.shape[1]
    return rows, cols


def display_missing_values(df):
    missing = df.isnull().sum()
    return missing

def total_missing_values(df):
    missing_count = df.isnull().values.sum()
    return missing_count

def display_duplicate_values(df):
    duplicates = df[df.duplicated(keep=False)]
    return duplicates

def total_duplicates_count(df):
    total_duplicates = df.duplicated().sum()
    return total_duplicates

def display_invalid_data(df):
    phone = df[pd.to_numeric(df['Phone'], errors='coerce').isna()]
    price = df[pd.to_numeric(df['PurchaseAmount'], errors='coerce').isna()]
    age = df[pd.to_numeric(df['Age'], errors='coerce').isna()]
    signup_date = df[pd.to_datetime(df['SignupDate'], errors='coerce').isna()]
    return phone, age, signup_date, price

def total_invalid_counts_from_display(df):
    phone, age, signup_date, price = display_invalid_data(df)
    invalid_phone_count = len(phone) 
    invalid_price_count = len(price)
    invalid_age_count = len(age)
    invalid_signup_count = len(signup_date)
    invalid_counts_from_display = invalid_phone_count + invalid_age_count + invalid_price_count + invalid_signup_count
    return invalid_counts_from_display


def wrong_data_types(df):
    for col, expected in expected_types.items():
        actual = df[col].dtype
        if actual != expected:
            print(f"Column {col} has dtype {df[col].dtype}, expected {expected}")


# name, email, country
def detect_text_formatting(df):
    email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    df["valid_email"] = df['Email'].str.match(email, na=False)
    emails = df[~df['valid_email']]

    names_spacs = df["CustomerName"].str.startswith(' ')
    names = df[names_spacs]

    country_mixed = df["Country"].str.match(r'^(?:[A-Z][a-z]+(?:\s[A-Z][a-z]+)*)$')
    countries = df[country_mixed]

    return emails, names, countries


def total_invalid_counts_from_formatting(df):
    emails, names, countries = detect_text_formatting(df)
    invalid_emails_count = emails.shape[0]
    invalid_names_count = len(names)
    invalid_countries_count = len(countries)
    invalid_counts_from_formatting = invalid_emails_count + invalid_names_count + invalid_countries_count
    return invalid_counts_from_formatting   


def display_report(df):
    data_type = display_data_structure(df)
    missing = display_missing_values(df)
    duplicates = display_duplicate_values(df)
    phone, age, signup_date, price = display_invalid_data(df)
    return data_type, missing, duplicates, phone, age, signup_date, price

def inspection_report(df):
    row, cols = shape_of_data(df)
    total_missing = total_missing_values(df)
    duplicates = total_duplicates_count(df)
    invalid_counts_from_display = total_invalid_counts_from_display(df)
    invalid_counts_from_formatting = total_invalid_counts_from_formatting(df)
    invalids = invalid_counts_from_formatting + invalid_counts_from_display
    return row, cols, total_missing, duplicates, invalids


def print_statement(text, *args):
    print(text, *args)

def main():
    df = load_csv(data_file)
    data_type, missing, duplicates, invalid, age, signup_date, price = display_report(df)
    row, cols, total_missing, all_duplicates, invalids = inspection_report(df)
    
    print_statement("Data types: ", data_type)
    print_statement("Missing Values:\n ", missing)
    print_statement("Duplicate Values: ", duplicates)
    print_statement("Invalid Values: ", invalid)
    print_statement("Invalid Age: ", age)
    print_statement("Invalid Signup format: ", signup_date)
    print_statement("Invalid prices: ", price)

    emails, names, countries = detect_text_formatting(df)
    print_statement("unformatted emails: ", emails)
    print_statement("unformatted names: ", names)
    print_statement("unformatted countries: ", countries)
    wrong_data_types(df)

    print_statement("all rows: ", row)
    print_statement("all columns: ", cols)
    print_statement("all missing values count: ", total_missing)
    print_statement("all duplicate counts: ", all_duplicates)
    print_statement("all invalids data count: ", invalids)

if __name__ == "__main__":
    main()