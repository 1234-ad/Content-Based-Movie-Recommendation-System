# Movie Recommendation System - Setup and Usage Guide

## 📝 Instructions for Getting TMDB API Key

To display movie posters in the Streamlit app, you'll need a TMDB API key:

1. **Create TMDB Account**
   - Go to https://www.themoviedb.org/
   - Click "Join TMDB" and create a free account
   - Verify your email address

2. **Request API Key**
   - Log in to your TMDB account
   - Go to Settings → API
   - Click "Request an API Key"
   - Choose "Developer" option
   - Fill in the application form:
     - Application Name: Movie Recommender
     - Application URL: http://localhost
     - Application Summary: Personal movie recommendation project
   - Accept terms and submit

3. **Copy Your API Key**
   - Once approved (usually instant), you'll see your API Key (v3 auth)
   - Copy this key

4. **Add to app.py**
   - Open `app.py`
   - Find line: `TMDB_API_KEY = "YOUR_TMDB_API_KEY_HERE"`
   - Replace with your actual key: `TMDB_API_KEY = "your_actual_key_here"`

## 📂 Download Dataset

Download the TMDB 5000 Movie Dataset from Kaggle:

1. Go to: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
2. Click "Download" button
3. Extract the ZIP file
4. Copy these two files to the project folder:
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`

## 🚀 Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Jupyter Notebook**
   - Open `movie_recommender.ipynb`
   - Run all cells to:
     - Load and process the dataset
     - Create the recommendation model
     - Generate pickle files (movies.pkl, similarity.pkl)

3. **Launch Streamlit App**
   ```bash
   streamlit run app.py
   ```

4. **Open in Browser**
   - The app will automatically open at http://localhost:8501
   - Select a movie and get recommendations!

## 📊 Project Structure

```
Content-Based-Movie-Recommendation-System/
│
├── movie_recommender.ipynb    # Main notebook with model building
├── app.py                     # Streamlit web application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── SETUP_GUIDE.md            # This file
│
├── tmdb_5000_movies.csv      # Dataset (download from Kaggle)
├── tmdb_5000_credits.csv     # Dataset (download from Kaggle)
│
├── movies.pkl                # Generated: Movie dataframe
├── similarity.pkl            # Generated: Similarity matrix
└── vectorizer.pkl            # Generated: CountVectorizer
```

## 🔧 Troubleshooting

### Issue: "FileNotFoundError: movies.pkl"
**Solution:** Run the Jupyter notebook first to generate the pickle files.

### Issue: "Movie posters not loading"
**Solution:** 
- Check if TMDB_API_KEY is correctly set in app.py
- Verify your API key is active on TMDB website
- Check internet connection

### Issue: "Module not found"
**Solution:** Install missing dependencies:
```bash
pip install <module-name>
```

### Issue: "Movie not found in database"
**Solution:** Use the dropdown menu to select from available movies. The database contains ~4800 movies.

## 📸 Screenshots

After running the app, take screenshots of:
1. Movie selection interface
2. Recommendation results with posters
3. Different movie recommendations

## 🎯 Features

- ✅ Content-based recommendation using 5000+ features
- ✅ Cosine similarity for accurate recommendations
- ✅ Interactive web interface with Streamlit
- ✅ Movie poster display using TMDB API
- ✅ Clean and responsive UI
- ✅ Fast recommendation generation

## 📚 How It Works

1. **Data Processing**: Combines movie overview, genres, keywords, cast, and director into a single feature
2. **Text Vectorization**: Converts text to numerical vectors using CountVectorizer
3. **Similarity Calculation**: Computes cosine similarity between all movies
4. **Recommendation**: Returns top 5 most similar movies based on content features

## 🔗 Resources

- TMDB Dataset: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
- TMDB API Docs: https://developers.themoviedb.org/3
- Streamlit Docs: https://docs.streamlit.io
- Scikit-learn Docs: https://scikit-learn.org

## 📝 Notes

- The similarity matrix can be large (~200MB) depending on dataset size
- First-time loading may take a few seconds
- Movie posters require internet connection to load from TMDB
- Without API key, app will show placeholder images

## ✨ Optional Enhancements

1. Add movie ratings and release year
2. Implement user rating prediction
3. Add collaborative filtering
4. Include movie trailers
5. Deploy to Streamlit Cloud or Heroku
