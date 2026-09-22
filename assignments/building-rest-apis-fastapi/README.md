# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Create a small REST API that manages a collection of books using the FastAPI framework. This activity will help you practice building endpoints, validating input with Pydantic models, handling errors, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Set Up the FastAPI Application

#### Description
Create a new FastAPI application and define a simple root endpoint that returns a welcome message.

#### Requirements
The completed project must:

- Install and import `FastAPI`.
- Create an app instance using `FastAPI()`.
- Add a `GET /` endpoint that returns a message such as `"Welcome to the Book API"`.
- Run the app locally with `uvicorn`.

### 🛠️ Build a Book Collection API

#### Description
Implement a set of endpoints to store and manage a list of books.

#### Requirements
The completed project must:

- Define a `Book` model with fields such as `id`, `title`, `author`, and `price`.
- Create a list of sample books in memory.
- Add a `GET /books` endpoint to return all books.
- Add a `GET /books/{book_id}` endpoint to return a single book by ID.
- Add a `POST /books` endpoint to create a new book.

### 🛠️ Update, Delete, and Validate Data

#### Description
Add the remaining CRUD operations and improve the API with validation and error handling.

#### Requirements
The completed project must:

- Add a `PUT /books/{book_id}` endpoint to update an existing book.
- Add a `DELETE /books/{book_id}` endpoint to remove a book.
- Return `404` when a requested book is not found.
- Validate input fields so required data is present and values are reasonable.
- Use `status_code` for successful create/update operations.

### 🛠️ Document and Test the API

#### Description
Make the API easier to use and verify that the endpoints behave as expected.

#### Requirements
The completed project must:

- Include a `title` and a short description for the app.
- Use clear, consistent JSON responses.
- Test the endpoints using FastAPI's interactive docs at `/docs`.
- Confirm that the API works for reading, creating, updating, and deleting books.

## ✅ Challenge Extension

Try adding one of the following improvements:

- Add a filter for books by author.
- Sort the books by price or title.
- Add a `GET /health` endpoint.
- Include pagination for a larger collection.

## 💡 Tips

- Use Pydantic models to keep request and response data structured.
- Keep the app simple and focus on one resource: books.
- Test each endpoint with the browser or with `curl` before moving to the next one.
