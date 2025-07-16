"""
Database configuration and models for Jam Tayang Pro Bot
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
"""

import os
import asyncio
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Boolean, Float, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from contextlib import asynccontextmanager

# Database URL from environment
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///jam_tayang_pro.db')

# Convert sqlite URL for async if needed
if DATABASE_URL.startswith('sqlite:///'):
    ASYNC_DATABASE_URL = DATABASE_URL.replace('sqlite:///', 'sqlite+aiosqlite:///')
else:
    ASYNC_DATABASE_URL = DATABASE_URL

# Create async engine
engine = create_async_engine(ASYNC_DATABASE_URL, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

class User(Base):
    """User model"""
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    telegram_id = Column(String(20), unique=True, nullable=False)
    username = Column(String(50))
    first_name = Column(String(100))
    last_name = Column(String(100))
    phone_number = Column(String(20))
    email = Column(String(100))
    
    # Token system
    tokens = Column(Integer, default=50)  # Start with 50 free tokens
    total_earned_tokens = Column(Integer, default=50)
    total_spent_tokens = Column(Integer, default=0)
    
    # Registration info
    registration_date = Column(DateTime, default=datetime.utcnow)
    last_active = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(45))  # Support IPv6
    device_info = Column(Text)
    
    # Status
    is_active = Column(Boolean, default=True)
    is_banned = Column(Boolean, default=False)
    ban_reason = Column(Text)
    
    # Premium features
    is_premium = Column(Boolean, default=False)
    premium_until = Column(DateTime)
    
    # Relationships
    orders = relationship("Order", back_populates="user")
    token_transactions = relationship("TokenTransaction", back_populates="user")
    ad_views = relationship("AdView", back_populates="user")

class Order(Base):
    """Order/Task model"""
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Service details
    service_type = Column(String(50), nullable=False)  # youtube_watchtime, instagram_likes, etc.
    platform = Column(String(30), nullable=False)  # youtube, instagram, tiktok, etc.
    target_url = Column(String(500), nullable=False)
    
    # Order specifications
    quantity = Column(Integer, nullable=False)  # Amount requested
    completed_quantity = Column(Integer, default=0)  # Amount completed
    tokens_cost = Column(Integer, nullable=False)
    
    # Status tracking
    status = Column(String(20), default='pending')  # pending, processing, completed, failed, cancelled
    created_at = Column(DateTime, default=datetime.utcnow)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    
    # Progress tracking
    progress_percentage = Column(Float, default=0.0)
    estimated_completion = Column(DateTime)
    
    # Additional info
    notes = Column(Text)
    error_message = Column(Text)
    
    # Relationships
    user = relationship("User", back_populates="orders")

class TokenTransaction(Base):
    """Token transaction history"""
    __tablename__ = 'token_transactions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Transaction details
    transaction_type = Column(String(20), nullable=False)  # earned, spent, bonus, refund
    amount = Column(Integer, nullable=False)  # Positive for earned, negative for spent
    balance_after = Column(Integer, nullable=False)
    
    # Source/reason
    source = Column(String(50), nullable=False)  # ad_view, order, registration_bonus, admin_grant
    reference_id = Column(String(100))  # Order ID, Ad ID, etc.
    description = Column(String(200))
    
    # Timestamp
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="token_transactions")

class AdView(Base):
    """Advertisement view tracking"""
    __tablename__ = 'ad_views'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Ad details
    ad_url = Column(String(500), nullable=False)
    ad_title = Column(String(200))
    tokens_earned = Column(Integer, default=5)
    
    # Viewing details
    started_at = Column(DateTime, default=datetime.utcnow)
    completed_at = Column(DateTime)
    view_duration = Column(Integer)  # seconds
    is_completed = Column(Boolean, default=False)
    
    # Verification
    ip_address = Column(String(45))
    user_agent = Column(Text)
    
    # Relationships
    user = relationship("User", back_populates="ad_views")

class SystemConfig(Base):
    """System configuration"""
    __tablename__ = 'system_config'
    
    id = Column(Integer, primary_key=True)
    key = Column(String(100), unique=True, nullable=False)
    value = Column(Text)
    description = Column(String(200))
    updated_at = Column(DateTime, default=datetime.utcnow)

class IPTracker(Base):
    """IP address tracking for fraud prevention"""
    __tablename__ = 'ip_tracker'
    
    id = Column(Integer, primary_key=True)
    ip_address = Column(String(45), nullable=False)
    user_count = Column(Integer, default=1)
    first_seen = Column(DateTime, default=datetime.utcnow)
    last_seen = Column(DateTime, default=datetime.utcnow)
    is_blocked = Column(Boolean, default=False)
    block_reason = Column(String(200))

@asynccontextmanager
async def get_db_session():
    """Get database session context manager"""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def init_database():
    """Initialize database tables"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # Insert default system configurations
    async with get_db_session() as session:
        # Check if configs already exist
        from sqlalchemy import select
        result = await session.execute(select(SystemConfig).limit(1))
        if not result.first():
            default_configs = [
                SystemConfig(key="registration_bonus", value="50", description="Bonus tokens for new users"),
                SystemConfig(key="ad_reward_tokens", value="5", description="Tokens earned per ad view"),
                SystemConfig(key="ad_skip_time", value="30", description="Minimum ad view time in seconds"),
                SystemConfig(key="max_daily_ads", value="20", description="Maximum ads per user per day"),
                SystemConfig(key="max_ip_users", value="3", description="Maximum users per IP address"),
                SystemConfig(key="youtube_watchtime_rate", value="1", description="Tokens per minute of watchtime"),
                SystemConfig(key="instagram_like_rate", value="1", description="Tokens per Instagram like"),
                SystemConfig(key="tiktok_view_rate", value="1", description="Tokens per TikTok view"),
                SystemConfig(key="maintenance_mode", value="false", description="System maintenance mode"),
            ]
            
            for config in default_configs:
                session.add(config)
            
            await session.commit()

async def get_user_by_telegram_id(telegram_id: str):
    """Get user by Telegram ID"""
    async with get_db_session() as session:
        from sqlalchemy import select
        result = await session.execute(
            select(User).where(User.telegram_id == str(telegram_id))
        )
        return result.scalar_one_or_none()

async def create_user(telegram_id: str, username: str = None, first_name: str = None, 
                     last_name: str = None, ip_address: str = None):
    """Create new user"""
    async with get_db_session() as session:
        user = User(
            telegram_id=str(telegram_id),
            username=username,
            first_name=first_name,
            last_name=last_name,
            ip_address=ip_address,
            tokens=50,  # Registration bonus
            total_earned_tokens=50
        )
        session.add(user)
        await session.commit()
        
        # Add registration bonus transaction
        transaction = TokenTransaction(
            user_id=user.id,
            transaction_type="earned",
            amount=50,
            balance_after=50,
            source="registration_bonus",
            description="Bonus pendaftaran gratis"
        )
        session.add(transaction)
        await session.commit()
        
        return user

async def update_user_tokens(user_id: int, amount: int, transaction_type: str, 
                           source: str, description: str = "", reference_id: str = None):
    """Update user tokens and create transaction record"""
    async with get_db_session() as session:
        from sqlalchemy import select
        
        # Get user
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one()
        
        # Update tokens
        user.tokens += amount
        if amount > 0:
            user.total_earned_tokens += amount
        else:
            user.total_spent_tokens += abs(amount)
        
        # Create transaction record
        transaction = TokenTransaction(
            user_id=user_id,
            transaction_type=transaction_type,
            amount=amount,
            balance_after=user.tokens,
            source=source,
            reference_id=reference_id,
            description=description
        )
        session.add(transaction)
        await session.commit()
        
        return user.tokens

async def get_system_config(key: str, default_value: str = None):
    """Get system configuration value"""
    async with get_db_session() as session:
        from sqlalchemy import select
        result = await session.execute(
            select(SystemConfig).where(SystemConfig.key == key)
        )
        config = result.scalar_one_or_none()
        return config.value if config else default_value

async def set_system_config(key: str, value: str, description: str = ""):
    """Set system configuration value"""
    async with get_db_session() as session:
        from sqlalchemy import select
        result = await session.execute(
            select(SystemConfig).where(SystemConfig.key == key)
        )
        config = result.scalar_one_or_none()
        
        if config:
            config.value = value
            config.updated_at = datetime.utcnow()
        else:
            config = SystemConfig(key=key, value=value, description=description)
            session.add(config)
        
        await session.commit()
