# 🚀 Panduan Lengkap Menjalankan Bot di Replit.com

## ❌ Mengatasi Error "ModuleNotFoundError: No module named 'telegram.ext'"

Error ini terjadi karena dependencies belum terinstall dengan benar di Replit. Berikut solusinya:

---

## 🔧 **SOLUSI 1: Install Dependencies Manual**

### Langkah 1: Buka Shell di Replit
1. Klik tab "Shell" di bagian bawah Replit
2. Jalankan perintah berikut satu per satu:

```bash
# Update pip
python -m pip install --upgrade pip

# Install telegram bot library
pip install python-telegram-bot==20.7

# Install dependencies lainnya
pip install python-dotenv
pip install sqlalchemy
pip install aiohttp
pip install requests
pip install beautifulsoup4
```

### Langkah 2: Verifikasi Instalasi
```bash
python -c "import telegram; print('✅ Telegram library installed successfully')"
```

---

## 🔧 **SOLUSI 2: Gunakan Script Setup Otomatis**

### Jalankan script setup yang sudah saya buat:
```bash
python replit_setup.py
```

Script ini akan:
- ✅ Install semua dependencies yang diperlukan
- ✅ Membuat konfigurasi Replit yang benar
- ✅ Setup environment yang optimal

---

## 🔧 **SOLUSI 3: Install dari Requirements.txt**

### Di Shell Replit, jalankan:
```bash
pip install -r requirements.txt --force-reinstall
```

Jika masih error, coba:
```bash
pip install --no-cache-dir -r requirements.txt
```

---

## ⚙️ **KONFIGURASI SECRETS DI REPLIT**

### 1. Buka Tab Secrets
- Klik tab "Secrets" di sidebar kiri Replit
- Atau klik ikon gembok 🔒

### 2. Tambahkan BOT_TOKEN
- Klik "New Secret"
- **Key**: `BOT_TOKEN`
- **Value**: Token dari @BotFather (contoh: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 3. Tambahkan ADMIN_USER_IDS
- Klik "New Secret" lagi
- **Key**: `ADMIN_USER_IDS`
- **Value**: Telegram User ID Anda (contoh: `123456789`)

### 4. Secrets Tambahan (Opsional)
```
DATABASE_URL = sqlite:///jam_tayang_pro.db
SECRET_KEY = jam_tayang_pro_secret_2025
DEBUG = false
```

---

## 🤖 **CARA MENDAPATKAN BOT TOKEN**

### 1. Chat dengan BotFather
1. Buka Telegram
2. Cari `@BotFather`
3. Kirim `/start`
4. Kirim `/newbot`
5. Ikuti instruksi:
   - Nama bot: `Jam Tayang Pro Bot`
   - Username: `JamTayangProBot` (harus unik)

### 2. Copy Token
- BotFather akan memberikan token seperti:
  ```
  1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
  ```
- Copy token ini ke Secrets Replit

---

## 🆔 **CARA MENDAPATKAN USER ID**

### Metode 1: Gunakan @userinfobot
1. Chat dengan `@userinfobot` di Telegram
2. Kirim pesan apa saja
3. Bot akan reply dengan info Anda
4. Copy "Id" number

### Metode 2: Gunakan @RawDataBot
1. Chat dengan `@RawDataBot`
2. Kirim pesan apa saja
3. Cari bagian `"id": 123456789`
4. Copy angka tersebut

---

## 🚀 **MENJALANKAN BOT DI REPLIT**

### 1. Setelah Setup Selesai
- Pastikan semua dependencies terinstall
- Pastikan BOT_TOKEN sudah di Secrets
- Pastikan ADMIN_USER_IDS sudah di Secrets

### 2. Klik Tombol Run
- Klik tombol hijau "Run" di atas
- Bot akan mulai berjalan
- Lihat output di Console

### 3. Cek Status Bot
Jika berhasil, Anda akan melihat output seperti:
```
🚀 Jam Tayang Pro Bot is starting...
Database initialized successfully
Task scheduler started
Bot initialized successfully
```

---

## 🔍 **TROUBLESHOOTING COMMON ERRORS**

### Error: "BOT_TOKEN tidak ditemukan"
**Solusi:**
- Pastikan BOT_TOKEN ada di Secrets
- Restart Repl dengan Ctrl+Shift+F10
- Cek spelling: harus `BOT_TOKEN` (huruf besar semua)

### Error: "ModuleNotFoundError"
**Solusi:**
```bash
# Di Shell Replit
pip install python-telegram-bot==20.7 --force-reinstall
```

### Error: "Database connection failed"
**Solusi:**
- Database SQLite akan dibuat otomatis
- Pastikan folder `data` ada
- Restart bot jika perlu

### Error: "Unauthorized"
**Solusi:**
- Cek BOT_TOKEN benar
- Pastikan bot tidak diblokir
- Test token dengan curl:
```bash
curl https://api.telegram.org/bot<YOUR_TOKEN>/getMe
```

---

## 📱 **TESTING BOT SETELAH RUNNING**

### 1. Cari Bot di Telegram
- Buka Telegram
- Cari username bot Anda (yang dibuat di BotFather)
- Atau klik link yang diberikan BotFather

### 2. Test Commands
```
/start - Memulai bot
/help - Melihat bantuan
/daftar - Registrasi pengguna
/profil - Melihat profil
/layanan - Daftar layanan
```

### 3. Test Admin Commands (jika Anda admin)
```
/admin - Panel admin
/token - Info token sistem
```

---

## 🔄 **KEEP ALIVE DI REPLIT**

### Replit Free Tier
- Bot akan sleep setelah tidak ada aktivitas
- Gunakan UptimeRobot atau similar untuk ping bot
- Atau upgrade ke Replit Hacker Plan

### Ping URL
Setelah bot running, Replit akan memberikan URL seperti:
```
https://jam-tayang-pro-bot.username.repl.co
```

---

## 📊 **MONITORING BOT**

### 1. Lihat Logs di Console
- Tab "Console" menampilkan real-time logs
- Monitor aktivitas user
- Cek error messages

### 2. Database Monitoring
```bash
# Di Shell, cek database
python -c "
import sqlite3
conn = sqlite3.connect('jam_tayang_pro.db')
cursor = conn.cursor()
cursor.execute('SELECT name FROM sqlite_master WHERE type=\"table\"')
print('Tables:', cursor.fetchall())
conn.close()
"
```

---

## 🆘 **SUPPORT & BANTUAN**

### Jika Masih Bermasalah:
1. **Screenshot error** yang muncul
2. **Copy paste** error message lengkap
3. **Cek** apakah semua langkah sudah diikuti
4. **Restart** Repl dan coba lagi

### Kontak Support:
- **Website**: https://www.kantongaplikasi.com/
- **Email**: support@kantongaplikasi.com
- **Telegram**: @kantongaplikasi

---

## ✅ **CHECKLIST FINAL**

Sebelum menjalankan bot, pastikan:

- [ ] ✅ Python dependencies terinstall
- [ ] ✅ BOT_TOKEN ada di Secrets
- [ ] ✅ ADMIN_USER_IDS ada di Secrets  
- [ ] ✅ File .replit dan pyproject.toml ada
- [ ] ✅ Bot username sudah dibuat di BotFather
- [ ] ✅ Telegram User ID sudah didapat

**Jika semua checklist ✅, bot siap dijalankan!**

---

## 🎉 **SELAMAT!**

Bot Telegram Anda sekarang siap berjalan 24/7 di Replit.com!

**Features yang tersedia:**
- 🤖 Telegram Bot Interface
- 💰 Token Economy System  
- 📱 Social Media Automation
- 👥 User Management
- 📊 Admin Dashboard
- 🔄 Task Scheduler
- 💾 SQLite Database
- 📝 Comprehensive Logging

**Nikmati bot Anda! 🚀**
