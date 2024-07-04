import pandas as pd

# Cols names.lower().strip()
# Standardizes the column names of the DataFrame by stripping whitespace, converting to lowercase and replacing spaces with underscores.
# Parameters:df (pd.DataFrame): The DataFrame whose columns are to be standardized.
# Returns: pd.DataFrame: The DataFrame with standardized column names.


def column_names(df):
    df.columns = [column.strip().lower().replace(" ", "_")
                  for column in df.columns]
    return df.columns

# Define categorical and numerical data


def extract_categorical_data(df):
    categorical_columns = ["Type", "Country", "State",
                           "Location", "Activity", "Name", "Sex", "Injury", "Source"]
    return df[categorical_columns]


def extract_numerical_data(df):
    numerical_columns = ["Date", "Year", "Age", "Time"]
    return df[numerical_columns]

# Columns: drop the columns with NaN


def drop_columns(df):
    column_to_drop = ['pdf', 'href formula', 'href', 'Case Number', 'Case Number.1',
                      'original order', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 11']
    df1 = df.copy()
    df1 = df1.drop(columns=column_to_drop)
    return df1


# remove all the rows have no values

def drop_all_na_rows(df):
    return df.dropna(how='all')


# Checking is we still have NaN columns

def check_all_nan_rows(df):
    all_nan_rows = df.isna().all(axis=1)
    return all_nan_rows
