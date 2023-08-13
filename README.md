# SQL_BOT

Великолепный бот для тренировки SQL запросов прямо в Telegram.

## Как работает бот:

Просто вставьте токен и пользуйтесь на здоровье! В комплекте идет готовая база данных с таблицами:

- 'users'
- 'student'
- 'group_student'
- 'teacher'
- 'subject'

Для просмотра структуры базы данных и для просмотра структуры таблиц в базе данных выподняй следующую команду:
```sql
SELECT name FROM sqlite_master WHERE type='table';

PRAGMA table_info(table_name);


