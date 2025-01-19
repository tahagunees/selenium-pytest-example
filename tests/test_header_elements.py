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

def test_search_bar(driver):
    """Arama çubuğuna 'spin olta' anahtar kelimesini yazar ve arama işlemini test eder."""
    logger.info("Arama çubuğu testi başlatıldı.")
    
    try:
        # Arama çubuğunu bul
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]'))
        )
        
        # Arama çubuğuna 'spin olta' yaz
        search_input.clear()  # Önce temizle
        search_input.send_keys("spin olta")
        logger.info("'spin olta' anahtar kelimesi arama çubuğuna yazıldı.")

        time.sleep(2)  # Gerekirse bekleme süresi ekleyin

        # İsteğe bağlı olarak, arama butonuna tıklama işlemi ekleyebilirsiniz
        # search_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')  # Arama butonunu bul
        # search_button.click()  # Arama butonuna tıkla
        # logger.info("Arama butonuna tıklandı.")

    except Exception as e:
        logger.error(f"Arama çubuğu testi sırasında hata oluştu: {e}")
        raise e