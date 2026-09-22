# 📘 Assignment: Database APIs with Authentication

## 🎯 Objective

Build a small FastAPI application that stores task data in a SQLite database and requires a simple login flow to protect the endpoints. This assignment helps students practice persistence, API design, validation, and basic authentication in a real-world web service.

## 📝 Tasks

### 🛠️ Create the Database Model

#### Description
Set up a SQLite database and define the tables needed to persist users and tasks for the application.

#### Requirements
The completed project must:

- Use `sqlite3` or SQLAlchemy to connect to a local database.
- Create a `users` table with at least `id`, `username`, and `password`.
- Create a `tasks` table with at least `id`, `title`, `description`, and `completed`.
- Ensure the database is created when the app starts.
- Use clear and consistent column names.

### 🛠️ Build the Task API

#### Description
Create endpoints for creating, reading, updating, and deleting tasks stored in the database.

#### Requirements
The completed project must:

- Add a `GET /tasks` endpoint to list all tasks.
- Add a `POST /tasks` endpoint to create a task.
- Add a `GET /tasks/{task_id}` endpoint to fetch one task by ID.
- Add a `PUT /tasks/{task_id}` endpoint to update an existing task.
- Add a `DELETE /tasks/{task_id}` endpoint to delete a task.
- Return `404` when a task does not exist.
- Validate required fields before saving to the database.

### 🛠️ Add Basic Authentication

#### Description
Protect the task routes so only authenticated users can create or modify tasks.

#### Requirements
The completed project must:

- Add a `POST /register` endpoint for creating a new user.
- Add a `POST /login` endpoint that accepts a username and password.
- Return a token or session identifier after successful login.
- Require the token in the request headers for protected routes.
- Reject requests without valid authentication with `401 Unauthorized`.
- Keep the authentication flow simple and understandable.

## 📝 Tasks

### 🛠️ Test the Full Workflow

#### Description
Verify that the API works end-to-end from registration to task management.

#### Requirements
The completed project must:

- Register a user successfully.
- Log in and receive a valid token.
- Create a task with the authenticated user.
- Retrieve and update that task.
- Confirm that unauthorized requests fail correctly.
- Check the API using FastAPI docs at `/docs`.
