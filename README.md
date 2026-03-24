# 💰 Sales Profit Prediction — EDA & Machine Learning

An end-to-end data science project covering **Exploratory Data Analysis (EDA)** and **Machine Learning-based Profit Prediction** with a Streamlit web app.

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
- `OneHotEncoder` (drop='first', handle_unknown='ignore') for categorical columns
- `ColumnTransformer` pipeline — fit on train, transform on test
- Train/Test split: 72% / 28% (`random_state=42`)

### Models Evaluated

| Model | Train R² | Test R² |
|---|---|---|
| Linear Regression | 0.699 | 0.702 |
| Decision Tree | 1.000 | 0.998 |
| Gradient Boosting | 0.972 | 0.972 |
| AdaBoost | — | — |

### Hyperparameter Tuning

`GridSearchCV` with 5-fold cross-validation on `GradientBoostingRegressor`:

```
Best Params: learning_rate=0.1, max_depth=5, n_estimators=120, subsample=1.0
Best CV Score (R²): 0.9855
```

### Final Model Performance (Tuned GradientBoostingRegressor)

```
MAE  : 16.45
MSE  : 960.08
RMSE : 30.99
R²   : 0.9953
```

### Model & Preprocessor Saved

```python
import pickle

with open("model.pkl", "wb") as f:
    pickle.dump(gb, f)

with open("preprocessor.pkl", "wb") as f:
    pickle.dump(preprocessor, f)
```

---

## 🌐 Part 3 — Streamlit Web App (`main.py`)

A live profit prediction web app. Users fill in customer and product details and get an instant predicted profit along with an expected range.

### Input Fields

| Field | Type | Options |
|---|---|---|
| Month | Dropdown | January – December (12 options) |
| Customer Age | Number | 10 – 100 |
| Customer Gender | Dropdown | M, F |
| Country | Dropdown | Australia, Canada, France, Germany, United Kingdom, United States |
| State | Dropdown | All 53 states/regions across the 6 countries |
| Product Category | Dropdown | Accessories, Bikes, Clothing |
| Sub Category | Dropdown | 17 sub-categories (Bike Racks, Road Bikes, Helmets, etc.) |
| Product | Dropdown | All 130 products from the dataset |
| Order Quantity | Number | Min 1 |
| Unit Cost | Number | — |
| Unit Price | Number | — |

### Output
- **Predicted Profit** — single value from the model
- **Expected Range** — predicted value ± 50

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
   git clone https://github.com/<your-username>/sales-profit-prediction-ml.git
   cd sales-profit-prediction-ml
   ```

2. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn streamlit
   ```

3. Open notebooks in order:
   - `sales_eda.ipynb` — start here for data understanding
   - `model_training.ipynb` — train the model, this saves `model.pkl` and `preprocessor.pkl`

4. Launch the web app:
   ```bash
   streamlit run main.py
   ```

> No local data download needed — the dataset is loaded directly from a public GitHub URL inside the notebooks.

---

## 📌 Future Improvements

- Try `XGBoostRegressor` or `LightGBM` for comparison
- Add cross-validation scores for all models
- Deploy the Streamlit app on [Streamlit Cloud](https://streamlit.io/cloud) for public access
- Filter states dynamically based on selected country in the web app