import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(5)  # small implicit wait as a safety net
    yield drv
    drv.quit()


def test_login_page_loads(driver):
    driver.get(BASE_URL)
    assert "Sample PHP Login" in driver.title
    assert driver.find_element(By.ID, "username")
    assert driver.find_element(By.ID, "password")


def test_successful_login(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "login-btn").click()

    welcome = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "welcome-message"))
    )
    assert "Welcome, admin" in welcome.text


def test_failed_login_shows_error(driver):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("wrongpassword")
    driver.find_element(By.ID, "login-btn").click()

    error = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "error-message"))
    )
    assert "Invalid username or password" in error.text