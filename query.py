import sqlite3
import pandas as pd

conn = sqlite3.connect("food.db")

def providers_receivers_per_city():
    query = """
    SELECT p.City,
           COUNT(DISTINCT p.Provider_ID) AS total_providers,
           COUNT(DISTINCT r.Receiver_ID) AS total_receivers
    FROM providers p
    LEFT JOIN receivers r ON p.City = r.City
    GROUP BY p.City
    """
    return pd.read_sql(query, conn)

if __name__ == "__main__":
 print(providers_receivers_per_city())
    