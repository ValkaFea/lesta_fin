# lesta_fin

Flask-приложение 

## Запуск проекта

### Требования
- Docker и Docker Compose установленные на системе

### Инструкция по запуску
1. Клонируйте репозиторий:
```bash
git clone https://github.com/ValkaFea/lesta_fin.git
cd lesta_fin

### Настройка окружения
2.cp .env.example .env
Отредактируйте файл .env, указав свои значения переменных

### Запустите сервисы:
3.docker-compose up -d

###Приложение будет доступно:

4.Основной URL: http://localhost:5000
http://http://localhost:5000/results
Swagger UI: http://localhost:5000/apidocs/

Для остановки:
5. docker-compose down



Как настроить Jenkins
1. Установите Jenkins с Docker plugin
2. Запустите Jenkins Agent
3. Добавьте credentials:

- Учетные данные Docker Hub (имя юзера, прописными буквами, токен с правами на запись и чтение)
- SSH-ключи для сервера

3. Создайте новый Pipeline:

- Укажите "Pipeline script from SCM"
- Выберите Git и URL репозитория
- Ветка: main
- Путь к Jenkinsfile: Jenkinsfile

4. Как работает CI/CD
- Checkout: Клонирование репозитория
- Build: Сборка Docker образа
- Test: Запуск flake8 для проверки кода
- Push: Загрузка образа в Docker Hub
- Deploy: Развертывание на сервере:
- Обновление кода
- Перезапуск контейнеров через docker-compose


