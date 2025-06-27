<h2>🍽️ Restaurant Revenue Forecasting with SARIMAX and Power BI</h2>

<h3>📌 Project Overview</h3>
<p>
This project predicts <strong>restaurant revenues</strong> using <strong>SARIMAX time series forecasting in Python</strong> and visualizes <strong>historical vs. forecasted revenues</strong> in <strong>Power BI</strong> for actionable business insights.
</p>

<h3>🎯 Objective</h3>
<p>
Predict <strong>monthly revenue 12 months ahead</strong> to support <strong>restaurant demand planning and budgeting</strong>.
</p>

<h3>🛠️ Tools Used</h3>
<ul>
<li><strong>Python:</strong> Pandas, SARIMAX (statsmodels), US federal holidays</li>
<li><strong>Power BI:</strong> Interactive dashboard creation and trend visualization</li>
</ul>

<h3>📂 Data</h3>
<p>
Historical <strong>monthly revenue data (1992 – April 2025)</strong>.
</p>

<h3>🚀 Features</h3>

<h4>1️⃣ Data Cleaning</h4>
<ul>
<li>Removed non-numeric and summary rows (e.g., “TOTAL”).</li>
<li>Cleaned (p), (r) flags from month columns.</li>
<li>Converted columns to proper datetime index for modeling.</li>
</ul>

<h4>2️⃣ Feature Engineering</h4>
<ul>
<li>Added <strong>holiday flags</strong> using the US federal holiday calendar.</li>
<li>Created <strong>month-over-month growth %</strong> for business tracking.</li>
</ul>

<h4>3️⃣ Forecasting with SARIMAX</h4>
<ul>
<li>Implemented <strong>SARIMAX with exogenous variables (holiday flags)</strong> to capture seasonality.</li>
<li>Extended forecasts up to <strong>May 2026</strong>.</li>
<li>Evaluated performance using <strong>MAE</strong> and <strong>RMSE</strong>.</li>
</ul>

<h4>4️⃣ Visualization with Power BI</h4>
<ul>
<li>Combined <strong>historical and forecasted data</strong> for direct comparison.</li>
<li>Displayed <strong>revenue trends, YoY growth, and forecast vs. actual</strong> using clear line and bar charts.</li>
<li>Included <strong>KPI cards</strong> for forecast values and growth tracking.</li>
</ul>

<h3>📈 Results</h3>
<ul>
<li><strong>MAE:</strong> ~6,400 on a ~70,000 revenue scale (~9% relative error)</li>
<li><strong>RMSE:</strong> ~6,600</li>
<li>Clear visual differentiation between <strong>historical and forecasted revenues</strong>.</li>
<li>Tracked month-over-month growth % for <strong>actionable business insights</strong>.</li>
</ul>

