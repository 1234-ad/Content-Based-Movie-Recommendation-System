"""
Utility functions for the Movie Recommendation System
"""

import pickle
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


def load_models(movies_path='movies.pkl', similarity_path='similarity.pkl'):
    """
    Load pickled models
    
    Parameters:
    movies_path (str): Path to movies pickle file
    similarity_path (str): Path to similarity matrix pickle file
    
    Returns:
    tuple: (movies_df, similarity_matrix)
    """
    try:
        movies = pickle.load(open(movies_path, 'rb'))
        similarity = pickle.load(open(similarity_path, 'rb'))
        return movies, similarity
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None


def get_movie_recommendations(movie_title, movies_df, similarity_matrix, n=5):
    """
    Get movie recommendations
    
    Parameters:
    movie_title (str): Title of the movie
    movies_df (DataFrame): Movie dataframe
    similarity_matrix (ndarray): Cosine similarity matrix
    n (int): Number of recommendations (default: 5)
    
    Returns:
    list: List of recommended movie titles
    """
    try:
        # Get movie index
        movie_index = movies_df[movies_df['title'] == movie_title].index[0]
        
        # Get similarity scores
        distances = similarity_matrix[movie_index]
        
        # Sort and get top n+1 (excluding the movie itself)
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:n+1]
        
        # Extract movie titles
        recommendations = [movies_df.iloc[i[0]].title for i in movies_list]
        
        return recommendations
    
    except IndexError:
        return f"Movie '{movie_title}' not found in database"
    except Exception as e:
        return f"Error: {str(e)}"


def get_movie_details(movie_title, movies_df, similarity_matrix, n=5):
    """
    Get movie recommendations with similarity scores
    
    Parameters:
    movie_title (str): Title of the movie
    movies_df (DataFrame): Movie dataframe
    similarity_matrix (ndarray): Cosine similarity matrix
    n (int): Number of recommendations (default: 5)
    
    Returns:
    DataFrame: DataFrame with movie titles and similarity scores
    """
    try:
        movie_index = movies_df[movies_df['title'] == movie_title].index[0]
        distances = similarity_matrix[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:n+1]
        
        result = pd.DataFrame({
            'Movie': [movies_df.iloc[i[0]].title for i in movies_list],
            'Similarity Score': [i[1] for i in movies_list]
        })
        
        return result
    
    except IndexError:
        return f"Movie '{movie_title}' not found in database"
    except Exception as e:
        return f"Error: {str(e)}"


def search_movies(query, movies_df, limit=10):
    """
    Search for movies by title
    
    Parameters:
    query (str): Search query
    movies_df (DataFrame): Movie dataframe
    limit (int): Maximum number of results
    
    Returns:
    list: List of matching movie titles
    """
    query_lower = query.lower()
    matches = movies_df[movies_df['title'].str.lower().str.contains(query_lower)]
    return matches['title'].head(limit).tolist()


def get_random_movies(movies_df, n=5):
    """
    Get random movies from the database
    
    Parameters:
    movies_df (DataFrame): Movie dataframe
    n (int): Number of random movies
    
    Returns:
    list: List of random movie titles
    """
    return movies_df['title'].sample(n=n).tolist()


def calculate_diversity_score(recommendations, similarity_matrix, movies_df):
    """
    Calculate diversity score of recommendations
    (Lower score means more diverse recommendations)
    
    Parameters:
    recommendations (list): List of recommended movie titles
    similarity_matrix (ndarray): Cosine similarity matrix
    movies_df (DataFrame): Movie dataframe
    
    Returns:
    float: Average pairwise similarity score
    """
    try:
        indices = [movies_df[movies_df['title'] == movie].index[0] for movie in recommendations]
        similarities = []
        
        for i in range(len(indices)):
            for j in range(i+1, len(indices)):
                similarities.append(similarity_matrix[indices[i]][indices[j]])
        
        return np.mean(similarities) if similarities else 0
    
    except Exception as e:
        return f"Error: {str(e)}"


def get_statistics(movies_df, similarity_matrix):
    """
    Get statistics about the recommendation system
    
    Parameters:
    movies_df (DataFrame): Movie dataframe
    similarity_matrix (ndarray): Cosine similarity matrix
    
    Returns:
    dict: Dictionary with statistics
    """
    stats = {
        'total_movies': len(movies_df),
        'matrix_shape': similarity_matrix.shape,
        'avg_similarity': np.mean(similarity_matrix),
        'max_similarity': np.max(similarity_matrix),
        'min_similarity': np.min(similarity_matrix[similarity_matrix > 0])
    }
    return stats


if __name__ == "__main__":
    # Example usage
    movies, similarity = load_models()
    
    if movies is not None:
        print("Models loaded successfully!")
        print(f"Total movies: {len(movies)}")
        
        # Test recommendation
        test_movie = "Avatar"
        recommendations = get_movie_recommendations(test_movie, movies, similarity)
        print(f"\nRecommendations for '{test_movie}':")
        for i, movie in enumerate(recommendations, 1):
            print(f"{i}. {movie}")
        
        # Get statistics
        stats = get_statistics(movies, similarity)
        print(f"\nSystem Statistics:")
        for key, value in stats.items():
            print(f"{key}: {value}")
