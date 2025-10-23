# Development

## Project Structure

- `app.py`: Main Flask application.
- `requirements.txt`: Python dependencies (create if missing).

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install flask
```

## Testing

You can test endpoints using `curl` or Postman:

```bash
curl http://localhost:5000/api/v1/healthz
curl http://localhost:5000/api/v1/details
```

## Deployment

For production, consider using a WSGI server like Gunicorn.

```bash
pip install gunicorn
gunicorn app:app
```