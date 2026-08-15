import pandas as pd

# keep using messy kaggle datasets for learning

data_file = (
    r"C:\Users\acer\Desktop\AI ML Ideas Build\Python AI ML\phase-1-track-2\project-2-data-cleaner\customerData.csv"
)

def load_csv(file):
    df = pd.read_csv(file, on_bad_lines="warn")
    return df

def inspect_structure(file):
    df = load_csv(file)
    info = df.info()
    return info

def describe_data(file):
    df = load_csv(file)
    describe = df.describe()
    return describe

def missing_values(file):
    df = load_csv(file)
    missing = df.isnull().sum()
    return missing

def duplicate_values(file):
    df= load_csv(file)
    duplicates = df.duplicated().sum()
    return duplicates

def generate_report(file):
    info = inspect_structure(file)
    describe = describe_data(file)
    missing = missing_values(file)
    duplicates = duplicate_values(file)
    return info, describe, missing, duplicates

def print_statement(text, func):
    print(text, func)

def main():
    info, describe, missing, duplicates = generate_report(data_file)
    print_statement("Info: ", info)
    print_statement("Data Description: ", describe)
    print_statement("Missing Values:\n ", missing)
    print_statement("Duplicate Values: ", duplicates)

if __name__ == "__main__":
    main()