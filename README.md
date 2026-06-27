# Easy Port Scanner

Basit seviyede Python ile yazılmış port tarayıcı örnekleri. Bu depo, farklı yaklaşımlarla yazılmış TCP port tarama scriptlerini içerir.

> ⚠️ **Yasal uyarı:** Bu araçları yalnızca sahibi olduğunuz veya açık izne sahip olduğunuz sistemlerde kullanın.

## Repo Özeti

Bu depoda 3 adet temel tarayıcı scripti bulunuyor:

- `good_scanner.py` → IPv4 için başlangıç seviyesi port tarayıcı
- `best-scanner.py` → Daha görsel çıktı ve banner denemesi yapan IPv4 tarayıcı
- `ip6.scanner6.py` → IPv6 hedefleri için tarayıcı + port 80 için HTTP header denemesi

Dil dağılımı: **%100 Python**

## Dosya Analizi

### 1) `good_scanner.py`

- `socket.AF_INET` + `SOCK_STREAM` ile TCP bağlantı kontrolü yapar.
- Kullanıcıdan IP, başlangıç portu, bitiş portu alır.
- `connect_ex` sonucu `0` ise portu açık kabul eder.
- Her port için açık/kapalı bilgisi yazdırır.

**Artıları:**
- Basit ve öğrenmesi kolay
- Yeni başlayanlar için anlaşılır akış

**Eksileri / İyileştirme alanları:**
- Domain çözümleme, input doğrulama ve hata yönetimi sınırlı
- Tüm portlarda çıktı üretmek çok uzun olabilir

---

### 2) `best-scanner.py`

- `good_scanner.py` üzerine daha zengin çıktı ekler.
- Açık portlarda `recv(1024)` ile banner okumayı dener.
- Her port denemesi arasında rastgele bekleme (`time.sleep(random.randint(1,4))`) uygular.

**Artıları:**
- Banner alma denemesi ile servis hakkında ek bilgi sağlar
- Daha okunabilir çıktı formatı

**Dikkat edilmesi gerekenler:**
- Banner her zaman gelmez; `recv` bloklayabilir veya boş dönebilir
- Rastgele bekleme taramayı ciddi yavaşlatır

---

### 3) `ip6.scanner6.py`

- `socket.AF_INET6` ile IPv6 TCP taraması yapar.
- Açık portta banner denemesi yapar.
- Port `80` açıksa `requests` ile HTTP isteği atıp header bilgilerini yazdırmayı dener.
- IPv6 URL formatı için köşeli parantez kullanımı (`http://[ipv6]`) düşünülmüş.

**Artıları:**
- IPv6 desteği eklenmiş
- Sadece socket değil HTTP seviyesinde de ek kontrol yapıyor

**Dikkat edilmesi gerekenler:**
- `requests` bağımlılığı gerekir (`pip install requests`)
- Port 443 için HTTPS kontrolü bulunmuyor

## Kurulum

### Gereksinimler

- Python 3.8+
- (Opsiyonel ama `ip6.scanner6.py` için gerekli) `requests`

```bash
pip install requests
```

## Kullanım

### `good_scanner.py`

```bash
python good_scanner.py
```

### `best-scanner.py`

```bash
python best-scanner.py
```

### `ip6.scanner6.py`

```bash
python ip6.scanner6.py
```

Script çalışınca senden hedef adres ve port aralığını ister.

## Önemli Notlar

- Çok geniş port aralığı (örn. `1-65535`) uzun sürebilir.
- Düşük timeout daha hızlı fakat hatalı negatif sonuçlara neden olabilir.
- Banner bilgisi her serviste dönmez.
- Güvenlik araçlarını etik ve yasal sınırlar içinde kullan.

## Geliştirme Önerileri

İstersen bir sonraki adımda şu iyileştirmeler eklenebilir:

1. **CLI argümanları** (`argparse`) ile interaktif input’u azaltmak
2. **Threading/async** ile daha hızlı tarama
3. **Servis adı çözümleme** (`socket.getservbyport`) ve daha temiz rapor
4. **JSON/CSV çıktı**
5. **IPv4 + IPv6 birleşik tek script**
6. **HTTPS (443) için SSL/TLS banner veya sertifika bilgisi**

---

Geri bildirim verirsen README’yi Türkçe + İngilizce çift dilli versiyona da çevirebilirim.