# Project Management System

This project is a **Django-based Project Management System** that provides a RESTful API for managing users, projects, tasks, and comments. It includes user authentication with JWT tokens and API documentation with Swagger and ReDoc.

---

## Features
### User Management
- **Register User**: Create a new user account.
- **Login User**: Authenticate user and return JWT tokens.
- **CRUD Operations**: Manage user details (retrieve, update, delete).

### Project Management
- **List Projects**: Retrieve all projects.
- **Create Project**: Add a new project.
- **Retrieve, Update, Delete Project**: Manage specific projects.

### Task Management
- **List Tasks**: Retrieve tasks within a specific project.
- **CRUD Operations**: Create, retrieve, update, and delete tasks.

### Comments Management
- **List Comments**: Retrieve comments for a specific task.
- **CRUD Operations**: Create, retrieve, update, and delete comments.

### API Documentation
- **Swagger**: Interactive API documentation.
- **ReDoc**: Simplified, user-friendly documentation.

---

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/project-management.git
cd project-management
```

### Set Up the Environment
Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```
### Configure the Database
Apply migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server
Start the Django development server:

```bash
python manage.py runserver
```
The application will be available at http://127.0.0.1:8000/.

## API Endpoints

Below are the main endpoints categorized by resource:

### User Endpoints
| Method | Endpoint              | Description                     |
|--------|-----------------------|---------------------------------|
| POST   | /api/users/register/   | Register a new user.            |
| POST   | /api/users/login/      | Login and get JWT tokens.      |
| GET    | /api/users/            | List all users (Admin only).   |
| GET    | /api/users/{id}/       | Get details of a user.         |
| PUT    | /api/users/{id}/       | Update a user.                 |
| DELETE | /api/users/{id}/       | Delete a user.                 |

### Project Endpoints
| Method | Endpoint               | Description                     |
|--------|------------------------|---------------------------------|
| GET    | /api/projects/          | List all projects.             |
| POST   | /api/projects/          | Create a new project.          |
| GET    | /api/projects/{id}/     | Get details of a project.      |
| PUT    | /api/projects/{id}/     | Update a project.              |
| DELETE | /api/projects/{id}/     | Delete a project.              |

### Task Endpoints
| Method | Endpoint                           | Description                     |
|--------|------------------------------------|---------------------------------|
| GET    | /api/projects/{project_id}/tasks/   | List tasks in a project.       |
| POST   | /api/projects/{project_id}/tasks/   | Create a task in a project.    |
| GET    | /api/tasks/{id}/                   | Get details of a task.         |
| PUT    | /api/tasks/{id}/                   | Update a task.                 |
| DELETE | /api/tasks/{id}/                   | Delete a task.                 |

### Comment Endpoints
| Method | Endpoint                               | Description                     |
|--------|----------------------------------------|---------------------------------|
| GET    | /api/tasks/{task_id}/comments/         | List comments on a task.       |
| POST   | /api/tasks/{task_id}/comments/         | Create a comment on a task.    |
| GET    | /api/comments/{id}/                    | Get details of a comment.      |
| PUT    | /api/comments/{id}/                    | Update a comment.              |
| DELETE | /api/comments/{id}/                    | Delete a comment.              |




## Authentication
This project uses JWT for authentication. Use the /api/users/login/ endpoint to obtain an access token and a refresh token. Include the access token in the Authorization header for subsequent requests:

```base
Authorization: Bearer <your_access_token>
```
## API Documentation
```base
Swagger UI: http://127.0.0.1:8000/api/swagger/
ReDoc: http://127.0.0.1:8000/api/redoc/
```

## Project Structure
```base
project-management/
├── project_management/     # Main project folder
│   ├── settings.py         # Django settings
│   ├── urls.py             # URL routing
├── app/                    # Application folder
│   ├── models.py           # Models for the database
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views
│   ├── urls.py             # API routes
├── templates/              # HTML templates (if any)
├── static/                 # Static files
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```
## Contribution

To contribute:
    Fork the repository.
    Create a feature branch.
    Commit your changes.
    Submit a pull request.

## License
This project is licensed under the MIT License. See LICENSE for details.

Enjoy building with the Project Management System! 🚀
