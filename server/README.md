
## Installation

1. Clone the repository
2. Create a virtual environment and install the dependencies
- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add the following variables:
- `SECRET_KEY`: A secret key for the server
- `DATABASE_URL`: The URL for the database
- `DATABASE_NAME`: The name of the database
- `DATABASE_USER`: The username for the database
- `DATABASE_PASSWORD`: The password for the database
- `DATABASE_HOST`: The host for the database
- `DATABASE_PORT`: The port for the database
4. Create database & tables
- Connect to the database and run the following SQL script:
  - `CREATE DATABASE <DATABASE_NAME>;`
- Run the following command to create the tables:
  - `alembic upgrade head`
5. Run the server
- `uvicorn app.main:app --reload`
