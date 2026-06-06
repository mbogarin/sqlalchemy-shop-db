# Relational Database Management with SQLAlchemy

## Project Description

This project demonstrates how to build and manage a relational database using Python and SQLAlchemy ORM. The application models a simple shop database consisting of users, products, and orders while establishing relationships between tables through foreign keys.

The project showcases core database operations including creating tables, inserting data, querying records, updating existing data, and deleting records. It also includes bonus functionality such as tracking order shipment status and generating order statistics.

### Why These Technologies?

- Python provides a clean and readable syntax for database applications.
- SQLAlchemy ORM simplifies database interactions by allowing Python classes to represent database tables.
- SQLite offers a lightweight database solution that requires no separate database server configuration.

### Challenges Faced

- Understanding one-to-many relationships between users and orders
- Implementing foreign key relationships correctly
- Navigating related data through SQLAlchemy relationships
- Managing delete operations while maintaining referential integrity
- Writing efficient queries using SQLAlchemy ORM syntax

### Future Improvements

- Add a command-line interface (CLI) for user interaction
- Implement product inventory tracking
- Add order totals and sales reporting
- Create customer search and filtering functionality
- Migrate to MySQL or PostgreSQL for larger-scale applications

---

## Table of Contents

- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Database Structure](#database-structure)
- [Features](#features)
- [Project Structure](#project-structure)
- [Roadmap](#roadmap)
- [Collaborators](#collaborators)
- [Credits](#credits)

---

## Installation & Setup

### Prerequisites

- Python 3.x
- SQLAlchemy

### Clone the Repository

```bash
git clone https://github.com/mbogarin/rb-sqlalchemy.git cd rb-sqlalchemy
```

### Create and Activate a Virtual Environment (Optional)

```bash
python -m venv venv
```

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install SQLAlchemy
```

### Run the Application

```bash
python shop-db.py
```

Running the script will:

- Create the SQLite database (shop.db)
- Create all database tables
- Insert sample users, products, and orders
- Execute CRUD operations
- Display query results in the terminal
- Demonstrate update and delete functionality

---

## Usage

This project is a demonstration script and does not require user input.

When executed, the script automatically:

1. Creates the database and tables
2. Inserts sample users, products, and orders
3. Displays all users
4. Displays all products
5. Displays all orders with related user and product information
6. Queries and displays unshipped orders
7. Counts the total number of orders per user
8. Updates a product price
9. Deletes a user and their associated orders

The results are displayed directly in the terminal.

---

## Database Structure

### Users Table

| Column | Type                  |
| ------ | --------------------- |
| id     | Integer (Primary Key) |
| name   | String                |
| email  | String (Unique)       |

### Products Table

| Column | Type                  |
| ------ | --------------------- |
| id     | Integer (Primary Key) |
| name   | String                |
| price  | Integer               |

### Orders Table

| Column     | Type                  |
| ---------- | --------------------- |
| id         | Integer (Primary Key) |
| user_id    | Foreign Key           |
| product_id | Foreign Key           |
| quantity   | Integer               |
| shipped    | Boolean               |

### Relationships

- One User can have many Orders
- One Product can appear in many Orders
- Each Order belongs to one User and one Product

---

## Features

### Core Assignment Features

- SQLAlchemy ORM models
- Table relationships
- SQLite database integration
- Data insertion
- Data retrieval queries
- Update operations
- Delete operations

### Bonus Features Implemented

- Order shipment status tracking
- Query for unshipped orders
- Count total orders per user

---

## Project Structure

```bash
rb-sqlalchemy/
│
├── shop-db.py
├── shop.db
├── README.md
└── .gitignore
```

---

## Roadmap

- Add inventory quantities to products
- Add customer order history reports
- Add filtering and sorting queries
- Add CLI-based user interaction
- Expand reporting capabilities

---

## Collaborators

Currently this project was developed independently.

Future collaborators can be listed here:

---

## Credits

Classmates and mentors at Coding Temple
