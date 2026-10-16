# Easy Port Scanner

Bu repo, Python öğrenirken geliştirdiğim basit siber güvenlik araçlarını içeriyor. Şu anki örneklerde port tarama, banner bilgisi alma ve kelime listesi oluşturma gibi konuları deniyorum.

Bu projeyi hazırlarken özellikle Python'da `socket`, listeler, döngüler, fonksiyonlar ve komut satırı argümanlarını öğrenmeye çalışıyorum.

## Yasal ve etik kullanım

Bu araçları sadece sahibi olduğum veya açıkça izin aldığım sistemlerde kullanıyorum. İzinsiz port taraması yapmak veya oluşturulan listeleri başkalarının hesaplarında denemek yasal ve etik değildir.

## Dosyalar

### `ag.py`

Komut satırından verilen IP adresi ve port aralığını tarar. Örneğin `22-80` aralığı verildiğinde bu aralıktaki TCP portlarını kontrol eder.

Kullanım:

```bash
python ag.py 192.168.1.1 22-80
```

Bu dosyada `socket.connect_ex()` kullanılıyor. Sonuç `0` olduğunda portun açık olduğunu yazdırıyor. Şimdilik sadece açık portları gösteriyor.

### `tarar.py`

Kodun içinde belirlenmiş olan bir IP adresindeki bazı portları kontrol eder. Örnek olarak SSH, DNS, HTTP ve HTTPS gibi yaygın portlar listede bulunuyor.

Açık bir port bulursa banner bilgisi almaya çalışıyor. Her servis banner bilgisi göndermediği için bu bölüm her zaman sonuç vermeyebilir.

Çalıştırmak için:

```bash
python tarar.py
```

Dosyanın içindeki `ipa` değişkenini kendi test ortamımdaki IP adresine göre değiştirmem gerekiyor.

### `generator.py`

`admin`, `login` ve `panel` gibi kelimelerden farklı kelime kombinasyonları üretir. Yılları kelimelerin başına veya sonuna ekler ve bazı sonuçların sonuna `!` sembolü koyar.

Bu dosyayı listeler ve `for` döngülerini daha iyi anlamak için yazdım.

Çalıştırmak için:

```bash
python generator.py
```

### `username-generator.py`

Belirlenen kelimeleri 2005 ile 2025 arasındaki yıllarla ve bazı sembollerle birleştirir. Oluşturulan listeyi Windows masaüstündeki `list.txt` dosyasına yazmaya çalışır.

Bu dosyada kendi bilgisayarımda kullandığım bir dosya yolu olduğu için farklı bir bilgisayarda çalıştırmadan önce şu satırı değiştirmek gerekir:

```python
with open(r"C:\Users\USERNAME\Desktop\list.txt", "w", encoding="utf-8") as dosya:
```

Daha taşınabilir olması için ileride dosya yolunu kullanıcıdan almayı veya projenin bulunduğu klasöre kayıt yapmayı planlıyorum.

## Kurulum

Python 3 kurulu olması yeterli. Harici bir paket kullanmıyorum.

Projeyi indirdikten sonra dosyaları doğrudan çalıştırabilirim:

```bash
python ag.py 127.0.0.1 1-1024
python tarar.py
python generator.py
python username-generator.py
```

Windows'ta `python` komutu çalışmazsa `py` komutunu denemek gerekebilir.

## Şu an öğrendiklerim

Bu projeyi geliştirirken şu konularda pratik yapıyorum:

- Python listeleri
- `for` döngüleri
- Fonksiyon oluşturma
- `try` ve `except` ile hata yakalama
- `socket` modülü ile TCP bağlantısı deneme
- `sys.argv` ile komut satırı girdisi alma
- Dosyaya veri yazma
- Basit banner bilgisi alma denemeleri

## Eksikler ve geliştirme fikirleri

Bu proje başlangıç seviyesinde olduğu için bazı eksikleri var. İleride şunları eklemek istiyorum:

- IP adresi ve port aralığı için daha iyi giriş kontrolü
- Geçersiz komut satırı girdileri için açıklayıcı hata mesajları
- Domain adı ile tarama yapabilme
- Açık portların yanında servis adlarını gösterme
- Daha düzenli çıktı formatı
- Sonuçları TXT, JSON veya CSV dosyasına kaydetme
- Threading veya async kullanarak taramayı hızlandırma
- IPv6 desteği
- Banner alma işleminde timeout kontrolünü iyileştirme
- Test amacıyla ayrı bir yerel ağ ve sanal makine ortamı kullanma

## Not

Bu repo profesyonel bir port tarayıcı değildir. Python ve temel ağ programlama konularını öğrenmek için hazırladığım küçük örneklerden oluşuyor. Kodları geliştirirken güvenli, kontrollü ve izinli test ortamları kullanmaya dikkat ediyorum.
