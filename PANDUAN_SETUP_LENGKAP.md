# Panduan Setup Lengkap - Jam Tayang Pro Bot

## Status: ✅ SEMUA ERROR SUDAH DIPERBAIKI - TINGGAL KONFIGURASI

---

## 🚀 LANGKAH-LANGKAH SETUP:

### 1. ✅ Dependencies Sudah Diinstall
Dependencies sudah berhasil diinstall dengan perintah:
```bash
pip install -r requirements.txt
```

### 2. 🔧 Konfigurasi BOT_TOKEN (WAJIB)

Anda perlu mendapatkan BOT_TOKEN dari BotFather di Telegram:

#### A. Buat Bot di Telegram:
1. Buka Telegram dan cari `@BotFather`
2. Kirim perintah `/newbot`
3. Ikuti instruksi untuk memberi nama bot
4. Copy TOKEN yang diberikan (format: `1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ`)

#### B. Set BOT_TOKEN di file .env:
1. Buka file `.env` di root directory
2. Tambahkan atau edit baris:
```
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrSTUvwxYZ
```
3. Ganti dengan TOKEN asli dari BotFather
4. Simpan file

### 3. 🗄️ Konfigurasi Database (Opsional)
Bot menggunakan SQLite secara default. Untuk database lain, edit di `.env`:
```
DATABASE_URL=sqlite:///jam_tayang_pro.db
```

### 4. 👨‍💼 Konfigurasi Admin (Opsional)
Untuk akses admin panel, tambahkan di `.env`:
```
ADMIN_USER_IDS=123456789,987654321
```
Ganti dengan Telegram User ID admin.

---

## 🏃‍♂️ CARA MENJALANKAN BOT:

### Opsi 1: Jalankan Langsung
```bash
python main.py
```

### Opsi 2: Menggunakan Start Script
```bash
python start_bot.py
```

### Opsi 3: Windows Batch File
```bash
start_bot.bat
```

### Opsi 4: Linux/Mac Shell Script
```bash
./start_bot.sh
```

---

## 🔍 VERIFIKASI BOT BERJALAN:

Setelah bot dijalankan, Anda akan melihat:
```
🚀 Jam Tayang Pro Bot is starting...
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
Database initialized successfully
Task scheduler started
All handlers added successfully
```

### Test Bot:
1. Cari bot Anda di Telegram (nama yang dibuat di BotFather)
2. Kirim perintah `/start`
3. Bot akan merespon dengan menu utama

---

## 📁 FILE YANG AKAN TERBUAT:

Setelah bot berjalan pertama kali:
- `jam_tayang_pro.db` - Database SQLite
- `logs/` directory dengan file log
- `data/` directory untuk data tambahan

---

## 🛠️ TROUBLESHOOTING:

### Error: BOT_TOKEN tidak ditemukan
```
❌ BOT_TOKEN tidak ditemukan!
Silakan copy .env.example ke .env dan isi BOT_TOKEN Anda
```
**Solusi:** Set BOT_TOKEN di file .env

### Error: Invalid token
```
❌ Error: Invalid token
```
**Solusi:** Periksa TOKEN dari BotFather, pastikan tidak ada spasi

### Error: Network connection
```
❌ Network error
```
**Solusi:** Periksa koneksi internet

---

## 🎯 FITUR BOT YANG TERSEDIA:

### 🎬 YouTube Services:
- ⏰ Jam Tayang - Untuk monetisasi
- 👥 Subscriber - Tingkatkan kredibilitas  
- 👍 Likes - Boost engagement
- 👀 Views - Viral content

### 📸 Instagram Services:
- ❤️ Likes - Tingkatkan engagement
- 👥 Followers - Perbesar audience
- 👀 Views - Video & Reels viral

### 🎵 TikTok Services:
- 👀 Views - Masuk FYP
- ❤️ Likes - Boost algoritma
- 👥 Followers - Bangun fanbase

### 📘 Facebook Services:
- 👍 Likes - Post engagement
- 👥 Followers - Profile followers
- 🔄 Shares - Viral content

### 💰 Token System:
- 🎁 50 token gratis saat daftar
- 📺 Tonton iklan untuk token tambahan
- 👥 Referral bonus
- 💎 Upgrade premium

---

## 📞 SUPPORT:

Jika mengalami masalah:
1. Periksa file log di `logs/` directory
2. Pastikan semua dependencies terinstall
3. Verifikasi BOT_TOKEN valid
4. Restart bot setelah perubahan konfigurasi

---

**Status:** ✅ READY TO RUN  
**Next Step:** Set BOT_TOKEN dan jalankan bot!
