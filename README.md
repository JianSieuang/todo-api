# Todo App with OAuth and Docker

A simple and secure Todo application built with Flask, using OAuth for authentication (GitHub and Google), and Docker for containerization.

---

## 🌟 Features
- User authentication with **GitHub** and **Google** using OAuth.
- Create, read, update, and delete (CRUD) TODO items.
- Mark TODO items as completed.
- Responsive API endpoints for easy integration.
- Dockerized for easy deployment.

---

## 🛠️ Technologies Used
- **Python**: Backend language
- **Flask**: Web framework
- **Flask-Dance**: OAuth integration
- **SQLAlchemy**: ORM for database management
- **PostgreSQL**: Database
- **Docker**: Containerization

---

## 🚀 Running the Application

### 📝 **Prerequisites**
- Docker
- Docker Compose
- Python 3.10

---

### 🗂️ **1. Clone the Repository:**
```bash
git clone https://github.com/username/todo-oauth-app.git
cd todo-oauth-app
```

---

### 🐍 **2. Local Development:**
  1. Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```

  2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

  3. Set up environment variables:
  ```bash
  cp .env.example .env
  ```

  4. Run the Flask app:
  ```bash
  flask run --host=0.0.0.0 --port=5000
  ```

  5. Access the application at:
  ```bash
  http://localhost:5000
  ```

---

### 🐋 **3. Running with Docker:**
  1. Building the Docker Image:
  ```bash
  docker-compose -f docker_compose.yml build
  ```

  2. Starting the Containers:
  ```bash
  docker-compose -f docker_compose.yml up
  ```

  3. Access the Application:
  ```bash
  http://localhost:5000
  ```

  4. Stopping the Containers:
  ```bash
  docker-compose -f docker_compose.yml down
  ```

---

### 🧪 **4. Testing the Application**
  1. Running Tests Locally:
  ```bash
  pytest -v
  ```

  2. Runnning Tests in Docker:
  ```bash
  docker-compose -f docker_compose.yml run web pytest -v
  ```

---

### 🌐 **5. Interface Documentation**
🌟 OAuth Login Flow:
  - GitHub:
    Endpoint:
    ```bash
    /auth/github
    ```
    Callback URL:
    ```bash
    http://localhost:5000/auth/github_login/github/authorized
    ```
  - Google:
    Endpoint:
    ```bash
    /auth/google
    ```
    Callback URL:
    ```bash
    http://localhost:5000/auth/google_login/google/authorized
    ```
    
📑 API Endpoints:
  - Get All Todos:
    ```bash
    GET /api/todos/
    ```
      - Response:
        ```json
        [
          {
            "id": 1,
            "content": "Buy milk",
            "completed": false
          }
        ]
        ```
  - Add a New Todo:
    ```bash
    POST /api/todos/
    Content-Type: application/json
    {
      "content": "Learn Docker"
    }
    ```
  - Toggle Completion Status:
    ```bash
    PUT /api/todos/1/toggle-completed
    ```
  - Delete a Todo:
    ```bash
    DELETE /api/todos/1
    ```
