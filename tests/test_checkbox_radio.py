import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    logger.info("Selenium WebDriver başarıyla başlatıldı.")
    yield driver
    logger.info("Selenium WebDriver kapatılıyor...")
    driver.quit()
    logger.info("Selenium WebDriver başarıyla kapatıldı.")

def test_checkbox_and_radio_buttons(driver):
    """Checkbox ve radio butonlarına tıklama işlemini test eder."""
    logger.info("Checkbox ve radio butonları testi başlatıldı.")
    try:
        # Checkbox'ları bul ve tıkla
        checkboxes = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='grid md:grid-cols-2 gap-8']//button[@role='checkbox']"))
        )
        
        for checkbox in checkboxes:
            checkbox.click()  # Checkbox'a tıkla
            logger.info(f"{checkbox.get_attribute('id')} checkbox'ına tıklandı.")
            time.sleep(2)  # 2 saniye bekleme süresi

        # Radio butonlarını bul ve tıkla
        radio_buttons = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@role='radiogroup']//button[@role='radio']"))
        )
        
        for radio_button in radio_buttons:
            radio_button.click()  # Radio butonuna tıkla
            logger.info(f"{radio_button.get_attribute('id')} radio butonuna tıklandı.")
            time.sleep(2)  # 2 saniye bekleme süresi

    except Exception as e:
        logger.error(f"Checkbox ve radio butonları testi sırasında hata oluştu: {e}")
        raise e