# Stage1Repo
HNG14 DEVOPS Challenge program. Stage1 challenge for building api  

# Production-Ready FastAPI Deployment with Nginx Reverse Proxy (AWS EC2)

## Project Overview
This project demonstrates a production-ready deployment of a FastAPI application using:
- AWS EC2 (Ubuntu)
- Nginx as a reverse proxy
- systemd for process management
- HTTPS with Let's Encrypt SSL

It includes both:
- Stage 0 (Nginx static API endpoint)
- Stage 1 (FastAPI backend service)

**1. Objective**
Build a minimal backend API
Deploy it on a VPS (your existing server can be reused)
Expose it publicly via Nginx Reverse Proxy
Ensure it is production-ready (persistent, fast, secure)

**2. API Development Requirements**
Endpoint 1
GET /
{
 "message": "API is running"
}

Endpoint 2
GET /health
{
 "message": "healthy"
}

Endpoint 3
GET /me
{
 "name": "Your Full Name",
 "email": "you@example.com",
 "github": "https://github.com/yourusername"
}

**Strict API Rules**
All endpoints must:
Return Content-Type: application/json
Return HTTP status: 200
Respond within ≤ 500ms
Return exact JSON format (no deviation)

**PHASE 1: Build API (Python – FastAPI recommended)**
1. Install dependencies (local or server)
sudo apt update
sudo apt install python3-pip -y
pip3 install fastapi uvicorn

2. Create project
mkdir stage1-api
cd stage1-api
nano main.py

3. Add API code
from fastapi import FastAPI
from fastapi.responses import JSONResponse

#this is code
app = FastAPI()
@app.get("/")
def root():
   return JSONResponse(content={"message": "API is running"}, status_code=200)
@app.get("/health")
def health():
   return JSONResponse(content={"message": "healthy"}, status_code=200)
@app.get("/me")
def me():
   return JSONResponse(content={
       "name": "IFIOK EMMANUEL",
       "email": "ifiokbassey.e@gmail.com",
       "github": "https://github.com/YOUR_USERNAME"
   }, status_code=200)

**PHASE 2: Deploy on Server**
1. Copy project to server (if needed)
scp -i hng-key.pem -r stage1-api ubuntu@server_ip_address:~

2. Run API on server
cd stage1-api
uvicorn main:app --host 127.0.0.1 --port 8000

PHASE 3: Configure Nginx Reverse Proxy
1. Edit Nginx config
sudo nano /etc/nginx/sites-enabled/default

2. Replace server block
server {
   listen 80;
   listen [::]:80;
   server_name trubytes.work.gd;

   location / {
       proxy_pass http://127.0.0.1:8000;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
   }
}

3. Test and reload
sudo nginx -t
sudo systemctl reload nginx

4. Test publicly
curl http://trubytes.work.gd
curl http://trubytes.work.gd/health
curl http://trubytes.work.gd/me

**PHASE 4: Make Service Persistent **
## Live API
Base URL: https://trubytes.work.gd

---

## 📡 API Endpoints

### 1. Root Endpoint
