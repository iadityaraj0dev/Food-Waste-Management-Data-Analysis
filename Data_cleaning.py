import pandas as pd

def clean_providers(df):
    df = df.drop_duplicates()

    # Standardize columns
    df.columns = df.columns.str.strip()

    df['Name'] = df['Name'].str.strip().str.title()
    df['Type'] = df['Type'].str.strip().str.title()
    df['City'] = df['City'].str.strip().str.title()

    # Handle nulls
    df['Contact'] = df['Contact'].fillna('Not Available')

    return df

# previous code

def clean_receivers(df):
    df = df.drop_duplicates()
    df.columns = df.columns.str.strip()

    # Standardize columns 
    df['Name'] = df['Name'].str.strip().str.title()
    df['Type'] = df['Type'].str.strip().str.title()
    df['City'] = df['City'].str.strip().str.title()

    # Handle nulls
    df['Contact'] = df['Contact'].fillna('Not Available')

    return df


def clean_food(df):
    df = df.drop_duplicates()
    df.columns = df.columns.str.strip()

    # Fix text
    df['Food_Name'] = df['Food_Name'].str.strip().str.title()
    df['Food_Type'] = df['Food_Type'].str.strip().str.lower()
    df['Meal_Type'] = df['Meal_Type'].str.strip().str.lower()
    df['Location'] = df['Location'].str.strip().str.title()

    # Fix quantity
    df = df[df['Quantity'] > 0]

    # Fix dates
    df['Expiry_Date'] = pd.to_datetime(df['Expiry_Date'], errors='coerce')

    return df


def clean_claims(df):
    df = df.drop_duplicates()
    df.columns = df.columns.str.strip()

    df['Status'] = df['Status'].str.strip().str.title()

    # Fix timestamp
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

    return df


if __name__ == "__main__":
    print("Data cleaning functions ready.")
