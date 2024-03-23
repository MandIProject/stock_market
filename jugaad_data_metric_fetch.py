from datetime import date
from jugaad_data.nse import stock_df

ABB_India_stock_df = stock_df(symbol='ABB', from_date=date(2023,12,1), to_date=date(2024,2,1), series='EQ')

print(ABB_India_stock_df)