from datetime import datetime

import pytest
import asyncio
from pathlib import Path

from aiologger_wrapper.enums import Levels
from aiologger_wrapper.config import logger
from aiologger_wrapper.config import LOGGERS_BY_DATE

TEST_LOGGER_NAME: str = "TEST_SERVICE"


@pytest.mark.asyncio
class TestLogger:
    @pytest.mark.parametrize(
        "level, message, logger_name",
        [
            (Levels.INFO, "Info message!", TEST_LOGGER_NAME),
            (Levels.DEBUG, "Debug message!", TEST_LOGGER_NAME),
            (Levels.CRITICAL, "Critical message!", TEST_LOGGER_NAME),
            (Levels.ERROR, "Error message!", TEST_LOGGER_NAME),
            (Levels.WARNING, "Warning message!", TEST_LOGGER_NAME),
        ]
    )
    async def test_logger(
            self,
            level: Levels,
            message: str,
            logger_name: str,
            tmp_path: Path  # Temporary directory pytest
    ) -> None:
        await logger(
            level=level,
            message=message,
            directory_path=tmp_path,
            logger_name=logger_name
        )
        await asyncio.sleep(0.2)  # Guaranteed recording time

        today = datetime.now().strftime("%d.%m.%Y")
        if today in LOGGERS_BY_DATE:
            log_instance = LOGGERS_BY_DATE[today]
            await log_instance.shutdown()
            del LOGGERS_BY_DATE[today]

        log_dir = tmp_path / "logs"
        log_files = list(log_dir.glob("*.log"))

        assert len(log_files) == 1, f"Expected 1 file, found {len(log_files)}"

        log_file = log_files[0]
        content = log_file.read_text()

        assert message in content, f"Message '{message}' not found"
        assert level.value in content, f"Level '{level.value}' not found"
        assert logger_name in content, f"Logger name '{logger_name}' not found"

        log_file.unlink()
        log_dir.rmdir()
