import pandas as pd

# keep using messy kaggle datasets for learning

data_file = "customerData.csv"

expected_types = {
    'customer_id': "int64",
    'customer_name': "str",
    'age': "int",
    'gender': "str",               
    'email': "str",                
    'phone': "int",              
    'signup_date': "datetime",           
    'country': "str",            
    'purchase_amount' : "int",       
    'membership_status': "text"    
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

def missing_values_count(df):
    missing = df.isnull().sum(axis=1)
    return missing


def display_duplicate_values(df):
    duplicates = df[df.duplicated(keep=False)]
    return duplicates

def duplicate_values_count(df):
    duplicates = df.duplicated().sum()
    return duplicates


def display_invalid_data(df):
    phone = df[pd.to_numeric(df['Phone'], errors='coerce').isna()]
    price = df[pd.to_numeric(df['PurchaseAmount'], errors='coerce').isna()]
    age = df[pd.to_numeric(df['Age'], errors='coerce').isna()]
    signup_date = df[pd.to_datetime(df['SignupDate'], errors='coerce').isna()]
    return phone, age, signup_date, price

def wrong_data_types_count(df):
    new = df['Age'].apply(type).value_counts()
    ids = df['Gender'].apply(type).value_counts()
    email = df['Email'].apply(type).value_counts()
    phone = df['Phone'].apply(type).value_counts()
    amount = df["PurchaseAmount"].apply(type).value_counts()
    return new, ids, email, phone, amount

def display_report(df):
    data_type = display_data_structure(df)
    missing = display_missing_values(df)
    duplicates = display_duplicate_values(df)
    phone, age, signup_date, price = display_invalid_data(df)
    return data_type, missing, duplicates, phone, age, signup_date, price

def inspection_report(df):
    row, cols = shape_of_data(df)
    missing = missing_values_count(df)
    duplicates = duplicate_values_count(df)
    new, ids, email, phone, amount = wrong_data_types_count(df)

    return row, cols, missing, duplicates, new, ids, email, phone, amount



def print_statement(text, *args):
    print(text, *args)

def main():
    df = load_csv(data_file)
    data_type, missing, duplicates, invalid, age, signup_date, price = display_report(df)
    row, cols, all_missing, all_duplicates, new, ids, email, phone, amount = inspection_report(df)
    
    print_statement("Data types: ", data_type)
    print_statement("Missing Values:\n ", missing)
    print_statement("Duplicate Values: ", duplicates)
    print_statement("Invalid Values: ", invalid)
    print_statement("Invalid Age: ", age)
    print_statement("Invalid Signup format: ", signup_date)
    print_statement("Invalid prices: ", price)

    print_statement("row inspection: ", row)
    print_statement("cols inpection: ", cols)
    print_statement("all missing values count: ", all_missing)
    print_statement("all duplicate counts: ", all_duplicates)
    print_statement("all missing age count: ", new)
    print_statement("all gender missing count: ", ids)
    print_statement("all missing email count: ", email)
    print_statement("all missing phones count: ", phone)
    print_statement("all missing purchase amount: ", amount)

if __name__ == "__main__":
    main()