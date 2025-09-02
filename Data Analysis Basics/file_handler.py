import pandas as pd
import sqlite3

# Reading Functions

def read_csv(path):
    return pd.read_csv(path)

def read_excel(path):
    return pd.read_excel(path)

def read_json(path):
    return pd.read_json(path)

def read_db(connection_string, query="SELECT * FROM students"):
    conn = sqlite3.connect(connection_string)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Saving Functions

def save_csv(df, path):
    df.to_csv(path, index=False)

def save_excel(df, path):
    df.to_excel(path, index=False)

def save_json(df, path):
    df.to_json(path, orient="records", indent=4)

def save_db(df, connection_string, table_name="students"):
    conn = sqlite3.connect(connection_string)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
