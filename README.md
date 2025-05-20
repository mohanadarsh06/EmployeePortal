# Employee Feedback Portal

A comprehensive web application designed to streamline performance management and employee feedback within organizations. This application implements a hierarchical access control system that enables line managers to effectively view, provide, and track feedback for their team members based on the organizational structure.

## Features

- **Hierarchical Access Control**: Line managers can only view/edit feedback for their direct and indirect reportees
- **Employee Management**: Complete CRUD operations for employee details
- **Feedback System**: Managers can provide, view, edit, and delete feedback for their team
- **Dashboard**: Overview of team statistics and performance metrics
- **Authentication**: Secure login and access control
- **Responsive Design**: Works on desktop and mobile devices

## Technology Stack

### Hybrid Architecture (Current)
- **API Server**: Flask with SQLAlchemy
- **Proxy Server**: Express.js with TypeScript
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript with Bootstrap
- **Authentication**: Flask-Login
- **Communication**: Node.js proxy to Flask application

### Key Components
- Node.js Express server running on port 5000 (main entry point)
- Python Flask application running on port 5001 (API server)
- Proxy middleware forwarding relevant requests from Express to Flask

## Project Structure (Hybrid Architecture)

```
├── app/                      # Flask application package
│   ├── models/               # Database models
│   ├── routes/               # API route handlers
│   ├── static/               # Static assets (CSS, JS)
│   │   ├── css/              # CSS stylesheets
│   │   └── js/               # JavaScript files
│   ├── templates/            # HTML templates
│   │   ├── auth/             # Authentication templates
│   │   ├── dashboard/        # Dashboard templates
│   │   ├── employees/        # Employee management templates
│   │   └── feedback/         # Feedback templates
│   ├── utils/                # Utility functions
│   ├── __init__.py           # Application factory
│   └── config.py             # Configuration
├── server/                   # Node.js Express server
│   ├── index.ts              # Express server entry point with Flask proxy
│   ├── routes.ts             # Express route handlers
│   ├── storage.ts            # Data storage interface
│   └── vite.ts               # Frontend build configuration
├── client/                   # Frontend assets
│   ├── src/                  # Frontend source files
│   └── static files          # HTML/CSS/JS files
├── run.py                    # Flask application entry point
├── .env                      # Environment variables
└── README.md                 # Project documentation (this file)
```

## How to Run in Visual Studio Code

### Prerequisites

1. [Python](https://www.python.org/) (v3.8 or higher)
2. [Visual Studio Code](https://code.visualstudio.com/)
3. [PostgreSQL](https://www.postgresql.org/) database

### Setup Steps

1. **Clone or download the repository**

2. **Open the project in VS Code or your preferred IDE**

3. **Configure database connection**

   Create a `.env` file in the root directory with the following content:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/feedback_portal
   SECRET_KEY=your-secret-key
   ```
   Replace `username`, `password` with your PostgreSQL credentials and set a secure `SECRET_KEY`.

4. **Install Dependencies**

   For the Node.js Express server:
   ```
   npm install
   ```

   For the Flask application:
   ```
   pip install flask flask-sqlalchemy flask-login psycopg2-binary python-dotenv werkzeug openpyxl
   ```

5. **Initialize the database**
   
   The database will be automatically initialized when you first start the application.

6. **Start the hybrid application**

   In Replit:
   ```
   npm run dev
   ```

   This will start both the Express server (port 5000) and Flask application (port 5001),
   with the Express server proxying relevant requests to Flask.

7. **Access the application**
   
   Open your browser and navigate to the Express server's URL (typically http://localhost:5000 or the Replit preview URL)

## Usage Guide

1. **Login**: Use one of the sample users to login (available on the login page)
2. **Dashboard**: View summary statistics about your team
3. **Employees**: Manage employee details with full CRUD functionality
4. **Feedback**: Provide and manage feedback for direct reports

## Data Model

The application uses the following main entities:

- **Employees**: Contains employee information, including hierarchical relationships
- **Feedback**: Stores feedback entries provided by managers to their reportees

## Security Features

- Line managers can only access data of their direct and indirect reportees
- Authentication ensures secure access to protected resources
- Input validation prevents malicious data entry
- Password hashing for secure credential storage

## Deployment

This application can be deployed to any platform supporting Python applications such as Heroku, PythonAnywhere, or AWS Elastic Beanstalk.

## License

This project is licensed under the MIT License - see the LICENSE file for details.