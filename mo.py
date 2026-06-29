import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Page Configuration
st.set_page_config(page_title="Movie Analysis App", layout="wide")
st.title("🎬 Movie Industry Interactive Dashboard")
st.markdown("This app displays key movie metrics and correlation analysis from your cleaned dataset.")

# 2. Load the Local Data
@st.cache_data
def load_data():
    # Looks for the CSV in the exact same folder as this script
    df = pd.read_csv("cleaned_movies.csv")
    return df

try:
    df = load_data()
    
    # ---------------- SIDEBAR FILTERS ----------------
    st.sidebar.header("Filter Dashboard")
    min_year, max_year = int(df['year'].min()), int(df['year'].max())
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (2000, max_year))
    
    # Filter dataset based on slider selection
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    
    # ---------------- KEY METRICS (KPIs) ----------------
    st.subheader("🏆 Key Performance Indicators")
    kpi1, kpi2, kpi3 = st.columns(3)
    
    if not filtered_df.empty:
        # Highest Rated Movie
        top_rated = filtered_df.sort_values(by='score', ascending=False).iloc[0]
        kpi1.metric("⭐ Highest Rated Movie", f"{top_rated['name']}", f"{top_rated['score']}/10")
        
        # Most Voted Movie
        top_votes = filtered_df.sort_values(by='votes', ascending=False).iloc[0]
        kpi2.metric("🗳️ Most Voted Movie", f"{top_votes['name']}", f"{top_votes['votes']:,} votes")
        
        # Highest Revenue Country
        top_country = filtered_df.groupby('country')['gross'].sum().idxmax()
        kpi3.metric("🌎 Top Grossing Country Market", top_country)
    else:
        st.warning("No data available for the selected year range.")

    st.markdown("---")
    
    # ---------------- VISUALIZATIONS ----------------
    col1, col2 = st.columns(2)
    
    # Helper formatting function for cleaner axes ($M / $B)
    def format_currency(x, pos):
        if x >= 1e9: 
            return f"${x*1e-9:.1f}B"
        return f"${x*1e-6:.0f}M"

    with col1:
        st.subheader("📊 Budget vs. Gross Revenue")
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.regplot(data=filtered_df, x='budget', y='gross', 
                    scatter_kws={'alpha':0.4, 'color': '#1f77b4'}, 
                    line_kws={'color': 'red', 'linewidth': 2}, ax=ax1)
        ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_currency))
        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_currency))
        plt.tight_layout()
        st.pyplot(fig1)

    with col2:
        st.subheader("💎 Top 5 Highest ROI Hidden Gems")
        # Filter for budgets over $1M to avoid division-by-zero skewing
        roi_df = filtered_df[filtered_df['budget'] > 1000000].sort_values(by='roi', ascending=False).head(5)
        
        if not roi_df.empty:
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            sns.barplot(data=roi_df, x='roi', y='name', palette='viridis', ax=ax2)
            ax2.set_xlabel("ROI Multiplier (e.g., 5x = 500% Return)")
            ax2.set_ylabel("")
            plt.tight_layout()
            st.pyplot(fig2)
        else:
            st.write("Not enough budget data to calculate ROI for this timeframe.")

except Exception as e:
    st.error("Error loading application. Make sure 'cleaned_movies.csv' is saved in the exact same folder as this script!")
    st.info(f"System details: {str(e)}")