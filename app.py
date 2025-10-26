import streamlit as st
import pickle
import pandas as pd
import requests
from requests.exceptions import RequestException

# Page configuration
st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        padding: 0.5rem;
        border-radius: 5px;
    }
    .movie-card {
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
    .movie-title {
        font-weight: bold;
        margin-top: 10px;
        color: #1f1f1f;
    }
    </style>
    """, unsafe_allow_html=True)

# Load the saved models
@st.cache_data
def load_data():
    """Load pickled movie data and similarity matrix"""
    try:
        movies = pickle.load(open('movies.pkl', 'rb'))
        similarity = pickle.load(open('similarity.pkl', 'rb'))
        return movies, similarity
    except FileNotFoundError:
        st.error("Error: Model files not found. Please run the Jupyter notebook first to generate 'movies.pkl' and 'similarity.pkl'")
        return None, None
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None

# TMDB API configuration
TMDB_API_KEY = "YOUR_TMDB_API_KEY_HERE"  # Replace with your actual API key
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

def fetch_poster(movie_title):
    """
    Fetch movie poster from TMDB API
    
    Parameters:
    movie_title (str): Title of the movie
    
    Returns:
    str: URL of the movie poster or placeholder image
    """
    try:
        # Search for the movie
        search_url = f"{TMDB_BASE_URL}/search/movie"
        params = {
            'api_key': TMDB_API_KEY,
            'query': movie_title
        }
        response = requests.get(search_url, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                poster_path = data['results'][0].get('poster_path')
                if poster_path:
                    return f"{TMDB_IMAGE_BASE_URL}{poster_path}"
        
        # Return placeholder if poster not found
        return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"
    
    except RequestException:
        return "https://via.placeholder.com/500x750.png?text=No+Poster+Available"
    except Exception as e:
        return "https://via.placeholder.com/500x750.png?text=Error+Loading+Poster"

def recommend(movie, movies_df, similarity_matrix):
    """
    Recommend top 5 similar movies
    
    Parameters:
    movie (str): Title of the movie
    movies_df (DataFrame): Movie dataframe
    similarity_matrix (ndarray): Cosine similarity matrix
    
    Returns:
    tuple: (list of movie titles, list of poster URLs)
    """
    try:
        # Get the index of the movie
        movie_index = movies_df[movies_df['title'] == movie].index[0]
        
        # Get similarity scores
        distances = similarity_matrix[movie_index]
        
        # Get top 5 similar movies (excluding the movie itself)
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        # Get movie titles and posters
        recommended_movies = []
        recommended_posters = []
        
        for i in movies_list:
            movie_title = movies_df.iloc[i[0]].title
            recommended_movies.append(movie_title)
            recommended_posters.append(fetch_poster(movie_title))
        
        return recommended_movies, recommended_posters
    
    except IndexError:
        st.error(f"Movie '{movie}' not found in the database. Please check the title and try again.")
        return [], []
    except Exception as e:
        st.error(f"Error generating recommendations: {str(e)}")
        return [], []

# Main app
def main():
    # Header
    st.title("🎬 Movie Recommendation System")
    st.markdown("### Discover movies similar to your favorites!")
    st.markdown("---")
    
    # Load data
    movies_df, similarity_matrix = load_data()
    
    if movies_df is None or similarity_matrix is None:
        st.stop()
    
    # Sidebar
    with st.sidebar:
        st.header("About")
        st.info(
            """
            This is a **Content-Based Movie Recommendation System** 
            that suggests movies based on:
            - Plot Overview
            - Genres
            - Keywords
            - Cast
            - Director
            
            The system uses **Cosine Similarity** to find movies 
            with similar content features.
            """
        )
        
        st.header("📊 Dataset Info")
        st.write(f"Total Movies: **{len(movies_df)}**")
        
        st.header("🔧 Technology Stack")
        st.write("- Python")
        st.write("- Scikit-learn")
        st.write("- Pandas")
        st.write("- Streamlit")
        st.write("- TMDB API")
    
    # Main content
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Movie selection
        selected_movie = st.selectbox(
            "Select a movie you like:",
            movies_df['title'].values,
            index=0
        )
    
    with col2:
        st.write("")
        st.write("")
        recommend_button = st.button("Get Recommendations", use_container_width=True)
    
    # Alternative: Text input
    with st.expander("Or type a movie name"):
        movie_input = st.text_input("Enter movie title:")
        if movie_input:
            if movie_input in movies_df['title'].values:
                selected_movie = movie_input
                recommend_button = True
            else:
                st.warning("Movie not found in database. Please select from the dropdown.")
    
    # Display recommendations
    if recommend_button:
        with st.spinner('Finding similar movies...'):
            recommended_movies, recommended_posters = recommend(selected_movie, movies_df, similarity_matrix)
        
        if recommended_movies:
            st.success(f"Movies similar to **{selected_movie}**:")
            st.markdown("---")
            
            # Display recommendations in columns
            cols = st.columns(5)
            
            for idx, col in enumerate(cols):
                with col:
                    st.markdown(
                        f'<div class="movie-card">'
                        f'<img src="{recommended_posters[idx]}" width="100%">'
                        f'<p class="movie-title">{recommended_movies[idx]}</p>'
                        f'</div>',
                        unsafe_allow_html=True
                    )
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: gray;'>
            <p>Built with ❤️ using Streamlit | Data from TMDB 5000 Movie Dataset</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
