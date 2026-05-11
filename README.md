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
- `app.py`: Streamlit prototype

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

## Streamlit Demo
```bash
streamlit run app.py
```

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

## Notes
This is an educational prototype and should support, not replace, human academic decisions.
