# Playwright + Python UI Test Automation Framework (POM)

A **UI Test Automation Framework** built with **Playwright**, **Python**, and **Pytest** using the **Saucelab demo app** and **Page Object Model (POM)** design pattern.  
This framework is designed for **scalability, maintainability, and readability**, making it easy to add and maintain UI test cases.

---

## 🚀 Features
- **Playwright + Python** for fast, reliable browser automation.
- **Page Object Model (POM)** for clean separation of page locators and actions.
- **Pytest** as the test runner with built-in fixtures.
- **Cross-browser testing** (Chromium, Firefox, WebKit).
- **Headless & headed execution** modes.
- **HTML reporting** with `pytest-html`.
- Easy to integrate into **CI/CD pipelines**.

---

## 🛠️ Installation & Setup
1. **Clone the repository**
```bash
git clone https://github.com/yourusername/playwright-pom-framework.git
cd into the project root
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ▶️ Running Tests
Run all tests:
```bash
pytest
```

Run tests with HTML report:
```bash
pytest --html=reports/report.html
```

Run in headed mode:
```bash
pytest --headed
```

Run in a specific browser:
```bash
pytest --browser=firefox
```

---
