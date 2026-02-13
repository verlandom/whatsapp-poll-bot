FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY whatsapp_poll_bot.py .

# Run the bot
CMD ["python", "whatsapp_poll_bot.py"]
