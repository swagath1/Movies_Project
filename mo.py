import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Page Configuration
st.set_page_config(page_title="Movie Analysis App", layout="wide")
st.title("🎬 Ultimate Movie Industry Market Dashboard")

# 2. Load the Local Data File safely
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_movies.csv")
    df.columns = df.columns.str.lower()
    
    # Force budget and gross columns to be numbers so charts and tables don't crash
    if 'budget' in df.columns:
        df['budget'] = pd.to_numeric(df['budget'], errors='coerce').fillna(0)
    if 'gross' in df.columns:
        df['gross'] = pd.to_numeric(df['gross'], errors='coerce').fillna(0)
        
    # Calculate Profit and ROI dynamically
    if 'budget' in df.columns and 'gross' in df.columns:
        df['profit'] = df['gross'] - df['budget']
        df['roi'] = df.apply(lambda row: row['gross'] / row['budget'] if row['budget'] > 0 else 0, axis=1)
        
    return df

try:
    df = load_data()
    
    # ---------------- SIDEBAR FILTERS ----------------
    st.sidebar.header("Filter Dashboard")
    min_year, max_year = int(df['year'].min()), int(df['year'].max())
    year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (1980, max_year))
    
    filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]
    
    # ---------------- SECTION 1: TOP HEADLINE KPIs ----------------
    st.header("🏆 Top Headline Metrics")
    kpi1, kpi2, kpi3 = st.columns(3)
    
    if not filtered_df.empty and 'name' in filtered_df.columns:
        if 'score' in filtered_df.columns and filtered_df['score'].notna().any():
            top_rated = filtered_df.sort_values(by='score', ascending=False).iloc[0]
            kpi1.metric("⭐ Highest Rated Movie", f"{top_rated['name']}", f"{top_rated['score']}/10")
        
        if 'votes' in filtered_df.columns and filtered_df['votes'].notna().any():
            top_votes = filtered_df.sort_values(by='votes', ascending=False).iloc[0]
            kpi2.metric("🗳️ Most Voted Movie", f"{top_votes['name']}", f"{top_votes['votes']:,} votes")
        
        if 'gross' in filtered_df.columns and 'country' in filtered_df.columns:
            yearly_country = filtered_df.groupby(['year', 'country'])['gross'].sum().reset_index()
            if not yearly_country.empty:
                top_market = yearly_country.sort_values(by='gross', ascending=False).iloc[0]
                kpi3.metric("🌎 Top Grossing Country Market", f"{top_market['country']}", f"{top_market['year']}")

    st.markdown("---")
    
    # ---------------- SECTION 2: CHARTS ----------------
    st.header("📊 Market & Budget Visualizations")
    col_chart1, col_chart2, col_chart3 = st.columns(3)
    
    def format_currency(x, pos):
        if x >= 1e9: return f"${x*1e-9:.1f}B"
        return f"${x*1e-6:.0f}M"

    with col_chart1:
        st.subheader("📊 Budget vs. Gross Revenue")
        if not filtered_df.empty:
            fig1, ax1 = plt.subplots(figsize=(5, 4))
            sns.regplot(data=filtered_df, x='budget', y='gross', 
                        scatter_kws={'alpha':0.3, 'color': '#1f77b4'}, 
                        line_kws={'color': 'red', 'linewidth': 2}, ax=ax1)
            ax1.xaxis.set_major_formatter(ticker.FuncFormatter(format_currency))
            ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_currency))
            plt.tight_layout()
            st.pyplot(fig1)

    with col_chart2:
        st.subheader("🔥 Feature Correlation Heatmap")
        core_numeric = ['budget', 'gross', 'runtime', 'score', 'votes', 'roi', 'profit']
        existing_numeric = [col for col in core_numeric if col in filtered_df.columns]
        
        if len(existing_numeric) > 1:
            fig_heat, ax_heat = plt.subplots(figsize=(5, 4))
            corr_matrix = filtered_df[existing_numeric].corr()
            sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax_heat, cbar=False)
            plt.tight_layout()
            st.pyplot(fig_heat)

    with col_chart3:
        st.subheader("💎 Top 5 Highest ROI Hidden Gems")
        if 'roi' in filtered_df.columns and 'budget' in filtered_df.columns:
            roi_df = filtered_df[filtered_df['budget'] > 1000000].sort_values(by='roi', ascending=False).head(5)
            if not roi_df.empty:
                fig2, ax2 = plt.subplots(figsize=(5, 4))
                sns.barplot(data=roi_df, x='roi', y='name', palette='viridis', ax=ax2)
                ax2.set_xlabel("ROI Multiplier (e.g., 5x = 500% Return)")
                ax2.set_ylabel("")
                plt.tight_layout()
                st.pyplot(fig2)

    st.markdown("---")

    # ---------------- SECTION 3: LEADERBOARDS ----------------
    st.header("👑 Industry Leaderboards")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🏢 Top 10 Companies by Budget")
        if 'company' in filtered_df.columns and 'budget' in filtered_df.columns:
            top_companies = filtered_df.groupby('company')['budget'].sum().reset_index().sort_values(by='budget', ascending=False).head(10)
            st.dataframe(top_companies.style.format({'budget': '${:,.0f}'}), use_container_width=True, hide_index=True)
        
    with col2:
        st.subheader("🎭 Top 5 Grossing Actors")
        if 'star' in filtered_df.columns and 'gross' in filtered_df.columns:
            top_actors = filtered_df.groupby('star')['gross'].sum().reset_index().sort_values(by='gross', ascending=False).head(5)
            st.dataframe(top_actors.style.format({'gross': '${:,.0f}'}), use_container_width=True, hide_index=True)
        
    with col3:
        st.subheader("🎬 Top 5 Grossing Directors")
        if 'director' in filtered_df.columns and 'gross' in filtered_df.columns:
            top_directors = filtered_df.groupby('director')['gross'].sum().reset_index().sort_values(by='gross', ascending=False).head(5)
            st.dataframe(top_directors.style.format({'gross': '${:,.0f}'}), use_container_width=True, hide_index=True)

except Exception as e:
    st.error("Error loading application.")
    st.info(f"System details: '{str(e)}'")
