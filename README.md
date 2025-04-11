# Ask Azra

A Quora-inspired question and answer platform built with Django. Ask, answer, and connect!

## Overview

Ask Azra is a web application that allows users to ask questions, provide answers, and engage with a community of knowledge-sharing individuals. The platform is designed to be intuitive, responsive, and feature-rich, providing a seamless experience for users seeking information or wanting to share their expertise.

## Features

### Current Features

- **User Authentication**
  - Register with username, email, and password
  - Login/logout functionality
  - User profiles with question and answer history

- **Question Management**
  - Ask questions with rich text formatting
  - Edit and delete your own questions
  - View all questions on the home page with pagination

- **Answer System**
  - Post answers to questions with rich text formatting
  - Edit and delete your own answers
  - Like/unlike answers to show appreciation

- **Rich Text Editing**
  - CKEditor integration for formatting text
  - Support for images, links, and other media in questions and answers

- **Responsive Design**
  - Bootstrap-based UI that works on mobile, tablet, and desktop
  - Clean and intuitive interface

### Features To Be Added
- **Enhanced UI**
  - Improve the visual appeal of the platform
  - Add animations and transitions for a more engaging experience

- **Search Functionality**
  - Search for questions by keywords
  - Filter questions by categories or tags

- **Notifications**
  - Get notified when someone answers your question
  - Receive notifications for likes on your answers

- **User Reputation System**
  - Earn points for quality contributions
  - Unlock privileges based on reputation

- **Categories and Tags**
  - Organize questions by categories
  - Add tags to questions for better discoverability

- **Comments on Answers**
  - Allow discussions on individual answers
  - Nested comments for threaded conversations

- **Bookmark Questions**
  - Save interesting questions for later reference
  - Manage bookmarks in user profile


## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ask_azra.git
   cd ask_azra
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
   ```bash
   pip install poetry
   ```
   ```bash
   poetry install
   ```
4. Create Superuser:
   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the application in your browser at http://localhost:8000

## LICENSE
This project is licensed under the MIT License.