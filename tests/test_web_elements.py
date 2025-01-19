import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Logger oluştur
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Log dosyası oluştur
log_file = "test_log.log"
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.DEBUG)

# Log formatı oluştur
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Logger'a file handler ekle
logger.addHandler(file_handler)

@pytest.fixture(scope="module")
def driver():
    """Selenium WebDriver'ı başlatır ve testler bittikten sonra kapatır."""
    logger.info("Selenium WebDriver başlatılıyor...")
    driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("https://gwkggwzaqjvnl4db.vercel.app/")  # Test edilecek sayfanın URL'si
    yield driver
    logger.info("Selenium WebDriver kapatılıyor...")
    driver.quit()
    logger.info("Selenium WebDriver başarıyla kapatıldı.")

def test_button_clicks(driver):
    """Butonlara sırayla tıklama işlemini test eder."""
    logger.info("Butonlara tıklama testi başlatıldı.")
    
    try:
        # Artı butonuna tıkla
        plus_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button:has(svg.lucide-plus)'))
        )
        plus_button.click()
        logger.info("Artı butonuna tıklandı.")
        time.sleep(2)  # Tıklama sonrası bekleme süresi

        # Sepete Ekle butonuna tıkla
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.bg-primary'))
        )
        add_to_cart_button.click()
        logger.info("Sepete Ekle butonuna tıklandı.")
        time.sleep(2)  # Tıklama sonrası bekleme süresi

        # Alışveriş Sepeti butonuna tıkla
        cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button:has(svg.lucide-shopping-cart)'))
        )
        cart_button.click()
        logger.info("Alışveriş Sepeti butonuna tıklandı.")
        time.sleep(5)  # Tıklama sonrası bekleme süresi

    except Exception as e:
        logger.error(f"Butonlara tıklama testi sırasında hata oluştu: {e}")
        raise e