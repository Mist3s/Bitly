# Обрезка ссылок с помощью Битли

Консольная утилита для сокращения и просмотра статистики переходов по ссылке.

### Как установить

1. Получить токен API Bitly:

- [Сервис Bitly](https://bit.ly/) — зарегистрируйтесь
- [Документации Bitly](https://dev.bitly.com/get_started.html)
  - [Генератор токенов](https://bitly.com/a/oauth_apps)
- GENERIC ACCESS TOKEN — нужный тип токена

2. Поместь полученый токен в файл _token.env_ в переменую _BITLY_TOKEN_

3. Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
