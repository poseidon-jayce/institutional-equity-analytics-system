# institutional-equity-analytics-system
Institutional-grade Risk Engine &amp; Predictive Analytics platform for NIFTY 50 equities. Features an Oracle 21c RDBMS backend, 60k+ record ETL pipeline, and 10,000-path Monte Carlo simulations for Value at Risk (VaR) forecasting. Engineered for advanced DBMS and Predictive Analytics portfolio standards. Linked to live Cloud Dashboard.
# 📊 Institutional Equity Risk & Predictive Analytics System
*A Full-Stack Financial Engineering Portfolio | Powered by Oracle 21c & Python*

## 🚀 Project Overview
This system is an end-to-end quantitative platform designed to ingest, store, and analyze 5 years of historical market data for the *NIFTY 50* index. It bridges *Enterprise Database Management (DBMS)* with *Stochastic Predictive Modeling (PA)*.
---

## 🛠 Technical Architecture
1. *Extraction (ETL):* Automated Python pipeline utilizing yfinance to ingest ~60,000 records.
2. *Persistence (DBMS):* *Oracle 21c RDBMS* utilizing a relational schema with Foreign Key constraints and indexing for time-series optimization.
3. *Analytics (Quant):* 
   - *Risk Engine:* Calculation of *Beta ($\beta$)* and *Sharpe Ratios* (CFA Level 1 Standards).
   - *Predictive Engine:* *Monte Carlo Simulations* (10,000 paths) using Geometric Brownian Motion.
4. *Interface (UI):* Interactive *Gradio* dashboard for real-time data visualization.

---

## 📂 Repository Structure
*   schema.sql: Oracle 21c Table Definitions & Indexing logic.
*   app.py: Dashboard Source Code.
*   gs_project_phase1.ipynb: Original Research & Oracle development notebook.

*Contact:* Krishna Nibe 
*Objective:* to build a high fidelity risk assessment and analytics system 
