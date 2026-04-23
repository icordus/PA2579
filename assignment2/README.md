# OWASP Juice Shop Selenium WebDriver Test Suite

This project is a small but structured Selenium WebDriver test suite for the publicly available
intentionally vulnerable web application:

- Application under test: https://juice-shop.herokuapp.com/
- Project homepage: https://juice-shop.github.io/
- Selenium: https://www.selenium.dev/

The suite contains **10 automated test scenarios** and is designed to demonstrate the core qualities from the lecture **VGT Best Practices**:

- **Maintainability** through Page Object Model classes and centralized selectors
- **Reusability** through shared fixtures and reusable page methods
- **Modularity** through separation into `pages/`, `tests/`, and shared setup
- **Readability** through short, focused test methods with clear names
- **Synchronization** through explicit waits (`WebDriverWait`) instead of static sleeps

## Project structure

```text
assignment2/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── pages/
│   ├── base_page.py          # shared helpers + dismiss_overlays()
│   ├── login_page.py         # /#/login
│   ├── inventory_page.py     # /#/search  (product listing)
│   ├── product_page.py       # product detail dialog
│   ├── cart_page.py          # /#/basket
│   └── checkout_page.py      # /#/register  (registration / validation)
└── tests/
    └── test_saucedemo.py     # TestJuiceShop – 10 scenarios
```

## Included test scenarios

1. Valid login opens the product listing
2. Invalid login shows an error message
3. Products page lists multiple products
4. Product detail dialog shows name and price
5. Adding a product to the basket updates the basket counter
6. Basket shows the added product
7. Search filters the product list
8. Registration form validates e-mail format
9. Logout returns the user to the unauthenticated state
10. Product detail dialog can be closed

## Credentials used

| Account | E-mail | Password |
|---------|--------|----------|
| Admin   | `admin@juice-sh.op` | `admin123` |

## Prerequisites

- Python 3.11+ recommended
- Google Chrome installed
- Internet access (tests run against the live Heroku demo)

## Setup

Create and activate a virtual environment.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run all tests

```bash
pytest
```

or with verbose output:

```bash
pytest -v
```

## Robustness check

To demonstrate stability, execute the suite several times in a row:

### Windows (PowerShell)

```powershell
1..3 | ForEach-Object { pytest -v }
```

### macOS / Linux

```bash
for i in 1 2 3; do pytest -v; done
```

## Notes

- The test suite uses **explicit waits** and avoids `time.sleep()`.
- Test data (URL, credentials) is centralized in `conftest.py`.
- Page locators are encapsulated inside page objects to reduce maintenance effort.
- `dismiss_overlays()` in `BasePage` handles the cookie-consent banner and any
  Angular Material dialogs (welcome banner, challenge notifications) that appear on load.
- Each test receives a **fresh browser session**, so basket state is clean per test.
