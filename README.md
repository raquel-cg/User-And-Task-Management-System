# User and Task Management System
## Overview:
This project implements a Python-based task and user management system for a small business. It allows secure login, user registration (admin only), task creation, and task viewing. The program uses text files for persistent storage, applying **file handling**, **string manipulation**, **loops**, and **conditional logic** to manage and display information.

## Tools & Technologies Used:
- Python (file I/O, datetime, string methods, loops, conditionals)
- Text files (`user.txt`, `tasks.txt`)
- Command-Line Interface (CLI)

## Project Structure:
Part 1: User Login & Authentication  
Part 2: Register New Users (Admin only)  
Part 3: Add New Tasks  
Part 4: View All Tasks / View My Tasks  
Part 5: Display Statistics (Admin only) 

## Features
- Secure login system with validation against stored credentials  
- Admin-only user registration with password confirmation  
- Add tasks with automatic date assignment and completion status  
- View all tasks in a formatted layout  
- View only tasks assigned to the logged-in user  
- Admin statistics showing total tasks and total users

## Key Insights
- Implemented **persistent storage** through reading and writing to `.txt` files.  
- Designed a **menu-driven CLI** that adapts based on user role (`admin` vs regular user).  
- Applied **string manipulation** to format task details for clear display.  
- Used **loops** and **conditional logic** for input validation and user interaction flow.  
- Incorporated **date handling** to automatically assign the current date to new tasks.

