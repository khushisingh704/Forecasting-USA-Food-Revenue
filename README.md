# Forecasting-USA-Food-Revenue
# Restaurant Revenue Forecasting with SARIMAX and Power BI
=>Project Overview
This project predicts restaurant revenues using SARIMAX time series forecasting with Python and visualizes historical vs. forecasted revenues in Power BI for actionable business insights.

=>Objective: Predict monthly revenue for 12 months ahead to support restaurant demand planning.

=>Tools Used: Python (Pandas, SARIMAX), Power BI

=>Data: Historical monthly revenue data (1992–2025)

=>Features :
1. Data Cleaning:

Removed non-numeric, summary rows (e.g., “TOTAL”)

Cleaned (p), (r) flags from month columns

Converted columns to proper datetime index

2. Feature Engineering:

Added Holiday Flags for US federal holidays

Created growth % compared to previous month for business tracking

✅ Forecasting with SARIMAX:

Used SARIMAX with exogenous variables (holiday flag)

Extended forecasts up to 2026

Evaluated using MAE, RMSE

3. Visualization with Power BI:

Combined historical and forecasted data for clear tracking

Displayed revenue trends, YoY growth, forecast vs. actual in line and bar visuals

Included KPI cards for forecast values and growth tracking

Results
Forecast Accuracy:

MAE: ~6400 on ~70,000 revenue scale (~9% relative error)

RMSE: ~6600

Clear visual differentiation between historical and forecasted revenues

Growth % calculated for each month to support actionable monitoring

