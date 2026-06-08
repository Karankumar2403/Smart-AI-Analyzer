# 🚀 **Smart AI Analyzer**

An all-in-one, intelligent enterprise resume optimization platform powered by **Google Gemini AI** and **Streamlit**. Seamlessly calculate ATS scores, extract critical skill gaps, auto-recommend skill-building courses, and construct standard resumes within a premium glassmorphic dashboard.

---

## 📽️ **Walkthrough & Demo**

Here is a quick video demonstration of the Smart AI Analyzer in action, showcasing the secure entry gate, next-gen theme switching, real-time Gemini analysis, and interactive dashboard analytics:

<div align="center">
  <video src="assets/walkthrough.mp4" width="100%" controls style="border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.35);">
    Your browser does not support the video tag.
  </video>
  <p><i>Note: Place your screen recording inside the <code>assets/</code> folder named <code>walkthrough.mp4</code> to update this demo!</i></p>
</div>

---

## 🌟 **Key Features**

*   🔒 **Secure Entry Login Gate**: Restricts application access to authorized users with custom JWT session management and OAuth (Google & GitHub) logins.
*   🎨 **Next-Generation Theming**: Instant switching between **Sleek Dark**, **Modern Light**, and **Sunset Glow** themes, adapting all charts, metrics, and segmented controls dynamically.
*   🔍 **AI-Powered Resume Analysis**: Calculates exact ATS matches, formatting quality, structure consistency, and isolates missing keywords via Google Gemini API.
*   📝 **Smart Resume Builder**: Generate resumes and export them instantly to **MS Word (.docx)**, **PDF (.pdf)**, and **Plain Text (.txt)** files.
*   📊 **Analytics Dashboard**: Tracks profile scores, views, and downloads. Includes chronological line charts mapping career progression.
*   🎯 **Role-Based Suggestions**: In-depth analysis of engineering, marketing, management, and product roles with tailored keyword tracking.
*   💡 **Resource Recommendation**: Auto-curates matching YouTube courses and playlists to fill detected skill gaps.

---

## 🚀 **Quick Start**

### 1. Clone & Initialize
```bash
git clone https://github.com/Karankumar2403/Smart-AI-Analyzer.git
cd Smart-AI-Analyzer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Setup Environment Variables
Create a `.env` file in the root directory:
```env
# Gemini API Key (Supports either variable name)
GEMINI_API_KEY=your_gemini_api_key_here
GOOGLE_API_KEY=your_gemini_api_key_here

# OAuth Keys (Retrieve from Google & GitHub Developer Consoles)
GOOGLE_CLIENT_ID=your_google_client_id_here
GOOGLE_CLIENT_SECRET=your_google_client_secret_here
GITHUB_CLIENT_ID=your_github_client_id_here
GITHUB_CLIENT_SECRET=your_github_client_secret_here

# JWT Session Configuration
JWT_SECRET=super_secret_jwt_key
```

### 4. Run the Application
```bash
python run_app.py
```
Or start via Streamlit directly:
```bash
streamlit run app.py
```

---

## 🛠️ **Technologies Used**

*   **Frontend**: Streamlit, HTML5, Custom CSS3, Lottie Animations, Google Fonts (Outfit, Inter)
*   **AI Engine**: Google Gemini AI (Generative AI API)
*   **Data Analysis & DB**: SQLite3, Pandas, Plotly Express
*   **Document Parsers & Generators**: ReportLab (PDF), python-docx (Word), pdfminer.six, docx2txt

---

## 📝 **License & Credits**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Developed by [Karan Kumar](https://github.com/Karankumar2403).
