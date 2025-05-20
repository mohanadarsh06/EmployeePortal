# Employee Feedback Portal - Development Documentation

## Project Overview
The Employee Feedback Portal is designed to streamline performance management and enable line managers to effectively view, provide, and track feedback for their team members. The application implements a hierarchical access control system based on manager-reportee relationships.

## Application Architecture
We're implementing a hybrid architecture:
- **API Server**: Python Flask with SQLAlchemy
- **Proxy Server**: Node.js Express with TypeScript
- **Database**: PostgreSQL
- **Authentication**: Flask-Login
- **Frontend**: HTML, CSS, JavaScript
- **Communication**: Node.js proxy to Flask application

## Key Features
1. Hierarchical access control (managers can only access data for their reportees)
2. Employee management with CRUD operations
3. Feedback submission and tracking
4. Dashboard with performance metrics and visualization
5. Simplified authentication for demo purposes

## Database Schema

### Employees Table
```
employees
├── id (PK)
├── name
├── email
├── employee_id
├── position
├── department
├── manager_id (FK to employees.id)
├── join_date
└── is_active
```

### Feedback Table
```
feedbacks
├── id (PK)
├── employee_id (FK to employees.id)
├── giver_id (FK to employees.id)
├── rating
├── comment
├── feedback_date
├── areas_for_improvement
└── categories
```

## Application Screens

### Login Page
Users can log in using their email and password (simplified for demo).

### Dashboard
- Overview of team performance
- Recent feedback summary
- Performance metrics visualization
- Quick links to frequently used functions

### Employees Page
- List of employees the manager has access to
- Add/Edit/Delete employee functionality
- Import employees from Excel

### Feedback Page
- View feedback for reportees
- Submit new feedback
- Filter by employee, date range, rating

## Development Progress
- ✓ Set up Flask application structure
- ✓ Implemented database models with SQLAlchemy
- ✓ Created authentication system with Flask-Login
- ✓ Fixed database schema mismatch issues
- ✓ Implemented hierarchical access control
- ✓ Created Node.js Express proxy server to Flask application
- ✓ Added Flask process management in Node.js server
- ✓ Set up path rewriting for Flask endpoints
- → Creating templates and frontend components
- → Adding data visualization to the dashboard
- → Implementing Excel import functionality

## Implementation Notes

### Authentication
For demo purposes, we've implemented a simplified authentication system where:
- All users can log in with the password "password"
- User identity is determined by email address
- Session is managed by Flask-Login

### Access Control
The hierarchical access control is implemented at both the model and route levels:
- Employee model has methods to retrieve management chains and all reportees
- Route decorators verify permission before displaying data or allowing operations

### Database Connection
The application uses a PostgreSQL database with connection parameters from environment variables.

### Hybrid Architecture
The application uses a hybrid architecture with two main components:
1. **Node.js Express Server** - Serves as the entry point for all requests, running on port 5000.
   - Manages the lifecycle of the Flask application
   - Serves static assets from the client directory
   - Proxies specific requests to the Flask API

2. **Python Flask Application** - Acts as the API server, running on port 5001.
   - Handles all business logic and data access
   - Implements the hierarchical access control
   - Manages authentication through Flask-Login
   - Provides API endpoints for the frontend

The communication between the two servers happens through an HTTP proxy middleware in Express that forwards relevant requests to the Flask application.