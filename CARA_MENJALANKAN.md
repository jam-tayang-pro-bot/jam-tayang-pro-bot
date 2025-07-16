# 🚀 CARA MENJALANKAN JAM TAYANG PRO BOT

## 📋 **LANGKAH-LANGKAH LENGKAP:**

---

## 🖥️ **OPSI 1: MENJALANKAN DI KOMPUTER LOKAL**

### **1. Persiapan:**
```cmd
# Buka Command Prompt atau Terminal
# Pastikan Python 3.8+ sudah terinstall
python --version
```

### **2. Install Dependencies:**
```cmd
# Di folder jam-tayang-pro-bot
pip install -r requirements.txt

# Jika ada error cryptography, hapus pyproject.toml dulu:
rm pyproject.toml
pip install -r requirements.txt
```

### **3. Setup Environment:**
- Buka file `.env`
- Pastikan BOT_TOKEN sudah diisi:
```
BOT_TOKEN=8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90
DATABASE_URL=sqlite:///jam_tayang_pro.db
```

### **4. Jalankan Bot:**
```cmd
python main.py
```

### **5. Hasil yang Diharapkan:**
```
🚀 Jam Tayang Pro Bot is starting...
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
✅ Database initialized successfully
✅ Task scheduler started
✅ All handlers added successfully
```

---

## 🌐 **OPSI 2: MENJALANKAN DI REPLIT (RECOMMENDED)**

### **1. Buka Replit:**
- Kunjungi [replit.com](https://replit.com)
- Login atau daftar akun

### **2. Import Project:**
- Klik **"Create Repl"**
- Pilih **"Import from GitHub"** atau **"Upload files"**
- Pilih **Python** sebagai language
- Upload semua file project

### **3. Set Environment Variables:**
- Klik tab **"Secrets"** (ikon 🔒 di sidebar kiri)
- Tambahkan:
```
Key: BOT_TOKEN
Value: 8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90

Key: DATABASE_URL  
Value: sqlite:///jam_tayang_pro.db
```

### **4. Install Dependencies:**
Di Replit Console:
```bash
pip install -r requirements.txt

# Jika ada error cryptography, jalankan ini:
rm pyproject.toml
pip install -r requirements.txt
```

### **5. Jalankan Bot:**
- Klik tombol **"Run"** hijau di atas
- Atau di Console: `python main.py`

### **6. Hasil di Replit:**
```
✅ Keep-alive server started for Replit
🚀 Jam Tayang Pro Bot is starting...
✅ Database initialized successfully
✅ Task scheduler started
✅ All handlers added successfully
```

---

## 📱 **OPSI 3: TEST BOT DI TELEGRAM**

### **1. Buka Telegram:**
- Cari bot: **@JamTayangProBot**
- Atau klik: https://t.me/JamTayangProBot

### **2. Mulai Percakapan:**
```
/start
```

### **3. Bot akan merespon:**
```
🎉 Selamat datang di Jam Tayang Pro! 🎉

Halo [Nama Anda]! 👋

Anda telah berhasil mendaftar dan mendapatkan:
🎁 50 Token GRATIS untuk memulai!

Apa yang bisa Anda lakukan:
📈 Tingkatkan jam tayang YouTube
❤️ Tambah likes Instagram & TikTok  
👀 Boost views semua platform
📊 Tingkatkan engagement sosial media
```

### **4. Coba Fitur Bot:**
- Ketik `/layanan` - Lihat semua layanan
- Ketik `/profil` - Lihat profil & token
- Ketik `/token` - Kelola token
- Ketik `/help` - Bantuan lengkap

---

## 🔧 **TROUBLESHOOTING:**

### **❌ Error: Module not found**
```cmd
pip install -r requirements.txt --upgrade

# Jika masih error, hapus pyproject.toml:
rm pyproject.toml
pip install -r requirements.txt
```

### **❌ Error: BOT_TOKEN not found**
- Pastikan file `.env` ada
- Pastikan BOT_TOKEN diisi dengan benar
- Di Replit: cek tab "Secrets"

### **❌ Error: Database locked**
```cmd
# Hapus database lama
del jam_tayang_pro.db
python main.py
```

### **❌ Bot tidak merespon di Telegram**
1. Pastikan bot sudah running (lihat console)
2. Cek BOT_TOKEN valid
3. Restart bot
4. Coba kirim `/start` lagi

### **❌ Error di Replit**
1. Refresh halaman Replit
2. Hapus pyproject.toml jika ada error cryptography:
   ```bash
   rm pyproject.toml
   pip install -r requirements.txt
   ```
3. Klik "Run" lagi
4. Cek tab "Console" untuk error messages
5. Pastikan "Secrets" sudah diisi

### **❌ Bot Tertutup Setelah Jalan (PENTING!)**
**Masalah**: Bot berhasil jalan tapi tertutup setelah 1 jam

**Solusi Terbaik**:
1. **Upgrade Replit Hacker Plan** ($7/bulan)
2. **Aktifkan "Always On"** di Settings
3. **Bot akan jalan 24/7** tanpa tertutup

**Solusi Gratis (Alternatif)**:
1. **Setup UptimeRobot** di [uptimerobot.com](https://uptimerobot.com)
2. **Monitor URL**: `https://[project-name].[username].repl.co`
3. **Ping setiap 5 menit** untuk keep bot alive
4. **Manual restart** jika bot sleep

**Cara Restart Manual**:
```bash
# Di Replit Console:
# 1. Klik tombol "Stop"
# 2. Klik tombol "Run" 
# 3. Test dengan /start di Telegram
```

📖 **Baca panduan lengkap**: `SOLUSI_BOT_TERTUTUP.md`

---

## 🎯 **CARA MENGGUNAKAN BOT:**

### **1. Untuk User Baru:**
```
1. Kirim /start → Dapat 50 token gratis
2. Pilih platform (YouTube/Instagram/TikTok)
3. Pilih layanan (Views/Likes/Followers)
4. Masukkan link konten Anda
5. Tentukan jumlah yang diinginkan
6. Konfirmasi pesanan
7. Tunggu proses otomatis!
```

### **2. Untuk Mendapatkan Token Tambahan:**
```
- Tonton iklan: 5 token per iklan
- Ajak teman: 25 token per referral
- Upgrade premium: bonus 500 token
- Tugas harian: 10-50 token
```

### **3. Untuk Admin:**
```
/admin - Panel admin
- Lihat statistik sistem
- Kelola user & token
- Monitor pesanan
- System maintenance
```

---

## 🎮 **LAYANAN YANG TERSEDIA:**

### 🎬 **YouTube:**
- ⏰ **Jam Tayang**: 1 token = 1 menit
- 👥 **Subscriber**: 1 token = 1 subscriber  
- 👍 **Likes**: Sesuai paket
- 👀 **Views**: Sesuai paket

### 📸 **Instagram:**
- ❤️ **Likes**: 1 token = 10 likes
- 👥 **Followers**: 1 token = 1 follower
- 👀 **Views**: Sesuai paket

### 🎵 **TikTok:**
- 👀 **Views**: 1 token = 100 views
- ❤️ **Likes**: 1 token = 5 likes
- 👥 **Followers**: 1 token = 1 follower

### 📘 **Facebook:**
- 👍 **Likes**: Sesuai paket
- 👥 **Followers**: Sesuai paket
- 🔄 **Shares**: Sesuai paket

---

## 🎉 **SELAMAT!**

**Bot Anda sudah siap menghasilkan engagement sosial media secara otomatis!**

### 📞 **Butuh Bantuan?**
- Website: https://www.kantongaplikasi.com/
- Bot Telegram: @JamTayangProBot

---

*By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/*
