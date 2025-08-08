# Order Management App

This is a simple order management application built with Flask and SQLAlchemy. It provides a RESTful API for managing orders.

## Features

- Create new orders
- Retrieve all orders
- Retrieve a specific order by ID
- Update existing orders
- Delete orders

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

The application will start running on `http://127.0.0.1:5000/`.

## API Endpoints

- `POST /orders`: Create a new order
- `GET /orders`: Retrieve all orders
- `GET /orders/<id>`: Retrieve a specific order
- `PUT /orders/<id>`: Update an existing order
- `DELETE /orders/<id>`: Delete an order

## Running Tests

To run the unit tests:

```
python -m unittest test_app.py
```

## License

This project is licensed under the terms of the LICENSE file included in the repository.