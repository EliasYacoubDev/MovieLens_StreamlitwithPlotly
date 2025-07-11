import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

# Step 1: Load data from SQLite
@st.cache_data
def load_data():
    conn = sqlite3.connect('db/movielens.db')  # or your DB path
    query = """
    SELECT 
        u.UserID,
        u.Gender,
        u.Age,
        u.Occupation,
        u.Zipcode,
        m.MovieID,
        m.Title,
        m.Genres,
        m.Year,
        r.Rating,
        r.Timestamp
    FROM ratings AS r
    INNER JOIN users AS u ON r.UserID = u.UserID
    INNER JOIN movies AS m ON r.MovieID = m.MovieID;
    """
    df = pd.read_sql_query(query, conn)
    df['Genres'] = df['Genres'].str.split('|')
    df = df.explode('Genres').reset_index(drop=True)
    df['YearofRating'] = pd.to_datetime(df['Timestamp'], unit='s').dt.year
    return df

df = load_data()

# Step 2: Streamlit layout
st.title("MovieLens EDA Dashboard")
st.markdown("""Explore demographic trends in movie ratings across gender, age, occupation, and zipcode.""")

# --- Gender Distribution ---
st.subheader("Gender Distribution")
gender_counts = df[['UserID', 'Gender']].drop_duplicates()['Gender'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Count']
fig_gender = px.bar(gender_counts,
                    x='Gender',
                    y='Count',
                    color='Gender',
                    title='Number of Users by Gender')
st.plotly_chart(fig_gender, use_container_width=True)

# --- Ratings by Gender per Genre
st.subheader("Ratings by Gender per Genre")
rating_by_gender_genre = df.groupby(['Gender', 'Genres'])['Rating'].mean().reset_index()
fig_gender_genre = px.bar(
    rating_by_gender_genre, x='Genres', y='Rating', color='Gender',
    barmode='group', title='Average Rating by Gender per Genre'
)
st.plotly_chart(fig_gender_genre, use_container_width=True)

# --- Age Distribution ---
st.subheader("Age Distribution")
# Define the mapping
age_map = {
    1: "Under 18",
    18: "18–24",
    25: "25–34",
    35: "35–44",
    45: "45–49",
    50: "50–55",
    56: "56+"
}

# Apply the mapping
df['AgeGroup'] = df['Age'].map(age_map)

unique_users = df[['UserID', 'AgeGroup']].drop_duplicates()

# Define the order of age groups
age_order = ["Under 18", "18–24", "25–34", "35–44", "45–49", "50–55", "56+"]

# Create histogram
fig_age = px.histogram(
    unique_users,
    x='AgeGroup',
    category_orders={'AgeGroup': age_order},
    color='AgeGroup',
    title='Histogram of Users by Age Group'
)

# Show in Streamlit
st.plotly_chart(fig_age, use_container_width=True)

# --- Average Rating by Age Group per Genre ---
st.subheader("Average Rating by Age Group per Genre")
age_rating = df.groupby(['AgeGroup', 'Genres'])['Rating'].mean().reset_index()
fig_age_genre = px.bar(
    age_rating, x='Genres', y='Rating', color='AgeGroup',
    barmode='group', title='Average Rating by Age Group per Genre'
)
st.plotly_chart(fig_age_genre, use_container_width=True)