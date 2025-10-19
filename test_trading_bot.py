#!/usr/bin/env python3
"""
Unit tests for the Trading Bot status functionality
"""

import unittest
from datetime import datetime
from trading_bot import TradingBot, BotStatus


class TestTradingBotStatus(unittest.TestCase):
    """Test cases for trading bot status functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.bot = TradingBot({'initial_balance': 10000.0})
    
    def test_initial_status(self):
        """Test that bot starts with STOPPED status"""
        self.assertEqual(self.bot.status, BotStatus.STOPPED)
        self.assertIsNone(self.bot.start_time)
        self.assertEqual(self.bot.total_trades, 0)
        self.assertEqual(self.bot.current_balance, 10000.0)
    
    def test_start_bot(self):
        """Test starting the bot"""
        self.bot.start()
        self.assertEqual(self.bot.status, BotStatus.RUNNING)
        self.assertIsNotNone(self.bot.start_time)
        self.assertIsInstance(self.bot.start_time, datetime)
    
    def test_stop_bot(self):
        """Test stopping the bot"""
        self.bot.start()
        self.bot.stop()
        self.assertEqual(self.bot.status, BotStatus.STOPPED)
    
    def test_pause_bot(self):
        """Test pausing the bot"""
        self.bot.start()
        self.bot.pause()
        self.assertEqual(self.bot.status, BotStatus.PAUSED)
    
    def test_resume_bot(self):
        """Test resuming the bot from paused state"""
        self.bot.start()
        self.bot.pause()
        self.bot.resume()
        self.assertEqual(self.bot.status, BotStatus.RUNNING)
    
    def test_get_status(self):
        """Test getting comprehensive status information"""
        self.bot.start()
        status = self.bot.get_status()
        
        # Check all required fields are present
        self.assertIn('status', status)
        self.assertIn('start_time', status)
        self.assertIn('uptime_seconds', status)
        self.assertIn('total_trades', status)
        self.assertIn('successful_trades', status)
        self.assertIn('failed_trades', status)
        self.assertIn('success_rate', status)
        self.assertIn('current_balance', status)
        self.assertIn('last_error', status)
        
        # Check status values
        self.assertEqual(status['status'], 'running')
        self.assertIsNotNone(status['start_time'])
        self.assertGreaterEqual(status['uptime_seconds'], 0)
    
    def test_success_rate_calculation(self):
        """Test success rate calculation"""
        # No trades
        self.assertEqual(self.bot._calculate_success_rate(), 0.0)
        
        # Some successful trades
        self.bot.total_trades = 10
        self.bot.successful_trades = 7
        self.bot.failed_trades = 3
        self.assertEqual(self.bot._calculate_success_rate(), 70.0)
        
        # All successful trades
        self.bot.total_trades = 5
        self.bot.successful_trades = 5
        self.bot.failed_trades = 0
        self.assertEqual(self.bot._calculate_success_rate(), 100.0)
    
    def test_status_transitions(self):
        """Test various status transitions"""
        # STOPPED -> RUNNING
        self.assertEqual(self.bot.status, BotStatus.STOPPED)
        self.bot.start()
        self.assertEqual(self.bot.status, BotStatus.RUNNING)
        
        # RUNNING -> PAUSED
        self.bot.pause()
        self.assertEqual(self.bot.status, BotStatus.PAUSED)
        
        # PAUSED -> RUNNING
        self.bot.resume()
        self.assertEqual(self.bot.status, BotStatus.RUNNING)
        
        # RUNNING -> STOPPED
        self.bot.stop()
        self.assertEqual(self.bot.status, BotStatus.STOPPED)
    
    def test_cannot_pause_stopped_bot(self):
        """Test that you cannot pause a stopped bot"""
        initial_status = self.bot.status
        self.bot.pause()
        # Status should remain unchanged
        self.assertEqual(self.bot.status, initial_status)
    
    def test_cannot_resume_running_bot(self):
        """Test that you cannot resume a running bot"""
        self.bot.start()
        self.bot.resume()
        # Should still be running
        self.assertEqual(self.bot.status, BotStatus.RUNNING)
    
    def test_status_with_custom_config(self):
        """Test bot with custom configuration"""
        custom_bot = TradingBot({'initial_balance': 50000.0})
        self.assertEqual(custom_bot.current_balance, 50000.0)
        
        status = custom_bot.get_status()
        self.assertEqual(status['current_balance'], 50000.0)


if __name__ == '__main__':
    unittest.main()
