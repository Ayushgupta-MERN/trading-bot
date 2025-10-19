#!/usr/bin/env python3
"""
Trading Bot - Main Module
A fully automated trading bot with status checking functionality
"""

import json
import time
from datetime import datetime
from enum import Enum
from typing import Dict, Optional


class BotStatus(Enum):
    """Enumeration for bot status states"""
    STOPPED = "stopped"
    RUNNING = "running"
    PAUSED = "paused"
    ERROR = "error"


class TradingBot:
    """Main trading bot class with status functionality"""
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize the trading bot
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.status = BotStatus.STOPPED
        self.start_time = None
        self.total_trades = 0
        self.successful_trades = 0
        self.failed_trades = 0
        self.current_balance = self.config.get('initial_balance', 10000.0)
        self.last_error = None
        
    def start(self):
        """Start the trading bot"""
        if self.status == BotStatus.RUNNING:
            print("Bot is already running")
            return
            
        self.status = BotStatus.RUNNING
        self.start_time = datetime.now()
        print(f"Trading bot started at {self.start_time}")
        
    def stop(self):
        """Stop the trading bot"""
        if self.status == BotStatus.STOPPED:
            print("Bot is already stopped")
            return
            
        self.status = BotStatus.STOPPED
        print("Trading bot stopped")
        
    def pause(self):
        """Pause the trading bot"""
        if self.status != BotStatus.RUNNING:
            print("Bot must be running to pause")
            return
            
        self.status = BotStatus.PAUSED
        print("Trading bot paused")
        
    def resume(self):
        """Resume the trading bot from paused state"""
        if self.status != BotStatus.PAUSED:
            print("Bot must be paused to resume")
            return
            
        self.status = BotStatus.RUNNING
        print("Trading bot resumed")
        
    def get_status(self) -> Dict:
        """
        Get the current status of the trading bot
        
        Returns:
            Dictionary containing comprehensive status information
        """
        status_info = {
            'status': self.status.value,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'uptime_seconds': (datetime.now() - self.start_time).total_seconds() if self.start_time else 0,
            'total_trades': self.total_trades,
            'successful_trades': self.successful_trades,
            'failed_trades': self.failed_trades,
            'success_rate': self._calculate_success_rate(),
            'current_balance': self.current_balance,
            'last_error': self.last_error
        }
        return status_info
    
    def _calculate_success_rate(self) -> float:
        """Calculate the success rate of trades"""
        if self.total_trades == 0:
            return 0.0
        return (self.successful_trades / self.total_trades) * 100
    
    def print_status(self):
        """Print the current status in a human-readable format"""
        status = self.get_status()
        print("\n" + "=" * 50)
        print("TRADING BOT STATUS")
        print("=" * 50)
        print(f"Status: {status['status'].upper()}")
        print(f"Start Time: {status['start_time'] or 'Not started'}")
        print(f"Uptime: {status['uptime_seconds']:.2f} seconds")
        print(f"Total Trades: {status['total_trades']}")
        print(f"Successful Trades: {status['successful_trades']}")
        print(f"Failed Trades: {status['failed_trades']}")
        print(f"Success Rate: {status['success_rate']:.2f}%")
        print(f"Current Balance: ${status['current_balance']:.2f}")
        if status['last_error']:
            print(f"Last Error: {status['last_error']}")
        print("=" * 50 + "\n")


def main():
    """Main function to demonstrate the trading bot"""
    # Create bot instance
    bot = TradingBot({'initial_balance': 10000.0})
    
    # Display initial status
    bot.print_status()
    
    # Start the bot
    bot.start()
    time.sleep(1)
    
    # Display running status
    bot.print_status()
    
    # Pause the bot
    bot.pause()
    bot.print_status()
    
    # Resume the bot
    bot.resume()
    time.sleep(1)
    bot.print_status()
    
    # Stop the bot
    bot.stop()
    bot.print_status()


if __name__ == "__main__":
    main()
