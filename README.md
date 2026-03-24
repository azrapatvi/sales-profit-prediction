# 🚲 Bike Sales — EDA & Profit Prediction

An end-to-end data science project on a real-world bike sales dataset covering **Exploratory Data Analysis (EDA)** and **Machine Learning-based Profit Prediction**.

---

## 📁 Project Structure

```
├── sales_eda.ipynb          # Exploratory Data Analysis
├── model_training.ipynb     # ML Model Training & Evaluation
├── main.py                  # Streamlit Web App
├── model.pkl                # Trained GradientBoosting model (saved after training)
├── preprocessor.pkl         # Fitted ColumnTransformer (saved after training)
└── README.md
```

---

## 📊 Dataset

- **Source:** [FreeCodeCamp Pandas Real-Life Example](https://github.com/ine-rmotr-curriculum/FreeCodeCamp-Pandas-Real-Life-Example)
- **Size:** 113,036 rows × 18 columns
- **Features:** Date, Customer Age, Gender, Country, State, Product Category, Sub-category, Product, Order Quantity, Unit Cost, Unit Price, Revenue, Cost, Profit

---

## 🔍 Part 1 — Exploratory Data Analysis (`sales_eda.ipynb`)

### Steps Covered
- Data loading, cleaning, and type conversion
- Duplicate removal
- Feature engineering: added **ROI** column `(profit / cost) * 100`
- Distribution analysis using box plots

### Key Insights

| Analysis | Finding |
|---|---|
| Revenue by Year | 2015 generated the highest sales; overall upward trend |
| Product Category | **Bikes** generate the most revenue and profit |
| Top Sub-category | Road Bikes lead in revenue |
| Age Group | **Adults (35–64)** are the most profitable segment |
| Gender | Female customers spend slightly more on average |
| Top Country | **United States** generates the highest revenue |
| Top State | **California** leads in sales |
| Correlation | Unit price (0.75) and revenue are strongly correlated with profit |

---

## 🤖 Part 2 — Model Training (`model_training.ipynb`)

### Target Variable
`profit`

### Features Used
`month`, `customer_age`, `customer_gender`, `country`, `state`, `product_category`, `sub_category`, `product`, `order_quantity`, `unit_cost`, `unit_price`

### Preprocessing
- `StandardScaler` for numerical columns
- `OneHotEncoder` (drop='first') for categorical columns
- `ColumnTransformer` pipeline — fit on train, transform on test

### Models Evaluated

| Model | Train R² | Test R² |
|---|---|---|
| Linear Regression | 0.699 | 0.702 |
| Decision Tree | 1.000 ⚠️ | ~0.95 |
| Gradient Boosting | — | 0.850 |
| AdaBoost | — | — |

> ⚠️ **Decision Tree overfits** — Train R² of 1.0 means it memorized the training data. Add `max_depth` and `min_samples_leaf` constraints to fix this.

### Hyperparameter Tuning

`GridSearchCV` with 5-fold cross-validation on `GradientBoostingRegressor`:

```
Best Params: learning_rate=0.1, max_depth=5, n_estimators=120, subsample=1.0
Best CV Score (R²): 0.9854
```

### Known Bugs Fixed / To Fix

1. **Decision Tree overfitting** — use `max_depth=10, min_samples_leaf=5`
2. **Wrong model used in Cell 29** — `model.predict()` was used instead of `gb.predict()`; `model` pointed to AdaBoost from the loop
3. **GridSearch best model not used** — `grid.best_estimator_` should be used for final evaluation, not a new default instance

---

## 🌐 Part 3 — Streamlit Web App (`main.py`)

A live profit prediction web app built with Streamlit. Users fill in customer and product details and get an instant predicted profit along with an expected range.

### Input Fields

| Field | Type |
|---|---|
| Month | Dropdown |
| Customer Age | Number (10–100) |
| Customer Gender | Dropdown (M / F) |
| Country | Text |
| State | Text |
| Product Category | Text |
| Sub Category | Text |
| Product Name | Text |
| Order Quantity | Number |
| Unit Cost | Number |
| Unit Price | Number |

### Output
- **Predicted Profit** — single value from the model
- **Expected Range** — predicted value ± 50 (confidence buffer)

### Prerequisites
Before running the app, save the trained model and preprocessor from `model_training.ipynb`:

```python
import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(best_gb, f)         # your trained GradientBoosting model

with open("preprocessor.pkl", "wb") as f:
    pickle.dump(preprocessor, f)    # your fitted ColumnTransformer
```

### Run the App

```bash
streamlit run main.py
```

---

## 🛠️ Tech Stack

- Python 3.x
- pandas, numpy
- matplotlib, seaborn
- scikit-learn
- streamlit

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/bike-sales-eda-profit-prediction.git
   cd bike-sales-eda-profit-prediction
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn streamlit
   ```

3. Open notebooks in order:
   - `sales_eda.ipynb` — start here for data understanding
   - `model_training.ipynb` — train the model and save `model.pkl` + `preprocessor.pkl`

4. Launch the web app:
   ```bash
   streamlit run main.py
   ```

> No local data download needed — the dataset is loaded directly from a public GitHub URL inside the notebooks.

---

## 📌 Future Improvements

- Fix the 3 bugs in `model_training.ipynb` (listed above)
- Try `XGBoostRegressor` or `LightGBM` for better performance
- Add cross-validation scores for all models
- Deploy the Streamlit app on [Streamlit Cloud](https://streamlit.io/cloud) for public access
- Add input validation in the web app (e.g. check country/state against known values)