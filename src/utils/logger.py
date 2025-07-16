"""
Logging utility for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

def setup_logger(name="JamTayangPro", level=logging.INFO):
    """Setup logger with file and console handlers"""
    
    # Create logs directory if it doesn't exist
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Prevent duplicate handlers
    if logger.handlers:
        return logger
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
    )
    
    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        f"{logs_dir}/jam_tayang_pro.log",
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(detailed_formatter)
    
    # Error file handler
    error_handler = RotatingFileHandler(
        f"{logs_dir}/errors.log",
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(detailed_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)
    
    return logger

def log_user_action(user_id, username, action, details=""):
    """Log user actions for monitoring"""
    logger = logging.getLogger("UserActions")
    
    if not logger.handlers:
        # Setup user actions logger
        logs_dir = "logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        handler = RotatingFileHandler(
            f"{logs_dir}/user_actions.log",
            maxBytes=20*1024*1024,  # 20MB
            backupCount=10
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - USER:%(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    log_message = f"{user_id}|{username}|{action}|{details}"
    logger.info(log_message)

def log_system_event(event_type, message, level=logging.INFO):
    """Log system events"""
    logger = logging.getLogger("SystemEvents")
    
    if not logger.handlers:
        logs_dir = "logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        handler = RotatingFileHandler(
            f"{logs_dir}/system_events.log",
            maxBytes=15*1024*1024,  # 15MB
            backupCount=5
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - [%(message)s]'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    log_message = f"{event_type}: {message}"
    logger.log(level, log_message)

def log_security_event(user_id, ip_address, event, risk_level="LOW"):
    """Log security-related events"""
    logger = logging.getLogger("Security")
    
    if not logger.handlers:
        logs_dir = "logs"
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
        
        handler = RotatingFileHandler(
            f"{logs_dir}/security.log",
            maxBytes=10*1024*1024,  # 10MB
            backupCount=10
        )
        
        formatter = logging.Formatter(
            '%(asctime)s - SECURITY - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    
    log_message = f"USER:{user_id}|IP:{ip_address}|EVENT:{event}|RISK:{risk_level}"
    
    if risk_level in ["HIGH", "CRITICAL"]:
        logger.error(log_message)
    elif risk_level == "MEDIUM":
        logger.warning(log_message)
    else:
        logger.info(log_message)
