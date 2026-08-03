# 🚀 Mini Görev Yöneticisi (Task Manager API)
Bu proje, ğrojelerinizi ve bu projelere bağlı görevleri yönetmenizi sağlayan ** Django REST Framework (DRF)** tabamkı bir RESTful API servisidir.

---

## 🛠️ Teknolojiler ve Kurulum
* **Python** 3.14+
* **Django** 6.0+
* **Django REST Framework (DRF)**
* **Simple JWT** (JSON Web Token Authentication)

### Yerel Ortamda Çalıştırma

1. **Repoyu klonlayın:**
''' bash
git clone [https://github.com/nalintore/Mini-G-rev-Y-neticisi.git](https://github.com/nalintore/Mini-G-rev-Y-neticisi.git)
   cd Mini-G-rev-Y-neticisi

 1. Sanal ortamı oluşturun ve aktif edin:
 python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

2. Bağımlılıkları yükleyin: 
pip install -r requirements.txt

3. Veritabanını hazırlayın ve sunucuyu başlatın:
python manage.py migrate
python manage.py runserver

🔐 Kimlik Doğrulama (Authentication)

Tüm endpoint'ler IsAuthenticated izni ile korunmaktadır.

Token Alma Endpoint'i: POST /api/token/
İstek Header Yapısı: Authorization: Bearer <access_token>
📌 API Uç Noktaları (Endpoints)
Metot	Uç Nokta	Açıklama	Query Parametreleri
POST	/api/token/	JWT access & refresh token alır	-
GET	/api/projects/	Projeleri listeler (Sayfalanmış)	?search=...&page=...
POST	/api/projects/	Yeni proje oluşturur	-
GET	/api/projects/{id}/tasks/	Projeye ait görevleri listeler	?status=TODO&search=...&page=...
POST	/api/projects/{id}/tasks/	Projeye yeni görev ekler	-
PATCH	/api/tasks/{id}/	Görevi kısmi günceller	-
DELETE	/api/tasks/{id}/	Görevi siler	-
🏗️ Mimari Prensipler
ModelViewSet ve routers.DefaultRouter kullanılmamıştır. Saf APIView ve path() tercih edilmiştir.
Tüm iş mantığında hata yakalama (try-except) ve logging mekanizması uygulanmıştır.
 
    

