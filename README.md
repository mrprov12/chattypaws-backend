# ChattyPaws Backend

This repository contains the backend for ChattyPaws, including the image processing package and other backend functionalities.

## Project Structure

- `db/` - Database schema files
- `env/` - Virtual environment directory.
- `scripts/` - Directory containing utility scripts.
  - `reset_db.sh` - Script to reset the database.
- `src/` - Source code for the package.
  - `image-processing-package/` - Directory containing the image processing package.
  - `repo/` - SQL adapter
  - `tests/` - Test files for the package.
- `docker-compose.yml` - Docker Compose configuration file
- `requirements.txt` - List of dependencies.
- `README.md` - This file.

## Setting Up

1. Clone the repository:

```sh
   git clone https://github.com/yourusername/chattypaws-backend.git
   cd chattypaws-backend
```

2. Navigate to the project directory:

```sh
   cd chattypaws-backend
```

3. Set up the virtual environment:

```sh
   python3 -m venv env
```

4. Activate the virtual environment:

```sh
   source env/bin/activate  # On Windows: env\Scripts\activate
```

5. Install dependencies:

```sh
   make update_requirements
```

6. Setup docker-compose.yml
   Ensure you have a docker-compose.yml file configured for PostgreSQL. Here’s an example:

```sh
version: '3.8'

services:
  db:
    image: postgres:latest
    container_name: chattypaws_db
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    ports:
      - "${DB_PORT}:${DB_PORT}"
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:

```

7. Start the Docker container with:

```sh
   docker-compose up -d
```

8. Setup PostgreSQL container:
   For initial setup:

```sh
# Connect to the database:
docker exec -it chattypaws_db psql -U ${DB_USER} -d ${DB_NAME}

# Create the database
docker exec -it $DB_CONTAINER_NAME psql -U $DB_USERNAME -d postgres -c "CREATE DATABASE $DB_DATABASE_NAME;"

# Load the database schema:
cat ${SCHEMA_FILE} | docker exec -i chattypaws_db psql -U ${DB_USER} -d ${DB_NAME}
```

To reset the database (drop, create, import):

```sh
make reset_db
```

### Environment Variables

The `chattypaws-backend` project uses environment variables for configuration. Below is the format of the required environment variables in `.env`, `.env.test`, `.env.prod` (using local as example):

```plaintext
FLASK_ENV=development
SECRET_KEY=your_secret_key

# SQL credentials
DB_HOST=localhost
DB_PORT=5432
DB_NAME=chattypaws_backend_db
DB_USER=admin
DB_PASSWORD=your_database_password
SCHEMA_FILE=./db/schema.sql

# Stream credentials
RTSP_URL=your_rtsp_url
STREAM_USERNAME=your_stream_username
STREAM_PASSWORD=your_stream_password

# ONVIF Credentials
ONVIF_IP=your_onvif_ip
ONVIF_PORT=your_onvif_port
ONVIF_USERNAME=your_onvif_username
ONVIF_PASSWORD=your_onvif_password

# Application settings
APP_HOST=localhost
APP_PORT=5000
```

## Set Up

Ensure your .env file is properly configured with the necessary environment variables.

Setup app:

```sh

make init
```

Setup DB:

```sh
make init_db
```

Run the app:

```sh
python src/app.py  # This will initialize the database and start the server

#OR

make run
```

Clean up:

```sh
# Clean the environment (remove virtual environment)
clean:
	rm -rf env

# Reset the database
reset_db:
	./scripts/reset_db.sh
```

The server should now be running and accessible at http://<APP_HOST>:<APP_PORT>.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

# ChattyPaws Backend

This repository contains the backend code for ChattyPaws, an interactive pet button interpreter system. The ChattyPaws Backend handles video processing, object detection, database integration, and provides API endpoints for the frontend applications.

## Key Features

- **Video Processing:** Capture and process video feeds from various cameras.
- **Object Detection:** Use machine learning to detect button presses and interactions.
- **Database Integration:** Store and manage interaction data in a PostgreSQL database.
- **API Endpoints:** Provide RESTful API endpoints for the frontend applications.
- **User Authentication:** Secure login using Google SSO (with plans to add Apple and Facebook SSO).

## API Endpoints

Use Swagger endpoint for easy interaction with endpoints: `${host}/swagger`

- **POST /user/login:** Login with local handling.
- **POST /user/register:** Register with local handling.
- **POST /image_processing/process:** Process video feed and store interactions (authentication required).
- **POST /image_processing/stream_integration:** Integrate a new camera feed stream (authentication required).
- **GET /user:** Get the current logged-in user.
- **GET /notification/user/{user_id}/stream/{stream_id}:** Get the history of notifications, with support for pagination in the future.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue or contact the project maintainer at meaganprovencher@gmail.com.
