# OWASP Juice Shop Selenium Test Suite (Python)

This project contains a Selenium WebDriver test suite with **10 annotated test cases** for the public OWASP Juice Shop demo application.

It is designed to demonstrate the qualities emphasized in **VGT Best Practices**:
- **Maintainability** through Page Object Model (POM)
- **Reusability** through shared login and navigation methods
- **Modularity** through separation of pages, tests, and setup
- **Readability** through small tests with clear names
- **Synchronization** through explicit waits instead of static sleeps

## Public web application used
- Main project page: https://juice-shop.github.io/
- Public demo used by the tests: https://demo.owasp-juice.shop/#/

## Project structure

```text
juice_shop_selenium_suite_full/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── home_page.py
│   ├── login_page.py
│   └── product_details_page.py
└── tests/
    └── test_juice_shop.py
```

## Preconditions
- Python 3.10+
- Google Chrome installed
- Internet access to the public Juice Shop demo

## Setup

Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the full suite

```bash
pytest
```

## Optional environment variables

Run with a visible browser:
```bash
export HEADLESS=false
pytest
```

Run against a specific Juice Shop URL:
```bash
export JUICE_SHOP_URL="https://demo.owasp-juice.shop/#/"
pytest
```

## Robustness check

```bash
for i in 1 2 3; do pytest || break; done
```

## Covered scenarios
1. Valid login redirects to the home page
2. Invalid login shows an error message
3. Logout returns the user to a logged-out state
4. Product catalog is visible
5. Search filters products
6. Adding an item updates the basket counter
7. Basket contains the added product
8. Removing an item updates the basket contents
9. Sorting changes the displayed product order
10. Product details dialog opens successfully
