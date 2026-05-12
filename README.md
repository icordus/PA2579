# Student Performance Risk Prediction

## Overview
This project predicts whether a student is likely to **Pass** or **Fail** using the UCI Student Performance dataset and a Decision Tree model.

Target definition:
- Pass: `G3 >= 10`
- Fail: `G3 < 10`

To avoid data leakage, `G3` is removed from input features after creating the target.

## Project Structure
- `data/`: raw and processed datasets
- `models/`: saved trained model
- `results/`: metrics and plots
- `src/`: preprocessing, training, evaluation, prediction, API
- `tests/`: unit and API tests

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run Pipeline
1. Preprocess:

```bash
python -m src.preprocess
```

2. Train model:

```bash
python -m src.train --data data/raw/student-mat.csv
```

3. Run demo prediction:

```bash
python -m src.predict --data data/raw/student-mat.csv
```

## API
Start API locally:

```bash
python -m src.api
```

Health endpoint:
- `GET /health`

Prediction endpoint:
- `POST /predict`

## Tests
Run all tests:

```bash
pytest -q
```

Run only API tests:

```bash
pytest tests/api -v
```

## Outputs
After training, expected outputs include:
- model artifact in `models/`
- metrics and plots in `results/`

## Publishing to TestPyPI

The `release.yml` workflow publishes the package to [TestPyPI](https://test.pypi.org) automatically when a version tag is pushed, or manually via `workflow_dispatch`.

### 1. Create a TestPyPI account and API token

1. Register at [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/)
2. Go to **Account Settings → API tokens**
3. Click **Add API token**
   - Token name: `github-actions`
   - Scope: **Entire account** (or limit to this project once uploaded)
4. Copy the generated token (starts with `pypi-`)

### 2. Add the token to GitHub Actions

1. Open the repository on GitHub
2. Go to **Settings → Secrets and variables → Actions**
3. Click **New repository secret**
   - Name: `TESTPYPI_TOKEN`
   - Value: paste the token from TestPyPI
4. Click **Add secret**

### 3. Trigger a release

Tag a commit and push to trigger the workflow automatically:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Or run it manually from **Actions → Release Package → Run workflow**.

## Notes
This is an educational prototype and should support, not replace, human academic decisions.
