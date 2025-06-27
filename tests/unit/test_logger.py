from typing import Dict

import pytest

from datetime import datetime
from pathlib import Path
from asyncio import sleep as asyncio_sleep

from aiologger import Logger as AioLogger  # type: ignore

from aiologger_x9_wrapper.enums import Levels, LogFormats
from aiologger_x9_wrapper.formatters import LogFormatter
from aiologger_x9_wrapper.handlers import FolderHandler
from aiologger_x9_wrapper.logger import Logger, LOGGERS_STORAGE, shutdown_loggers


@pytest.mark.asyncio
class TestLogger:
    @pytest.mark.parametrize(
        "log_formatter, filename, logger_name, log_level, log_message",
        [
            (
                LogFormatter(),
                "logs",
                "SERVICE",
                Levels.DEBUG,
                "Hello World!_1",
            ),
            (
                LogFormatter(
                    log_format=(LogFormats.NAME, LogFormats.LEVEL, LogFormats.MESSAGE),
                ),
                "MY_LOGS",
                "TEST_SERVICE",
                Levels.INFO,
                "Hello World!_2"
            )
        ]
    )
    async def test_logger(
            self,
            log_formatter: LogFormatter,
            filename: str,
            logger_name: str,
            log_level: Levels,
            log_message: str,

            tmp_path: Path,  # Temporary directory pytest
    ) -> None:
        tmp_file_handler: FolderHandler = FolderHandler(
            path=tmp_path,
            name=filename,
        )

        custom_logger: Logger = Logger(
            log_formatter=log_formatter,
            folder_handler=tmp_file_handler,
        )

        await custom_logger.write_log(
            log_level=log_level,
            message=log_message,
            logger_name=logger_name,
        )
        await asyncio_sleep(0.1)  # Guaranteed recording time

        current_date: str = datetime.now().strftime("%d.%m.%Y")
        if current_date in LOGGERS_STORAGE:
            logger: AioLogger = LOGGERS_STORAGE[current_date]

            await logger.shutdown()
            del LOGGERS_STORAGE[current_date]

        tmp_log_dir: Path = tmp_path / filename
        tmp_log_files = list(tmp_log_dir.glob("*.log"))

        assert len(tmp_log_files) == 1, f"Expected 1 file, found {len(tmp_log_files)}"

        tmp_log_file: Path = tmp_log_files[0]
        content = tmp_log_file.read_text()

        assert log_message in content, f"Message '{log_message}' not found"
        assert log_level.value in content, f"Level '{log_level.value}' not found"
        assert logger_name in content, f"Logger name '{logger_name}' not found"

        tmp_log_file.unlink()
        tmp_log_dir.rmdir()


@pytest.mark.asyncio
class TestShutdownLoggers:
    @pytest.mark.parametrize(
        "logger_key, logger_value",
        [
            ("01.01.2001", AioLogger()),
            ("02.02.2002", AioLogger()),
            ("03.03.2003", AioLogger()),
        ]
    )
    async def test_shutdown_loggers(
            self,
            logger_key: str,
            logger_value: AioLogger,
    ) -> None:
        test_loggers_storage: Dict[str, AioLogger] = {
            logger_key: logger_value
        }

        assert logger_key in test_loggers_storage, f"{logger_key} not in storage"
        assert test_loggers_storage[logger_key] == logger_value

        await shutdown_loggers(loggers_storage=test_loggers_storage)

        assert test_loggers_storage == {}
