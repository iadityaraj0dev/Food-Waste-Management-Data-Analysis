import sqlite3
import pandas as pd
from Data_cleaning import (
    clean_providers,
    clean_receivers,
    clean_food,
    clean_claims
)
conn = sqlite3.connect("food.db")
cursor = conn.cursor() 
def create_tables():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS providers (
        Provider_ID INTEGER PRIMARY KEY,
        Name TEXT,
        Type TEXT,
        Address TEXT,
        City TEXT,
        Contact NUMERIC
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS receivers (
        Receiver_ID INTEGER PRIMARY KEY,
        Name TEXT,
        Type TEXT,
        City TEXT,
        Contact NUMERIC
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS food_listings (
        Food_ID INTEGER PRIMARY KEY,
        Food_Name TEXT,
        Quantity INTEGER,
        Expiry_Date TEXT,
        Provider_ID INTEGER,
        Provider_Type TEXT,
        Location TEXT,
        Food_Type TEXT,
        Meal_Type TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS claims (
        Claim_ID INTEGER PRIMARY KEY,
        Food_ID INTEGER,
        Receiver_ID INTEGER,
        Status TEXT,
        Timestamp TEXT
    )
    """)

    conn.commit()

def load_data():

    providers = clean_providers(pd.read_csv("providers_data.csv"))
    receivers = clean_receivers(pd.read_csv("receivers_data.csv"))
    food = clean_food(pd.read_csv("food_listings_data.csv"))
    claims = clean_claims(pd.read_csv("claims_data.csv"))

    providers.to_sql("providers", conn, if_exists="replace", index=False)
    receivers.to_sql("receivers", conn, if_exists="replace", index=False)
    food.to_sql("food_listings", conn, if_exists="replace", index=False)
    claims.to_sql("claims", conn, if_exists="replace", index=False)

    conn.commit()
    
if __name__ == "__main__":
    create_tables()
    load_data()
    conn.close()
    print("Database created and data inserted successfully!")
