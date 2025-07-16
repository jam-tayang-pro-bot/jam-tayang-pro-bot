"""
Keep Alive System for Replit
Menjaga bot tetap aktif di Replit dengan web server sederhana
"""

from flask import Flask
from threading import Thread
import time

app = Flask('')

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Jam Tayang Pro Bot</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f0f0f0; }
            .container { background: white; padding: 30px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); max-width: 600px; margin: 0 auto; }
            .status { color: #28a745; font-size: 24px; font-weight: bold; }
            .info { color: #666; margin: 20px 0; }
            .link { color: #007bff; text-decoration: none; }
            .features { text-align: left; margin: 20px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Jam Tayang Pro Bot</h1>
            <div class="status">✅ Bot is Running!</div>
            <div class="info">Professional Social Media Engagement Service</div>
            
            <div class="features">
                <h3>🎯 Available Services:</h3>
                <ul>
                    <li>🎬 YouTube: Jam Tayang, Subscriber, Likes, Views</li>
                    <li>📸 Instagram: Likes, Followers, Views</li>
                    <li>🎵 TikTok: Views, Likes, Followers</li>
                    <li>📘 Facebook: Likes, Followers, Shares</li>
                </ul>
                
                <h3>💰 Token System:</h3>
                <ul>
                    <li>🎁 50 token gratis saat daftar</li>
                    <li>📺 Tonton iklan untuk token tambahan</li>
                    <li>👥 Referral bonus</li>
                </ul>
            </div>
            
            <p>
                <a href="https://t.me/JamTayangProBot" class="link" target="_blank">
                    📱 Start Using Bot
                </a>
            </p>
            
            <div class="info">
                <small>By Kantong Aplikasi 2025 - https://www.kantongaplikasi.com/</small>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/status')
def status():
    return {
        "status": "running",
        "bot": "Jam Tayang Pro Bot",
        "url": "https://t.me/JamTayangProBot",
        "services": [
            "YouTube Services",
            "Instagram Services", 
            "TikTok Services",
            "Facebook Services"
        ],
        "features": [
            "Auto Processing 24/7",
            "Token System",
            "Admin Panel",
            "Real-time Analytics"
        ]
    }

@app.route('/health')
def health():
    return {"status": "healthy", "timestamp": time.time()}

def run():
    """Run Flask server"""
    app.run(host='0.0.0.0', port=8080, debug=False)

def keep_alive():
    """Start keep alive server in background thread"""
    print("🌐 Starting keep-alive server...")
    t = Thread(target=run)
    t.daemon = True
    t.start()
    print("✅ Keep-alive server started on port 8080")

if __name__ == "__main__":
    keep_alive()
    # Keep the main thread alive
    while True:
        time.sleep(60)
