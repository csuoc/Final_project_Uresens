# Import box
from sqltools.sql_connection import engine
import pandas as pd

# Defining queries

def get_everything ():
    query = """SELECT * FROM samples;"""
    df = pd.read_sql_query(query, engine)
    return df

def insert_one_row (patientid, blood_pressure, albumin, sugar, blood_urea, creatinine, hypertension):
    query = f"""INSERT INTO samples
     (patient, blood_pressure, albumin, sugar, blood_urea, creatinine, hypertension, ckd) 
        VALUES ('{patientid}', '{blood_pressure}', '{albumin}', '{sugar}', '{blood_urea}', '{creatinine}', '{hypertension}');
    """
    engine.execute(query)
    return f"Correctly introduced!"

def delete_one_row (patientid):
    query = f"""DELETE FROM samples
            WHERE patient = '{patientid}';
            """
    engine.execute(query)
    return f"Sucessfully deleted!"