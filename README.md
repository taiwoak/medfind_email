# Medbuddy Email Automation Backend

This is a lightweight Django backend service that exposes an API endpoint (`/api/send-mail`) to trigger notification emails via the SMTP Email configuration.

---

## Features

- Accepts notification email data from frontend or API clients
- Sends email with the data using templates
- Simple error handling and response forwarding

---

## Tech Stack

- Python 3.x
- Django 4.x+
- Requests (for HTTP calls)
- Environment-based configuration using `.env`

---

## Installation

1. **Clone the project**

```bash
git clone https://github.com/taiwoak/medfind_email.git
cd medfind_email
```

2. **Set up a virtual environment**

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create .env file**

```bash
EMAIL_HOST_USER=email.com
EMAIL_HOST_PASSWORD=password
DEFAULT_FROM_EMAIL=MedFind
SECRET_KEY=your_secret_key
FRONTEND_URL=your_frontend_url
HOST=localhost or 127.0.0.1 or your_backend.com
```

## Running the Server

```bash
python manage.py runserver
```

Visit http://localhost:8000/api/send-mail (POST only).


## Testing with Postman

```bash
curl --location 'http://127.0.0.1:8000/api/send-mail' \
--header 'Content-Type: application/json' \
--data-raw '{
    "to": "dannyjanx@gmail.com",
    "from": "Medfind <taiwoakerele98@gmail.com>",
    "context": {
        "name": "All Smiles Dental",
        "address": "Oniru, Lekki, Victoria Island",
        "category": "Primary Health Center"
    },
    "template": "medfind_health_center_addition"
}'
```

## Author

Built by Taiwo Akerele

