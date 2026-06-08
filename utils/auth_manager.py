import os
import jwt
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load env variables
load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
REDIRECT_URI = os.getenv("OAUTH_REDIRECT_URI", "http://localhost:8501")
JWT_SECRET = os.getenv("JWT_SECRET", "smart-ai-analyzer-jwt-secret-key-2026-custom")

def get_google_auth_url():
    """Generate Google OAuth authorization URL"""
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "state": "google"
    }
    query_string = "&".join(f"{k}={requests.utils.quote(v)}" for k, v in params.items())
    return f"{base_url}?{query_string}"

def get_github_auth_url():
    """Generate GitHub OAuth authorization URL"""
    base_url = "https://github.com/login/oauth/authorize"
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user:email read:user",
        "state": "github"
    }
    query_string = "&".join(f"{k}={requests.utils.quote(v)}" for k, v in params.items())
    return f"{base_url}?{query_string}"

def handle_google_callback(code):
    """Exchange code for Google access token and fetch profile"""
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    
    try:
        # Request access token
        token_res = requests.post(token_url, data=data)
        token_res.raise_for_status()
        token_data = token_res.json()
        access_token = token_data.get("access_token")
        
        if not access_token:
            return None
            
        # Get user info
        userinfo_url = "https://www.googleapis.com/oauth2/v3/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}
        user_res = requests.get(userinfo_url, headers=headers)
        user_res.raise_for_status()
        user_data = user_res.json()
        
        return {
            "name": user_data.get("name", ""),
            "email": user_data.get("email", ""),
            "avatar": user_data.get("picture", ""),
            "provider": "google"
        }
    except Exception as e:
        print(f"Google OAuth Callback error: {e}")
        return None

def handle_github_callback(code):
    """Exchange code for GitHub access token and fetch profile"""
    token_url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    data = {
        "code": code,
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI
    }
    
    try:
        # Request access token
        token_res = requests.post(token_url, data=data, headers=headers)
        token_res.raise_for_status()
        token_data = token_res.json()
        access_token = token_data.get("access_token")
        
        if not access_token:
            return None
            
        # Get user profile
        user_url = "https://api.github.com/user"
        auth_headers = {"Authorization": f"token {access_token}"}
        user_res = requests.get(user_url, headers=auth_headers)
        user_res.raise_for_status()
        user_data = user_res.json()
        
        # Get primary email
        email_url = "https://api.github.com/user/emails"
        email_res = requests.get(email_url, headers=auth_headers)
        email_res.raise_for_status()
        emails = email_res.json()
        
        primary_email = ""
        for email_item in emails:
            if email_item.get("primary"):
                primary_email = email_item.get("email", "")
                break
        if not primary_email and emails:
            primary_email = emails[0].get("email", "")
            
        return {
            "name": user_data.get("name") or user_data.get("login", ""),
            "email": primary_email,
            "avatar": user_data.get("avatar_url", ""),
            "provider": "github"
        }
    except Exception as e:
        print(f"GitHub OAuth Callback error: {e}")
        return None

def generate_jwt_token(user_info):
    """Encode user information in a signed JWT token"""
    payload = {
        "name": user_info.get("name", ""),
        "email": user_info.get("email", ""),
        "avatar": user_info.get("avatar", ""),
        "provider": user_info.get("provider", ""),
        "exp": datetime.utcnow() + timedelta(days=7) # Session active for 7 days
    }
    try:
        token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
        return token
    except Exception as e:
        print(f"JWT generate error: {e}")
        return None

def decode_jwt_token(token):
    """Verify and decode JWT token"""
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        print("JWT token expired")
        return None
    except jwt.InvalidTokenError:
        print("Invalid JWT token")
        return None
    except Exception as e:
        print(f"JWT decode error: {e}")
        return None
