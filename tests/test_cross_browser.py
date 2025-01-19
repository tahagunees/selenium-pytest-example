import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
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

@pytest.fixture(params=["chrome", "edge"])
def driver(request):
    """Farklı tarayıcılarda Selenium WebDriver'ı başlatır ve testler bittikten sonra kapatır."""
    browser = request.param
    logger.info(f"{browser.capitalize()} tarayıcısı başlatılıyor...")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        # Headless modda çalıştırmak için aşağıdaki satırı açabilirsiniz
        # options.add_argument("--headless")
        service = ChromeService(executable_path=os.path.join(os.path.dirname(__file__), 'chromedriver.exe'))
        driver = webdriver.Chrome(service=service, options=options)

    

    elif browser == "edge":
        options = webdriver.EdgeOptions()
        # Headless modda çalıştırmak için aşağıdaki satırı açabilirsiniz
        # options.add_argument("--headless")
        service = EdgeService(executable_path=os.path.join(os.path.dirname(__file__), 'msedgedriver.exe'))
        driver = webdriver.Edge(service=service, options=options)
    time.sleep(2)
    driver.get("https://gwkggwzaqjvnl4db.vercel.app/")  # Test edilecek sayfanın URL'si
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    logger.info(f"{browser.capitalize()} tarayıcısı başarıyla başlatıldı.")
    yield driver
    logger.info(f"{browser.capitalize()} tarayıcısı kapatılıyor...")
    driver.quit()
    logger.info(f"{browser.capitalize()} tarayıcısı başarıyla kapatıldı.")
    
def test_title(driver):
    """Web sayfasının başlığını kontrol eder."""
    logger.info("Web sayfası başlığı testi başlatıldı.")
    try:
        assert "BalıkPro - Premium Balık Avı Ekipmanları" in driver.title, "Başlık beklenen ile eşleşmiyor!"
        logger.info("Web sayfası başlığı başarıyla doğrulandı.")
    except Exception as e:
        logger.error(f"Test sırasında hata oluştu: {e}")
        raise e

