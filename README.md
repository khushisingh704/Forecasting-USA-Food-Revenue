#Restaurant Revenue Forecasting with SARIMAX and Power BI

📌 Project Overview
This project predicts restaurant revenues using SARIMAX time series forecasting in Python and visualizes historical vs. forecasted revenues in Power BI for actionable business insights.

🎯 Objective
Predict monthly revenue 12 months ahead to support demand planning and budgeting for restaurants.

🛠️ Tools Used
Python: Pandas, SARIMAX (statsmodels), US federal holidays

Power BI: Interactive dashboard creation and trend visualization

📂 Data
Historical monthly revenue data (1992 – April 2025).

🚀 Features
1️⃣ Data Cleaning
Removed non-numeric and summary rows (e.g., “TOTAL”).

Cleaned (p), (r) flags from month columns.

Converted columns to proper datetime index for modeling.

2️⃣ Feature Engineering
Added holiday flags using the US federal holiday calendar.

Created month-over-month growth % for business tracking.

3️⃣ Forecasting with SARIMAX
Implemented SARIMAX with exogenous variables (holiday flags) for seasonality handling.

Extended forecasts up to May 2026.

Evaluated model performance using MAE and RMSE.

4️⃣ Visualization with Power BI
Combined historical and forecasted data for direct comparison.

Displayed revenue trends, YoY growth, and forecast vs. actual using clear line and bar charts.

Included KPI cards for forecast values and growth tracking.

📈 Results
MAE: ~6,400 on a ~70,000 revenue scale (~9% relative error).

RMSE: ~6,600.

Clear visual differentiation between historical and forecasted revenues.

Month-over-month growth % tracked for actionable business insights.


