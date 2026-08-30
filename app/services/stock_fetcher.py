import yfinance as yf
import matplotlib.pyplot as plt
meta = yf.Ticker("META")
for key, value in meta.info.items():
    print(f"{key}: {value}")
    
data = meta.history(period="1y")
print(data.to_string())
data['Close'].plot(title="Meta Stock Price (1 Year)")
plt.xlabel("Date")
plt.ylabel("Close Price (USD)")
plt.show()