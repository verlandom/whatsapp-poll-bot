# 🚀 Quick Deploy ke Cloud (Railway/Render)

## Mengapa Deploy ke Cloud?
- ✅ Bot jalan 24/7 tanpa komputer Anda harus nyala
- ✅ Gratis (free tier)
- ✅ Setup cepat (5-10 menit)
- ✅ Tidak perlu install Python di komputer

---

## Opsi 1: Railway.app (Recommended - Paling Mudah)

### 1. Persiapan
- Buat akun di https://railway.app (bisa pakai GitHub)
- Install Git di komputer (https://git-scm.com/)

### 2. Setup Repository
```bash
# Buat folder baru
mkdir whatsapp-poll-bot
cd whatsapp-poll-bot

# Copy semua file bot ke folder ini
# (whatsapp_poll_bot.py, requirements.txt, Dockerfile)

# Init git
git init
git add .
git commit -m "Initial commit"
```

### 3. Push ke GitHub
1. Buat repository baru di GitHub
2. Push code:
```bash
git remote add origin https://github.com/USERNAME/whatsapp-poll-bot.git
git branch -M main
git push -u origin main
```

### 4. Deploy di Railway
1. Login ke Railway.app
2. Klik "New Project" → "Deploy from GitHub repo"
3. Pilih repository Anda
4. Tambahkan Environment Variables:
   - Key: `TELEGRAM_BOT_TOKEN`, Value: (token bot Anda)
   - Key: `TELEGRAM_CHAT_ID`, Value: (chat ID Anda)
5. Railway akan otomatis deploy!

### 5. Update Script untuk Environment Variables

Edit `whatsapp_poll_bot.py`, ganti bagian configuration:

```python
import os

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID', 'YOUR_CHAT_ID_HERE')
```

Commit dan push lagi.

---

## Opsi 2: Render.com (Juga Gratis)

### 1. Persiapan
- Buat akun di https://render.com
- Push code ke GitHub (sama seperti Railway step 2-3)

### 2. Deploy
1. Di Render Dashboard, klik "New +"
2. Pilih "Background Worker"
3. Connect GitHub repository
4. Settings:
   - Name: whatsapp-poll-bot
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python whatsapp_poll_bot.py`
5. Tambah Environment Variables (sama seperti Railway)
6. Klik "Create Background Worker"

---

## Opsi 3: PythonAnywhere (Gratis, Tapi Manual Setup)

### 1. Buat Akun
- Daftar di https://www.pythonanywhere.com (free tier)

### 2. Upload Files
1. Dashboard → Files
2. Upload `whatsapp_poll_bot.py` dan `requirements.txt`

### 3. Install Dependencies
1. Dashboard → Consoles → Bash
2. Jalankan:
```bash
pip install --user -r requirements.txt
```

### 4. Edit Configuration
1. Edit `whatsapp_poll_bot.py` via web editor
2. Isi token dan chat ID

### 5. Setup Always-On Task
1. Dashboard → Tasks
2. Klik "Add a new task"
3. Scheduled task time: (pilih waktu)
4. Command: `python3 /home/USERNAME/whatsapp_poll_bot.py`

⚠️ **Catatan:** PythonAnywhere free tier tidak support "always-on" tasks, jadi ini kurang ideal.

---

## ✅ Verifikasi Bot Berjalan

Setelah deploy, test dengan:
1. Trigger manual test (jika ada fitur test di cloud service)
2. Atau tunggu hingga Selasa jam 9 pagi
3. Cek logs di dashboard cloud service

**Cek Logs:**
- Railway: Project → Deployments → View Logs
- Render: Service → Logs
- PythonAnywhere: Files → Log files

---

## 🔄 Update Bot

Jika Anda ingin update script:

```bash
# Edit file
# Kemudian:
git add .
git commit -m "Update bot"
git push
```

Railway dan Render akan otomatis re-deploy!

---

## 💰 Biaya

- **Railway:** $5 gratis per bulan (lebih dari cukup untuk bot sederhana)
- **Render:** Free tier available
- **PythonAnywhere:** Free tier (limited)

Bot ini sangat ringan, free tier sudah lebih dari cukup!

---

## 🆘 Troubleshooting

### Bot tidak kirim pesan
1. Cek logs untuk error
2. Pastikan environment variables sudah benar
3. Test token dan chat ID manual

### "Application error" di Railway
1. Cek logs
2. Pastikan semua dependencies ada di requirements.txt
3. Pastikan script tidak ada syntax error

### Render service sleep
Render free tier akan "sleep" setelah 15 menit tidak ada activity. Tapi karena bot ini pakai schedule, akan otomatis bangun saat waktunya.

---

## 🎉 Selesai!

Bot Anda sekarang jalan 24/7 di cloud, gratis! 

Setiap Selasa jam 9 pagi, Anda akan dapat reminder otomatis di Telegram.
