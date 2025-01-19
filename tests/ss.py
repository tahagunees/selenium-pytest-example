import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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

def test_scroll_and_take_screenshots(driver):
    """Sayfayı kaydırarak ekran görüntülerini alır ve kaydeder."""
    logger.info("Scroll ve ekran görüntüsü alma testi başlatıldı.")
    
    # Sayfanın tamamen yüklenmesini bekle
    time.sleep(2)  # Gerekirse bekleme süresi ekleyin

    # Sayfanın yüksekliğini al
    total_height = driver.execute_script("return document.body.scrollHeight")
    logger.info(f"Sayfanın toplam yüksekliği: {total_height}")

    # Ekran görüntülerini almak için kaydırma işlemi
    for i in range(0, total_height, 800):  # Her seferinde 800 piksel kaydır
        driver.execute_script(f"window.scrollTo(0, {i});")
        time.sleep(2)  # Kaydırma sonrası bekleme süresi

        # Ekran görüntüsünü al
        screenshot_path = os.path.join(os.path.dirname(__file__), f'screenshot_{i}.png')
        driver.save_screenshot(screenshot_path)
        logger.info(f"Ekran görüntüsü alındı ve {screenshot_path} konumuna kaydedildi.")

    logger.info("Tüm ekran görüntüleri alındı.")