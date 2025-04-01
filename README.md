# EMA Strategy with 1:30 Risk-Reward Ratio

## Overview

This project implements a trading strategy based on two Exponential Moving Averages (EMA): EMA 7 and EMA 25, using a 1:30 risk-reward ratio. The strategy is designed to capture sharp reversal moves in a high-volatility market by trading based on the relationship between short-term and long-term trends.

The strategy utilizes a combination of:
- **EMA 7** (short-term trend)
- **EMA 25** (long-term trend)

When the 15-minute candle closes at a specific time (e.g., 3:00), it decides the trade direction for the next 15 minutes, based on the relative positions of these two EMAs. The strategy enters **buy** positions in a **bullish trend** and **sell** positions in a **bearish trend**. A very tight stop loss is used to capture sharp moves with minimal risk.

The code is implemented with **Python** and includes backtesting logic for the strategy. Additionally, historical data can be fetched using the Binance API and used for backtesting.

## Key Features:

- **EMA Strategy**: Utilizes the relationship between EMA 7 and EMA 25 for trend direction determination.
- **1:30 Risk-Reward Ratio**: The strategy targets a risk-reward ratio of 1:30, optimizing the risk management process.
- **Backtesting**: Backtests the strategy using historical market data (CSV format), calculating the win rate and tracking capital over time.
- **Data Fetching**: Fetches real-time market data from Binance API, saving it in CSV format for use in backtesting.

## Strategy Logic:

### 1. Trend Identification
- When **EMA 25** is below **EMA 7** on the 15-minute chart, the market is considered bearish, and only **sell** positions are considered.
- When **EMA 25** is above **EMA 7**, the market is considered bullish, and only **buy** positions are considered.

### 2. Signal Generation
- The strategy waits for a confirmation of the trend from the 15-minute chart. The position is then entered in the direction of the prevailing trend on the 1-minute chart.

### 3. Position Management
- A **tight stop loss** is placed at the breaking candle's midpoint or calculated at 0.33 times the height of the breaking candle, depending on the strategy choice.
- The target is set based on a **1:30 risk-reward ratio**.

### 4. Objective
- Capture sharp reversal moves in high-volatility conditions and avoid choppy or ranging markets.

## Tech Stack

This project leverages the following technologies:

- **Python**: Main programming language for backtesting and implementing the strategy.
- **pandas**: Used for handling and processing market data (CSV, DataFrame operations).
- **NumPy**: Used for numerical operations and calculations.
- **TA-Lib**: A technical analysis library used for calculating indicators like RSI (Relative Strength Index).
- **Binance API**: Fetches real-time market data from Binance for backtesting and trading simulation.
- **Requests**: Handles HTTP requests to fetch data from the Binance API.


Install dependicies mentioned in requirent.txt
Fetch data in csv using data_fetcher.py


 
