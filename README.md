# Forecasting-USA-Food-Revenue
# Restaurant Revenue Forecasting with SARIMAX and Power BI
📌 Project Overview
This project predicts restaurant revenues using SARIMAX time series forecasting in Python and visualizes historical vs. forecasted revenues in Power BI for actionable business insights.

🎯 Objective
Predict monthly revenue 12 months ahead to support restaurant demand planning and budgeting.

🛠️ Tools Used
Python: Pandas, SARIMAX (statsmodels), holidays

Power BI: Interactive dashboard creation and trend visualization

📂 Data
Historical monthly revenue data from 1992 to April 2025.

🚀 Features
1️⃣ Data Cleaning
Removed non-numeric and summary rows (e.g., “TOTAL”).

Cleaned (p), (r) flags from month columns.

Converted columns to proper datetime index for modeling.

2️⃣ Feature Engineering
Added Holiday Flags using US federal holiday calendar.

Created month-over-month growth % for business tracking.

3️⃣ Forecasting with SARIMAX
Used SARIMAX with exogenous variables (holiday flag) for seasonality.

Extended forecasts up to May 2026.

Evaluated performance using MAE, RMSE.

4️⃣ Visualization with Power BI
Combined historical and forecasted data for direct comparison.

Displayed revenue trends, YoY growth, forecast vs. actual using clear line and bar visuals.

Included KPI cards for forecast values and growth tracking.

📈 Results
Forecast Accuracy:

MAE: ~6400 on ~70,000 revenue scale (~9% relative error).

RMSE: ~6600.

Clear visual differentiation between historical and forecasted revenues.

Month-over-month growth % tracked for actionable business insights.
