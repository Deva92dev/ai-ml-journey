import pandas as pd

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

def wrong_data_types(df):
    for col, expected in expected_types.items():
        actual = str(df[col].dtype)
        
def text_formatting(df):
    df["CustomerName"] = df["CustomerName"].str.strip().str.title()

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
    return row, cols, missing, duplicates



def print_statement(text, *args):
    print(text, *args)

def main():
    df = load_csv(data_file)
    data_type, missing, duplicates, invalid, age, signup_date, price = display_report(df)
    row, cols, all_missing, all_duplicates = inspection_report(df)
    
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

    text_formatting(df)
    wrong_data_types(df)

if __name__ == "__main__":
    main()