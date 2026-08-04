# 🚀 Mini Görev Yöneticisi (Task Manager API)

Bu proje, projelerinizi ve bu projelere bağlı görevleri yönetmenizi sağlayan **Django REST Framework (DRF)** tabanlı bir RESTful API servisidir.

---

## 🛠️ Teknolojiler ve Kurulum

* **Python** 3.14+
* **Django** 5.x / 6.0+
* **Django REST Framework (DRF)**
* **Simple JWT** (JSON Web Token Authentication)
* **drf-spectacular** (Swagger / OpenAPI 3.0 Dokümantasyonu)

### ⚡ QUICK START (Yerel Ortamda Çalıştırma)

1. **Repoyu klonlayın ve proje dizinine girin:**
   ```bash
git clone [https://github.com/nalintore/Mini-Gorev-Yoneticisi.git](https://github.com/nalintore/Mini-Gorev-Yoneticisi.git)
cd Mini-Gorev-Yoneticisi
   ```

2. **Sanal ortamı oluşturun ve aktif edin:**
   ```bash
   python -m venv .venv
   # Windows (PowerShell / CMD):
   .venv\Scripts\activate
   # Linux / macOS:
   source .venv/bin/activate
   ```

3. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Veritabanı migration işlemlerini yapın ve sunucuyu başlatın:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 📖 API Dokümantasyonu (Swagger / OpenAPI)

Sunucu çalıştıktan sonra API uç noktalarını interaktif arayüz üzerinden test etmek ve incelemek için aşağıdaki adresleri kullanabilirsiniz:

* **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
* **Redoc UI:** `http://127.0.0.1:8000/api/redoc/`
* **OpenAPI Schema:** `http://127.0.0.1:8000/api/schema/`

## 🔐 Kimlik Doğrulama (Authentication)

Korumalı tüm endpoint'ler `IsAuthenticated` izni ile çalışmaktadır.

* **Token Alma Endpoint'i:** `POST /api/token/`
* **İstek Header Yapısı:** `Authorization: Bearer <access_token>`

## 📌 API Uç Noktaları (Endpoints)

| Metot | Uç Nokta | Açıklama | Query Parametreleri |
|---|---|---|---|
| POST | `/api/token/` | JWT access & refresh token alır | - |
| POST | `/api/token/refresh/` | Access token'ı yeniler | - |
| GET | `/api/projects/` | Projeleri listeler (Sayfalanmış) | `?search=...&page=...` |
| POST | `/api/projects/` | Yeni proje oluşturur | - |
| GET | `/api/projects/{id}/tasks/` | Projeye ait görevleri listeler | `?status=TODO&search=...&page=...` |
| POST | `/api/projects/{id}/tasks/` | Projeye yeni görev ekler | - |
| PATCH | `/api/tasks/{id}/` | Görevi kısmi günceller | - |
| DELETE | `/api/tasks/{id}/` | Görevi siler | - |

## 🏗️ Mimari Prensipler

* **Clean Architecture & Custom Views:** `ModelViewSet` ve `routers.DefaultRouter` kullanılmamıştır. Esneklik ve tam kontrol için saf `APIView` ve `path()` tercih edilmiştir.
* **Error Handling & Logging:** Tüm iş mantığında hata yakalama (try-except) ve logging mekanizması uygulanarak 400, 404, 500 gibi durumlar kontrollü olarak yönetilmiştir.
* **Pagination & Filtering:** Sınırsız veri çekilmesini önlemek amacıyla özel `CustomPagination` yapısı ve `django.db.models.Q` ile filtrelenmiş arama motoru entegre edilmiştir.

