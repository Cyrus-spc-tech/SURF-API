# Simple Social API

A FastAPI-based social media backend with Streamlit frontend for sharing photos and videos.

## Features

- **User Authentication**: Register, login, and JWT-based authentication
- **File Upload**: Upload photos and videos with ImageKit integration
- **Feed**: View posts from all users in chronological order
- **User Management**: Delete own posts, view user profiles
- **Modern UI**: Clean Streamlit frontend with responsive design

## Tech Stack

### Backend

- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: Async ORM with SQLite database
- **FastAPI Users**: User authentication and management
- **ImageKit**: Cloud image/video storage and transformation
- **Pydantic**: Data validation and serialization

### Frontend

- **Streamlit**: Python web app framework
- **Requests**: HTTP client for API communication

## Setup

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd connect_tg
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install fastapi uvicorn streamlit requests fastapi-users sqlalchemy aiosqlite python-dotenv imagekitio
```

3. **Environment Variables**
   Create a `.env` file in the project root:

```env
IMAGEKIT_PRIVATE_KEY=your_private_key
IMAGEKIT_PUBLIC_KEY=your_public_key
IMAGEKIT_URL=your_url_endpoint
```

Get these credentials from [ImageKit Dashboard](https://imagekit.io/dashboard).

## Running the Application

### Start Backend Server

```bash
cd connect_tg
python main.py
```

The API will be available at `http://localhost:8000`

### Start Frontend (in separate terminal)

```bash
cd connect_tg
streamlit run frontend.py
```

The frontend will be available at `http://localhost:8501`

## API Endpoints

### Authentication

- `POST /auth/register` - Register new user
- `POST /auth/jwt/login` - Login and get JWT token
- `GET /users/me` - Get current user info

### Posts

- `POST /upload` - Upload file with caption (requires auth)
- `GET /feed` - Get all posts (requires auth)
- `DELETE /posts/{post_id}` - Delete post (requires auth, owner only)

## Database Schema

### Users Table

- `id` (UUID) - Primary key
- `email` (String) - User email
- `hashed_password` (String) - Encrypted password
- `is_active` (Boolean) - Account status
- FastAPI Users fields for verification, etc.

### Posts Table

- `id` (String) - Primary key (UUID)
- `user_id` (String) - Foreign key to users
- `caption` (Text) - Post description
- `url` (String) - ImageKit URL
- `file_type` (String) - 'image' or 'video'
- `file_name` (String) - Original filename
- `created_at` (DateTime) - Timestamp

## Project Structure

```
connect_tg/
├── app/
│   ├── __init__.py
│   ├── app.py          # Main FastAPI application
│   ├── db.py           # Database models and connection
│   ├── user.py         # User authentication setup
│   ├── schemas.py      # Pydantic models
│   └── images.py       # ImageKit configuration
├── frontend.py        # Streamlit frontend
├── main.py           # Application entry point
├── .env             # Environment variables
└── README.md         # This file
```

## Usage

1. **Register Account**: Open frontend, enter email and password, click "Sign Up"
2. **Login**: Use same credentials to login
3. **Upload Content**:
   - Click "Upload" in sidebar
   - Choose image/video file
   - Add caption
   - Click "Share"
4. **View Feed**: Posts appear in chronological order on main page
5. **Delete Posts**: Click trash icon on your own posts

## Development

### Adding New Features

- **New endpoints**: Add to `app/app.py`
- **Database models**: Modify `app/db.py`
- **Frontend pages**: Add functions to `frontend.py`
- **Authentication**: Extend `app/user.py`

### Database Migrations

The app uses SQLAlchemy auto-creation. For production, consider Alembic migrations.

## Deployment

### Backend (FastAPI)

```bash
uvicorn app.app:app --host 0.0.0.0 --port 8000
```

### Frontend (Streamlit)

```bash
streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0
```

### Environment Variables in Production

Set environment variables instead of using `.env` file for production deployments.

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
2. **Database Issues**: Delete `test.db` to reset
3. **ImageKit Errors**: Check `.env` credentials
4. **Port Conflicts**: Change ports in `main.py` or frontend

### Logs

- Backend: Check terminal output for FastAPI logs
- Frontend: Streamlit shows errors in the browser console

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Submit pull request

## Support

For issues and questions:

- Check the troubleshooting section
- Review the code comments
- Open an issue on the repository
