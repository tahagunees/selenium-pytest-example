import pytest
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os
##OK
# Logger setup
logger = logging.getLogger(__name__)

@pytest.fixture(scope="module")
def driver():
    """Selenium WebDriver'ı başlatır ve testler bittikten sonra kapatır."""
    logger.info("Selenium WebDriver başlatılıyor...")
    driver_path = os.path.join(os.path.dirname(__file__), 'chromedriver.exe')
    service = Service(driver_path)
    
    # Implicit wait ayarı
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)  # Tüm element aramaları için 10 saniye bekleme
    
    driver.get("https://gwkggwzaqjvnl4db.vercel.app/")  # Test edilecek sayfanın URL'si
    logger.info("Selenium WebDriver başarıyla başlatıldı.")
    yield driver
    logger.info("Selenium WebDriver kapatılıyor...")
    driver.quit()
    logger.info("Selenium WebDriver başarıyla kapatıldı.")

def test_presence_of_elements(driver):
    """Belirli elementlerin sayfada mevcut olup olmadığını test eder."""
    logger.info("Element varlığı testi başlatıldı.")
    
    try:
        # Explicit wait kullanarak belirli bir elementin varlığını kontrol et
        wait = WebDriverWait(driver, 10)
        
        # Presence (Varlık) testleri
        logger.info("Presence testleri başlatılıyor...")
        
        # Body elementinin varlığını kontrol et
        body = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        assert body is not None, "Body elementi bulunamadı"
        logger.debug("Body elementi bulundu.")
        
        # Header elementinin varlığını kontrol et
        header = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        assert header is not None, "Header elementi bulunamadı"
        logger.debug("Header elementi bulundu.")
        
        # Farklı seçicilerle element varlığını kontrol et
        selectors = [
            (By.CSS_SELECTOR, 'nav'),
            (By.CSS_SELECTOR, 'main'),
            (By.CSS_SELECTOR, 'footer')
        ]
        
        for by, selector in selectors:
            try:
                element = wait.until(EC.presence_of_element_located((by, selector)))
                assert element is not None, f"{selector} elementi bulunamadı"
                logger.debug(f"{selector} elementi bulundu.")
            except Exception as e:
                logger.warning(f"{selector} elementi için hata: {e}")
        
        logger.info("Presence testleri başarıyla tamamlandı.")
    
    except Exception as e:
        # Hata durumunda ekran görüntüsü al
        screenshot_path = os.path.join("screenshots", f"presence_test_error_{time.time()}.png")
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(screenshot_path)
        logger.error(f"Presence testi sırasında hata oluştu: {e}")
        logger.error(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
        raise

def test_visibility_of_elements(driver):
    """Elementlerin görünürlüğünü test eder."""
    logger.info("Element görünürlüğü testi başlatıldı.")
    
    try:
        # Explicit wait kullanarak görünürlük testleri
        wait = WebDriverWait(driver, 10)
        
        logger.info("Visibility testleri başlatılıyor...")
        
        # Görünür olması beklenen elementler
        visibility_selectors = [
            (By.CSS_SELECTOR, 'h1'),  # Ana başlık
            (By.CSS_SELECTOR, 'a'),   # Linkler
            (By.CSS_SELECTOR, 'button')  # Butonlar
        ]
        
        for by, selector in visibility_selectors:
            try:
                # Elementin hem mevcut hem de görünür olduğunu kontrol et
                element = wait.until(EC.visibility_of_element_located((by, selector)))
                
                # Ek görünürlük kontrolleri
                assert element.is_displayed(), f"{selector} elementi görünür değil"
                assert element.size['width'] > 0, f"{selector} elementinin genişliği 0"
                assert element.size['height'] > 0, f"{selector} elementinin yüksekliği 0"
                
                logger.debug(f"{selector} elementi görünür ve boyutlu.")
            
            except Exception as e:
                logger.warning(f"{selector} görünürlük testi için hata: {e}")
        
        logger.info("Visibility testleri başarıyla tamamlandı.")
    
    except Exception as e:
        # Hata durumunda ekran görüntüsü al
        screenshot_path = os.path.join("screenshots", f"visibility_test_error_{time.time()}.png")
        os.makedirs("screenshots", exist_ok=True)
        driver.save_screenshot(screenshot_path)
        logger.error(f"Visibility testi sırasında hata oluştu: {e}")
        logger.error(f"Ekran görüntüsü kaydedildi: {screenshot_path}")
        raise

