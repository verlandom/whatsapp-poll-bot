#!/usr/bin/env python3
"""
WhatsApp Poll Reminder Bot for Telegram
Sends weekly reminders to create WhatsApp polls for church service schedule
"""

import asyncio
import sys
from datetime import datetime, timedelta
from telegram import Bot
from telegram.error import TelegramError
import schedule
import time
import os

# Force immediate output flushing for Railway logs
sys.stdout.flush()

# ============================================
# CONFIGURATION - UPDATE THESE VALUES
# ============================================

# Get from environment variables (for cloud deployment) or use defaults
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', "YOUR_BOT_TOKEN_HERE")
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', "YOUR_CHAT_ID_HERE")

# Seksi names for each week
SEKSI_SCHEDULE = {
    1: "Lansia dan Magnificat",
    2: "Seksi Pria dan Nehemia",
    3: "Seksi Perempuan",
    4: "Seksi PP",
    5: "Seksi PI"
}


def log(message):
    """Print with timestamp and flush immediately for Railway"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}", flush=True)


def get_week_of_month(date):
    """Calculate which week of the month a date falls in (1-5)"""
    day = date.day
    week = (day - 1) // 7 + 1
    return min(week, 5)  # Cap at 5 weeks


def get_next_sunday(from_date=None):
    """Get the date of the upcoming Sunday in the same week"""
    if from_date is None:
        from_date = datetime.now()
    
    days_until_sunday = (6 - from_date.weekday()) % 7
    
    if days_until_sunday == 0:
        next_sunday = from_date
    else:
        next_sunday = from_date + timedelta(days=days_until_sunday)
    
    return next_sunday


def format_indonesian_date(date):
    """Format date in Indonesian style: '16 Februari 2025'"""
    months_id = {
        1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
        5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
        9: "September", 10: "Oktober", 11: "November", 12: "Desember"
    }
    return f"{date.day} {months_id[date.month]} {date.year}"


def generate_poll_message():
    """Generate the reminder message with poll details"""
    today = datetime.now()
    next_sunday = get_next_sunday(today)
    week_number = get_week_of_month(next_sunday)
    seksi_name = SEKSI_SCHEDULE.get(week_number, "Seksi PI")
    sunday_date = format_indonesian_date(next_sunday)
    
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
    """Send the reminder message via Telegram"""
    try:
        log("📤 Sending message to Telegram...")
        bot = Bot(token=TELEGRAM_BOT_TOKEN)
        message = generate_poll_message()
        
        await bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=message,
            parse_mode='Markdown'
        )
        log("✅ Message sent successfully!")
        
    except TelegramError as e:
        log(f"❌ Telegram Error: {e}")
    except Exception as e:
        log(f"❌ Unexpected error: {e}")


def run_async_task():
    """Wrapper to run async function in sync context"""
    asyncio.run(send_telegram_message())


def schedule_weekly_reminder():
    """Schedule the reminder to run every Tuesday"""
    # Schedule for every Tuesday at 9:00 AM
    schedule.every().tuesday.at("09:00").do(run_async_task)
    
    log("=" * 50)
    log("🤖 WhatsApp Poll Reminder Bot STARTED")
    log("=" * 50)
    log(f"📅 Scheduled: Every Tuesday at 09:00 WIB")
    log(f"🕐 Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log(f"📍 Bot Token: {'✅ Set' if TELEGRAM_BOT_TOKEN != 'YOUR_BOT_TOKEN_HERE' else '❌ NOT SET'}")
    log(f"📍 Chat ID: {'✅ Set' if TELEGRAM_CHAT_ID != 'YOUR_CHAT_ID_HERE' else '❌ NOT SET'}")
    log("⏳ Bot is running and waiting for scheduled time...")
    log("=" * 50)
    
    # Keep the script running indefinitely
    counter = 0
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
            
            # Log heartbeat every 60 minutes to show bot is alive
            counter += 1
            if counter % 60 == 0:
                log(f"💓 Bot still running... (uptime: {counter} minutes)")
                
    except KeyboardInterrupt:
        log("👋 Bot stopped by user")
    except Exception as e:
        log(f"❌ Error in main loop: {e}")
        log("🔄 Restarting in 60 seconds...")
        time.sleep(60)
        schedule_weekly_reminder()


def test_message():
    """Test function to send a message immediately"""
    log("🧪 TEST MODE - Sending message now...")
    run_async_task()
    log("✅ Test completed")


if __name__ == "__main__":
    # Check if running in test mode
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        log("=" * 50)
        log("TEST MODE ACTIVATED")
        log("=" * 50)
        test_message()
    else:
        schedule_weekly_reminder()
