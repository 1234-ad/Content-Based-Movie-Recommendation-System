# ▶️ EXECUTION GUIDE - Step by Step

Follow these exact steps to run your Movie Recommendation System.

---

## 📋 Prerequisites Check

Before starting, ensure you have:

```powershell
# Check Python version (should be 3.8 or higher)
python --version

# Check pip
pip --version
```

If Python is not installed, download from: https://www.python.org/downloads/

---

## 🎬 STEP 1: Download Dataset (5 minutes)

### Option A: Using Kaggle Website (Recommended)

1. **Create Kaggle Account** (if you don't have one)
   - Go to: https://www.kaggle.com/
   - Sign up (free)

2. **Download Dataset**
   - Visit: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
   - Click the "Download" button (12 MB ZIP file)
   - Extract the ZIP file

3. **Copy Files to Project**
   - Copy `tmdb_5000_movies.csv` to this folder
   - Copy `tmdb_5000_credits.csv` to this folder

### Option B: Using Kaggle API (Advanced)

```powershell
# Install Kaggle CLI
pip install kaggle

# Download dataset
kaggle datasets download -d tmdb/tmdb-movie-metadata

# Extract
Expand-Archive -Path tmdb-movie-metadata.zip -DestinationPath .
```

### ✅ Verify Dataset

```powershell
# Check if files exist
ls tmdb_5000_*.csv
```

You should see both files listed.

---

## 🔧 STEP 2: Install Dependencies (2 minutes)

```powershell
# Install all required packages
pip install -r requirements.txt

# This installs:
# - streamlit (web framework)
# - pandas (data processing)
# - numpy (numerical computing)
# - scikit-learn (machine learning)
# - nltk (text processing)
# - requests (API calls)
```

### ✅ Verify Installation

```powershell
# Check if streamlit is installed
streamlit --version

# Should output: Streamlit, version 1.x.x
```

---

## 📓 STEP 3: Run Jupyter Notebook (5-10 minutes)

### Option A: Using Jupyter Notebook

```powershell
# Install Jupyter if not already installed
pip install jupyter notebook

# Launch Jupyter
jupyter notebook
```

Then:
1. Browser opens automatically
2. Click on `movie_recommender.ipynb`
3. Click `Cell` → `Run All` (or press `Shift + Enter` for each cell)
4. Wait for completion (~5-10 minutes)

### Option B: Using VS Code

1. Open `movie_recommender.ipynb` in VS Code
2. Select Python kernel (3.8+)
3. Click "Run All" at the top
4. Wait for completion

### Option C: Using JupyterLab

```powershell
# Install JupyterLab
pip install jupyterlab

# Launch
jupyter lab

# Then open movie_recommender.ipynb and run all cells
```

### ✅ Verify Notebook Execution

After running all cells, check:

```powershell
# These files should be created
ls *.pkl

# Should show:
# movies.pkl
# similarity.pkl
# vectorizer.pkl
```

**File sizes should be:**
- `movies.pkl`: ~1-5 MB
- `similarity.pkl`: ~100-200 MB
- `vectorizer.pkl`: ~1-5 MB

---

## 🧪 STEP 4: Test the System (Optional but Recommended)

```powershell
# Run test suite
python test_recommender.py
```

**Expected output:**
```
🎬 ========================================================== 🎬
  MOVIE RECOMMENDATION SYSTEM - TEST SUITE
🎬 ========================================================== 🎬

TEST 1: Loading Models
============================================================
✓ Models loaded successfully!
  - Movies dataframe shape: (4803, 3)
  - Similarity matrix shape: (4803, 4803)

TEST 2: Testing Recommendations
============================================================
✓ Recommendations for 'Avatar':
  1. Guardians of the Galaxy
  2. Star Trek Into Darkness
  ...
```

If all tests pass (✓), you're ready to proceed!

---

## 🌐 STEP 5: Get TMDB API Key (Optional - 5 minutes)

### Skip this step if you want to run without movie posters

1. **Create TMDB Account**
   - Go to: https://www.themoviedb.org/
   - Click "Join TMDB"
   - Complete registration

2. **Request API Key**
   - Log in
   - Go to Settings (click your avatar → Settings)
   - Click "API" in left sidebar
   - Click "Request an API Key"
   - Choose "Developer"
   - Fill form:
     - Type: Website
     - Name: Movie Recommender
     - URL: http://localhost:8501
     - Description: Personal movie recommendation project
   - Submit

3. **Copy API Key**
   - You'll receive an API Key (v3 auth)
   - Copy this key

4. **Add to app.py**
   - Open `app.py` in text editor
   - Find line 33: `TMDB_API_KEY = "YOUR_TMDB_API_KEY_HERE"`
   - Replace with: `TMDB_API_KEY = "your_actual_api_key_here"`
   - Save file

### ✅ Verify API Key (Optional)

```powershell
# Test API key
python -c "import requests; print(requests.get('https://api.themoviedb.org/3/movie/550?api_key=YOUR_KEY_HERE').status_code)"

# Should output: 200 (success)
```

---

## 🚀 STEP 6: Launch Streamlit App

```powershell
# Run the app
streamlit run app.py
```

**Expected output:**
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

Browser opens automatically at http://localhost:8501

### ✅ Verify App is Running

You should see:
- "🎬 Movie Recommendation System" header
- Dropdown menu with movies
- Sidebar with project info
- "Get Recommendations" button

---

## 🎮 STEP 7: Use the Application

### Basic Usage

1. **Select a Movie**
   - Click dropdown menu
   - Type to search (e.g., "Avatar")
   - Select movie

2. **Get Recommendations**
   - Click "Get Recommendations" button
   - Wait 1-2 seconds
   - View 5 recommended movies

3. **Try Different Movies**
   - Recommended test movies:
     - Avatar
     - The Dark Knight
     - Inception
     - Toy Story
     - Interstellar

### Advanced Usage

1. **Text Search**
   - Expand "Or type a movie name"
   - Type movie title
   - Press Enter

2. **View Statistics**
   - Check sidebar for:
     - Total movies count
     - Technology stack
     - About section

---

## 🛑 How to Stop

### Stop Streamlit App

In the terminal where Streamlit is running:

```powershell
# Press Ctrl+C

# Confirm: y
```

### Stop Jupyter Notebook

In Jupyter browser:
1. Click "File" → "Close and Halt"
2. Close browser tab

Or in terminal:

```powershell
# Press Ctrl+C twice
```

---

## 📸 STEP 8: Take Screenshots (for Deliverables)

### Screenshot 1: Home Screen
- App just opened
- Dropdown visible
- Sidebar visible

### Screenshot 2: Recommendations
- Movie selected (e.g., "Avatar")
- 5 recommendations displayed
- Movie posters visible (if API key added)

### Screenshot 3: Different Movie
- Try "The Dark Knight"
- Show different recommendations

### Save Screenshots
Create folder: `screenshots/`
Save as:
- `home.png`
- `recommendations_avatar.png`
- `recommendations_dark_knight.png`

---

## 🔄 Daily Workflow

### Starting the App

```powershell
# Navigate to project folder
cd path\to\Content-Based-Movie-Recommendation-System-main

# Start app
streamlit run app.py
```

### Making Changes

1. Edit `app.py` or notebook
2. Save changes
3. Streamlit auto-reloads (or press R in browser)
4. Test changes

---

## ❓ Common Issues & Solutions

### Issue 1: "No module named 'streamlit'"
```powershell
# Solution
pip install streamlit
```

### Issue 2: "FileNotFoundError: movies.pkl"
```powershell
# Solution: Run notebook first
jupyter notebook movie_recommender.ipynb
# Then run all cells
```

### Issue 3: "Movie not found"
```powershell
# Solution: Use dropdown menu instead of typing
# Check available movies in dropdown
```

### Issue 4: Port already in use
```powershell
# Solution: Use different port
streamlit run app.py --server.port 8502
```

### Issue 5: Posters not loading
```powershell
# Solution: Check API key in app.py
# Or run without API key (placeholders will show)
```

### Issue 6: Notebook kernel error
```powershell
# Solution: Restart kernel
# In Jupyter: Kernel → Restart & Run All
```

---

## 📊 Performance Expectations

### First Run (Notebook)
- Time: 5-10 minutes
- Memory: 2-4 GB
- Files created: 3 pickle files

### Streamlit App
- First load: 3-5 seconds
- Recommendations: < 1 second
- Memory: 200-300 MB

### System Requirements
- **Minimum:**
  - Python 3.8+
  - 4 GB RAM
  - 500 MB disk space

- **Recommended:**
  - Python 3.10+
  - 8 GB RAM
  - 1 GB disk space
  - Internet connection (for posters)

---

## ✅ Success Checklist

After completing all steps:

- [ ] Dataset files downloaded
- [ ] Dependencies installed
- [ ] Jupyter notebook executed
- [ ] Pickle files generated
- [ ] Tests passed (if ran)
- [ ] TMDB API key added (optional)
- [ ] Streamlit app runs
- [ ] Recommendations work
- [ ] Screenshots taken

---

## 🎯 Next Steps After Setup

1. ✅ **Explore**: Try different movies
2. ✅ **Learn**: Read the Jupyter notebook
3. ✅ **Customize**: Modify the UI in app.py
4. ✅ **Share**: Show friends and colleagues
5. ✅ **Deploy**: Use DEPLOYMENT.md guide

---

## 📞 Getting Help

### Documentation Files
- `README.md` - Overview
- `QUICK_START.md` - 5-minute guide
- `SETUP_GUIDE.md` - Detailed setup
- `PROJECT_SUMMARY.md` - Complete summary
- `DEPLOYMENT.md` - Deployment guide
- `EXECUTION_GUIDE.md` - This file

### Check Logs
```powershell
# If streamlit crashes, check terminal output
# If notebook fails, check cell output
```

---

## 🎉 You're Done!

Your movie recommendation system is now:
- ✅ Fully set up
- ✅ Tested and working
- ✅ Ready to use
- ✅ Ready to deploy (optional)

Enjoy recommending movies! 🍿🎬

---

**Total Setup Time:** 20-30 minutes  
**Difficulty:** Easy to Medium  
**Result:** Production-ready recommendation system!
