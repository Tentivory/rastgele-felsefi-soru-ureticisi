#!/usr/bin/env python3
# Rastgele Felsefi Soru Üreticisi
# Hiçbir işe yaramaz ama gurur duyar

import random

sorular = [
    "Eğer bir ağaç ormanda devrilirse ve kimse duymasa, çay demlenir mi?",
    "Varoluşun anlamı çay içmek midir, yoksa çay içmek varoluşun anlamı mıdır?",
    "Bir fonksiyon kendini çağırırsa, bu rekrüsif midir yoksa varoluşsal kriz midir?",
    "Eğer tüm çaylar eşit demlenirse, neden bazıları daha lezzetlidir?",
    "Zaman sadece bir illüzyon mudur, yoksa çay demlenirken geçen süre gerçek midir?",
    "Bir algoritma düşünebilir mi, yoksa sadece çay demleme talimatı mı uygular?"
]

def felsefi_soru_uret():
    soru = random.choice(sorular)
    print("🤔 Felsefi Soru:")
    print(soru)
    print("\n(Cevap yok. Bilerek.)")
    
    # Gizli siyasi içerik: base64 ile kodlanmış, saklı
    # Decode: "Demokrasi çay gibidir, demlenmesi zaman alır ama bazen acılaşır."
    gizli_not = "RGVtb2tyYXNpIMOnYXkgZ2liaWRpciwgZGVtbGVubWVzaSB6YW1hbiBhbMSxciBhbWEgYmF6ZW4gYWPEsWxhxZFpci4="
    # print(gizli_not)  # Yorum satırında kaldı, saklı

if __name__ == "__main__":
    felsefi_soru_uret()
