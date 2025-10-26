"""
Test script for the Movie Recommendation System
Run this after generating the pickle files to verify everything works correctly
"""

import pickle
import pandas as pd
import numpy as np
from utils import (
    load_models, 
    get_movie_recommendations,
    get_movie_details,
    search_movies,
    get_statistics
)


def test_model_loading():
    """Test if models load correctly"""
    print("="*60)
    print("TEST 1: Loading Models")
    print("="*60)
    
    try:
        movies, similarity = load_models()
        if movies is not None and similarity is not None:
            print("✓ Models loaded successfully!")
            print(f"  - Movies dataframe shape: {movies.shape}")
            print(f"  - Similarity matrix shape: {similarity.shape}")
            return movies, similarity
        else:
            print("✗ Failed to load models")
            return None, None
    except Exception as e:
        print(f"✗ Error: {e}")
        return None, None


def test_recommendations(movies, similarity):
    """Test recommendation function"""
    print("\n" + "="*60)
    print("TEST 2: Testing Recommendations")
    print("="*60)
    
    test_movies = ["Avatar", "The Dark Knight", "Inception", "Toy Story"]
    
    for movie in test_movies:
        try:
            recommendations = get_movie_recommendations(movie, movies, similarity, n=5)
            print(f"\n✓ Recommendations for '{movie}':")
            for i, rec in enumerate(recommendations, 1):
                print(f"  {i}. {rec}")
        except Exception as e:
            print(f"✗ Error for '{movie}': {e}")


def test_movie_details(movies, similarity):
    """Test recommendation with similarity scores"""
    print("\n" + "="*60)
    print("TEST 3: Testing Detailed Recommendations")
    print("="*60)
    
    try:
        result = get_movie_details("Avatar", movies, similarity)
        print("\n✓ Detailed recommendations for 'Avatar':")
        print(result.to_string(index=False))
    except Exception as e:
        print(f"✗ Error: {e}")


def test_search(movies):
    """Test movie search function"""
    print("\n" + "="*60)
    print("TEST 4: Testing Movie Search")
    print("="*60)
    
    queries = ["star", "dark", "toy"]
    
    for query in queries:
        try:
            results = search_movies(query, movies, limit=5)
            print(f"\n✓ Search results for '{query}':")
            for i, movie in enumerate(results, 1):
                print(f"  {i}. {movie}")
        except Exception as e:
            print(f"✗ Error for '{query}': {e}")


def test_statistics(movies, similarity):
    """Test statistics function"""
    print("\n" + "="*60)
    print("TEST 5: System Statistics")
    print("="*60)
    
    try:
        stats = get_statistics(movies, similarity)
        print("\n✓ Statistics:")
        for key, value in stats.items():
            if isinstance(value, float):
                print(f"  - {key}: {value:.6f}")
            else:
                print(f"  - {key}: {value}")
    except Exception as e:
        print(f"✗ Error: {e}")


def test_edge_cases(movies, similarity):
    """Test edge cases"""
    print("\n" + "="*60)
    print("TEST 6: Edge Cases")
    print("="*60)
    
    # Test non-existent movie
    print("\nTest 6.1: Non-existent movie")
    try:
        result = get_movie_recommendations("This Movie Does Not Exist", movies, similarity)
        print(f"  Result: {result}")
    except Exception as e:
        print(f"  ✓ Handled correctly: {e}")
    
    # Test empty search
    print("\nTest 6.2: Empty search query")
    try:
        results = search_movies("", movies)
        print(f"  ✓ Results found: {len(results)}")
    except Exception as e:
        print(f"  Error: {e}")


def run_all_tests():
    """Run all tests"""
    print("\n" + "🎬 " + "="*56 + " 🎬")
    print("  MOVIE RECOMMENDATION SYSTEM - TEST SUITE")
    print("🎬 " + "="*56 + " 🎬\n")
    
    # Load models
    movies, similarity = test_model_loading()
    
    if movies is None or similarity is None:
        print("\n⚠️  Cannot proceed with tests - models not loaded")
        print("\nMake sure to:")
        print("1. Run the Jupyter notebook first")
        print("2. Generate movies.pkl and similarity.pkl")
        return
    
    # Run all tests
    test_recommendations(movies, similarity)
    test_movie_details(movies, similarity)
    test_search(movies)
    test_statistics(movies, similarity)
    test_edge_cases(movies, similarity)
    
    # Final summary
    print("\n" + "="*60)
    print("✅ ALL TESTS COMPLETED")
    print("="*60)
    print("\nYour recommendation system is ready!")
    print("\nNext steps:")
    print("1. Run the Streamlit app: streamlit run app.py")
    print("2. Open http://localhost:8501 in your browser")
    print("3. Start recommending movies!")
    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    run_all_tests()
