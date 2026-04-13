# 🚀 Deployment Guide: Sales Intelligence Platform

This project has been heavily optimized and is now light enough to be deployed for free on a variety of modern platforms! 

The huge `scikit-learn` and `django` dependencies have been removed, making the app's total slug size well under 50 MB (perfect for free tiers with memory limits). We have also added `gunicorn`, a production-grade Python web server, to the `requirements.txt`.

Here are the best ways to deploy this application for free:

---

## Option 1: Deploying on Render (Recommended & Easiest)

Render offers a very generous free tier for Python Web Services and automatically sets everything up for you.

### Step-by-Step Instructions:
1. **Push your code to GitHub**: 
   - Make sure your project (including `app.py`, `requirements.txt`, `src/`, `data/`, and `templates/`) is pushed to a Github repository.
2. **Sign up for [Render.com](https://render.com/)**.
3. **Create a New Web Service**:
   - Click the "New" button in the Render dashboard and select **"Web Service"**.
   - Connect it to your GitHub account and select your repository.
4. **Configure the Service**:
   - **Name**: Choose a name for your app.
   - **Region**: Choose a region closest to you.
   - **Branch**: `main` (or whatever your default branch is).
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app` (This tells Render to use gunicorn to serve the `app` object from `app.py`).
5. **Select the Free Plan** at the bottom and click **Create Web Service**.
6. Wait a few minutes. Render will install your dependencies and launch your application! You will get a live `.onrender.com` URL.

---

## Option 2: Deploying on PythonAnywhere

PythonAnywhere is a classic hosting provider specifically for Python applications and has a solid free tier.

### Step-by-Step Instructions:
1. Create a free account at [PythonAnywhere](https://www.pythonanywhere.com/).
2. Once logged in, go to the **Web** tab and click **Add a new web app**.
3. It will ask for a domain name. Just click **Next** to use your free `yourusername.pythonanywhere.com` domain.
4. Select **Flask** as the framework and choose the latest Python version (Python 3.10+).
5. For the app path, it will ask where your `app.py` is located. Point it to your directory.
6. Open the **Bash Console** in PythonAnywhere and clone your github repository or upload your files via the **Files** tab.
7. In the Bash Console, run:
   ```bash
   pip install -r requirements.txt --user
   ```
8. Go to your **Web** tab, scroll down to **Code**, find the `WSGI configuration file`, and click it. 
9. Ensure it imports your Flask app correctly (it usually provides a template that you just need to uncomment for Flask and point to `app:app`).
10. Hit the **Reload** button at the top of the **Web** tab to make your app go live!

> [!TIP]
> **Why is this project faster now?**
> By replacing `sklearn.linear_model.LinearRegression` with `numpy.polyfit`, the project retains the exact same mathematical predictions but removes over 200MB of backend bloat. This means faster start times, no out-of-memory errors on boot, and instant chart rendering.
