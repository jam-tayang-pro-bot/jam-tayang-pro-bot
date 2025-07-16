# 🚀 PANDUAN LENGKAP MENJALANKAN MAIN.PY DI REPLIT

## 📋 **LANGKAH DEMI LANGKAH - MUDAH & PASTI BERHASIL**

### **🎯 LANGKAH 1: PERSIAPAN AWAL**

#### 1.1 Buka Replit Project Anda
- Login ke [Replit.com](https://replit.com)
- Buka project **Jam Tayang Pro Bot** Anda
- Pastikan semua file sudah ter-upload dengan benar

#### 1.2 Cek File Structure
Pastikan struktur file seperti ini:
```
jam-tayang-pro-bot/
├── main.py
├── requirements.txt
├── fix_replit_complete.py
├── src/
│   ├── __init__.py
│   ├── bot/
│   │   ├── __init__.py
│   │   ├── handlers/
│   │   └── utils/
│   ├── services/
│   ├── database/
│   └── utils/
```

---

### **🔧 LANGKAH 2: FIX DEPENDENCIES & MODULES**

#### 2.1 Buka Shell di Replit
- Klik tab **"Shell"** di bagian bawah Replit
- Shell akan terbuka dengan prompt seperti: `~/workspace$`

#### 2.2 Jalankan Script Fix (WAJIB!)
```bash
python fix_replit_complete.py
```

**Tunggu sampai muncul:**
```
🎉 REPLIT FIX COMPLETED!
✅ Bot siap dijalankan!
```

#### 2.3 Install Dependencies Manual (Jika Diperlukan)
Jika script fix gagal, jalankan manual:
```bash
pip install python-telegram-bot==20.7
pip install python-dotenv==1.0.0
pip install sqlalchemy==2.0.23
pip install aiohttp==3.9.1
```

---

### **🔑 LANGKAH 3: SETUP BOT TOKEN & ADMIN**

#### 3.1 Dapatkan Bot Token dari BotFather
1. **Buka Telegram** di HP/PC
2. **Cari @BotFather** dan mulai chat
3. **Kirim perintah:** `/newbot`
4. **Ikuti instruksi:**
   - Nama bot: `Jam Tayang Pro Bot`
   - Username: `JamTayangProBot123` (harus unik, ganti angka jika perlu)
5. **COPY TOKEN** yang diberikan (contoh: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

#### 3.2 Dapatkan User ID Anda
1. **Cari @userinfobot** di Telegram
2. **Kirim pesan apa saja** ke bot tersebut
3. **COPY User ID** yang ditampilkan (contoh: `123456789`)

#### 3.3 Setup Secrets di Replit
1. **Klik tab "Secrets"** di sidebar kiri Replit (ikon gembok 🔒)
2. **Klik "New Secret"**
3. **Tambahkan Secret 1:**
   - **Key:** `BOT_TOKEN`
   - **Value:** Paste token dari BotFather
   - **Klik "Add Secret"**
4. **Tambahkan Secret 2:**
   - **Key:** `ADMIN_USER_IDS`
   - **Value:** Paste User ID Anda
   - **Klik "Add Secret"**

---

### **▶️ LANGKAH 4: JALANKAN MAIN.PY**

#### 4.1 Metode 1: Tombol Run (Recommended)
1. **Klik tombol hijau "Run"** di atas editor
2. **Tunggu beberapa detik** untuk loading
3. **Lihat output di Console**

#### 4.2 Metode 2: Via Shell
```bash
python main.py
```

#### 4.3 Output yang Diharapkan
Jika berhasil, Anda akan melihat:
```
🚀 Jam Tayang Pro Bot is starting...
By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/
Database initialized successfully
Task scheduler started
Bot initialized successfully
```

---

### **✅ LANGKAH 5: TEST BOT**

#### 5.1 Cari Bot di Telegram
1. **Buka Telegram**
2. **Cari username bot** yang Anda buat di BotFather
3. **Atau klik link** yang diberikan BotFather

#### 5.2 Test Commands
Kirim perintah berikut untuk test:
```
/start    - Memulai bot
/help     - Melihat bantuan
/daftar   - Registrasi pengguna
/profil   - Melihat profil
/layanan  - Daftar layanan
```

#### 5.3 Test Admin Commands (Jika Anda Admin)
```
/admin    - Panel admin
/token    - Info token sistem
```

---

### **🔍 TROUBLESHOOTING - SOLUSI MASALAH UMUM**

#### ❌ **Error: "BOT_TOKEN tidak ditemukan"**
**Solusi:**
- Pastikan BOT_TOKEN ada di tab Secrets
- Cek spelling: harus `BOT_TOKEN` (huruf besar semua)
- Restart Repl: tekan `Ctrl + Shift + F10`

#### ❌ **Error: "ModuleNotFoundError: No module named 'src.bot'"**
**Solusi:**
```bash
# Jalankan di Shell:
python fix_replit_complete.py
```

#### ❌ **Error: "ModuleNotFoundError: No module named 'telegram'"**
**Solusi:**
```bash
# Jalankan di Shell:
pip install python-telegram-bot==20.7
```

#### ❌ **Error: "Unauthorized"**
**Solusi:**
- Cek BOT_TOKEN benar dari BotFather
- Pastikan tidak ada spasi di awal/akhir token
- Test token dengan curl:
```bash
curl https://api.telegram.org/bot<YOUR_TOKEN>/getMe
```

#### ❌ **Bot tidak merespon di Telegram**
**Solusi:**
- Pastikan bot sudah running di Replit (lihat Console)
- Cek username bot benar
- Pastikan bot tidak diblokir
- Restart bot di Replit

---

### **📊 MONITORING BOT**

#### Monitor Real-time
- **Tab Console:** Lihat log aktivitas bot
- **Tab Shell:** Jalankan perintah debugging
- **Tab Secrets:** Cek konfigurasi

#### Log Messages
Bot akan menampilkan log seperti:
```
INFO - User 123456789 started the bot
INFO - Processing /help command
INFO - Database query executed successfully
```

---

### **🔄 RESTART BOT**

#### Jika Bot Bermasalah:
1. **Stop bot:** Tekan `Ctrl + C` di Console
2. **Atau klik "Stop"** jika ada tombolnya
3. **Klik "Run"** lagi untuk restart

#### Hard Restart:
1. **Tekan `Ctrl + Shift + F10`** untuk restart Repl
2. **Tunggu loading selesai**
3. **Klik "Run"** lagi

---

### **🎉 SELAMAT! BOT ANDA BERJALAN**

Jika semua langkah diikuti dengan benar, bot Telegram Anda sekarang:
- ✅ **Berjalan 24/7** di Replit
- ✅ **Merespon commands** di Telegram
- ✅ **Database aktif** untuk menyimpan data
- ✅ **Admin panel** tersedia
- ✅ **Token system** berfungsi
- ✅ **Social media automation** siap digunakan

---

### **📞 BANTUAN LEBIH LANJUT**

#### Jika Masih Bermasalah:
1. **Screenshot error** yang muncul
2. **Copy paste** error message lengkap
3. **Cek** apakah semua langkah sudah diikuti
4. **Hubungi support** Kantong Aplikasi

#### Kontak Support:
- **Website:** https://www.kantongaplikasi.com/
- **Email:** support@kantongaplikasi.com
- **Telegram:** @kantongaplikasi

---

## 🚀 **RINGKASAN CEPAT**

```bash
# 1. Fix dependencies
python fix_replit_complete.py

# 2. Setup Secrets di Replit:
#    BOT_TOKEN = token dari @BotFather
#    ADMIN_USER_IDS = User ID Anda

# 3. Jalankan bot
python main.py
# ATAU klik tombol "Run"

# 4. Test di Telegram dengan /start
```

**Bot Telegram profesional Anda siap digunakan! 🎉**
