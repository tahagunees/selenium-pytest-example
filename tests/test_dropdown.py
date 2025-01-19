import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
##OK
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

def test_categories_button(driver):
    """Kategoriler butonunun varlığını ve tıklanabilirliğini test eder."""
    logger.info("Kategoriler butonu testi başlatıldı.")
    
    try:
        # Kategoriler butonunu bul
        categories_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="category-dropdown"]'))
        )
        
        # Butonun görünür olduğunu kontrol et
        assert categories_button.is_displayed(), "Kategoriler butonu görünür değil!"
        logger.info("Kategoriler butonu görünür.")

        # Butona tıkla
        categories_button.click()
        logger.info("Kategoriler butonuna tıklandı.")

        time.sleep(2)  # Tıklama sonrası bekleme süresi

        # Butonun durumu kontrol edilebilir (örneğin, açılıp açılmadığını kontrol etmek için)
        assert categories_button.get_attribute("aria-expanded") == "true", "Kategoriler menüsü açılmadı!"
        logger.info("Kategoriler menüsü başarıyla açıldı.")

    except Exception as e:
        logger.error(f"Kategoriler butonu testi sırasında hata oluştu: {e}")
        raise e