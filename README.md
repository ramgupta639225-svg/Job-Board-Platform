# Job Board Platform

A backend-focused Job Board Platform REST API developed using **Django** and **Django REST Framework** as part of the **CodeAlpha Internship**.

## 🎯 Project Overview

The Job Board Platform provides REST APIs for managing employers, candidates, job listings, and job applications.

The main purpose of this project is to create a backend system where employers can manage job opportunities and candidates can search for jobs, apply for suitable positions, upload resumes, and track their application status.

## 🚀 Features

- Employer management
- Candidate management
- Job listing and management
- Job search and filtering
- Job applications
- Resume upload
- Cover letter support
- Application status tracking
- Employer email notifications
- Application statistics
- User management API
- Django Admin Panel
- Database relationships between employers, jobs, candidates, and applications
- REST API testing using Postman

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Postman
- Git
- GitHub

## 📋 CodeAlpha Task Requirements

This project was developed according to the Job Board Platform task requirements:

- Set up a backend using Django.
- Create models for employers, candidates, jobs, and applications.
- Build REST API endpoints for job listings.
- Implement job searching and filtering.
- Allow candidates to apply for jobs.
- Support resume uploads.
- Track application status.
- Create relationships between employers, jobs, candidates, and applications.
- Send notifications to employers when candidates apply.
- Provide application statistics and basic user management.
- Test the APIs using Postman.

## 👥 Main Modules

### Employer

Employers can manage their company information and job listings.

Employer information includes:

- Company name
- Email
- Description
- Location
- Website

### Candidate

Candidates can store their profile information and apply for jobs.

Candidate information includes:

- Name
- Email
- Phone
- Skills
- Experience

### Jobs

Each job listing contains:

- Employer
- Job title
- Description
- Location
- Salary
- Job type
- Required experience
- Created date

Supported job types:

- Full Time
- Part Time
- Internship
- Remote

### Applications

Candidates can apply for jobs by submitting:

- Candidate information
- Job information
- Resume
- Cover letter
- Application status
- Application date

## 📊 Application Status

Applications can have the following statuses:

- Pending
- Reviewed
- Shortlisted
- Rejected
- Accepted

## 🔎 Job Search and Filtering

The Job API supports searching and filtering by:

- Job title or keyword
- Location
- Job type

Example:

GET /api/jobs/?search=Python
GET /api/jobs/?location=Delhi
GET /api/jobs/?job_type=Internship
