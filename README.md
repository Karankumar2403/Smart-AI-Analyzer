# 🚀 **Smart AI Analyzer**

Hi! I'm Karan Kumar. I built **Smart AI Analyzer** as a self-made personal project to solve a challenge many job-seekers face: optimizing resumes to beat applicant tracking systems (ATS) without losing the human touch. 

This is an all-in-one, intelligent resume optimization and builder platform powered by **Google Gemini AI** and **Streamlit**. It allows candidates to calculate precise ATS scores, map missing keywords, generate tailored resumes, and track their preparation progress within a beautiful glassmorphic dashboard.

---

## 📽️ **Walkthrough Demo**

Here is a quick demonstration showing how the application functions, from the secure login gate to dynamic theme switching, real-time AI resume analysis, and exporting builder content:

<div align="center">
  <video src="assets/walkthrough.mp4" width="100%" controls style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.35);">
    Your browser does not support the video tag.
  </video>
  <p><i>Note: Place your screen recording inside the <code>assets/</code> folder named <code>walkthrough.mp4</code> to update this demo!</i></p>
</div>

---

## 🌟 **Key Features I Implemented**

*   🔒 **Secure Portal Login**: Restricts app access using OAuth (Google & GitHub) and standard Administrator login verification, securing workspaces behind custom JWT tokens.
*   🎨 **Sleek Dynamic Theming**: Built-in toggle to swap between **Sleek Dark**, **Modern Light**, and **Sunset Glow** themes, updating all Plotly charts, segmented control tabs, and card highlights in real-time.
*   🔍 **AI-Powered Analysis**: Integrates the Google Gemini API to analyze uploaded resumes, score format quality, and pinpoint missing keywords.
*   📝 **Multi-Format Resume Builder**: Generates standard resumes and supports downloading them instantly in **Word (.docx)**, **PDF (.pdf)**, and **Plain Text (.txt)** formats.
*   📊 **Analytics & Progression Tracking**: Logs resume uploads over time and maps ATS score progression chronologically on a beautiful Plotly line chart.
*   🎯 **Targeted Career Suggestions**: Provides specific keyword matches for different job roles, auto-recommending skill-building video courses to fill gaps.

---

## 🧠 **My Learnings**

Building this project from scratch was an incredible learning experience that helped me level up as a software engineer:
1.  **State Management in Streamlit**: Streamlit is highly reactive, which can make managing state complex. I learned how to utilize `st.session_state` to store JWT sessions, preserve form configurations, and keep theme choices consistent across reruns.
2.  **API Integration & Prompt Engineering**: Working with the Google Gemini API taught me how to write robust prompts to extract highly structured JSON feedback from resumes.
3.  **Dynamic PDF Generation**: I learned how to use ReportLab to build PDF generator logic programmatically, handling page margins, fonts, and text flow dynamically.
4.  **Database Design**: Integrated SQLite to build custom tables, running relational joins to link uploaded resumes with ATS score results for tracking user metrics.

---

## 🛠️ **Challenges Faced & How I Overcame Them**

### 1. Securing App Routes in Streamlit
*   **The Challenge**: Streamlit doesn't support built-in middleware or page route guards. Users could bypass pages simply by editing state variables.
*   **How I Solved It**: I structured a routing wall at the entry point of my `main()` loops, checking for session tokens before letting any page components load. If authentication checks fail, all page components are blocked behind the login cards.

### 2. Bypassing Git Secret Scans
*   **The Challenge**: When setting up OAuth client configurations, git push protection rules blocked my updates because of hardcoded credential profiles.
*   **How I Solved It**: I refactored the credentials out of code files, setting up local environment variable loading via `.env` files. This keeps key strings private while maintaining public code integrity.

### 3. Dynamic Color Variable Inheritance
*   **The Challenge**: Standard Streamlit elements don't inherit CSS custom properties easily, meaning changing the UI theme would often leave background elements or charts mismatched (e.g., hardcoded green boxes).
*   **How I Solved It**: I wrote global CSS variable overrides that target Streamlit's underlying elements (like `button[data-baseweb="tab"]` and `.stCard`), binding their attributes directly to `:root` theme variables. Now, all colors change instantly.

---

## 🚀 **Quick Setup**

### 1. Clone the Project
```bash
git clone https://github.com/Karankumar2403/Smart-AI-Analyzer.git
cd Smart-AI-Analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure `.env` variables
Create a `.env` file in the root directory:
```env
# Gemini AI
GEMINI_API_KEY=your_gemini_api_key_here

# Google & GitHub OAuth Console credentials
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
GITHUB_CLIENT_ID=your_github_client_id_here
GITHUB_CLIENT_SECRET=your_github_client_secret_here

# JWT configuration
JWT_SECRET=your_jwt_secret_key_here
```

### 4. Run the Project
```bash
python run_app.py
```

---

## 📝 **License**

This project is licensed under the MIT License. 

Developed with 💙 by **Karan Kumar**.
