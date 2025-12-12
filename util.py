import pandas as pd
import joblib


model = joblib.load("random_forest_movie_success_model.pkl")
title_encoder = joblib.load("title_encoder.pkl")
director_encoder = joblib.load("director_encoder.pkl")
imputer = joblib.load("imputer.pkl")

df = pd.read_csv("movie_success_rate.csv")

df = df.rename(columns={
    'Revenue (Millions)': 'Revenue_Millions',
    'Runtime (Minutes)': 'Runtime_Minutes'
})

df = df[['Title', 'Director']]

def get_titles_and_directors():
    titles = df['Title'].unique().tolist()
    directors = df['Director'].unique().tolist()
    return titles, directors


def predict_movie_success(data):
    """
    data = JSON input dictionary from POST request
    """

    try:
        title = title_encoder.transform([data['Title']])[0]
        director = director_encoder.transform([data['Director']])[0]

    except Exception:
        return "Invalid Title or Director"

    input_df = pd.DataFrame({
        'Title': [title],
        'Director': [director],
        'Runtime_Minutes': [data['Runtime_Minutes']],
        'Rating': [data['Rating']],
        'Revenue_Millions': [data['Revenue_Millions']],
        'Action': [data['Action']],
        'Adventure': [data['Adventure']],
        'Comedy': [data['Comedy']],
        'Family': [data['Family']],
        'Horror': [data['Horror']],
        'Sport': [data['Sport']]
    })

    input_df_imputed = imputer.transform(input_df)

    prediction = model.predict(input_df_imputed)[0]

    if prediction == 1:
        return "Success"
    else:
        return "Fail"
