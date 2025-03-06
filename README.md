# Online Soccer Manager (OSM) Reklam Scripti

Bu Python scripti, Selenium kullanarak Online Soccer Manager (OSM) web sitesinde reklamları otomatik olarak tıklayan ve boss coin kazandıran bottur.

## Gereksinimler

* Python 3.x
* Selenium kütüphanesi (`pip install selenium`)
* OSM hesabı

## Kurulum

1.  Python ve pip'in kurulu olduğundan emin olun.
2.  Selenium kütüphanesini kurun:

    ```bash
    pip install selenium
    ```

3.  Osm.py içinden `username` ve `password` değişkenlerini kendi OSM hesap bilgilerinizle güncelleyin.

    ```python
    username = "YourUserNameHere"
    password = "YourPasswordHere"
    ```

## Kullanım

1.  Scripti çalıştırın:

    ```bash
    python Osm.py
    ```

2.  Script, Chrome tarayıcısını açacak, OSM'ye giriş yapacak ve reklamları otomatik olarak tıklamaya başlayacaktır.Her izlediği reklam başına boss coin kazandıracaktır.

## İşleyiş

* Script, OSM'ye giriş yapar ve reklam izleme sayfasına gider.
* Bir döngü içinde, reklamı tıklamaya çalışır ve ardından "Reklamı Geç" butonunu bulup tıklamaya çalışır.
* Reklamın bitip bitmediğini kontrol eder.
* Her saatte bir sayfayı yeniler.
* Herhangi bir hata durumunda, hata mesajını yazdırır ve belirli bir süre bekler.

## Dikkat Edilmesi Gerekenler

* Web sitesinin yapısı değişirse, script çalışmayabilir. XPATH'lerin güncellenmesi gerekebilir.
* Hesabınızın güvenliği için, şifrenizi scriptte açık bir şekilde saklamamaya özen gösterin. Çevre değişkenleri veya güvenli bir yapılandırma dosyası kullanmayı düşünebilirsiniz.
* Çalıştırılan scriptin aşırı kullanımı, OSM tarafından hesabınızın askıya alınmasına veya yasaklanmasına neden olabilir. Scripti dikkatli ve sorumlu bir şekilde kullanın.