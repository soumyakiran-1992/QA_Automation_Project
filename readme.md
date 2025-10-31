# 🧪 QA Automation Framework (Playwright + Pytest + Python)

This project is a **UI Test Automation Framework** built using **Playwright** and **Pytest** in Python.  
It follows the **Page Object Model (POM)** structure and includes **automatic HTML report generation** after every test run.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/soumyakiran-1992/QA_Automation_Project.git
cd QA_Automation_Project

## ⚙️ Setup Instructions
pip install -r requirements.txt

playwright install

python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate    # On macOS/Linux

pytest tests/test_login_logout.py
