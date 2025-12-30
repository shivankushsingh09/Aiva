# Aiva - AI Chatbot

A modern, web-based AI chatbot built with Python Flask and Bootstrap 5.

## Features

- 🤖 Intelligent conversation capabilities
- 🎨 Modern, responsive UI with Bootstrap 5
- ⚡ Real-time messaging with typing indicators
- 🐳 Docker support for easy deployment
- 📱 Mobile-friendly design
- 🔒 Secure containerized deployment

## Quick Start

### Option 1: Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser and go to `http://localhost:5000`

### Option 2: Docker Deployment

#### Using Docker Compose (Recommended)

1. Build and run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

2. Access the chatbot at `http://localhost:5000`

#### Using Docker directly

1. Build the image:
   ```bash
   docker build -t aiva-chatbot .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 aiva-chatbot
   ```

3. Access the chatbot at `http://localhost:5000`

## Chatbot Capabilities

Aiva can handle various types of conversations:

- **Greetings**: Hello, hi, hey, greetings
- **Farewells**: Bye, goodbye, see you
- **Time/Date**: Current time and date inquiries
- **Personal Info**: Name, abilities, help requests
- **General Chat**: Contextual responses for various topics

## Project Structure

```
Aiva/
├── app.py                 # Flask application and chatbot logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend HTML with Bootstrap
├── Dockerfile            # Docker configuration
├── docker-compose.yml    # Docker Compose configuration
├── .dockerignore         # Docker ignore file
└── README.md            # This file
```

## Environment Variables

- `FLASK_APP`: Application entry point (default: app.py)
- `FLASK_ENV`: Environment mode (development/production)

## API Endpoints

- `GET /`: Main chat interface
- `POST /chat`: Send message to chatbot
- `GET /api/health`: Health check endpoint

## Development

To extend Aiva's capabilities, modify the `AivaChatbot` class in `app.py`:

```python
# Add new response patterns
self.responses["new_pattern"] = ["Response 1", "Response 2"]

# Add new logic in get_response method
elif "keyword" in user_input:
    return random.choice(self.responses["new_pattern"])
```

## Docker Configuration

The Dockerfile includes:
- Python 3.12 slim base image
- Non-root user for security
- Health checks
- Optimized layer caching
- Production-ready configuration

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.
