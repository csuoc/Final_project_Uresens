def remove_columns(df, column_name):
    
    """
    This is a function that removes undesired columns. Requires two arguments.
    Arguments: dataframe, column name
    Input: the current dataframe
    Output: the current dataframe without the selected columns
    """
    
    df.drop(columns=f"{column_name}", inplace=True)
    
    return df

def rename_columns(df, old_name, new_name):
    
    """
    This a functions that renames the name of any given columns. Requires three arguments.
    Arguments: dataframe, old name of the column, new name of the column.
    Input: the current column name
    Output: the column renamed
    """
    
    df.rename(columns={f"{old_name}": f"{new_name}"}, inplace=True)
    return df

def integrify(df, column_name):
    """
    This is a function that integers any value. Requires two arguments.
    Arguments: dataframe, name of the column where you want to rewrite the values
    Input: a string or float
    Output: an interger
    """
    df[f"{column_name}"] = df[f"{column_name}"].astype(int)
    return df