# Асинхронная высокоуровневая обертка для aiologger

---

## 📦 Информация о пакете

[![PyPI](https://img.shields.io/pypi/v/aiologger-x9-wrapper?color=blue&label=PyPI%20version)](https://pypi.org/project/aiologger-x9-wrapper/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
![Test-coverage](https://img.shields.io/badge/coverage-94%25-brightgreen)
---

[![ru](https://img.shields.io/badge/🌐_lang-RU-2ECC71.svg?style=for-the-badge&logo=globe&logoColor=white)](./README_RUS.md)
[![en](https://img.shields.io/badge/🌐_lang-ENG-E74C3C.svg?style=for-the-badge&logo=globe&logoColor=white)](./README.md)

---

# Внимание! ⚠

### Данная обертка не является законченной, функционал может меняться в зависимости от версий

---

## 🔹Главная функция:

> 🔶 **Асинхронное логирование с записью в файл "сегодняшнего" дня**

---

## 🔹Установка?:🧩

```shell
pip install aiologger_x9_wrapper
```

> Внимание! Данная обертка не будет работать без aiologger и aiofiles

---

## 🔹Импортируйте зависимости:

```
from aiologger_x9_wrapper import (
    # Enums: (Обязательно)
    "Levels",
    "LogFormats",

    # Основные классы: (Обязательно)
    "LogFormatter",
    "FolderHandler",
    "Logger",

    # Функции:
    "shutdown_loggers",  # Обязательно, если вы хотите вручную очищать хранилища

    # Внутренности: (Опционально)
    "LOGGERS_STORAGE",
    "FormatterDTO",
    "FolderHandlerDTO",
    "AsyncLogger",
)
```

---

## 🔹Краткая справка по зависимостям:

```
Levels -> Enum класс с разрешенными уровнями логирования
LogFormats -> Enum класс с разрешенными частями формата логов

LogFormatter -> Определяет формат записи лога
FolderHandler -> Определяет имя и расположения директории для логов

Logger -> Основной класс конфигурации логирования. Принимает форматтер и файловый обработчик, а также необязательное имя для конкретного лога (Базово - "SERVICE")

shutdown_loggers -> Функции очистки хранилища логов. Обязательно, если нужна ручкая очистка

LOGGERS_STORAGE -> Базовое хранилище логгеров
FormatterDTO -> DTO обработчика
FolderHandlerDTO -> DTO обработчика
AsyncLogger -> Кастомный тип данных, используемый для аннотации, обычно значения хранилища логгеров: Dict[str, AsyncLogger]
```

---

## 🔹Как использовать?:

---

> **Определите требуемый формат вывода логов с помощью LogFormatter:**

```
MY_LOG_FORMATTER: LogFormatter = LogFormatter(
    log_format=(LogFormats.TIME, LogFormats.NAME, LogFormats.LEVEL, LogFormats.MESSAGE),  # default
    separator=" - ",  # default
    datettime_format= "%d.%m.%Y %H:%M"  # default
)
```

---

> **Определите атрибуты созданной папки с помощью класса FolderHandler:**

```
MY_FOLDER_HANDLER: FolderHandler = FolderHandler(
    path=Path(__file__).parent,  # Required, or path="log_folder"
    name="logs"  # default
)
```

---

> **Инициализировать логгер с созданными конфигурациями:**

```
# Опционально: создать свое хранилище логгеров
CUSTOM_LOGGER_STORAGE: Dict[str, AsyncLogger] = {}

MY_LOGGER: Logger = Logger(
    log_formatter=MY_LOG_FORMATTER,
    folder_handler=MY_FOLDER_HANDLER,
    logger_storage=CUSTOM_LOGGER_STORAGE
)
```

---

> **Использовать метод write_log экземпляра класса Logger:**

```
await MY_LOGGER.write_log(
    log_level=Levels.INFO/DEBUG/WARNING/ERROR/CRITICAL,
    message="Hello world!",
    logger_name="SERVICE"  # Optional
)
```

---

> **Если нужна ручная очистка хранилища, используйте функцию shutdown_loggers::**

```
await shutdown_loggers(loggers_storage=CUSTOM_LOGGER_STORAGE)

# Если loggers_storage не был передан, используется базовое хранилище
```

---
