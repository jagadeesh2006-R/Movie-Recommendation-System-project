import pandas as pd# type: ignore
import numpy as np# type: ignore
import requests# type: ignore
import streamlit as st # type: ignore

from sklearn.metrics.pairwise import cosine_similarity # type: ignore

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    layout="wide"
)

st.title("🎬 Movie Recommendation System")

st.markdown(
    "Get movie recommendations based on genres and watched movies."
)

# ---------------------------------------------------
# OMDb API KEY
# ---------------------------------------------------
API_KEY = "ef238b94"

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------
ratings = pd.read_csv(
    'u.data',
    sep='\t',
    names=['user_id', 'movie_id', 'rating', 'timestamp']
)

movie_cols = [
    'movie_id', 'title', 'release_date', 'video_release_date',
    'IMDb_URL', 'unknown', 'Action', 'Adventure', 'Animation',
    'Children', 'Comedy', 'Crime', 'Documentary', 'Drama',
    'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery',
    'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western'
]

movies = pd.read_csv(
    'u.item',
    sep='|',
    encoding='latin-1',
    names=movie_cols
)

# ---------------------------------------------------
# MERGE DATA
# ---------------------------------------------------
data = pd.merge(ratings, movies, on='movie_id')

# ---------------------------------------------------
# GENRE LIST
# ---------------------------------------------------
genres = [
    'Action', 'Adventure', 'Animation', 'Children',
    'Comedy', 'Crime', 'Documentary', 'Drama',
    'Fantasy', 'Film-Noir', 'Horror', 'Musical',
    'Mystery', 'Romance', 'Sci-Fi', 'Thriller',
    'War', 'Western'
]

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.header("🎯 Select Preferences")

selected_genre = st.sidebar.selectbox(
    "Choose Genre",
    genres
)

# ---------------------------------------------------
# FILTER MOVIES BY GENRE
# ---------------------------------------------------
genre_movies = movies[movies[selected_genre] == 1]

movie_list = sorted(genre_movies['title'].tolist())

selected_movie = st.sidebar.selectbox(
    "Select Watched Movie",
    movie_list
)

# ---------------------------------------------------
# CREATE USER-MOVIE MATRIX
# ---------------------------------------------------
movie_matrix = data.pivot_table(
    index='user_id',
    columns='title',
    values='rating'
)

movie_matrix_filled = movie_matrix.fillna(0)

# ---------------------------------------------------
# COLLABORATIVE FILTERING
# ---------------------------------------------------
similarity = cosine_similarity(movie_matrix_filled.T)

similarity_df = pd.DataFrame(
    similarity,
    index=movie_matrix.columns,
    columns=movie_matrix.columns
)

# ---------------------------------------------------
# AVERAGE RATINGS
# ---------------------------------------------------
avg_ratings = data.groupby('title')['rating'].mean()

rating_counts = data.groupby('title')['rating'].count()

# ---------------------------------------------------
# FETCH MOVIE DETAILS
# ---------------------------------------------------
def fetch_movie_details(movie_name):

    try:

        clean_name = movie_name.split('(')[0].strip()

        url = f"http://www.omdbapi.com/?t={clean_name}&apikey={API_KEY}"

        response = requests.get(url)

        movie_data = response.json()

        if movie_data['Response'] == 'True':
            return movie_data

    except:
        pass

    return None

# ---------------------------------------------------
# RECOMMEND MOVIES
# ---------------------------------------------------
def recommend_movies(movie_name, n=10):

    if movie_name not in similarity_df.columns:
        return []

    similar_scores = similarity_df[movie_name]

    similar_movies = similar_scores.sort_values(
        ascending=False
    )

    similar_movies = similar_movies.iloc[1:n+1]

    return similar_movies.index.tolist()

# ---------------------------------------------------
# DISPLAY SELECTED MOVIE
# ---------------------------------------------------
st.subheader("🎥 Selected Movie")

col1, col2 = st.columns([1, 2])

movie_details = fetch_movie_details(selected_movie)

with col1:

    if movie_details and movie_details['Poster'] != "N/A":
        st.image(movie_details['Poster'])

with col2:

    st.markdown(f"## {selected_movie}")

    if selected_movie in avg_ratings:
        st.write(
            f"⭐ Average Rating: "
            f"{round(avg_ratings[selected_movie], 2)} / 5"
        )

    if selected_movie in rating_counts:
        st.write(
            f"👥 Total Ratings: "
            f"{rating_counts[selected_movie]}"
        )

    if movie_details:

        st.write(f"📅 Year: {movie_details.get('Year', 'N/A')}")

        st.write(f"🎭 Genre: {movie_details.get('Genre', 'N/A')}")

        st.write(f"🎬 Director: {movie_details.get('Director', 'N/A')}")

        st.write(f"👨‍🎤 Actors: {movie_details.get('Actors', 'N/A')}")

        st.write(
            f"⭐ IMDb Rating: "
            f"{movie_details.get('imdbRating', 'N/A')}"
        )

        st.write("📝 Plot:")

        st.info(movie_details.get('Plot', 'No plot available'))

# ---------------------------------------------------
# RECOMMENDATIONS
# ---------------------------------------------------
st.subheader("🔥 Recommended Movies")

recommendations = recommend_movies(selected_movie)

cols = st.columns(5)

for idx, movie in enumerate(recommendations[:5]):

    movie_info = fetch_movie_details(movie)

    with cols[idx]:

        if movie_info and movie_info['Poster'] != "N/A":
            st.image(movie_info['Poster'])

        st.write(f"### {movie}")

        if movie in avg_ratings:
            st.write(
                f"⭐ {round(avg_ratings[movie], 2)}"
            )

        if movie_info:
            st.write(
                f"📅 {movie_info.get('Year', 'N/A')}"
            )

# ---------------------------------------------------
# TOP RATED MOVIES
# ---------------------------------------------------
st.subheader("🏆 Top Rated Movies")

top_movies = (
    data.groupby('title')['rating']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

top_movies_df = pd.DataFrame({
    'Movie': top_movies.index,
    'Rating': top_movies.values
})

st.dataframe(top_movies_df)

# ---------------------------------------------------
# GENRE DISTRIBUTION
# ---------------------------------------------------
st.subheader("📊 Genre Distribution")

genre_counts = []

for genre in genres:
    genre_counts.append(movies[genre].sum())

genre_df = pd.DataFrame({
    'Genre': genres,
    'Movies Count': genre_counts
})

st.bar_chart(
    genre_df.set_index('Genre')
)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")

st.markdown(
    "Developed using Python, Streamlit, Collaborative Filtering, "
    "MovieLens Dataset, and OMDb API"
)
