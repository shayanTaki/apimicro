# میکرو سرویس احراز هویت جنگو با Docker

این پروژه یک میکرو سرویس احراز هویت ساده است که با استفاده از جنگو REST Framework و Docker پیاده‌سازی شده است. این سرویس امکان احراز هویت کاربران بر اساس نام کاربری و رمز عبور و همچنین ثبت نام کاربران جدید توسط ادمین را فراهم می‌کند.

## ویژگی‌ها

*   **احراز هویت مبتنی بر JWT:** تولید و اعتبارسنجی توکن‌های JWT برای احراز هویت API.
*   **مدل کاربری جنگو:** استفاده از مدل پیش‌فرض `User` جنگو.
*   **ثبت نام توسط ادمین:** امکان ثبت نام کاربران جدید توسط کاربران با سطح دسترسی ادمین.
*   **Dockerized:** بسته بندی شده با Docker برای استقرار آسان.

## فناوری‌های استفاده شده

*   [Python](https://www.python.org/)
*   [Django](https://www.djangoproject.com/)
*   [Django REST Framework](https://www.django-rest-framework.org/)
*   [djangorestframework-simplejwt](https://github.com/darthvader42/django-rest-framework-simplejwt)
*   [Docker](https://www.docker.com/)
*   [Docker Compose](https://docs.docker.com/compose/)
*   [PostgreSQL](https://www.postgresql.org/)

## پیش‌نیازها

*   [Docker](https://docs.docker.com/engine/install/)
*   [Docker Compose](https://docs.docker.com/compose/install/)

## نصب و راه‌اندازی

1. **کلون کردن ریپازیتوری:**

    ```bash
    git clone <your_repository_url>
    cd django-auth-service
    ```

2. **ایجاد و پیکربندی فایل `.env`:**

    یک فایل با نام `.env` در دایرکتوری اصلی پروژه ایجاد کنید و متغیرهای محیطی زیر را در آن قرار دهید:

    ```env
    SECRET_KEY=your_secret_key_here
    ```

    *   `SECRET_KEY`: یک کلید مخفی برای جنگو. آن را با یک مقدار امن و تصادفی جایگزین کنید.

3. **اجرای کانتینرها با Docker Compose:**

    ```bash
    docker-compose up -d --build
    ```

4. **اجرای مایگریشن‌ها (در صورت نیاز):**

    ```bash
    docker exec -it django-auth-service-web-1 bash
    python manage.py makemigrations authentication
    python manage.py migrate
    exit
    ```

## نقاط پایانی API

### دریافت توکن JWT

*   **URL:** `/auth/token/`
*   **Method:** `POST`
*   **بدنه درخواست (JSON):**

    ```json
    {
        "username": "your_username",
        "password": "your_password"
    }
    ```

*   **پاسخ موفق (JSON):**

    ```json
    {
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
    }
    ```

### ثبت نام کاربر جدید (نیاز به احراز هویت ادمین)

*   **URL:** `/auth/register/`
*   **Method:** `POST`
*   **احراز هویت:** نیاز به توکن JWT معتبر یک کاربر ادمین در هدر `Authorization` (Bearer Token).
*   **بدنه درخواست (JSON):**

    ```json
    {
        "admin_username": "admin_username",
        "admin_password": "admin_password",
        "new_username": "new_username",
        "new_password": "new_password"
    }
    ```

*   **پاسخ موفق (JSON):**

    ```json
    {
        "id": 1,
        "admin_username": "admin_username",
        "new_username": "new_username",
        "created_at": "2023-05-28T10:30:00.000000Z"
    }
    ```

## متغیرهای محیطی

*   `SECRET_KEY`: کلید مخفی جنگو برای امنیت.

## نکات مهم

*   **امنیت:** به خاطر داشته باشید که `SECRET_KEY` یک مقدار حساس است و باید به صورت امن مدیریت شود. هرگز آن را در کد منبع قرار ندهید.
*   **HTTPS:** برای محیط‌های پروداکشن، استفاده از HTTPS برای رمزنگاری ترافیک توصیه می‌شود.
*   **کاربر ادمین:** قبل از استفاده از نقطه پایانی `/auth/register/`، باید یک کاربر با سطح دسترسی `is_staff=True` (کاربر ادمین) در جنگو ایجاد کنید. می‌توانید این کار را از طریق پنل ادمین جنگو پس از اجرای مایگریشن‌ها انجام دهید.

## مشارکت

برای مشارکت در این پروژه، می‌توانید pull request ارسال کنید یا issue جدید ایجاد کنید.

## لایسنس

[MIT](LICENSE)
