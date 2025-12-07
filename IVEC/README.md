# IVEC Project

IVEC is a full-stack web application designed for investment tracking and automatic interest calculation. The application is built using Django and Django REST Framework for the backend, and React.js for the frontend. 

## Features

- User authentication and management with role-based access (Admin, Investor, Agent).
- Investment tracking with automatic interest calculation.
- Transaction history for investments.
- Responsive and user-friendly interface built with React.js.

## Project Structure

```
IVEC
├── backend
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── ivec_project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── apps
│       ├── users
│       └── investments
├── frontend
│   ├── package.json
│   ├── Dockerfile
│   ├── public
│   │   └── index.html
│   └── src
│       ├── index.jsx
│       ├── App.jsx
│       ├── api
│       ├── services
│       ├── components
│       └── pages
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Setup Instructions

### Backend

1. Navigate to the `backend` directory.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations to set up the database:
   ```
   python manage.py migrate
   ```
4. Start the Django development server:
   ```
   python manage.py runserver
   ```

### Frontend

1. Navigate to the `frontend` directory.
2. Install the required packages:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Usage

- Access the application through your web browser at `http://localhost:3000`.
- Use the provided authentication endpoints to register and log in.
- Track your investments and view transaction history.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.