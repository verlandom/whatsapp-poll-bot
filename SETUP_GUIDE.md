# Panduan Setup Bot Telegram - WhatsApp Poll Reminder
# Setup Guide for Telegram Bot - WhatsApp Poll Reminder

## 📋 Apa yang Bot Ini Lakukan? / What Does This Bot Do?

Bot ini akan:
- Berjalan otomatis setiap hari **Selasa jam 9 pagi**
- Menghitung minggu ke berapa dalam bulan tersebut
- Menentukan Seksi mana yang harus melayani
- Mengirim pesan reminder ke Telegram Anda dengan:
  - Judul polling yang sudah siap
  - Nama Seksi yang melayani
  - Tanggal Minggu berikutnya

This bot will:
- Run automatically every **Tuesday at 9:00 AM**
- Calculate which week of the month it is
- Determine which Seksi should serve
- Send a reminder message to your Telegram with:
  - The ready-made poll title
  - The name of the serving Seksi
  - The date of the upcoming Sunday

---

## 🚀 Langkah Setup / Setup Steps

### Step 1: Buat Bot Telegram / Create Telegram Bot

1. Buka Telegram dan cari **@BotFather**
2. Kirim perintah: `/newbot`
3. Ikuti instruksi:
   - Berikan nama untuk bot Anda (contoh: "WhatsApp Poll Reminder")
   - Berikan username (harus diakhiri dengan 'bot', contoh: "wapoll_reminder_bot")
4. BotFather akan memberikan **token** seperti ini:
   ```
   1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   ```
5. **SIMPAN TOKEN INI** - Anda akan membutuhkannya nanti

---

### Step 2: Dapatkan Chat ID Anda / Get Your Chat ID

**Opsi A: Untuk pesan pribadi / For personal messages**

1. Cari bot **@userinfobot** di Telegram
2. Mulai chat dengan bot tersebut
3. Bot akan memberikan Chat ID Anda (angka, contoh: 123456789)
4. **SIMPAN CHAT ID INI**

**Opsi B: Untuk grup / For group chat**

1. Tambahkan bot Anda ke grup
2. Kirim pesan apa saja di grup
3. Buka browser dan kunjungi:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
   (Ganti `<YOUR_BOT_TOKEN>` dengan token dari Step 1)
4. Cari `"chat":{"id":-1001234567890` - angka ini adalah chat ID grup
5. **SIMPAN CHAT ID INI** (termasuk tanda minus jika ada)

---

### Step 3: Install Python / Install Python

**Windows:**
1. Download Python dari https://www.python.org/downloads/
2. Jalankan installer
3. ✅ **CENTANG** "Add Python to PATH"
4. Klik "Install Now"

**Mac:**
Python sudah terinstall. Untuk update:
```bash
brew install python3
```

**Linux:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

### Step 4: Setup Bot Script / Setup Bot Script

1. Buat folder baru untuk bot:
   ```bash
   mkdir whatsapp_poll_bot
   cd whatsapp_poll_bot
   ```

2. Simpan file `whatsapp_poll_bot.py` dan `requirements.txt` di folder ini

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
   Atau install manual:
   ```bash
   pip install python-telegram-bot schedule
   ```

4. Edit file `whatsapp_poll_bot.py`:
   - Buka dengan text editor (Notepad, VSCode, dll)
   - Cari baris ini:
     ```python
     TELEGRAM_BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
     TELEGRAM_CHAT_ID = "YOUR_CHAT_ID_HERE"
     ```
   - Ganti dengan token dan chat ID Anda:
     ```python
     TELEGRAM_BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
     TELEGRAM_CHAT_ID = "123456789"
     ```
   - Simpan file

---

### Step 5: Test Bot / Test Bot

Sebelum menjalankan secara otomatis, tes dulu:

```bash
python whatsapp_poll_bot.py test
```

Anda harus menerima pesan di Telegram dengan detail polling!

---

### Step 6: Jalankan Bot Secara Otomatis / Run Bot Automatically

**Opsi A: Keep Running di Terminal / Keep Running in Terminal**

```bash
python whatsapp_poll_bot.py
```

Bot akan terus berjalan dan mengirim pesan setiap Selasa jam 9 pagi.
⚠️ **Komputer/server harus tetap menyala**

**Opsi B: Jalankan di Background (Linux/Mac)**

Gunakan `screen` atau `tmux`:
```bash
screen -S pollbot
python whatsapp_poll_bot.py
# Tekan Ctrl+A lalu D untuk detach
```

Untuk kembali:
```bash
screen -r pollbot
```

**Opsi C: Gunakan Cloud Service (Recommended)**

Deploy ke layanan cloud gratis:
- **PythonAnywhere** (free tier available)
- **Heroku** (dengan clock process)
- **Railway.app**
- **Render.com**

---

## 🔧 Kustomisasi / Customization

### Ubah Waktu Pengiriman / Change Send Time

Edit baris ini di script:
```python
schedule.every().tuesday.at("09:00").do(run_async_task)
```

Ganti `"09:00"` dengan waktu yang Anda inginkan (format 24 jam)

### Ubah Jadwal Seksi / Change Seksi Schedule

Edit dictionary `SEKSI_SCHEDULE`:
```python
SEKSI_SCHEDULE = {
    1: "Lansia dan Magnificat",
    2: "Seksi Pria dan Nehemia",
    3: "Seksi Perempuan",
    4: "Seksi PP",
    5: "Seksi PI"
}
```

---

## ❓ Troubleshooting

### "ModuleNotFoundError"
```bash
pip install python-telegram-bot schedule
```

### "Unauthorized" error
- Token bot salah
- Pastikan tidak ada spasi di awal/akhir token

### Tidak menerima pesan
- Pastikan Anda sudah start chat dengan bot (tekan "Start")
- Cek Chat ID sudah benar
- Untuk grup: pastikan bot sudah di-add ke grup

### Bot berhenti sendiri
- Jika komputer mati, bot akan berhenti
- Gunakan cloud service atau VPS untuk menjalankan 24/7

---

## 📱 Cara Menggunakan Setelah Menerima Reminder

Setiap Selasa jam 9 pagi, Anda akan menerima pesan seperti ini:

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

**Lalu:**
1. Buka WhatsApp
2. Buka grup yang dituju
3. Ketuk ikon attachment → Poll
4. Copy-paste judul dari pesan Telegram
5. Tambahkan opsi: "Ya" dan "Tidak"
6. Kirim polling!

---

## 🎯 Fitur Tambahan yang Bisa Ditambahkan

Jika Anda ingin menambah fitur:
- ✅ Kirim reminder ke multiple chat/grup
- ✅ Custom format pesan
- ✅ Tambah emoji atau formatting khusus
- ✅ Kirim reminder H-1 atau H-2
- ✅ Log history pengiriman

Beritahu saya jika Anda ingin menambah fitur!

---

## 📞 Support

Jika ada masalah, pastikan:
1. ✅ Python terinstall dengan benar
2. ✅ Dependencies terinstall
3. ✅ Token dan Chat ID sudah benar
4. ✅ Bot sudah di-start di Telegram
5. ✅ Script sedang berjalan

Good luck! 🚀
