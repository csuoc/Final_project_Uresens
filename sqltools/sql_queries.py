# Import box
from sqlconfig.sql_connection import engine
import pandas as pd

# Defining queries

def get_everything ():
    query = """SELECT * FROM patients;"""
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def insert_one_row (patient, blood_pressure, albumin, sugar, blood_urea, creatinine, hypertension, ckd):
    query = f"""INSERT INTO patients
     (patient, blood_pressure, albumin, sugar, blood_urea, creatinine, hypertension, ckd) 
        VALUES ('{patient}', '{blood_pressure}', '{albumin}', '{sugar}', '{blood_urea}', '{creatinine}', '{hypertension}', '{ckd}');
    """
    engine.execute(query)
    return f"Correctly introduced!"

def delete_one_row (patient):
    query = f"""DELETE FROM patients
            WHERE patient = '{patient}';
            """
    engine.execute(query)
    return f"Sucessfully deleted!"