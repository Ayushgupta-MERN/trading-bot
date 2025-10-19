# Trading Bot Project

This repository contains the source code for the fully automated trading bot.

## Features

- **Status Checking**: Comprehensive status monitoring for the trading bot
- **State Management**: Start, stop, pause, and resume functionality
- **Trade Tracking**: Monitor total trades, success rate, and balance
- **Error Handling**: Track and report errors

## Installation

No external dependencies required. The bot uses only Python standard library.

```bash
git clone https://github.com/Ayushgupta-MERN/trading-bot.git
cd trading-bot
```

## Usage

### Running the Bot

```bash
python3 trading_bot.py
```

### Checking Status

The bot provides comprehensive status information including:
- Current state (stopped, running, paused, error)
- Start time and uptime
- Total trades, successful trades, and failed trades
- Success rate percentage
- Current balance
- Last error (if any)

### Example Code

```python
from trading_bot import TradingBot

# Create bot instance
bot = TradingBot({'initial_balance': 10000.0})

# Start the bot
bot.start()

# Check status
status = bot.get_status()
print(status)

# Print formatted status
bot.print_status()

# Pause the bot
bot.pause()

# Resume the bot
bot.resume()

# Stop the bot
bot.stop()
```

## Testing

Run the unit tests:

```bash
python3 -m unittest test_trading_bot.py -v
```

## Status API

The `get_status()` method returns a dictionary with the following fields:

- `status`: Current status (stopped, running, paused, error)
- `start_time`: ISO formatted start time
- `uptime_seconds`: Uptime in seconds
- `total_trades`: Total number of trades executed
- `successful_trades`: Number of successful trades
- `failed_trades`: Number of failed trades
- `success_rate`: Success rate as percentage
- `current_balance`: Current account balance
- `last_error`: Last error message (if any)

## License

MIT