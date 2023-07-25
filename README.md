# Wagtail Clear Cache

Let your clients clear template caching with the click of a button.

This package will add a "clear cache" option to the Admin/Site Settings panel

## Installation

1. `pip install wagtail-clear-cache`
2. Add `wagtail_clear_cache` to your `INSTALLED_APPS`

## Usage

Open your Wagtail Admin, go into "Settings", and you'll see "Clear Cache" as an option.

## Developer Installation

1. Clone this repo
2. Create a virtualenv
3. `pip install -e '.[develop]'`
4. Run `make init-testapp` to initialise the test app
5. Run `make server` to start the test app
6. Open your browser `http://localhost:8000/admin/`
7. Login with username `test` and password `test`
8. Go to "Settings" and you'll see "Clear Cache" as an option.

### Formatting and Linting

You can run `make lint` to format and lint all files.

## Compatibility

This package has been tested with the following versions of Wagtail:

- Wagtail 4.1+
- Python 3.8+
- Django 3.2+

## Todos

[ ] Add cache busting for Redis
