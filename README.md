# Django REST Tourist CRUD

A full-stack web application for managing tourist destinations. This project provides a user-friendly platform to create, view, update, and delete tourist destination information including images, weather conditions, location details, and Google Maps integration.

## About The Project

This application serves as a comprehensive tourist destination management system that combines the power of Django REST Framework for the backend API with a Bootstrap-based frontend interface. It allows users to:

- Add new tourist destinations with detailed information
- Upload and manage destination images
- View destination details including weather and location
- Search through destinations easily
- Update destination information as needed
- Remove outdated destinations


The project demonstrates the implementation of RESTful API principles while maintaining a clean and responsive user interface. It's built with scalability in mind and can be easily extended with additional features.

## Features

- RESTful API endpoints for tourist destinations
- Complete CRUD functionality (Create, Read, Update, Delete)
- Image upload support for destinations
- Search functionality for destinations
- Responsive UI using Bootstrap


## Tech Stack

- **Backend:**
  - Django 
  - Django REST Framework
  - SQLite3

- **Frontend:**
  - HTML5
  - Bootstrap 5
  - JavaScript

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/create/` | List all destinations / Create new destination |
| GET | `/api/retrieve/<int:pk>/` | Retrieve specific destination |
| PUT | `/api/update/<int:pk>/` | Update specific destination |
| DELETE | `/api/delete/<int:pk>/` | Delete specific destination |
| GET | `/api/search/<str:search>/` | Search destinations |
 
