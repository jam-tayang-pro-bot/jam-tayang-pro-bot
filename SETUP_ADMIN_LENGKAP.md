# 🔧 SETUP ADMIN LENGKAP - JAM TAYANG PRO BOT

## 🎯 **LANGKAH 1: SETUP ADMIN USER ID**

### **Cara Mendapatkan Telegram User ID Anda:**

**Metode 1 - Menggunakan Bot:**
1. Buka chat dengan bot @userinfobot di Telegram
2. Kirim pesan apa saja ke bot tersebut
3. Bot akan memberikan informasi lengkap termasuk User ID
4. Copy User ID tersebut (contoh: 123456789)

**Metode 2 - Menggunakan Bot Anda Sendiri:**
1. Kirim pesan `/start` ke bot Jam Tayang Pro
2. Lihat di logs Replit, akan ada informasi User ID
3. Atau tambahkan kode debug sementara di start_handler.py

### **Setup di Replit Secrets:**

1. **Buka Replit Project Anda**
2. **Klik tab "Secrets" (ikon kunci di sidebar kiri)**
3. **Tambahkan Secret baru:**
   ```
   Key: ADMIN_USER_IDS
   Value: 123456789,987654321,555666777
   ```
   *(Pisahkan dengan koma jika ada beberapa admin)*

4. **Restart Bot:**
   - Stop bot (Ctrl+C di console)
   - Run ulang dengan `python main.py`

## 🎛️ **LANGKAH 2: AKSES ADMIN PANEL**

### **Command untuk Akses Admin:**

**Primary Command:**
```
/admin
```

**Alternative Commands:**
```
admin
panel admin
dashboard
```

### **Tampilan Admin Panel:**
Setelah berhasil akses, Anda akan melihat:

```
🔧 Admin Panel - Jam Tayang Pro

📊 Statistik Sistem:

👥 Users:
• Total Users: 1,234
• Active Today: 45
• New Today: 12
• Premium Users: 89
• Banned Users: 3

📋 Orders:
• Total Orders: 567
• Pending: 12
• Processing: 8
• Completed: 520
• Failed: 27
• Today's Orders: 34

💰 Tokens:
• Total Distributed: 125,000
• Spent Today: 2,340
• Earned Today: 1,890
• Average per User: 45.2

📺 Advertisements:
• Views Today: 234
• Total Views: 12,456
• Tokens from Ads: 62,280

🖥️ System Info:
• Uptime: 24h 15m
• Memory Usage: 67.3%
• Active Tasks: 5
• Database Size: 15.2 MB

📈 Performance:
• Success Rate: 91.2%
• Avg Processing Time: 2.5 min
• Error Rate: 4.8%
```

### **Admin Menu Buttons:**
```
👥 Users    📊 Stats
💰 Tokens   📋 Orders
⚙️ Config   🔧 System
📢 Broadcast 🚫 Ban User
```

## 📋 **LANGKAH 3: MENGELOLA PESANAN**

### **A. Melihat Pesanan Baru:**

**Notifikasi Otomatis:**
Bot akan otomatis mengirim notifikasi ke semua admin ketika ada pesanan baru:

```
🔔 NEW ORDER #1234
==================
👤 User: John Doe (@johndoe)
📱 ID: 123456789
🎯 Service: YouTube Watch Time
🔗 URL: https://youtube.com/watch?v=xxxxx
📊 Quantity: 1,000 minutes
💰 Cost: 50 tokens
📅 Created: 16/01/2025 10:30
⏰ Status: Pending

[Approve] [Reject] [Details]
```

### **B. Review Detail Pesanan:**

**Klik "Orders" di Admin Panel:**
```
📋 PENDING ORDERS (12)
======================

#1234 - YouTube Watch Time
👤 @johndoe | 1,000 min | 50 tokens
📅 16/01/2025 10:30
[Approve] [Reject] [View]

#1235 - Instagram Likes  
👤 @janedoe | 5,000 likes | 25 tokens
📅 16/01/2025 10:25
[Approve] [Reject] [View]

#1236 - TikTok Views
👤 @mikejohn | 10,000 views | 10 tokens
📅 16/01/2025 10:20
[Approve] [Reject] [View]
```

### **C. Aksi Admin untuk Pesanan:**

**1. Approve Order (Setujui):**
```
✅ ORDER APPROVED #1234
=======================
Status changed: Pending → Processing
Processing started automatically
ETA: 2-4 hours
User notified: ✅
```

**2. Reject Order (Tolak):**
```
❌ ORDER REJECTED #1234
=======================
Reason: [Select or type reason]
• Invalid URL
• Service not available
• Suspicious activity
• Custom reason: ___________

Token refund: ✅ Automatic
User notified: ✅
```

**3. Manual Processing:**
```
🔄 MANUAL PROCESSING #1234
==========================
Current status: Processing
Progress: ████████░░ 80%
Completed: 800/1,000 minutes
Actions:
[Pause] [Resume] [Complete] [Fail]
```

## 🚨 **LANGKAH 4: MONITORING REAL-TIME**

### **A. Dashboard Monitoring:**

**System Health:**
```
🖥️ SYSTEM STATUS
================
🟢 Bot Status: Online
🟢 Database: Connected  
🟢 API Services: Active
🟡 Queue: 12 pending
🔴 Failed Jobs: 3 (needs attention)

📊 REAL-TIME METRICS
===================
• Orders/hour: 15
• Success rate: 94.2%
• Avg response: 1.2s
• Active users: 45
```

### **B. Order Processing Queue:**

```
🔄 PROCESSING QUEUE (8)
======================
#1234 YouTube Watch Time    ████████░░ 80%
#1235 Instagram Likes       ██████░░░░ 60%  
#1236 TikTok Views         ████░░░░░░ 40%
#1237 Facebook Likes       ██░░░░░░░░ 20%
#1238 YouTube Subscribers  ░░░░░░░░░░ 0%
```

### **C. Error Handling:**

**Failed Orders Alert:**
```
⚠️ FAILED ORDER ALERT
=====================
Order #1234 failed after 3 attempts
Error: API rate limit exceeded
Suggested action:
• Retry in 30 minutes
• Switch to backup API
• Manual processing
• Refund user

[Auto Retry] [Manual Fix] [Refund]
```

## 👥 **LANGKAH 5: USER MANAGEMENT**

### **A. User Search & Details:**

**Command:** `/admin user 123456789`

```
👤 USER DETAILS
===============
Name: John Doe
Username: @johndoe
Telegram ID: 123456789
Registration: 15/01/2025
Last Active: 16/01/2025 10:30
Status: Active

💰 TOKEN INFO
=============
Current Balance: 125 tokens
Total Earned: 500 tokens
Total Spent: 375 tokens
From Ads: 200 tokens
From Referrals: 100 tokens

📊 ORDER HISTORY
================
Total Orders: 25
Completed: 23 (92%)
Failed: 2 (8%)
Avg Order Value: 15 tokens
Last Order: 16/01/2025

🎯 ACTIONS
==========
[Add Tokens] [Ban User] [Send Message]
[View Orders] [Make Premium] [Reset Password]
```

### **B. Bulk User Actions:**

```
👥 BULK USER MANAGEMENT
=======================
📊 Filter Users:
• Registration date: [Date range]
• Activity: Active/Inactive/Banned
• Token balance: [Min-Max range]
• Order count: [Min-Max range]

🎯 Bulk Actions:
[Add Tokens] [Send Broadcast] [Export Data]
[Ban Multiple] [Premium Upgrade] [Reset Stats]
```

## 💰 **LANGKAH 6: TOKEN MANAGEMENT**

### **A. Manual Token Operations:**

**Add Tokens to User:**
```
💎 ADD TOKENS
=============
User ID: 123456789
Current Balance: 125 tokens
Amount to Add: [Input field]
Reason: [Dropdown]
• Compensation
• Bonus reward  
• Manual adjustment
• Promotion
• Custom: ___________

[Add Tokens] [Cancel]
```

**Bulk Token Rewards:**
```
🎁 BULK TOKEN REWARD
===================
Target Users:
○ All active users
○ Premium users only
○ Users with 0 balance
○ Custom filter

Token Amount: [Input]
Message: [Text area]
Schedule: 
○ Send now
○ Schedule for: [Date/Time]

[Send Reward] [Preview] [Cancel]
```

### **B. Token Analytics:**

```
📊 TOKEN ANALYTICS
==================
💰 Distribution Today:
• From ads: 1,250 tokens
• From referrals: 500 tokens  
• Manual rewards: 200 tokens
• Registration bonus: 300 tokens

💸 Usage Today:
• YouTube services: 800 tokens
• Instagram services: 600 tokens
• TikTok services: 400 tokens
• Facebook services: 200 tokens

📈 Trends:
• Daily average: 2,000 tokens
• Weekly growth: +15%
• Most popular: YouTube (40%)
```

## 📢 **LANGKAH 7: BROADCAST SYSTEM**

### **A. Send Broadcast Message:**

```
📢 BROADCAST MESSAGE
===================
Target Audience:
☑️ All users (1,234)
☐ Active users only (456)
☐ Premium users (89)
☐ Users with orders (567)
☐ Custom filter

Message Type:
○ Text only
○ Text + Image
○ Text + Button
○ Rich media

Message Content:
[Text area - supports Markdown]

Buttons (optional):
Button 1: [Text] [URL/Callback]
Button 2: [Text] [URL/Callback]

Schedule:
○ Send immediately
○ Schedule: [Date] [Time]

[Preview] [Send] [Save Draft]
```

### **B. Broadcast Analytics:**

```
📊 BROADCAST STATS
==================
Last Message: "New Year Promo"
Sent: 16/01/2025 09:00
Recipients: 1,234 users

📈 Performance:
• Delivered: 1,230 (99.7%)
• Read: 892 (72.5%)
• Clicked: 234 (19.0%)
• Conversions: 45 (3.7%)

💰 Revenue Impact:
• Orders generated: 45
• Revenue: 1,125 tokens
• ROI: 450%
```

## 🔧 **LANGKAH 8: SYSTEM MAINTENANCE**

### **A. Database Management:**

```
🗄️ DATABASE MANAGEMENT
======================
📊 Statistics:
• Total records: 15,234
• Database size: 15.2 MB
• Last backup: 16/01/2025 06:00
• Growth rate: +2.3% daily

🧹 Cleanup Options:
[Delete old logs] [Archive completed orders]
[Remove inactive users] [Optimize tables]

💾 Backup Options:
[Manual backup] [Schedule backup]
[Download backup] [Restore backup]
```

### **B. API Management:**

```
🔌 API MANAGEMENT
=================
🎬 YouTube API:
Status: 🟢 Active
Rate limit: 450/500 requests
Last error: None
Uptime: 99.8%

📸 Instagram API:
Status: 🟡 Limited
Rate limit: 95/100 requests  
Last error: 2 hours ago
Uptime: 97.2%

🎵 TikTok API:
Status: 🟢 Active
Rate limit: 200/300 requests
Last error: None
Uptime: 99.5%

[Test APIs] [Reset Limits] [Switch Backup]
```

## 🚨 **TROUBLESHOOTING ADMIN PANEL**

### **Problem 1: Admin Panel Tidak Muncul**

**Solusi:**
1. ✅ Cek User ID di Replit Secrets
2. ✅ Pastikan format ADMIN_USER_IDS benar
3. ✅ Restart bot setelah update secrets
4. ✅ Test dengan `/admin` langsung

**Debug Command:**
```python
# Tambahkan di start_handler.py sementara
print(f"User ID: {user.id}")
print(f"Admin IDs: {os.getenv('ADMIN_USER_IDS')}")
```

### **Problem 2: Pesanan Tidak Diproses**

**Solusi:**
1. ✅ Cek status API external
2. ✅ Verify database connection
3. ✅ Check scheduler service
4. ✅ Review error logs di Replit

### **Problem 3: Notifikasi Admin Tidak Masuk**

**Solusi:**
1. ✅ Pastikan bot tidak diblokir admin
2. ✅ Cek setting notifikasi Telegram
3. ✅ Verify admin handler berfungsi
4. ✅ Test dengan pesanan manual

## 🎯 **BEST PRACTICES ADMIN**

### **Daily Tasks:**
- ✅ Check pending orders (pagi & sore)
- ✅ Monitor system health
- ✅ Review failed orders
- ✅ Respond to user support
- ✅ Check revenue metrics

### **Weekly Tasks:**
- ✅ Analyze user growth
- ✅ Review service performance  
- ✅ Update pricing if needed
- ✅ Backup database
- ✅ Plan promotions

### **Monthly Tasks:**
- ✅ Generate revenue report
- ✅ Optimize system performance
- ✅ Update service offerings
- ✅ Review admin access
- ✅ Plan feature updates

---

**🎊 SELAMAT! ADMIN PANEL SIAP DIGUNAKAN!**

*Setup Admin Lengkap by BLACKBOXAI*
*By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/*
