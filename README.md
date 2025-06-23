# Asynchronous high-level logging wrapper (via aiologger)

---

## 📦 Package Info

[![PyPI](https://img.shields.io/pypi/v/aiologger-x9-wrapper?color=blue&label=PyPI%20version)](https://pypi.org/project/aiologger-x9-wrapper/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)

---

## Main function:

> 🔶 **Asynchronous logging of messages with the specified level. Automatically creates the logs/ folder (if it does not
exist), at the required level of the service structure by changing the LOGGER_PATH constant and writes messages to files
of the DD.MM.YYYY.log format with grouping by days**

---

### 🔹How to use?:🧩

Install the wrapper:

```shell
pip install aiologger_x9_wrapper
```

> Attention! This module will not work without the libraries: aiofiles, aiologger

### Import the required dependencies:

```
from aiologger_x9_wrapper import logger, Levels

# Where Levels:
class Levels(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
```

### Use the function where you need it:

#### The function has the form:

```
await logger(
        # Required
        level: Levels,  # Registered logging level via enums -> Levels (Exapmle: Levels.INFO)
        message: str,  # Any message in str format
        directory_path: Path | str  # Path where the log folder will be created  (Example: Path(__file__).parent)
        # Optional:
        directory_name: Path | str = Path("logs"),  # Name of the folder for logs
        logger_name: str = "SERVICE"  # Logger name in logs
)
```

#### Basically used as::

```
await logger(level=Levels.INFO, message="Hello world", directory_path=Path(__file__).parent)
```
