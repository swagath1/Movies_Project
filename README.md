# 🎬 Ultimate Movie Industry Market Dashboard

 👉 **[Click Here to View the Live Interactive Dashboard!](https://moviesproject-vgw8h3k26mdfkw7afsjvwp.streamlit.app)**

An end-to-end data analytics project using Python to engineer data pipelines, perform exploratory analysis, and deploy an interactive web-based business intelligence dashboard examining the market forces behind film industry profitability.

---

## 📊 Dashboard Preview

### 📈 Market Trends & Interactions
![Movie Market Analysis Dashboard Preview 1](Dashboard%20Preview.png)

### 👑 Industry Leaderboards
![Movie Market Analysis Dashboard Preview 2](Dashboard%20Preview1.png)

---

## 🚀 Key Business Insights Discovered
* **The Revenue Driver:** Financial budget scaling exhibits a massive, predictable linear relationship with gross returns ($R^2$ verified via statistical regression). 
* **The ROI Myth:** While massive production studios control the absolute budget volume, nimble independent films routinely secure dramatically higher ROI multipliers on tightly constrained budgets.
* **Feature Interactions:** The automated heatmap reveals a strong positive correlation (0.63) between public engagement/voting activity and gross financial performance, suggesting that early audience traction is a critical leading indicator for executive forecasting.

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
