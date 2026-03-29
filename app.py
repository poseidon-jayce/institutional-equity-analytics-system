import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Configuration ---
st.set_page_config(page_title="Asset Risk & Predictive Analytics", layout="wide")
st.title("📊 Institutional Equity Risk & Predictive Analytics")
st.markdown("### Professional Market Intelligence Dashboard | NIFTY 50 Universe")

# --- 1. High-Performance Data Loading (Using CSV) ---
@st.cache_data
def load_data():
    # Load the 60,000+ rows we exported from Oracle
    df = pd.read_csv('nifty50_market_data.csv')
    df.columns = [c.upper() for c in df.columns]
    # Ensure PRICE_DATE is in datetime format for proper plotting
    df['PRICE_DATE'] = pd.to_datetime(df['PRICE_DATE'])
    
    # Load the Pre-calculated Risk Metrics (Beta/Sharpe)
    risk_df = pd.read_csv('nifty50_risk_metrics.csv')
    risk_df.columns = [c.upper() for c in risk_df.columns]
    return df, risk_df

# Safe execution: handle potential file missing errors
try:
    df_market, df_risk = load_data()
except Exception as e:
    st.error(f"Data Source Error: {e}. Ensure CSV files are uploaded to the Space.")
    st.stop()

# --- 2. Sidebar Navigation ---
st.sidebar.header("Control Panel")
option = st.sidebar.selectbox("Analysis Engine", ["Market Correlation Matrix", "Stochastic Price Simulation"])

# --- 3. Feature: Market Correlation Matrix ---
if option == "Market Correlation Matrix":
    st.header("NIFTY 50 Sector-Wide Correlation Heatmap")
    st.write("Quantifying inter-asset relationships for systematic risk mitigation (CFA Standard).")
    
    # Filter for YTD data to keep the matrix high-resolution
    recent_df = df_market[df_market['PRICE_DATE'] > '2024-01-01']
    pivot_df = recent_df.pivot(index='PRICE_DATE', columns='TICKER', values='CLOSE_PRICE').pct_change().dropna()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(pivot_df.corr(), cmap='RdYlGn', center=0, ax=ax, linewidths=0.1)
    st.pyplot(fig)

# --- 4. Feature: Stochastic Price Simulation ---
elif option == "Stochastic Price Simulation":
    ticker = st.selectbox("Select Asset Ticker", sorted(df_market['TICKER'].unique()))
    
    # Fetch Risk Metrics for the selected ticker
    ticker_risk = df_risk[df_risk['TICKER'] == ticker]
    beta = ticker_risk['BETA'].values[0] if not ticker_risk.empty else 0.0
    sharpe = ticker_risk['SHARPE_RATIO'].values[0] if not ticker_risk.empty else 0.0
    
    st.header(f"Predictive Risk Modeling: {ticker}")
    col1, col2 = st.columns(2)
    col1.metric("Beta (Systematic Risk)", f"{beta:.2f}")
    col2.metric("Sharpe Ratio (Risk-Adj. Return)", f"{sharpe:.2f}")

    # Monte Carlo Logic (Geometric Brownian Motion)
    prices = df_market[df_market['TICKER'] == ticker].sort_values('PRICE_DATE')['CLOSE_PRICE']
    returns = prices.pct_change().dropna()
    mu, sigma, last_price = returns.mean(), returns.std(), prices.iloc[-1]
    
    num_sims = 1000  # Optimized for web-server performance
    num_days = 30
    sim_results = np.zeros((num_days, num_sims))

    for i in range(num_sims):
        path = [last_price]
        for d in range(num_days - 1):
            path.append(path[-1] * (1 + np.random.normal(mu, sigma)))
        sim_results[:, i] = path

    # Plotting the Fan Chart (Predictive Range)
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    ax2.plot(sim_results, color='grey', alpha=0.05)
    ax2.axhline(y=last_price, color='blue', linestyle='--', label="Current Price")
    ax2.set_title(f"30-Day Monte Carlo Price Forecast: {ticker}")
    ax2.set_ylabel("Price (INR)")
    ax2.set_xlabel("Days into Future")
    st.pyplot(fig2)
    
    # Value at Risk (VaR) Analytics
    var_95 = np.percentile(sim_results[-1, :], 5)
    potential_loss = ((last_price - var_95) / last_price) * 100
    st.warning(f"*Institutional Risk Assessment:* At a 95% confidence interval, the maximum potential 30-day loss is projected at *{potential_loss:.2f}%*.")

st.sidebar.markdown("---")
st.sidebar.write("Developed for: *Advanced DBMS & Predictive Analytics Portfolio*")