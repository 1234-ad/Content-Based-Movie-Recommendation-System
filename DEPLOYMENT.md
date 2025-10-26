# 🚀 Deployment Guide

## Deploy Your Movie Recommendation System to the Cloud

This guide covers multiple deployment options for your Streamlit app.

---

## Option 1: Streamlit Cloud (Recommended - FREE!)

### Prerequisites
- GitHub account
- Streamlit Cloud account (free)

### Steps

1. **Prepare Your Repository**
   ```bash
   # Initialize git (if not already done)
   git init
   git add .
   git commit -m "Initial commit - Movie Recommendation System"
   ```

2. **Push to GitHub**
   ```bash
   # Create a new repository on GitHub, then:
   git remote add origin https://github.com/yourusername/movie-recommender.git
   git branch -M main
   git push -u origin main
   ```

3. **Upload Dataset to GitHub**
   - Since the pickle files are large, use Git LFS or generate them after deployment
   - Alternative: Store on cloud storage and download in app

4. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io/
   - Click "New app"
   - Select your GitHub repository
   - Set main file: `app.py`
   - Click "Deploy"

5. **Environment Variables**
   - In Streamlit Cloud dashboard, add your TMDB_API_KEY in Secrets

### Important Notes
- Free tier includes 1GB RAM (may need optimization for large models)
- Pickle files should be < 100MB or use cloud storage
- First load may take time to generate models

---

## Option 2: Heroku

### Prerequisites
- Heroku account
- Heroku CLI installed

### Setup Files

1. **Create Procfile**
   ```
   web: sh setup.sh && streamlit run app.py
   ```

2. **Create setup.sh**
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   headless = true
   port = $PORT
   enableCORS = false
   " > ~/.streamlit/config.toml
   ```

3. **Update requirements.txt**
   Add: `gunicorn`

### Deploy
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-movie-recommender

# Set buildpacks
heroku buildpacks:add heroku/python

# Deploy
git push heroku main

# Open app
heroku open
```

---

## Option 3: AWS EC2

### Steps

1. **Launch EC2 Instance**
   - Choose Ubuntu Server
   - t2.medium or larger (for 4GB+ RAM)
   - Configure security group (port 8501)

2. **Connect and Setup**
   ```bash
   # SSH into instance
   ssh -i your-key.pem ubuntu@your-ec2-ip

   # Update system
   sudo apt update && sudo apt upgrade -y

   # Install Python and pip
   sudo apt install python3-pip python3-venv -y

   # Clone repository
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender

   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt

   # Run app
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   ```

3. **Keep App Running**
   ```bash
   # Install PM2 for process management
   sudo apt install npm -y
   sudo npm install -g pm2

   # Create startup script
   cat > run_app.sh << EOF
   #!/bin/bash
   source venv/bin/activate
   streamlit run app.py --server.port 8501 --server.address 0.0.0.0
   EOF

   chmod +x run_app.sh

   # Start with PM2
   pm2 start run_app.sh --name movie-recommender
   pm2 save
   pm2 startup
   ```

4. **Access App**
   - Open: `http://your-ec2-ip:8501`

---

## Option 4: Docker

### Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build and Run

```bash
# Build image
docker build -t movie-recommender .

# Run container
docker run -p 8501:8501 movie-recommender

# Access at http://localhost:8501
```

### Docker Compose

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8501:8501"
    environment:
      - TMDB_API_KEY=${TMDB_API_KEY}
    volumes:
      - ./data:/app/data
```

---

## Option 5: Google Cloud Platform (Cloud Run)

### Prerequisites
- GCP account
- gcloud CLI installed

### Steps

```bash
# Build container
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/movie-recommender

# Deploy to Cloud Run
gcloud run deploy movie-recommender \
  --image gcr.io/YOUR_PROJECT_ID/movie-recommender \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 2Gi

# Get URL
gcloud run services describe movie-recommender --format 'value(status.url)'
```

---

## Optimization Tips for Deployment

### 1. Reduce Model Size

```python
# Use sparse matrix for similarity
from scipy.sparse import save_npz, load_npz
save_npz('similarity_sparse.npz', similarity)
```

### 2. Lazy Loading

```python
# Load models only when needed
@st.cache_data
def load_models():
    # Load models
    pass
```

### 3. External Storage

Store large files on:
- AWS S3
- Google Cloud Storage
- Dropbox/Google Drive (with public links)

```python
import requests

def download_model():
    url = 'https://your-storage-url/similarity.pkl'
    response = requests.get(url)
    with open('similarity.pkl', 'wb') as f:
        f.write(response.content)
```

### 4. Environment Variables

Create `.streamlit/secrets.toml`:
```toml
TMDB_API_KEY = "your_api_key_here"
```

Access in code:
```python
import streamlit as st
TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
```

---

## Performance Monitoring

### Add Analytics

```python
# Google Analytics
st.components.v1.html("""
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR_GA_ID"></script>
""")
```

### Error Tracking

Use Sentry:
```python
import sentry_sdk
sentry_sdk.init(dsn="YOUR_SENTRY_DSN")
```

---

## Cost Comparison

| Platform | Free Tier | Paid (Est.) | Best For |
|----------|-----------|-------------|----------|
| Streamlit Cloud | 1 app, 1GB RAM | N/A | Demos, portfolios |
| Heroku | 550 hours/month | $7/month | Small projects |
| AWS EC2 | 750 hours (1st year) | $20-50/month | Production |
| GCP Cloud Run | 2M requests/month | Pay per use | Variable traffic |
| Docker (local) | Free | Hosting costs | Testing |

---

## Security Best Practices

1. **Never commit API keys**
   ```bash
   # Add to .gitignore
   echo "config.py" >> .gitignore
   echo ".env" >> .gitignore
   ```

2. **Use environment variables**
   ```python
   import os
   API_KEY = os.getenv('TMDB_API_KEY')
   ```

3. **HTTPS only**
   - Enable SSL on production
   - Use Cloudflare for free SSL

4. **Rate limiting**
   ```python
   from streamlit import cache_data
   @cache_data(ttl=3600)  # Cache for 1 hour
   def fetch_poster(movie):
       # API call
       pass
   ```

---

## Troubleshooting Deployment

### Out of Memory
- Reduce model size
- Use external storage
- Upgrade instance

### Slow Loading
- Use caching (`@st.cache_data`)
- Optimize model loading
- Use CDN for static files

### Build Failures
- Check Python version compatibility
- Verify all dependencies in requirements.txt
- Review deployment logs

---

## Post-Deployment Checklist

- [ ] App loads successfully
- [ ] Recommendations work correctly
- [ ] Posters display properly
- [ ] No errors in logs
- [ ] Fast response times (< 2 seconds)
- [ ] Mobile responsive
- [ ] Custom domain configured (optional)
- [ ] Analytics enabled (optional)
- [ ] Backup plan in place

---

## Custom Domain (Optional)

### Streamlit Cloud
1. Go to app settings
2. Add custom domain
3. Update DNS records

### Other Platforms
Use Cloudflare or domain registrar's DNS settings

---

## Maintenance

### Regular Updates
```bash
# Update dependencies
pip install --upgrade -r requirements.txt

# Test locally
streamlit run app.py

# Deploy
git push origin main
```

### Monitoring
- Check app performance weekly
- Monitor API usage
- Review error logs
- Update models with new data

---

## Need Help?

- Streamlit Docs: https://docs.streamlit.io/
- Heroku Docs: https://devcenter.heroku.com/
- AWS Docs: https://docs.aws.amazon.com/
- Docker Docs: https://docs.docker.com/

---

**Happy Deploying! 🚀**
