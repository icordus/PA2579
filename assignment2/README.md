# OWASP Juice Shop Selenium Test Suite (Assignment 2)

This folder contains a Selenium + pytest test suite for OWASP Juice Shop.

- Application under test: https://juice-shop.herokuapp.com/
- Tech stack: Python, pytest, Selenium WebDriver, Page Object Model (POM)
- Scope: 10 end-to-end UI scenarios

## Goals

The suite is structured around core VGT best practices:

- Maintainability: locators and UI actions are encapsulated in page objects
- Reusability: shared fixtures and helper methods are centralized
- Modularity: setup, pages, and tests are clearly separated
- Readability: tests are small, direct, and clearly named
- Synchronization: explicit waits are used instead of static sleeps

## Project structure

```text
assignment2/
|- conftest.py
|- pytest.ini
|- requirements.txt
|- README.md
|- pages/
|  |- base_page.py
|  |- login_page.py
|  |- inventory_page.py
|  |- product_page.py
|  |- cart_page.py
|  `- checkout_page.py
`- tests/
   `- test_juice_shop.py
```

## Test scenarios

1. Valid login opens the product listing
2. Invalid login shows an error message
3. Products page lists multiple products
4. Product detail dialog shows name and price
5. Adding a product to the basket updates the basket counter
6. Basket shows the added product
7. Search filters the product list
8. Registration form validates email format
9. Logout returns the user to the unauthenticated state
10. Product detail dialog can be closed

## Credentials used

| Account | Email | Password |
|---------|-------|----------|
| Admin   | admin@juice-sh.op | admin123 |

## Requirements

- Python 3.11+
- Google Chrome installed
- Internet access (tests run against live Juice Shop)

## Environment note

- This suite was tested on Ubuntu 24 VM running in VirtualBox.
- On that setup, Chromium and a compatible Chrome WebDriver/Chromedriver are required.

## Setup

Run the commands from the assignment2 folder.

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run tests

Run all tests:

```bash
pytest -v
```

Run only this suite file:

```bash
pytest -v tests/test_juice_shop.py
```

## Pytest discovery note

`pytest.ini` is configured to collect tests only from `tests/` in this folder.
This avoids collecting other nested suites and prevents import collisions.

## Troubleshooting

- `pytest: command not found`
  - Activate your virtual environment first.
  - Or run with `python -m pytest -v`.

- Browser startup issues
  - Verify Chrome is installed and up to date.
  - Reinstall dependencies: `pip install -r requirements.txt --upgrade`.

- Collection or import errors
  - Run `pytest --collect-only -q` to inspect discovery.
  - Check that you are in the assignment2 folder when running pytest.

## Notes

- Tests use explicit waits and avoid `time.sleep()`.
- Test constants (base URL and credentials) are kept in `conftest.py`.
- Each test uses a fresh browser session for isolation.
