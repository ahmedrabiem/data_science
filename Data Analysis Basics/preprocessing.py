def check_data_types(df):
    return df.dtypes

def convert_data_type(df, column, new_type):
    df[column] = df[column].astype(new_type)
    return df

def check_missing_values(df):
    return df.isnull().sum()

def fill_missing_with_mean(df, column):
    df[column] = df[column].fillna(df[column].mean())
    return df

def fill_missing_with_median(df, column):
    df[column] = df[column].fillna(df[column].median())
    return df

def fill_missing_with_mode(df, column):
    df[column] = df[column].fillna(df[column].mode()[0])
    return df

def drop_missing(df):
    df = df.dropna()
    return df