# PHP + Selenium + GitHub Actions Demo

A minimal PHP login page (`index.php`) with a Selenium test suite (`tests/test_login.py`)
that runs automatically in GitHub Actions on every push/PR.

## Run locally

1. Start the PHP app:
   ```bash
   php -S localhost:8000
   ```
2. In another terminal, install Python deps and run the tests:
   ```bash
   pip install -r requirements.txt
   BASE_URL=http://localhost:8000 pytest tests/ -v
   ```
   (Requires Chrome + a matching chromedriver on your machine, or use
   `webdriver-manager` to auto-manage the driver.)

## Run in CI

Push this repo to GitHub. The workflow at
`.github/workflows/selenium-tests.yml` will:
1. Spin up PHP's built-in server to host `index.php`.
2. Install Chrome + ChromeDriver.
3. Install Python + Selenium + pytest.
4. Run the 3 tests against the live PHP page (page load, successful login,
   failed login).

## Test credentials

- Username: `admin`
- Password: `password123`
