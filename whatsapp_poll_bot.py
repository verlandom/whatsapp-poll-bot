#!/usr/bin/env python3
"""
WhatsApp Poll Reminder Bot for Telegram
Sends weekly reminders to create WhatsApp polls for church service schedule
"""

import asyncio
from datetime import datetime, timedelta
from telegram import Bot
from telegram.error import TelegramError
import schedule
import time

# ============================================
# CONFIGURATION - UPDATE THESE VALUES
# ============================================
import os

# Get from environment variables (for cloud deployment) or use defaults
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', "YOUR_BOT_TOKEN_HERE")  # Get from @BotFather
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', "YOUR_CHAT_ID_HERE")      # Your personal chat ID or group chat ID

# Seksi names for each week
SEKSI_SCHEDULE = {
    1: "Lansia dan Magnificat",
    2: "Seksi Pria dan Nehemia",
    3: "Seksi Perempuan",
    4: "Seksi PP",
    5: "Seksi PI"
}


def get_week_of_month(date):
    """
    Calculate which week of the month a date falls in (1-5)
    """
    first_day = date.replace(day=1)
    # Get the day of month
    day = date.day
    # Calculate week number (1-indexed)
    week = (day - 1) // 7 + 1
    return min(week, 5)  # Cap at 5 weeks


def get_next_sunday(from_date=None):
    """
    Get the date of the upcoming Sunday in the same week
    If today is Tuesday, get the Sunday that comes after (in the same week)
    """
    if from_date is None:
        from_date = datetime.now()
    
    # Calculate days until Sunday (0=Monday, 6=Sunday)
    # For Tuesday (weekday=1): 6-1 = 5 days until Sunday
    days_until_sunday = (6 - from_date.weekday()) % 7
    
    # If today is Sunday (days_until_sunday = 0), keep it as today
    # Otherwise calculate the upcoming Sunday
    if days_until_sunday == 0:
        next_sunday = from_date  # Today is Sunday
    else:
        next_sunday = from_date + timedelta(days=days_until_sunday)
    
    return next_sunday


def format_indonesian_date(date):
    """
    Format date in Indonesian style: "16 Februari 2025"
    """
    months_id = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
        5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
        9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    return f"{date.day} {months_id[date.month]} {date.year}"


def generate_poll_message():
    """
    Generate the reminder message with poll details
    """
    today = datetime.now()
    next_sunday = get_next_sunday(today)
    
    # Determine which week of the month next Sunday falls in
    week_number = get_week_of_month(next_sunday)
    
    seksi_name = SEKSI_SCHEDULE.get(week_number, "Seksi PI")
    sunday_date = format_indonesian_date(next_sunday)
    
    # Generate the poll question
    poll_question = f"Untuk Minggu {sunday_date} apakah {seksi_name} dan Sola Gratia akan melayani?"
    
    message = f"""🔔 **Pengingat Polling WhatsApp**

📅 Hari ini: {format_indonesian_date(today)}
📆 Minggu berikutnya: {sunday_date}
📊 Minggu ke-{week_number} bulan ini

**Seksi yang melayani:** {seksi_name}

**Judul Polling:**
_{poll_question}_

**Opsi Polling:**
✅ Ya
❌ Tidak

---
💡 Silakan buat polling di grup WhatsApp dengan judul dan opsi di atas.
"""
    
    return message


async def send_telegram_message():
    """
    Send the reminder message via Telegram
    """
    try:
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        message = generate_poll_message()
        
        await bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=message,
            parse_mode='Markdown'
        )
        print(f"✅ Message sent successfully at {datetime.now()}")
        
    except TelegramError as e:
        print(f"❌ Error sending message: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def run_async_task():
    """
    Wrapper to run async function in sync context
    """
    asyncio.run(send_telegram_message())


def schedule_weekly_reminder():
    """
    Schedule the reminder to run every Tuesday
    """
    # Schedule for every Tuesday at 9:00 AM
    schedule.every().tuesday.at("09:00").do(run_async_task)
    
    print("=" * 50)
    print("🤖 Bot started successfully!")
    print("📅 Scheduled to run every Tuesday at 09:00")
    print("⏳ Waiting for scheduled time...")
    print(f"🕐 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📍 Next Tuesday at 09:00")
    print("\nPress Ctrl+C to stop the bot.")
    print("=" * 50)
    print()
    
    # Keep the script running indefinitely
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"\n❌ Bot stopped due to error: {e}")
        # Don't exit, keep trying
        time.sleep(60)
        schedule_weekly_reminder()  # Restart


def test_message():
    """
    Test function to send a message immediately (for testing)
    """
    print("🧪 Testing message send...")
    run_async_task()


if __name__ == "__main__":
    import sys
    
    # Check if running in test mode
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        print("=" * 50)
        print("TEST MODE - Sending message now")
        print("=" * 50)
        test_message()
    else:
        print("=" * 50)
        print("WhatsApp Poll Reminder Bot")
        print("=" * 50)
        schedule_weekly_reminder()
