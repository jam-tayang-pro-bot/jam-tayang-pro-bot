# 📖 Panduan Instalasi Jam Tayang Pro Bot

## 🎯 Persyaratan Sistem

### Minimum Requirements:
- **Python**: 3.8 atau lebih baru
- **RAM**: 512 MB (Recommended: 1 GB+)
- **Storage**: 500 MB free space
- **OS**: Windows 10/11, Linux, macOS
- **Internet**: Koneksi stabil untuk bot operation

### Yang Dibutuhkan:
1. **Telegram Bot Token** - Dapatkan dari [@BotFather](https://t.me/botfather)
2. **Telegram User ID** - Untuk akses admin panel
3. **VPS/Server** (Optional) - Untuk running 24/7

---

## 🚀 Instalasi Otomatis

### Langkah 1: Download & Extract
```bash
# Download project
git clone https://github.com/kantongaplikasi/jam-tayang-pro-bot.git
cd jam-tayang-pro-bot

# Atau download ZIP dan extract
```

### Langkah 2: Jalankan Installer
```bash
# Windows
python install.py

# Linux/Mac
python3 install.py
```

### Langkah 3: Konfigurasi
1. Edit file `.env` yang sudah dibuat
2. Isi `BOT_TOKEN` dengan token dari BotFather
3. Isi `ADMIN_USER_IDS` dengan Telegram ID Anda
4. Sesuaikan konfigurasi lainnya jika diperlukan

### Langkah 4: Jalankan Bot
```bash
# Windows
start_bot.bat
# atau
python main.py

# Linux/Mac
./start_bot.sh
# atau
python3 main.py
```

---

## 🔧 Instalasi Manual

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Environment
```bash
cp .env.example .env
# Edit .env file dengan konfigurasi Anda
```

### 3. Buat Direktori
```bash
mkdir logs data temp backups
```

### 4. Initialize Database
```bash
python -c "import asyncio; from src.database.database import init_database; asyncio.run(init_database())"
```

### 5. Test Bot
```bash
python main.py
```

---

## ⚙️ Konfigurasi Lengkap

### File .env Configuration:

```env
# Bot Configuration
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
BOT_USERNAME=JamTayangProBot

# Database
DATABASE_URL=sqlite:///jam_tayang_pro.db
REDIS_URL=redis://localhost:6379

# Admin Access
ADMIN_USER_IDS=123456789,987654321
ADMIN_CHAT_ID=-1001234567890

# Security
SECRET_KEY=your-secret-key-here
JWT_SECRET=your-jwt-secret-here

# Advertisement System
AD_SKIP_TIME=30
AD_REWARD_TOKENS=5
AD_URLS=https://example.com/ad1,https://example.com/ad2

# Rate Limiting
MAX_REQUESTS_PER_MINUTE=10
MAX_TASKS_PER_USER=5

# Automation Settings
HUMAN_DELAY_MIN=2
HUMAN_DELAY_MAX=8
BATCH_SIZE=10
```

---

## 🤖 Membuat Telegram Bot

### 1. Chat dengan BotFather
1. Buka Telegram dan cari [@BotFather](https://t.me/botfather)
2. Kirim `/start`
3. Kirim `/newbot`
4. Ikuti instruksi untuk membuat bot baru

### 2. Konfigurasi Bot
```
/setname - Set nama bot
/setdescription - Set deskripsi bot
/setabouttext - Set about text
/setuserpic - Upload foto profil bot
/setcommands - Set command list
```

### 3. Command List untuk Bot:
```
start - Mulai menggunakan bot
help - Bantuan dan panduan
daftar - Daftar akun baru
profil - Lihat profil Anda
layanan - Daftar semua layanan
token - Informasi token
admin - Panel admin (admin only)
```

---

## 🗄️ Database Setup

### SQLite (Default - Recommended untuk pemula)
```env
DATABASE_URL=sqlite:///jam_tayang_pro.db
```

### PostgreSQL (Recommended untuk production)
```env
DATABASE_URL=postgresql://username:password@localhost/jam_tayang_pro
```

### MySQL
```env
DATABASE_URL=mysql://username:password@localhost/jam_tayang_pro
```

---

## 🔒 Security Setup

### 1. Dapatkan Telegram User ID
- Chat dengan [@userinfobot](https://t.me/userinfobot)
- Atau gunakan [@RawDataBot](https://t.me/rawdatabot)
- Copy User ID Anda

### 2. Setup Admin Access
```env
ADMIN_USER_IDS=123456789,987654321
```

### 3. Generate Secret Keys
```python
import secrets
print("SECRET_KEY:", secrets.token_urlsafe(32))
print("JWT_SECRET:", secrets.token_urlsafe(32))
```

---

## 🌐 Deployment ke VPS

### 1. Setup VPS (Ubuntu/Debian)
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python3 python3-pip python3-venv -y

# Install Git
sudo apt install git -y

# Install Redis (optional)
sudo apt install redis-server -y
```

### 2. Deploy Bot
```bash
# Clone repository
git clone https://github.com/kantongaplikasi/jam-tayang-pro-bot.git
cd jam-tayang-pro-bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup configuration
cp .env.example .env
nano .env  # Edit configuration

# Run installer
python install.py
```

### 3. Setup Systemd Service (Linux)
```bash
sudo nano /etc/systemd/system/jam-tayang-pro.service
```

```ini
[Unit]
Description=Jam Tayang Pro Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/jam-tayang-pro-bot
Environment=PATH=/home/ubuntu/jam-tayang-pro-bot/venv/bin
ExecStart=/home/ubuntu/jam-tayang-pro-bot/venv/bin/python main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable jam-tayang-pro
sudo systemctl start jam-tayang-pro

# Check status
sudo systemctl status jam-tayang-pro
```

---

## 🔍 Troubleshooting

### Bot Tidak Merespon
1. **Check Bot Token**
   ```bash
   curl https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getMe
   ```

2. **Check Logs**
   ```bash
   tail -f logs/jam_tayang_pro.log
   ```

3. **Test Database Connection**
   ```python
   python -c "from src.database.database import init_database; import asyncio; asyncio.run(init_database())"
   ```

### Error Dependencies
```bash
# Upgrade pip
pip install --upgrade pip

# Install specific versions
pip install python-telegram-bot==20.7

# Clear cache and reinstall
pip cache purge
pip install -r requirements.txt --force-reinstall
```

### Permission Errors (Linux)
```bash
# Fix file permissions
chmod +x start_bot.sh
chmod +x install.py

# Fix directory permissions
sudo chown -R $USER:$USER .
```

### Database Errors
```bash
# Reset database
rm jam_tayang_pro.db
python -c "import asyncio; from src.database.database import init_database; asyncio.run(init_database())"
```

---

## 📊 Monitoring & Maintenance

### 1. Log Files
- `logs/jam_tayang_pro.log` - Main application logs
- `logs/errors.log` - Error logs only
- `logs/user_actions.log` - User activity logs
- `logs/security.log` - Security events
- `logs/system_events.log` - System events

### 2. Database Backup
```bash
# SQLite backup
cp jam_tayang_pro.db backups/backup_$(date +%Y%m%d_%H%M%S).db

# PostgreSQL backup
pg_dump jam_tayang_pro > backups/backup_$(date +%Y%m%d_%H%M%S).sql
```

### 3. System Monitoring
```bash
# Check bot status
ps aux | grep python

# Check memory usage
free -h

# Check disk space
df -h

# Check logs
tail -f logs/jam_tayang_pro.log
```

---

## 🆘 Support & Help

### 📞 Kontak Support:
- **Website**: https://www.kantongaplikasi.com/
- **Email**: support@kantongaplikasi.com
- **Telegram**: @kantongaplikasi
- **WhatsApp**: +62-xxx-xxxx-xxxx

### 📚 Resources:
- **Documentation**: [Link to full docs]
- **Video Tutorial**: [Link to YouTube]
- **FAQ**: [Link to FAQ page]
- **Community**: [Link to Telegram group]

### 🐛 Bug Reports:
Jika menemukan bug, silakan laporkan dengan informasi:
1. Versi Python yang digunakan
2. Operating System
3. Error message lengkap
4. Langkah untuk reproduce bug
5. Screenshot jika memungkinkan

---

## 📄 Lisensi

```
Jam Tayang Pro Bot
By Kantong Aplikasi 2025
https://www.kantongaplikasi.com/

All rights reserved.
```

---

**🎉 Selamat! Bot Anda siap digunakan!**

Jangan lupa untuk:
- ⭐ Star repository ini jika bermanfaat
- 🔄 Share ke teman-teman developer
- 💬 Join komunitas untuk update terbaru
- 📧 Subscribe newsletter untuk tips & tricks
