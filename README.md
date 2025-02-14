# 📅 Reservation Microservice with FastAPI

## 📝 Description
This project is a **reservation microservice** built with **FastAPI**. It allows users to manage reservations, including creating, updating, and retrieving bookings. The service communicates with other microservices using JSON.

## 🚀 Features
- ✅ **FastAPI-based API** for handling reservations
- ✅ **Microservices architecture**, integrating with other services
- ✅ **CRUD operations** for reservations
- ✅ **Validation with Pydantic** for data integrity
- ✅ **Custom authentication** (username & password)
- ✅ **Chain of Responsibility pattern** for reservation validation
- ✅ **Dockerized deployment** for easy setup

## 🏗️ Project Structure
```
📂 backendpython_reservation
 ├── 📂 controllers  # API route handlers
 ├── 📂 repositories # Data access logic (JSON storage)
 ├── 📂 services     # Business logic & validation
 ├── 📂 models       # Pydantic models for request validation
 ├── main.py         # FastAPI entry point
 ├── requirements.txt # Dependencies
 ├── Dockerfile      # Docker setup
```

## 🛠️ Installation & Setup

### 🔹 Prerequisites
- Python **3.13.2**
- Poetry (for dependency management)
- Docker (for containerization)

### 🔹 Clone the Repository
```bash
git clone https://github.com/yourusername/reservation-microservice.git
cd reservation-microservice
```

### 🔹 Install Dependencies
Using Poetry:
```bash
poetry install
```
Or using pip:
```bash
pip install -r requirements.txt
```

### 🔹 Run the FastAPI Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
API will be available at: **http://localhost:8000/docs** 🚀

---

## 🐳 Running with Docker
### 🔹 Build the Docker Image
```bash
docker build -t reservation-service .
```

### 🔹 Run the Container
```bash
docker run -d -p 8000:8000 --name reservation-container reservation-service
```

---

## 🔗 API Endpoints

### 📌 **Reservations**
| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/reservations/` | Create a new reservation |
| `GET` | `/reservations/` | Get all reservations |
| `GET` | `/reservations/actives/` | Get active reservations |
| `PUT` | `/reservations/{id}` | Update a reservation |
| `DELETE` | `/reservations/{id}` | Delete a reservation |

API Documentation available at **`/docs`** or **`/redoc`**.

---

## 🏗️ Architecture & Patterns
- **Microservices:** This service handles reservations and communicates with other services via JSON.
- **Chain of Responsibility Pattern:** Used for **reservation validation** (date availability, employee schedule conflicts).
- **Repository Pattern:** Abstracts data storage operations.

---

## 📌 Contribution
1. **Fork** the repository 🍴
2. **Clone** your forked repo locally  
   ```bash
   git clone https://github.com/yourusername/reservation-microservice.git
   ```
3. **Create a new branch** for your feature  
   ```bash
   git checkout -b feature-name
   ```
4. **Commit** and **push** your changes  
   ```bash
   git add .
   git commit -m "Add new feature"
   git push origin feature-name
   ```
5. Open a **Pull Request** 🚀

---

## 📜 License
This project is licensed under the **MIT License**.

---

### ✨ Developed by [Your Name](https://github.com/yourusername)


