---

## 🧑‍💻 Developer

**Made with ❤️ by Zainul Aabdeen**  
📬 Contact: [zainulcode@gmail.com](mailto:zainulcode@gmail.com)

---

## 🛡️ License

MIT License — free to use, modify, and share.

---

## ⭐️ Support This Project

If you found this helpful, leave a ⭐️ on GitHub or share the app with friends!

---

## 🧩 Challenges Faced

Creating this project wasn't just about building a UI — it involved overcoming tricky real-world data and deployment problems. Here's what we tackled:

### 1. 🧾 Unstructured PDF Data

- The original CAP cutoff data came as a **non-tabular, cluttered PDF**
- Data was vertically aligned, with no consistent table structure
- Tools like Camelot and Tabula failed because they rely on tabular formatting

**🛠 Solution:**  
A custom parser was built using `pdfplumber`, regular expressions, and a stateful logic system to extract and align data into a usable CSV.

---

### 2. 🔗 Mapping Categories to Cutoffs

- Category labels and cutoff values appeared separately in the PDF
- Their positions varied and alignment was not guaranteed

**🛠 Solution:**  
Used position-based pairing and a custom `ParsingState` class to track college, branch, and category context while parsing.

---

### 3. 💥 Incompatibility with Python 3.13

- `streamlit` wasn't installable with Python 3.13, causing deployment issues

**🛠 Solution:**  
Switched to **Python 3.11**, created a virtual environment, and ensured compatibility across all modules.

---

### 4. 🧨 Replit & Cloud Limitations

- Replit lacked support for `streamlit`, and PowerShell blocked script activation on Windows
- Interactive command-line input was limited

**🛠 Solution:**  
Shifted to full **local development with PyCharm**, used Git for version control, and deployed using **Streamlit Cloud** with GitHub integration.

---

### 5. 🚀 Live Deployment via GitHub

- Learned that Streamlit Cloud only deploys from **public GitHub repositories** on the free tier
- Understood how to set up `requirements.txt`, push changes, and trigger redeployment

**🛠 Solution:**  
Structured the project cleanly, added environment files, and deployed the app publicly at [Streamlit Cloud](https://streamlit.io/cloud)

---

This app is a great example of how real-world data projects often involve not just code, but **debugging, deployment, and design thinking** as well.

### More about the web app if you are intrested you can read this :
# 🎓 MHT CET College Predictor 2023–24

A powerful web-based tool to help MHT CET aspirants explore engineering college options based on their percentile, category, and preferred branch — with support for eligibility analysis and near-miss insights.

![App Screenshot](https://user-images.githubusercontent.com/your-username/your-logo-or-screenshot.png)

---

## 🚀 Features

- 🔍 Predict colleges based on your **MHT CET percentile**
- 🎯 See **Eligible**, **Safe**, and **Near Miss** colleges
- 📊 Filter by **Category**, **Branch**, and **College Name**
- 💡 Clean Streamlit UI with real-time updates
- 🧠 Uses official **CAP Round 1 cutoffs (2023–24)**
- ❤️ Built with love by Zain

---

## 🖼️ Live Demo

👉 [View App on Streamlit Cloud](https://your-app-url.streamlit.app)

---

## 📂 Files Included

| File                        | Description                                   |
|----------------------------|-----------------------------------------------|
| `predictor.py`             | Main Streamlit app script                     |
| `final_structured_cutoffs.csv` | Structured dataset of college cutoffs        |
| `requirements.txt`         | Python packages required for deployment       |
| `logo.png` *(optional)*    | Your branding/logo file                       |

---

## 📦 Requirements

- Python 3.10 or 3.11 (✅ tested)
- Required Python packages:


