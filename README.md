# ChattyPaws Backend

This repository contains the backend for ChattyPaws, including the image processing package and other backend functionalities.

## Project Structure

- `env/` - Virtual environment directory.
- `image-processing-package/` - Directory containing the image processing package.
  - `src/` - Source code for the package.
  - `tests/` - Test files for the package.
  - `setup.py` - Setup script for packaging.
  - `README.md` - Readme for the package.
- `requirements.txt` - List of dependencies.
- `README.md` - This file.

## Setting Up

1. Clone the repository:
   git clone https://github.com/yourusername/chattypaws-backend.git

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
       source env/bin/activate
   ```
5. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Environment Variables

The `chattypaws-backend` project uses environment variables for configuration. Below is the format of the required environment variables in `.env`, `.env.test`, `.env.prod`:

```plaintext
# SQL credentials
DATABASE_USERNAME=your_database_username
DATABASE_PASSWORD=your_database_password

# Stream credentials
RTSP_URL=your_rtsp_url
STREAM_USERNAME=your_stream_username
STREAM_PASSWORD=your_stream_password
```

## Usage

Navigate to the `image-processing-package` directory and follow the usage instructions in the package's `README.md`.

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

## Getting Started

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/chattypaws-backend.git
   cd chattypaws-backend
   ```

2. **Set up a virtual environment:**

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

4. **Set up PostgreSQL:**

   - Ensure PostgreSQL is installed and running.
   - Create a new database for the project:
     createdb chattypaws

5. **Set up environment variables:**

   - Create a `.env` file in the root directory and add the following environment variables:
     ```
     FLASK_ENV=development
     DATABASE_URL=postgresql://user:password@localhost/chattypaws
     SECRET_KEY=your_secret_key
     GOOGLE_CLIENT_ID=your_google_client_id
     GOOGLE_CLIENT_SECRET=your_google_client_secret
     ```

6. **Run the application:**
   ```
   python src/main.py
   ```

## API Endpoints

- **POST /login:** Login with Google SSO.
- **POST /process:** Process video feed and store interactions (authentication required).
- **POST /camera:** Integrate a new camera feed (authentication required).
- **GET /current_user:** Get the current logged-in user.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please open an issue or contact the project maintainer at meaganprovencher@gmail.com.
