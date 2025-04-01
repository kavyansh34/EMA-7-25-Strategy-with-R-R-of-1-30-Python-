EMA 7 & 25 Strategy with 1:30 Risk:Reward
This repository contains the implementation of a momentum-based trading strategy using the Exponential Moving Averages (EMA) 7 and EMA 25. The strategy is designed to trade in the direction of sharp price reversals by analyzing short-term price action on a 1-minute timeframe with a confirmation trend derived from the 15-minute timeframe.

Strategy Overview:
*Trade Direction: The strategy checks the trend on the 15-minute timeframe at every 3:00 PM candle close:
* If EMA 7 crosses EMA 25 upwards, the trend is considered bullish, and long trades are considered.
* If EMA 25 is above EMA 7, the trend is bearish, and short trades are considered.
*Timeframe:
* 15-minute timeframe is used to determine the overall market trend.
* 1-minute timeframe is used for executing trades based on the price action and EMA crossovers.
*Risk Management:
* A tight stop-loss is used, set near the previous candle's low or high, depending on the direction of the trade.
* The risk-reward ratio is set to 1:30. For every unit of risk, the expected reward is 30 times that amount.
Key Features:
*Risk Per Trade: 0.1% of capital.
*Risk-Reward Ratio: 1:30.
*Trade Logic:
* Enter long (buy) trades when EMA 7 is above EMA 25 on the 1-minute chart, and the 15-minute trend is bullish.
* Enter short (sell) trades when EMA 7 is below EMA 25 on the 1-minute chart, and the 15-minute trend is bearish.

Backtest and Performance:
*Initial Capital: $10,000
*Risk Per Trade: $10 (0.1% of capital)
*Expected Return: 30 times risk per trade
*Win Rate: Calculated based on the number of profitable trades vs. total trades executed.

Tech Stack
*Python Libraries:
* Pandas for data handling.
* NumPy for numerical operations.
**Requests to fetch data from Binance API.
* TA-Lib for technical indicators like RSI, EMA.
* Matplotlib for plotting the equity curve.

*Data Source:
 *Binance API is used to fetch real-time market data (BTCUSDT).

How It Works ->
1. Fetch Data: The 1-minute and 15-minute data for BTCUSDT are fetched from Binance.
2. Compute EMAs: The script calculates the 7-period EMA and 25-period EMA for both 1-minute and 15-minute data.
3. Trend Detection: The trend on the 15-minute timeframe determines the direction of trades on the 1-minute timeframe.
4. Signal Generation:
*If the 15-minute trend is bullish, the strategy looks for buy signals on the 1-minute timeframe.
*If the 15-minute trend is bearish, the strategy looks for sell signals on the 1-minute timeframe.
5. Trade Execution: When a signal is generated, the strategy calculates the entry price, stop loss, and take profit based on the risk-reward ratio of 1:30.
6. Backtesting: The strategy is backtested on historical data to evaluate its performance, win rate, and profitability.

Feel free to open issues or submit pull requests if you'd like to improve the strategy or fix bugs. Contributions are welcome!   
