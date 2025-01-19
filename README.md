# selenium-pytest-example
Bu repo, Yazılım testi dersi için geliştirmiş olduğum Selenium ve Pytest kullanılarak oluşturulmuş bir test otomasyon projesidir. Web uygulamalarının UI (Kullanıcı Arayüzü) testlerini gerçekleştirmek için hazırlanmıştır.
Selenium Pytest Örneği 🚀
Bu proje, Selenium ve Pytest kullanarak tarayıcı testlerini otomatikleştirmenizi sağlar. Farklı web elemanlarını test ederek, uygulamanızın doğru çalıştığını doğrulayabilirsiniz. İsterseniz çapraz tarayıcı testleri yapabilir, YouTube iframe'lerini kontrol edebilir ve daha fazlasını test edebilirsiniz! test edilen sitenin linki : https://gwkggwzaqjvnl4db.vercel.app/



🚀 İçerik:
Test Dosyaları:
test_checkbox_radio.py: Onay kutuları ve radyo butonlarını test eder.
test_cross_browser.py: Chrome ve Edge tarayıcıları üzerinde çapraz tarayıcı testi yapar.
test_dropdown.py: Açılır menü öğelerinin doğruluğunu kontrol eder.
test_header_elements.py: Sayfa başlık öğelerinin doğruluğunu test eder.
test_web_elements.py: Genel web öğelerini test eder.
test_youtube_iframe.py: YouTube iframe'lerini test eder.
Diğer Dosyalar:
chromedriver.exe: Chrome için WebDriver.
msedgedriver.exe: Microsoft Edge için WebDriver.
test_log.log: Testlerin log dosyası.
screenshot_0.png, screenshot_1600.png, screenshot_2400.png, screenshot_800.png: Çözünürlük farkı ile ekran görüntüleri.
ss.py: Yardımcı Python scripti.
💻 Gereksinimler:
Python 3.x
Selenium: Tarayıcı otomasyonu için.
Pytest: Testlerin yönetilmesi ve raporlanması için.
📦 Kurulum:
Bağımlılıkları yükleyin:

bash
Kopyala
pip install -r requirements.txt
WebDriver'ları indirin:

ChromeDriver
Edge WebDriver
Testleri çalıştırın:

bash
Kopyala
pytest
🛠 Proje Yapısı:
c






