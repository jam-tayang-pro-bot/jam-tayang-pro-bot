# 🔧 PANDUAN ADMIN PANEL - JAM TAYANG PRO BOT

## 🎯 **CARA AKSES ADMIN PANEL:**

### **1. Setup Admin User ID:**

**Di file .env atau Replit Secrets, tambahkan:**
```env
BOT_TOKEN=8122372630:AAG35qn3YixrhbUvpipCadcZ0mBstFsdx90
ADMIN_USER_IDS=123456789,987654321
DATABASE_URL=sqlite:///jam_tayang_pro.db
```

**Cara mendapatkan User ID Anda:**
1. Start chat dengan bot @userinfobot di Telegram
2. Bot akan memberikan User ID Anda
3. Masukkan User ID tersebut ke ADMIN_USER_IDS
4. Pisahkan dengan koma jika ada beberapa admin

### **2. Akses Admin Panel:**

**Command untuk Admin:**
```
/admin - Akses panel admin utama
```

**Atau ketik pesan:**
```
admin
panel admin
dashboard
```

## 🎛️ **FITUR ADMIN PANEL:**

### **📊 Dashboard Utama:**
```
📊 ADMIN DASHBOARD
==================
👥 Total Users: 1,234
📋 Total Orders: 567
💰 Revenue Today: $123
🔄 Active Orders: 12
⚠️ Failed Orders: 3
📈 Success Rate: 95.2%
```

### **📋 Manajemen Pesanan:**

**1. Lihat Semua Pesanan:**
- Status: Pending, Processing, Completed, Failed
- Filter berdasarkan tanggal, user, layanan
- Detail lengkap setiap pesanan

**2. Aksi Admin untuk Pesanan:**
```
✅ Approve Order - Setujui pesanan manual
❌ Cancel Order - Batalkan pesanan
🔄 Retry Order - Coba ulang pesanan gagal
💰 Refund Tokens - Kembalikan token user
📝 Add Notes - Tambah catatan internal
```

**3. Bulk Actions:**
```
📦 Process All Pending - Proses semua pesanan pending
🔄 Retry All Failed - Coba ulang semua pesanan gagal
📊 Export Orders - Export data pesanan
🧹 Cleanup Old Orders - Bersihkan pesanan lama
```

### **👥 Manajemen User:**

**1. User Statistics:**
```
👤 User Details:
- Name: John Doe
- Username: @johndoe
- Telegram ID: 123456789
- Registration: 2025-01-15
- Last Active: 2025-01-16 10:30
- Total Orders: 25
- Total Spent: 1,250 tokens
- Status: Active/Banned
```

**2. User Actions:**
```
💰 Add Tokens - Tambah token manual
🚫 Ban User - Blokir user
✅ Unban User - Buka blokir user
👑 Make Admin - Jadikan admin
📊 View Orders - Lihat pesanan user
💬 Send Message - Kirim pesan ke user
```

### **💰 Token Management:**

**1. Token Operations:**
```
💎 Add Tokens to User - Tambah token manual
📊 Token Statistics - Statistik penggunaan token
🎁 Bulk Token Reward - Berikan token massal
💸 Token Transaction Log - Log transaksi token
```

**2. Promo & Rewards:**
```
🎉 Create Promo Code - Buat kode promo
🎁 Daily Bonus Setup - Atur bonus harian
📢 Broadcast Reward - Kirim reward massal
⏰ Scheduled Rewards - Reward terjadwal
```

### **📊 Analytics & Reports:**

**1. Revenue Analytics:**
```
💰 Daily Revenue: $XXX
📈 Weekly Growth: +XX%
📊 Monthly Report: $X,XXX
🏆 Top Services: YouTube (45%), Instagram (30%)
👥 Active Users: XXX
🔄 Conversion Rate: XX%
```

**2. Service Performance:**
```
🎬 YouTube Services:
- Watch Time: 95% success rate
- Subscribers: 98% success rate
- Average completion: 2.5 hours

📸 Instagram Services:
- Likes: 99% success rate
- Followers: 96% success rate
- Average completion: 1.2 hours
```

## 🚨 **NOTIFIKASI ADMIN:**

### **Auto Notifications:**
Bot akan otomatis mengirim notifikasi ke admin untuk:

**1. Pesanan Baru:**
```
🔔 NEW ORDER #1234
👤 User: @username
🎯 Service: YouTube Watch Time
📊 Quantity: 1000 minutes
💰 Cost: 50 tokens
⏰ Time: 2025-01-16 10:30
```

**2. Pesanan Gagal:**
```
⚠️ ORDER FAILED #1234
👤 User: @username
🎯 Service: Instagram Likes
❌ Error: API rate limit exceeded
🔄 Action: Auto retry in 30 minutes
```

**3. System Alerts:**
```
🚨 SYSTEM ALERT
⚠️ High error rate detected
📊 Failed orders: 15 in last hour
🔧 Recommended: Check API status
```

## 🛠️ **CARA MENGELOLA PESANAN:**

### **Ketika Ada Pesanan Baru:**

**1. Notifikasi Otomatis:**
- Admin akan dapat notifikasi real-time
- Detail pesanan lengkap
- Status dan progress tracking

**2. Review Pesanan:**
```
📋 ORDER DETAILS #1234
==================
👤 User: John Doe (@johndoe)
📱 Telegram ID: 123456789
🎯 Service: YouTube Watch Time
🔗 URL: https://youtube.com/watch?v=xxxxx
📊 Quantity: 1000 minutes
💰 Cost: 50 tokens
📅 Created: 2025-01-16 10:30
⏰ Status: Pending
```

**3. Aksi Admin:**
```
✅ APPROVE - Setujui dan mulai proses
❌ REJECT - Tolak dengan alasan
🔄 MODIFY - Ubah quantity/parameter
💬 CONTACT - Hubungi user untuk klarifikasi
```

### **Monitoring Progress:**

**1. Real-time Tracking:**
```
🔄 ORDER #1234 - PROCESSING
Progress: ████████░░ 80%
Completed: 800/1000 minutes
ETA: 30 minutes remaining
Last Update: 2 minutes ago
```

**2. Manual Intervention:**
```
⏸️ PAUSE - Hentikan sementara
▶️ RESUME - Lanjutkan proses
🔄 RESTART - Mulai ulang dari awal
❌ CANCEL - Batalkan dan refund
```

## 🎛️ **COMMAND ADMIN LENGKAP:**

### **Basic Commands:**
```
/admin - Panel admin utama
/stats - Statistik sistem
/users - Manajemen user
/orders - Manajemen pesanan
/tokens - Manajemen token
/broadcast - Kirim pesan massal
/backup - Backup database
/logs - Lihat system logs
```

### **Advanced Commands:**
```
/admin user [user_id] - Detail user spesifik
/admin order [order_id] - Detail pesanan spesifik
/admin ban [user_id] - Ban user
/admin unban [user_id] - Unban user
/admin tokens [user_id] [amount] - Tambah token
/admin refund [order_id] - Refund pesanan
/admin retry [order_id] - Retry pesanan gagal
/admin export orders - Export data pesanan
```

## 🔐 **KEAMANAN ADMIN:**

### **Multi-Level Access:**
```
🔴 SUPER ADMIN - Full access semua fitur
🟡 ADMIN - Manajemen pesanan & user
🟢 MODERATOR - View only & basic actions
```

### **Audit Log:**
```
📝 ADMIN ACTIONS LOG
===================
2025-01-16 10:30 - Admin @admin1 approved order #1234
2025-01-16 10:25 - Admin @admin1 added 100 tokens to user #123
2025-01-16 10:20 - Admin @admin2 banned user #456
2025-01-16 10:15 - System auto-processed 25 orders
```

## 🚀 **SETUP ADMIN PERTAMA KALI:**

### **1. Tambahkan Admin ID:**
```env
# Di Replit Secrets atau .env
ADMIN_USER_IDS=YOUR_TELEGRAM_USER_ID
```

### **2. Test Admin Access:**
1. Kirim `/admin` ke bot
2. Jika berhasil, akan muncul admin panel
3. Jika gagal, cek User ID di environment variables

### **3. Invite Admin Lain:**
```
/admin add [user_id] - Tambah admin baru
/admin remove [user_id] - Hapus admin
/admin list - Lihat daftar admin
```

## 📞 **SUPPORT & TROUBLESHOOTING:**

### **Jika Admin Panel Tidak Muncul:**
1. ✅ Pastikan User ID benar di ADMIN_USER_IDS
2. ✅ Restart bot setelah update environment
3. ✅ Cek logs untuk error messages
4. ✅ Test dengan command `/admin` langsung

### **Jika Pesanan Tidak Diproses:**
1. ✅ Cek status API external services
2. ✅ Verify database connection
3. ✅ Check scheduler service running
4. ✅ Review error logs

---

**🎯 READY TO MANAGE YOUR BOT LIKE A PRO!**

*Panduan Admin Panel by BLACKBOXAI*
*By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/*
