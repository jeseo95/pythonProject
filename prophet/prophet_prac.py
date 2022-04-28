# https://facebook.github.io/prophet/docs/saturating_forecasts.html#forecasting-growth

import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly


"""
prophet에 사용되는 데이터는 ds, y 컬럼으로 이루어져 있어야 함
## ds: dates
## y: value
"""

df = pd.read_csv('./example/example_wp_log_peyton_manning.csv')

# prophet object 생성 후 적합(fit)
m = Prophet()
m.fit(df)

# make_future_dataframe()
# period 를 이용해 원하는 기간 만큼 예측 가능
# freq 를 이용해 (일, 월 ... 단위 조정 가능, default="D")
future = m.make_future_dataframe(periods=365)

# predict()
forecast = m.predict(future)
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# plot()
fig1 = m.plot(forecast)
# fig1.savefig('./example/example_wp_log_peyton_manning_plot.png')

# plot_component()
fig2 = m.plot_components(forecast)
# fig2.savefig('./example/example_wp_log_peyton_manning_plot_component.png')
