# -*- coding: utf-8 -*-
"""
Bu Python dosyası, SQLite3 ile temel veritabanı işlemlerini öğretmek için oluşturulmuştur.
Bölümler halinde ayrılmış ve bolca yorum içermektedir.
"""

# ======= 1. BÖLÜM: VERİTABANINA BAĞLANTI =======
# sqlite3 kütüphanesi Python'un standart kütüphanelerindendir. Ekstra kurulum gerekmez.
import sqlite3

# Veritabanına bağlanmak veya yeni bir veritabanı dosyası oluşturmak için connect() kullanılır.
# "ornek.db" adlı bir veritabanı dosyası oluşturulur. Eğer dosya varsa, ona bağlanılır.
conn = sqlite3.connect("ornek.db")

# Veritabanıyla işlemler yapabilmek için bir imleç (cursor) oluşturulur.
cursor = conn.cursor()

print("Veritabanına bağlanıldı.")

# ======= 2. BÖLÜM: TABLO OLUŞTURMA =======
# Eğer veritabanında yoksa, bir "kisiler" tablosu oluşturalım.
cursor.execute("""
CREATE TABLE IF NOT EXISTS kisiler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Otomatik artan birincil anahtar
    isim TEXT,                            -- Kişinin adı
    yas INTEGER,                          -- Kişinin yaşı
    sehir TEXT                            -- Kişinin şehri
)
""")

print("Tablo oluşturuldu veya zaten mevcut.")

# ======= 3. BÖLÜM: VERİ EKLEME =======
def veri_ekle(isim, yas, sehir):
    """Veritabanına yeni bir kişi ekler."""
    cursor.execute("INSERT INTO kisiler (isim, yas, sehir) VALUES (?, ?, ?)", (isim, yas, sehir))
    conn.commit()  # Değişikliklerin kaydedilmesi gerekir.
    print(f"{isim} adlı kişi eklendi.")

# Örnek veri ekleme
veri_ekle("Ahmet", 25, "Ankara")
veri_ekle("Ayşe", 30, "İstanbul")

# ======= 4. BÖLÜM: VERİLERİ LİSTELEME =======
def verileri_listele():
    """Veritabanındaki tüm kişileri listeler."""
    cursor.execute("SELECT * FROM kisiler")
    veriler = cursor.fetchall()  # Tüm sonuçları alır
    print("\nKişiler Tablosu:")
    for veri in veriler:
        print(veri)

# Verileri listeleme
verileri_listele()

# ======= 5. BÖLÜM: VERİ ARAMA =======
def veri_arama(isim):
    """Veritabanında belirtilen isme sahip kişileri arar."""
    cursor.execute("SELECT * FROM kisiler WHERE isim = ?", (isim,))
    sonuc = cursor.fetchall()
    if sonuc:
        print(f"\n'{isim}' adlı kişi(ler) bulundu:")
        for kisi in sonuc:
            print(kisi)
    else:
        print(f"\n'{isim}' adlı kişi bulunamadı.")

# Örnek arama
veri_arama("Ahmet")

# ======= 6. BÖLÜM: VERİ GÜNCELLEME =======
def veri_guncelle(id, yeni_isim, yeni_yas, yeni_sehir):
    """Belirtilen ID'ye sahip kişinin bilgilerini günceller."""
    cursor.execute(
        "UPDATE kisiler SET isim = ?, yas = ?, sehir = ? WHERE id = ?",
        (yeni_isim, yeni_yas, yeni_sehir, id)
    )
    conn.commit()
    print(f"ID {id} olan kişinin bilgileri güncellendi.")

# Örnek güncelleme
veri_guncelle(1, "Mehmet", 26, "İzmir")
verileri_listele()

# ======= 7. BÖLÜM: VERİ SİLME =======
def veri_sil(id):
    """Belirtilen ID'ye sahip kişiyi siler."""
    cursor.execute("DELETE FROM kisiler WHERE id = ?", (id,))
    conn.commit()
    print(f"ID {id} olan kişi silindi.")

# Örnek silme
veri_sil(2)
verileri_listele()

# ======= 8. BÖLÜM: KAYNAKLARI SERBEST BIRAKMA =======
# İşlemler tamamlandıktan sonra bağlantıyı kapatmak önemlidir.
cursor.close()
conn.close()
print("Veritabanı bağlantısı kapatıldı.")
