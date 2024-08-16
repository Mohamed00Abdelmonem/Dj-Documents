
# Dj-Documents

Dj-Documents is a Django-based project designed to manage and handle various types of documents efficiently. This repository contains the source code for the application, including the project structure, settings, and document handling logic.

## Features

- **Document Upload**: Upload and store documents securely.
- **Document Management**: Organize and manage documents within the application.
- **Search Functionality**: Quickly search through documents.
- **User Authentication**: Secure access to the application with user authentication.
  
## Project Structure

- `docs_app/` - Main application handling documents.
- `project/` - Django project settings and configuration.
- `manage.py` - Django management script.
- `db.sqlite3` - SQLite database file.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Mohamed00Abdelmonem/Dj-Documents.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Dj-Documents
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the application via `http://127.0.0.1:8000/` after starting the server.
- Use the provided interface to upload, manage, and search documents.

