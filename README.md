

### 4. Configure PostgreSQL Database

Edit `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'task_db',
        'USER': 'task_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
## Authentication (JWT)

### 1. Obtain JWT Token

```http
POST /api/token/
```

#### Request:

```json
{
    "username": "admin",
    "password": "admin123"
}
```

#### Response:

```json
{
    "access": "jwt_access_token",
    "refresh": "jwt_refresh_token"
}
```

### 2. Refresh Token

```http
POST /api/token/refresh/
```

#### Request:

```json
{
    "refresh": "jwt_refresh_token"
}
```

#### Response:

```json
{
    "access": "new_jwt_access_token"
}
```

## Task API Endpoints

### 1. List and Create Tasks

```http
GET /api/tasks/
POST /api/tasks/
```

#### Request Headers:

```json
{
    "Authorization": "Bearer jwt_access_token"
}
```

#### Request Body (POST):

```json
{
    "title": "Complete Django Project",
    "description": "Work on the API and finish the UI",
    "status": "pending"
}
```

#### Response:

```json
{
    "id": 1,
    "title": "Complete Django Project",
    "description": "Work on the API and finish the UI",
    "status": "pending",
    "created_at": "2024-03-16T12:00:00Z"
}
```

### 2. Retrieve, Update, Delete Task

```http
GET /api/tasks/{id}/
PUT /api/tasks/{id}/
DELETE /api/tasks/{id}/
```

#### Request Body (PUT):

```json
{
    "title": "Complete Django API",
    "description": "Update and refine the API endpoints",
    "status": "completed"
}
```

#### Response (GET):

```json
{
    "id": 1,
    "title": "Complete Django API",
    "description": "Update and refine the API endpoints",
    "status": "completed",
    "created_at": "2024-03-16T12:00:00Z"
}
```

## Admin Panel

- URL: `http://127.0.0.1:8000/admin/`
- Use superuser credentials to log in and manage users and tasks.

json
- {
- "username": "admin",
-  "password": "admin123"
- }
