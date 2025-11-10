# Fresh Harvest Liberia

A Django web application for Fresh Harvest Liberia - an e-commerce platform for fresh food and produce.

## Features

- User authentication (login/register)
- Product catalog and browsing
- Product details view
- Shopping cart functionality
- Checkout process
- Contact page
- Responsive design with Bootstrap

## Project Structure

```
freshfood_harvest/
├── freshfood_harvest/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── freshharvest_webapp/        # Main application
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── static/                 # Static files (CSS, JS, images)
│   └── templates/              # HTML templates
├── db.sqlite3                  # SQLite database
└── manage.py                   # Django management script
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MorganTheTechEthusiast/Fresh_Harvest_Liberia.git
   cd freshfood_harvest
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   - Copy `.env.example` to `.env`:
     ```bash
     copy .env.example .env  # Windows
     # or
     cp .env.example .env    # macOS/Linux
     ```
   - Update the `.env` file with your configuration (SECRET_KEY, DATABASE_URL, etc.)

6. Run migrations:
   ```bash
   python manage.py migrate
   ```

7. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

8. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

9. Run the development server:
   ```bash
   python manage.py runserver
   ```

10. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

- Browse products at `/products/`
- View product details
- Add items to cart
- Proceed to checkout
- Contact the business via the contact form

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Bootstrap 5
- **JavaScript Libraries**: 
  - Owl Carousel
  - Lightbox
  - WayPoints
  - Easing
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Dependencies**:
  - python-decouple (environment variable management)
  - dj-database-url (database configuration)
  - pillow (image processing)
  - whitenoise (static file serving)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is proprietary software for Fresh Harvest Liberia.

## Contact

For any inquiries, please use the contact form on the website or reach out through the repository.
