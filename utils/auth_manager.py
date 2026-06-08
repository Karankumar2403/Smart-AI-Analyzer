import requests
import streamlit as st
from urllib.parse import urlencode

# OAuth Secrets
GOOGLE_CLIENT_ID = st.secrets.get("GOOGLE_CLIENT_ID") or ""
GOOGLE_CLIENT_SECRET = st.secrets.get("GOOGLE_CLIENT_SECRET") or ""

GITHUB_CLIENT_ID = st.secrets.get("GITHUB_CLIENT_ID") or ""
GITHUB_CLIENT_SECRET = st.secrets.get("GITHUB_CLIENT_SECRET") or ""

REDIRECT_URI = st.secrets.get("OAUTH_REDIRECT_URI") or ""


def get_google_auth_url():
    """Generate Google OAuth authorization URL"""
    params = {
        "client_id": GOOGLE_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "response_type": "code",
        "scope": "openid email profile",
        "state": "google"
    }

    return (
        "https://accounts.google.com/o/oauth2/v2/auth?"
        + urlencode(params)
    )


def get_github_auth_url():
    """Generate GitHub OAuth authorization URL"""
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user:email read:user",
        "state": "github"
    }

    return (
        "https://github.com/login/oauth/authorize?"
        + urlencode(params)
    )


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
        token_res = requests.post(token_url, data=data)
        token_res.raise_for_status()

        access_token = token_res.json().get("access_token")

        if not access_token:
            return None

        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        user_res = requests.get(
            "https://www.googleapis.com/oauth2/v3/userinfo",
            headers=headers
        )

        user_res.raise_for_status()
        user_data = user_res.json()

        return {
            "name": user_data.get("name", ""),
            "email": user_data.get("email", ""),
            "avatar": user_data.get("picture", ""),
            "provider": "google"
        }

    except Exception as e:
        print(f"Google OAuth error: {e}")
        return None


def handle_github_callback(code):
    """Exchange code for GitHub access token and fetch profile"""

    token_url = "https://github.com/login/oauth/access_token"

    headers = {
        "Accept": "application/json"
    }

    data = {
        "code": code,
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI
    }

    try:
        token_res = requests.post(
            token_url,
            data=data,
            headers=headers
        )

        token_res.raise_for_status()

        access_token = token_res.json().get("access_token")

        if not access_token:
            return None

        auth_headers = {
            "Authorization": f"token {access_token}"
        }

        user_res = requests.get(
            "https://api.github.com/user",
            headers=auth_headers
        )

        user_res.raise_for_status()
        user_data = user_res.json()

        email_res = requests.get(
            "https://api.github.com/user/emails",
            headers=auth_headers
        )

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
        print(f"GitHub OAuth error: {e}")
        return None