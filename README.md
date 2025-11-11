# **CargoMind – Real-Time Logistics and Fleet Management System**

CargoMind is a **production-grade real-time logistics and fleet management platform** built for high-performance delivery networks. It combines **FastAPI**, **Redis**, **PostgreSQL + PostGIS**, and **Celery** into a scalable system for **vehicle tracking, analytics, and route optimization**.

---

## 🚀 **Architecture Overview**

**Services:**

* `auth` – JWT-based authentication and role management.
* `tracking` – Real-time location updates via REST + WebSocket.
* `analytics` – Scheduled fleet metrics and reports.
* `worker` – Celery background tasks for persistence and route optimization.
* `nginx` – Reverse proxy for production-grade routing.

**Stack:**
`FastAPI` · `PostgreSQL + PostGIS` · `Redis` · `Celery` · `Docker Compose` · `Nginx`

---

## ⚙️ **Core Data Flow**

1. **Driver** sends GPS updates → `/track/update_location` (FastAPI).
2. **API** caches location in **Redis**, publishes update on `vehicle_updates` channel.
3. **Dispatch clients** listen via **WebSocket** `/ws/track` for live position streams.
4. **Celery worker** asynchronously writes updates to **PostgreSQL (PostGIS)**.
5. **Analytics tasks** aggregate usage reports daily for admins.

---

## 🧩 **Core Features**

| Feature                  | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| 🔐 Authentication        | JWT + OAuth2 with roles: `driver`, `dispatcher`, `admin`.    |
| 🚗 Live Vehicle Tracking | Redis Pub/Sub + WebSocket feed for dispatchers.              |
| 🗺️ Route Optimization   | Celery background worker using A* or Google Distance Matrix. |
| 📊 Fleet Analytics       | Daily Celery job aggregates trip data to JSON/CSV reports.   |
| ☁️ Scalable Infra        | Docker Compose with Redis, Postgres, FastAPI, Nginx.         |
| 🧠 Smart Persistence     | Async Celery writes reduce API latency and DB load.          |

---

## 🧱 **Project Structure**

```
cargomind/
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── tracking.py
│   │   │   ├── websocket_tracking.py
│   │   └── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── redis_client.py
│   │   ├── celery_app.py
│   │   ├── auth.py
│   ├── models/
│   │   ├── telemetry.py
│   ├── schemas/
│   │   ├── vehicle.py
│   ├── workers/
│       ├── persist.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

## 🧩 **API Endpoints**

| Endpoint                 | Method | Description                 | Auth Role  |
| ------------------------ | ------ | --------------------------- | ---------- |
| `/auth/login`            | POST   | Authenticate user           | All        |
| `/track/update_location` | POST   | Driver location update      | Driver     |
| `/ws/track`              | WS     | Real-time vehicle stream    | Dispatcher |
| `/analytics/report`      | GET    | Generate fleet usage report | Admin      |

---

## 🐳 **Docker Deployment**

```bash
docker-compose up --build
```

**Services started:**

* `api`: FastAPI app on port `8000`
* `worker`: Celery worker for async jobs
* `redis`: Cache + broker
* `postgres`: Database with PostGIS
* `nginx`: Reverse proxy on port `80`

---

## 🧠 **Key Design Choices**

* **Redis Hash + Pub/Sub** for instant updates.
* **Celery** for async persistence (fast writes, resilient retries).
* **PostGIS** for accurate spatial queries.
* **WebSocket** for continuous tracking.
* **Nginx reverse proxy** for production-grade routing and load balancing.

---

## 📊 **Analytics Snapshot**

Daily metrics include:

* Distance covered per vehicle.
* Idle vs. active time.
* Route efficiency (distance vs. optimal path).
* Fleet utilization rate.

Output formats: **JSON + downloadable CSV**.

---

## 🧰 **Tech Stack**

| Layer             | Tool                 |
| ----------------- | -------------------- |
| Backend Framework | FastAPI              |
| Database          | PostgreSQL + PostGIS |
| Cache / Broker    | Redis                |
| Task Queue        | Celery               |
| WebSocket Stream  | FastAPI native       |
| Reverse Proxy     | Nginx                |
| Deployment        | Docker Compose       |
| CI/CD             | GitHub Actions       |

---

## 🧭 **Future Extensions**

* Redis Streams or Kafka for scalable pub/sub.
* Geo-fencing alerts and notifications.
* AI-driven route optimization.
* GraphQL API for analytics dashboard.

---

## 🧑‍💻 **Contributors**

Built and maintained by a cross-functional engineering team led by **Neville Mabonga** — focused on **precision, scalability, and execution discipline**.

---

Do you want me to add a **Quickstart guide** (setup `.env`, DB migrations, running worker + testing endpoints) to the README next?
