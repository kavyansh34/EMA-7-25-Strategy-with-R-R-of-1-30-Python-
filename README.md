# EMA-7-25-Strategy-with-R-R-of-1-30-Python-
This repository contains the code for a trend-following EMA 7 &amp; EMA 25 strategy with a Risk-Reward Ratio of 1:30 implemented in Python. The strategy captures sharp reversal moves on small timeframes using Exponential Moving Averages (EMA) to filter market trends and execute buy or sell trades based on specific conditions. 

Overview :
* EMA 7 and EMA 25 are used to filter market trends.
* The 15-minute candle close determines the trading direction for the next 15 minutes.
* Trades are placed on the 1-minute timeframe, capturing short-term reversals based on the trend.
* Tight stop-loss to limit risk and allow for the capture of sharp price movements.

Key Features :
* Risk per Trade: 0.1% of capital
* Initial Capital: $10,000
* Risk-Reward Ratio: 1:30
* Return: $1,261,660 (backtested)

Timeframes:
* Trend filtering on the 15-minute timeframe
* Entries and exits on the 1-minute timeframe

Strategy Logic :
* If EMA 25 is above EMA 7, the trend is bearish, and the strategy looks for sell trades.
* If EMA 25 is below EMA 7, the trend is bullish, and the strategy looks for buy trades.
Trade Direction is confirmed by the 15-minute candle close, and entries are made on the 1-minute timeframe.

Backtesting Results :
* The strategy was backtested over 1 year of historical data.
* Despite a lower win rate, the Risk-Reward Ratio of 1:30 delivers significant profits.

Contributing
Feel free to open issues or submit pull requests for any improvements or optimizations!
