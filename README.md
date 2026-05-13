
# Financial News Sentiment Analysis

An end-to-end data engineering and analysis project to determine the correlation between financial news sentiment and stock market movements. This project was developed as part of the **Project Chimera** initiative.

## 📌 Project Overview
This project performs sentiment analysis on large-scale financial news datasets using **VADER** and correlates the findings with historical stock data fetched via the **yfinance** API.

## 🛠 Tech Stack
- **Language:** Python 3.12
- **Environment:** Ubuntu Linux
- **Libraries:** Pandas, NLTK (VADER), yfinance, Matplotlib, Seaborn
- **Infrastructure:** Git/GitHub for version control

## 📂 Project Structure
```text
news-sentiment-analysis/
├── data/
│   └── raw/              # Raw CSV data (Note: Large files ignored by git)
├── notebooks/
│   ├── EDA.ipynb         # Task 1: Exploratory Data Analysis & Sentiment
│   ├── Quantitative.ipynb# Task 2: Technical Indicators (SMA, MACD, RSI)
│   └── Correlation.ipynb # Task 3: Sentiment & Return Correlation
├── .gitignore            # Prevents large data uploads
└── README.md             # Project documentation

---

## 🛠 Technical Implementation Details

### 1. Data Pipeline
*   **Preprocessing:** Used `pandas` with `format='mixed'` to handle inconsistent date strings across the 300MB+ dataset.
*   **Sentiment Engine:** Integrated `NLTK VADER` to compute daily average sentiment scores, neutralizing high-frequency noise through daily aggregation.
*   **Data Integration:** Flattened `yfinance` MultiIndex headers to align 15 years of historical stock data with news events.

### 2. Analytical Approach
*   **Lag Analysis:** Addressed the "Market Lag" theory by correlating same-day sentiment with price action.
*   **Statistical Validation:** Used Pearson Correlation coefficients and regression plots to measure the strength of the signal.

### 3. Challenges Overcome
*   **Large File Handling:** Optimized the repository by excluding the 311MB raw data file from version control, ensuring a lightweight and deployable codebase.
*   **Timezone Alignment:** Standardized all temporal data to UTC to ensure precise merging between news timestamps and market trading hours.