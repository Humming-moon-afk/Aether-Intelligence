import yfinance as yf

class StockFetcher:
    def fetch_stock_data(self, ticker: str):
        stock = yf.Ticker(ticker)
        info = stock.info
        stock_data = {
            "ticker": ticker,
            "company_name": info.get("longName") or info.get("shortName"),
            "sector": info.get("sector", "N/A"),
            "pe_ratio": info.get("trailingPE", 0.0),
            "summary": info.get("longBusinessSummary", "")
        }
        return stock_data
    
    
    
if __name__ == "__main__":
    fetcher = StockFetcher()
    data = fetcher.fetch_stock_data("META")
    print(data)