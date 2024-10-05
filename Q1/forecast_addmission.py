# File: forecast_admissions.py
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load admissions data from admissions_data.csv
df_admissions = pd.read_csv('admissions_data.csv')

# Convert 'date' column to datetime
df_admissions['date'] = pd.to_datetime(df_admissions['date'])

# Filter data for one department, e.g., 'Cardiology'
cardiology_admissions = df_admissions[df_admissions['department'] == 'Cardiology']

# Set 'date' as the index for the time series
cardiology_admissions.set_index('date', inplace=True)

# Resample data to monthly admissions
monthly_admissions = cardiology_admissions['admissions'].resample('M').sum()

# Build and fit an ARIMA model
model = ARIMA(monthly_admissions, order=(5, 1, 0))  # ARIMA parameters (p, d, q)
model_fit = model.fit()

# Forecast future admissions for the next 12 months
forecast = model_fit.forecast(steps=12)

# Plot the historical admissions and the forecast
plt.figure(figsize=(10, 6))
plt.plot(monthly_admissions.index, monthly_admissions, label='Historical Admissions')
plt.plot(pd.date_range(monthly_admissions.index[-1], periods=12, freq='M'), forecast, color='red', label='Forecasted Admissions')
plt.title('Forecast of Future Admissions for Cardiology Department')
plt.xlabel('Date')
plt.ylabel('Number of Admissions')
plt.legend()
plt.show()

# Save the forecast data to forecasted_admissions.csv
forecast_df = pd.DataFrame({'date': pd.date_range(monthly_admissions.index[-1], periods=12, freq='M'), 'forecasted_admissions': forecast})
forecast_df.to_csv('forecasted_admissions.csv', index=False)
