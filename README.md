# 🎬 Movie Recommendation System

A Machine Learning-based Movie Recommendation System built using Python, Streamlit, Collaborative Filtering, MovieLens Dataset, and OMDb API. The application recommends movies similar to a selected movie based on user rating patterns and displays detailed movie information including posters, ratings, cast, director, and plot summaries.

---

## 🚀 Features

* Movie recommendations using Collaborative Filtering
* Genre-based movie selection
* Interactive Streamlit web interface
* Movie posters fetched from OMDb API
* IMDb ratings and movie details
* Top-rated movies section
* Genre distribution visualization
* User-friendly dashboard

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Scikit-learn
* MovieLens Dataset
* OMDb API
* Requests

---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── u.data
│   └── u.item
│
└── screenshots/
```

---

## 📊 Dataset

This project uses the MovieLens 100K Dataset containing:

* 100,000 movie ratings
* 943 users
* 1,682 movies

Dataset includes:

* User IDs
* Movie IDs
* Ratings
* Movie Genres

---

## 🤖 Recommendation Algorithm

The system uses **Item-Based Collaborative Filtering**.

### Steps:

1. Create User-Movie Rating Matrix
2. Fill missing ratings with zeros
3. Calculate Cosine Similarity between movies
4. Identify similar movies
5. Recommend top matching movies

Cosine Similarity helps determine how closely related two movies are based on user ratings.

---

## 🎥 Movie Information

The application integrates with the OMDb API to fetch:

* Movie Poster
* IMDb Rating
* Release Year
* Director
* Actors
* Plot Summary

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Movie-Recommendation-System.git
```

### Navigate to Project Folder

```bash
cd Movie-Recommendation-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Application Features

### Genre Selection

Users can choose a preferred movie genre.

### Movie Selection

Users select a movie they have watched.

### Personalized Recommendations

The system recommends similar movies based on user behavior patterns.

### Analytics Dashboard

* Top Rated Movies
* Genre Distribution Chart

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```text
screenshots/homepage.png
screenshots/recommendations.png
```

---

## 🔮 Future Enhancements

* Content-Based Filtering
* Hybrid Recommendation System
* User Authentication
* Favorite Movie Lists
* Search Functionality
* TMDb API Integration
* Deployment on Streamlit Cloud

---

## 👨‍💻 Author

Jagadeesh Rallapalli

B.Tech Computer Science Engineering

Aspiring Software Engineer | Data Science Enthusiast | Machine Learning Learner

---

## ⭐ Support

If you found this project helpful, please consider giving it a star on GitHub.
