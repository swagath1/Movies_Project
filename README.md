# 🎬 Ultimate Movie Industry Market Dashboard

 👉 **[Click Here to View the Live Interactive Dashboard!](https://moviesproject-vgw8b3kz6mdfkw7afsjvwp.streamlit.app/)**

An end-to-end data analytics project using Python to engineer data pipelines, perform exploratory analysis, and deploy an interactive web-based business intelligence dashboard examining the market forces behind film industry profitability.

---

## 📊 Dashboard Preview

### 📈 Market Trends & Interactions
![Movie Market Analysis Dashboard Preview 1](Dashboard%20Preview.png)

### 👑 Industry Leaderboards
![Movie Market Analysis Dashboard Preview 2](Dashboard%20Preview1.png)

---

## 📊 Key Business Insights Discovered
* **The Profit Engine:** Gross revenue has an incredibly strong positive correlation of **0.98** with net profit, proving that scaling absolute box office volume is the primary driver of net returns in this dataset.
* **The Budget Predictor:** Production budget shows a high positive correlation of **0.75** with gross revenue, validating that higher financial backing heavily correlates with higher box office returns.
* **Audience Engagement:** Public engagement via user voting (**votes**) shows a strong correlation of **0.63** with gross revenue, suggesting that widespread audience traction is a strong indicator of financial success.

---

## 🛠️ Project Architecture & Workflow

### 1. Exploratory Data Analysis & Engineering (`Movie_corelation_analysis.ipynb`)
* Managed data pipeline operations within a Google Colab notebook.
* Implemented defensive data handling routines using Pandas to coerce dirty column inputs into structured numeric types (`float64`/`int64`).
* Calculated target business logic metrics dynamically, including **Net Profit** ($Gross - Budget$) and **ROI Multipliers** ($Gross / Budget$).

### 2. Interactive Front-End Interface (`mo.py`)
* Designed a responsive responsive multi-column web layout using Streamlit.
* Engineered a reactive sidebar date slider filter to allow dynamic multi-era temporal slicing.
* Integrated advanced analytical visuals, bridging statistical packages with the frontend:
  * **Seaborn Regression Plots** mapping capital allocation curves.
  * **Correlation Heatmaps** displaying feature dependencies.
  * **Categorical Leaderboards** sorting talent and company market caps using aggregated groups.

---

## 🧰 Tech Stack & Libraries Used
* **Interactive App UI:** Streamlit
* **Data Engineering & Manipulation:** Python, Pandas, NumPy
* **Statistical Visualization:** Seaborn, Matplotlib

---

## 💻 How to Run This Project Locally

To pull down this repository and interact with the codebase on your local machine, run the following steps in your terminal:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/swagath1/Movies_Project.git](https://github.com/swagath1/Movies_Project.git)
   cd Movies_Project
