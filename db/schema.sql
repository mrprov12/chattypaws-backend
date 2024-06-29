CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL
);

CREATE TABLE stream_credentials (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    stream_type VARCHAR(50) NOT NULL, -- 'rtsp' or 'onvif'
    url VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
