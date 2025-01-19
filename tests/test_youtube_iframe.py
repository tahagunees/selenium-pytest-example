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

def test_iframe_youtube(driver):
    """Iframe içindeki YouTube videosunun başlığını alır ve videoyu oynatır."""
    logger.info("Iframe içindeki YouTube videosu testi başlatıldı.")
    
    try:
        # Iframe'e geçiş yap
        iframe = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
        )
        driver.switch_to.frame(iframe)
        logger.info("Iframe'e geçiş yapıldı.")

        time.sleep(2)  # Iframe içeriğinin yüklenmesi için bekleme süresi

        # Video başlığını almak için JavaScript kullan
        title = driver.execute_script("return document.title;")
        logger.info(f"YouTube video başlığı: {title}")

        # Videoyu oynat
        play_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.ytp-large-play-button'))  # Oynatma butonunu bul
        )
        play_button.click()
        logger.info("YouTube videosu oynatıldı.")

        time.sleep(5)  # Videonun oynatılması için bekleme süresi

    except Exception as e:
        logger.error(f"Iframe içindeki YouTube videosu testi sırasında hata oluştu: {e}")
        raise e
    finally:
        # Ana sayfaya geri dön
        driver.switch_to.default_content()
        logger.info("Ana sayfaya geri dönüldü.")