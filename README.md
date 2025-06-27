# Asynchronous high-level logging wrapper (via aiologger)

---

## 📦 Package Info

[![PyPI](https://img.shields.io/pypi/v/aiologger-x9-wrapper?color=blue&label=PyPI%20version)](https://pypi.org/project/aiologger-x9-wrapper/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
![Test-coverage](https://img.shields.io/badge/coverage-94%25-brightgreen)
---

[![en](https://img.shields.io/badge/🌐_lang-ENG-2ECC71.svg?style=for-the-badge&logo=globe&logoColor=white)](./README.md)
[![ru](https://img.shields.io/badge/🌐_lang-RU-E74C3C.svg?style=for-the-badge&logo=globe&logoColor=white)](./README_RUS.md)

---

# Attention! ⚠

### This wrapper is not complete, the functionality may change depending on the versions

---

## 🔹Main function:

> 🔶 **Asynchronous logging with recording to a file of "today" day**

---

## 🔹Installation?:🧩

```shell
pip install aiologger_x9_wrapper
```

> Attention! This module will not work without the libraries: aiofiles, aiologger

---

## 🔹Import the dependencies:

```
from aiologger_x9_wrapper import (
    # Enums: (Required)
    "Levels",
    "LogFormats",

    # Main classes: (Required)
    "LogFormatter",
    "FolderHandler",
    "Logger",

    # Functions:
    "shutdown_loggers",  # Required if you want to manually clean up storage

    # Internals: (Optional)
    "LOGGERS_STORAGE",
    "FormatterDTO",
    "FolderHandlerDTO",
    "AsyncLogger",
)
```

---

## 🔹Quick Reference on Dependencies:

```
Levels -> Enum class with allowed logging levels
LogFormats -> Enum class with allowed parts of log output format

LogFormatter -> Determines the format of log output (What will be written to the log, with what separator, in what time format)
FolderHandler -> Determines the name and location of the directory for log files.

Logger -> Main logging configuration class. Accepts formatter and file handler and also a logger storage (Optional)

shutdown_loggers -> logger storage clearing function. If no storage is passed, the base one is cleared

LOGGERS_STORAGE -> Basic Logger Storage
FormatterDTO -> handler dataclass
FolderHandlerDTO -> handler dataclass
AsyncLogger -> A custom type used for annotations, typically logger store values: Dict[str, AsyncLogger]
```

---

## 🔹How to use?:

---

> **Define the required log output format using LogFormatter:**

```
MY_LOG_FORMATTER: LogFormatter = LogFormatter(
    log_format=(LogFormats.TIME, LogFormats.NAME, LogFormats.LEVEL, LogFormats.MESSAGE),  # default
    separator=" - ",  # default
    datettime_format= "%d.%m.%Y %H:%M"  # default
)
```

---

> **Define the attributes of the created folder via the FolderHandler class:**

```
MY_FOLDER_HANDLER: FolderHandler = FolderHandler(
    path=Path(__file__).parent,  # Required, or path="log_folder"
    name="logs"  # default
)
```

---

> **Define a logger with created configurations:**

```
# Optional: create our own logger storage
CUSTOM_LOGGER_STORAGE: Dict[str, AsyncLogger] = {}

MY_LOGGER: Logger = Logger(
    log_formatter=MY_LOG_FORMATTER,
    folder_handler=MY_FOLDER_HANDLER,
    logger_storage=CUSTOM_LOGGER_STORAGE
)
```

---

> **Use the write_log method of the created class instance:**

```
await MY_LOGGER.write_log(
    log_level=Levels.INFO/DEBUG/WARNING/ERROR/CRITICAL,
    message="Hello world!",
    logger_name="SERVICE"  # Optional
)
```

---

> **If you want to manually clear the storage, use the shutdown_loggers function:**

```
await shutdown_loggers(loggers_storage=CUSTOM_LOGGER_STORAGE)

# If loggers_storage was not passed, the underlying storage is used
```

---
