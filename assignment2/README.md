# SauceDemo Selenium WebDriver Test Suite

This project is a small but structured Selenium WebDriver test suite for the public demo application:

- Application under test: https://www.saucedemo.com/
- Selenium: https://www.selenium.dev/

The suite contains **10 automated test scenarios** and is designed to demonstrate the core qualities from the lecture **VGT Best Practices**:

- **Maintainability** through Page Object Model classes and centralized selectors
- **Reusability** through shared fixtures and reusable page methods
- **Modularity** through separation into `pages/`, `tests/`, and shared setup
- **Readability** through short, focused test methods with clear names
- **Synchronization** through explicit waits (`WebDriverWait`) instead of static sleeps

## Project structure

```text
saucedemo_selenium_suite/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── product_page.py
│   ├── cart_page.py
│   └── checkout_page.py
└── tests/
    └── test_saucedemo.py
```

## Included test scenarios

1. Valid login opens the inventory page
2. Locked-out user sees the correct error message
3. Inventory contains the expected number of products
4. Product details page shows the expected information
5. Adding a product updates the cart badge
6. Cart preserves items and supports removal
7. Sorting by price low-to-high reorders products correctly
8. Checkout validates mandatory information
9. Successful checkout shows confirmation
10. Logout returns the user to the login page

## Prerequisites

- Python 3.11+ recommended
- Google Chrome installed
- Internet access to download the matching ChromeDriver on first run

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
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run all tests

The entire suite is executable from a single command:

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

## Notes for the report/submission

- The test suite uses **explicit waits** and avoids `time.sleep()`.
- Test data is centralized in `conftest.py`.
- Page locators are encapsulated inside page objects to reduce maintenance effort.
- Each test method has a descriptive name so the scenario is understandable without opening extra documentation.

## Suggested zip submission

Zip the root folder so the archive contains the full runnable project:

```bash
zip -r saucedemo_selenium_suite.zip saucedemo_selenium_suite
```
