# 📱 WhatsApp Poll Reminder Bot (Telegram)

Bot Telegram otomatis yang mengirimkan reminder setiap Selasa untuk membuat polling WhatsApp jadwal pelayanan gereja.

Automatic Telegram bot that sends reminders every Tuesday to create WhatsApp polls for church service schedules.

---

## 🎯 Fitur / Features

- ✅ Berjalan otomatis setiap **Selasa jam 9 pagi**
- ✅ Menghitung minggu ke-berapa dalam bulan
- ✅ Menentukan Seksi yang melayani berdasarkan minggu:
  - Minggu 1: Lansia dan Magnificat
  - Minggu 2: Seksi Pria dan Nehemia
  - Minggu 3: Seksi Perempuan
  - Minggu 4: Seksi PP
  - Minggu 5: Seksi PI
- ✅ Menghitung tanggal Minggu berikutnya
- ✅ Membuat judul polling yang siap pakai
- ✅ Format tanggal dalam Bahasa Indonesia

---

## 📦 File yang Disediakan / Files Included

1. **whatsapp_poll_bot.py** - Script utama bot
2. **requirements.txt** - Dependencies Python
3. **SETUP_GUIDE.md** - Panduan lengkap setup (Indonesia + English)
4. **CLOUD_DEPLOY_GUIDE.md** - Panduan deploy ke cloud (Railway/Render)
5. **Dockerfile** - Untuk containerized deployment
6. **README.md** - File ini

---

## 🚀 Quick Start

### Opsi 1: Local Computer

1. Install Python 3.8+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Edit `whatsapp_poll_bot.py` - isi Token dan Chat ID
4. Test:
   ```bash
   python whatsapp_poll_bot.py test
   ```
5. Run:
   ```bash
   python whatsapp_poll_bot.py
   ```

### Opsi 2: Cloud Deployment (Recommended)

**Lihat file `CLOUD_DEPLOY_GUIDE.md` untuk panduan lengkap deploy ke:**
- Railway.app (paling mudah)
- Render.com
- PythonAnywhere

---

## ⚙️ Configuration

Edit bagian ini di `whatsapp_poll_bot.py`:

```python
TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"
```

Atau set sebagai environment variables:
```bash
export TELEGRAM_BOT_TOKEN="1234567890:ABC..."
export TELEGRAM_CHAT_ID="123456789"
```

---

## 📖 Dokumentasi Lengkap / Full Documentation

- **Setup Guide:** Baca `SETUP_GUIDE.md`
- **Cloud Deployment:** Baca `CLOUD_DEPLOY_GUIDE.md`

---

## 💡 Contoh Output / Example Output

Setiap Selasa, bot akan kirim pesan seperti ini:

```
🔔 Pengingat Polling WhatsApp

📅 Hari ini: 13 Februari 2025
📆 Minggu berikutnya: 16 Februari 2025
📊 Minggu ke-3 bulan ini

Seksi yang melayani: Seksi Perempuan

Judul Polling:
Untuk Minggu 16 Februari 2025 apakah Seksi Perempuan dan Sola Gratia akan melayani?

Opsi Polling:
✅ Ya
❌ Tidak

---
💡 Silakan buat polling di grup WhatsApp dengan judul dan opsi di atas.
```

---

## 🛠️ Requirements

- Python 3.8 atau lebih baru
- python-telegram-bot 20.7
- schedule 1.2.0

---

## 📝 License

Free to use and modify for your church or organization.

---

## 🙏 Support

Jika ada pertanyaan atau butuh bantuan, silakan hubungi pembuat bot atau buka issue.

---

## 🔄 Updates

To update the bot when changes are made:

```bash
git pull origin main
# Restart the bot
```

---

**Made with ❤️ for automated church service scheduling**
