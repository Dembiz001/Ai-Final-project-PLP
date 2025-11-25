# Deployment Guide - AI Garden Assistant

## Overview
This guide covers deploying both frontend and backend of the AI Garden Assistant to production.

## Prerequisites
- GitHub account
- Vercel account (for frontend)
- Render/Heroku account (for backend)
- Git installed locally

---

## Frontend Deployment (Vercel)

### Step 1: Prepare Frontend

1. Update `.env.local` with production API URL:
```
REACT_APP_API_URL=https://your-backend-url.com
REACT_APP_ENV=production
```

2. Build the application:
```bash
cd frontend
npm run build
```

3. Test the build locally:
```bash
npm install -g serve
serve -s build
```

### Step 2: Deploy to Vercel

**Option A: Using Vercel CLI**

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Deploy:
```bash
vercel
```

3. Follow the prompts and select your project

**Option B: Using GitHub Integration**

1. Push code to GitHub
2. Go to https://vercel.com
3. Click "New Project"
4. Select your GitHub repository
5. Configure environment variables:
   - `REACT_APP_API_URL`: Your backend URL
   - `REACT_APP_ENV`: production
6. Click Deploy

### Step 3: Configure Domain (Optional)

1. In Vercel dashboard
2. Go to Project Settings → Domains
3. Add your custom domain
4. Update DNS records as instructed

---

## Backend Deployment (Render)

### Step 1: Prepare Backend

1. Update `backend/.env` for production:
```
FLASK_ENV=production
SECRET_KEY=your-secure-random-key
CORS_ORIGINS=https://your-frontend-url.com
```

2. Update `backend/app.py` debug settings:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

3. Create `Procfile`:
```
web: gunicorn app:app
```

4. Update `requirements.txt` with gunicorn:
```
Flask==2.3.3
Flask-CORS==4.0.0
gunicorn==21.2.0
tensorflow==2.13.0
Pillow==10.0.0
numpy==1.24.3
python-dotenv==1.0.0
firebase-admin==6.2.0
requests==2.31.0
```

### Step 2: Deploy to Render

1. Push code to GitHub

2. Go to https://render.com

3. Click "New +" → "Web Service"

4. Connect your GitHub repository

5. Configure:
   - **Name**: ai-garden-backend
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free or Paid (recommended Paid for TensorFlow)

6. Add environment variables:
   - `FLASK_ENV=production`
   - `SECRET_KEY=your-secure-key`
   - `CORS_ORIGINS=https://your-frontend-url.com`
   - Firebase credentials (if using)

7. Click "Create Web Service"

8. Wait for deployment to complete

9. Get your backend URL from Render dashboard

### Step 3: Update Frontend URL

After backend deployment, update frontend with new backend URL:

1. In Vercel:
   - Settings → Environment Variables
   - Update `REACT_APP_API_URL` with new backend URL
   - Redeploy

---

## Backend Deployment (Heroku Alternative)

### Step 1: Setup Heroku CLI

```bash
curl https://cli-assets.heroku.com/install.sh | sh
heroku login
```

### Step 2: Prepare App

1. Create `Procfile`:
```
web: gunicorn app:app
```

2. Create `runtime.txt`:
```
python-3.11.5
```

### Step 3: Deploy

```bash
cd backend
heroku create your-app-name
git push heroku main
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secure-key
heroku config:set CORS_ORIGINS=https://your-frontend-url.com
```

---

## Database Setup (Firebase)

### Step 1: Create Firebase Project

1. Go to https://console.firebase.google.com
2. Click "Create Project"
3. Follow setup wizard
4. Enable Realtime Database or Firestore

### Step 2: Get Credentials

1. Project Settings → Service Accounts
2. Click "Generate New Private Key"
3. Copy the JSON file

### Step 3: Set Environment Variables

Add to `.env`:
```
FIREBASE_API_KEY=your_api_key
FIREBASE_AUTH_DOMAIN=your_auth_domain.firebaseapp.com
FIREBASE_PROJECT_ID=your_project_id
FIREBASE_STORAGE_BUCKET=your_storage_bucket.appspot.com
FIREBASE_MESSAGING_SENDER_ID=your_sender_id
FIREBASE_APP_ID=your_app_id
```

---

## Database Setup (MongoDB Atlas)

### Step 1: Create Cluster

1. Go to https://www.mongodb.com/cloud/atlas
2. Sign up or log in
3. Create a new cluster
4. Configure settings

### Step 2: Get Connection String

1. Cluster → Connect
2. Choose "Connect your application"
3. Copy connection string

### Step 3: Set Environment Variable

```
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/database
```

---

## SSL/HTTPS

Most deployment platforms (Vercel, Render) provide free SSL certificates automatically.

---

## Monitoring & Logs

### Vercel
1. Dashboard → Select Project
2. Logs tab shows deployment logs
3. Use Vercel Analytics for performance

### Render
1. Dashboard → Select Service
2. Logs tab for application logs
3. Metrics tab for performance

### Heroku
```bash
heroku logs --tail
heroku metrics
```

---

## Performance Optimization

### Frontend (Vercel)
- Enable caching
- Use Web Vitals monitoring
- Optimize images
- Enable gzip compression

### Backend (Render/Heroku)
- Use Redis for caching
- Optimize database queries
- Use CDN for static files
- Enable gzip compression

---

## CI/CD Pipeline

### GitHub Actions Example

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Deploy Frontend
      run: |
        npm install
        npm run build
        vercel --prod --token ${{ secrets.VERCEL_TOKEN }}
    
    - name: Deploy Backend
      run: |
        git push heroku main
```

---

## Troubleshooting

### Frontend Issues
- **Blank page**: Check console for errors
- **API connection fails**: Verify backend URL in `.env`
- **Images not loading**: Check CORS headers

### Backend Issues
- **TensorFlow memory error**: Reduce batch size
- **Model loading fails**: Ensure model file exists
- **Database connection error**: Check connection string

---

## Rollback Procedure

### Vercel
1. Deployments tab
2. Select previous deployment
3. Click "..." → "Rollback"

### Render
1. Deploys tab
2. Select previous deployment
3. Click "Deploy"

### Heroku
```bash
heroku rollbacks
heroku rollback --version v3
```

---

## Security Checklist

- [ ] Change SECRET_KEY to secure random value
- [ ] Enable HTTPS/SSL
- [ ] Set appropriate CORS_ORIGINS
- [ ] Secure API keys and credentials
- [ ] Enable database encryption
- [ ] Set up rate limiting
- [ ] Implement CSRF protection
- [ ] Regular security updates
- [ ] Monitor logs for suspicious activity

---

## Cost Estimation

### Free Tier (Development)
- Frontend (Vercel): Free
- Backend (Render Free): Free
- Database (MongoDB Free): Free
- **Total: $0/month**

### Recommended (Production)
- Frontend (Vercel Pro): $20/month
- Backend (Render Paid): $7-12/month
- Database (MongoDB): $0-100+/month (depending on usage)
- **Estimated: $27-132/month**

---

## Next Steps

1. Deploy frontend to Vercel
2. Deploy backend to Render
3. Set up database (Firebase/MongoDB)
4. Test all features in production
5. Set up monitoring and alerts
6. Implement analytics
7. Plan feature updates

---

## Support

- Vercel Docs: https://vercel.com/docs
- Render Docs: https://render.com/docs
- Firebase Docs: https://firebase.google.com/docs
- MongoDB Docs: https://docs.mongodb.com/

---

Last Updated: November 2025
