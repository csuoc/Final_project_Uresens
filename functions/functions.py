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

def add_text_sidebar():
    import streamlit as st
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "UreSens Labs";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 80px;
                }
            </style>
            """,
            unsafe_allow_html=True
    )

def resize_images(image_path, width, height):
    from PIL import Image
    img = Image.open(image_path)
    resized_image = img.resize((width, height))
    return resized_image

def check_password():
    """Returns `True` if the user had a correct password."""
    import streamlit as st
    
    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True