# 🚀 Quick Start Guide

Get your movie recommendation system up and running in 5 minutes!

## Prerequisites Checklist

- [ ] Python 3.8+ installed
- [ ] pip package manager
- [ ] Internet connection (for downloading dataset and packages)

## Step-by-Step Setup

### 1️⃣ Download Dataset (2 minutes)

1. Go to: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
2. Click "Download" (you may need to create a free Kaggle account)
3. Extract the ZIP file
4. Copy `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` to this folder

### 2️⃣ Install Dependencies (1 minute)

Open terminal/command prompt in this folder and run:

```bash
pip install -r requirements.txt
```

### 3️⃣ Generate Models (2-3 minutes)

Run the Jupyter notebook:

**Option A: Using Jupyter Notebook**
```bash
jupyter notebook movie_recommender.ipynb
```
Then click "Run All" or run cells one by one.

**Option B: Using VS Code**
- Open `movie_recommender.ipynb` in VS Code
- Click "Run All" at the top

**What this does:**
- Loads and processes 4,800 movies
- Creates recommendation model
- Generates `movies.pkl` and `similarity.pkl`

### 4️⃣ Test the System (Optional but Recommended)

```bash
python test_recommender.py
```

This will run tests to ensure everything works correctly.

### 5️⃣ Launch the Web App (30 seconds)

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## 🎯 Your First Recommendation

1. Select a movie from the dropdown (try "Avatar" or "The Dark Knight")
2. Click "Get Recommendations"
3. See 5 similar movies instantly!

## 🖼️ Adding Movie Posters (Optional)

To display movie posters instead of placeholder images:

1. Get free TMDB API key:
   - Sign up at https://www.themoviedb.org/
   - Go to Settings → API
   - Request API Key (Developer)
   - Copy your API key

2. Open `app.py` and replace:
   ```python
   TMDB_API_KEY = "YOUR_TMDB_API_KEY_HERE"
   ```
   with your actual key.

## ⚠️ Troubleshooting

### Problem: "FileNotFoundError: movies.pkl"
**Solution:** Run the Jupyter notebook first (Step 3)

### Problem: "No module named 'streamlit'"
**Solution:** Install dependencies: `pip install -r requirements.txt`

### Problem: "Dataset not found"
**Solution:** Download CSV files from Kaggle (Step 1)

### Problem: Jupyter notebook won't open
**Solution:** Install Jupyter: `pip install jupyter notebook`

## 📱 Using the Streamlit App

### Features:
- **Dropdown Selection**: Choose from 4,800+ movies
- **Text Search**: Type movie name in the expander
- **Instant Results**: Get recommendations in < 1 second
- **Movie Posters**: Visual display of recommendations (with API key)
- **Sidebar Info**: View system statistics

### Tips:
- Try different genres to see how recommendations vary
- Popular movies like "Avatar", "Inception", "Toy Story" work well
- Use the search if you can't find a movie in the dropdown

## 📊 What's Happening Behind the Scenes?

```
Your Movie Selection
        ↓
Text Vectorization (5,000 features)
        ↓
Cosine Similarity Calculation
        ↓
Sort by Similarity Score
        ↓
Top 5 Recommendations
```

## 🎓 Learning Path

1. **Beginner**: Run the app and explore recommendations
2. **Intermediate**: Read the Jupyter notebook to understand the code
3. **Advanced**: Modify the model (try TF-IDF, adjust features)

## 📈 Performance Expectations

- **Model Generation**: 2-3 minutes (one-time)
- **App Loading**: 2-5 seconds
- **Recommendation Speed**: < 1 second
- **Memory Usage**: ~200-300 MB

## 🔥 Next Steps After Setup

1. ✅ Test with your favorite movies
2. ✅ Understand the recommendation algorithm
3. ✅ Try modifying features in the notebook
4. ✅ Share with friends!
5. ✅ Deploy to Streamlit Cloud (see README)

## 💡 Pro Tips

- **Faster Testing**: Use `test_recommender.py` to quickly verify changes
- **Better Results**: Add more features or use TF-IDF vectorization
- **Customization**: Modify the UI in `app.py` to match your style
- **Deployment**: Share your app on Streamlit Cloud for free!

## 📞 Need Help?

1. Check the detailed `SETUP_GUIDE.md`
2. Read the `README.md` for more information
3. Review the Jupyter notebook comments
4. Check error messages carefully

## ✅ Success Checklist

After setup, you should have:

- [ ] Dataset files in the project folder
- [ ] All dependencies installed
- [ ] `movies.pkl` and `similarity.pkl` generated
- [ ] Test script runs successfully
- [ ] Streamlit app opens in browser
- [ ] Recommendations display correctly

## 🎬 You're Ready!

Congratulations! Your movie recommendation system is ready to use.

Start discovering amazing movies! 🍿

---

**Time to setup**: ~5-10 minutes  
**Difficulty**: Easy  
**Fun level**: High! 🎉
