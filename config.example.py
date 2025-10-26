# Configuration file for the Movie Recommendation System
# Copy this file to config.py and add your actual API key

# TMDB API Configuration
TMDB_API_KEY = "YOUR_TMDB_API_KEY_HERE"
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

# Model Configuration
MAX_FEATURES = 5000  # Number of features for CountVectorizer
TOP_N_RECOMMENDATIONS = 5  # Number of recommendations to return
TOP_N_CAST = 3  # Number of cast members to include

# File Paths
MOVIES_PKL = "movies.pkl"
SIMILARITY_PKL = "similarity.pkl"
VECTORIZER_PKL = "vectorizer.pkl"

# Streamlit Configuration
PAGE_TITLE = "Movie Recommender System"
PAGE_ICON = "🎬"
LAYOUT = "wide"

# Dataset Paths
MOVIES_CSV = "tmdb_5000_movies.csv"
CREDITS_CSV = "tmdb_5000_credits.csv"
