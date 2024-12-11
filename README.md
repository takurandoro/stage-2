# Stage 2 - Django Project

## Project Overview
Stage 2 builds upon the foundational setup from Stage 1 by introducing enhancements and extending the functionality of the Django-based web application. This phase focuses on implementing basic API endpoints and refining the application structure.

## Repository Structure
```
stage-2/
├── api/                # Contains the API-related files and configurations
├── uninest/            # Core Django project directory
├── db.sqlite3          # Default SQLite database file
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies for the project
```

### 1. `api/`
The `api/` directory now contains initial implementations of serializers, views, and URLs. This setup enables basic CRUD operations and sets the stage for more complex functionality.

### 2. `uninest/`
The main Django project directory, with updates to the settings and URLs to accommodate the newly added APIs. It continues to serve as the central point for project-wide configurations.

### 3. `db.sqlite3`
SQLite remains the default database in this stage. It holds the data for the newly created models and API endpoints. For production, transitioning to PostgreSQL or MySQL is recommended.

### 4. `manage.py`
Used for managing Django functionalities, such as running the server, migrations, and creating apps. No significant changes from Stage 1.

### 5. `requirements.txt`
Additional dependencies, if any, will be listed here. Install them using the following command:
```bash
pip install -r requirements.txt
```

## Getting Started
Follow these steps to set up and run the project locally:

### Prerequisites
- Python (>= 3.8)
- pip (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd stage-2
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Key Updates in Stage 2
- Added initial API endpoints in the `api/` directory.
- Updated the `uninest/` directory to integrate the new endpoints.
- Established a foundation for data interaction and user-facing functionality.

---
Stay tuned for updates in Stage 3!
