-- Users Table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Pets Table
CREATE TABLE pets (
    pet_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    breed VARCHAR(255),
    sex VARCHAR(10),
    photo_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Buttons Table
CREATE TABLE buttons (
    button_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    pet_id INTEGER,
    tile_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    position_x INTEGER,
    position_y INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
    FOREIGN KEY (tile_id) REFERENCES tiles(tile_id)
);

-- Tiles Table
CREATE TABLE tiles (
    tile_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Button Presses Table
CREATE TABLE button_presses (
    press_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    pet_id INTEGER NOT NULL,
    button_id INTEGER NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    confidence FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
    FOREIGN KEY (button_id) REFERENCES buttons(button_id)
);

-- Video Streams Table
CREATE TABLE video_streams (
    stream_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    url TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Session History Table
CREATE TABLE session_history (
    session_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Settings Table
CREATE TABLE settings (
    setting_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    setting_key VARCHAR(255) NOT NULL,
    setting_value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Notifications Table
CREATE TABLE notifications (
    notification_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    type VARCHAR(255),
    read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Stream Credentials Table
CREATE TABLE stream_credentials (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    stream_type VARCHAR(50) NOT NULL, -- 'rtsp' or 'onvif'
    url VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
