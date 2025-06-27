import pytest

from typing import Tuple

from aiologger_x9_wrapper import LogFormats, LogFormatter
from aiologger_x9_wrapper.dto import FormatterDTO


class TestFormatter:
    @pytest.mark.parametrize(
        "log_format, separator, datetime_format",
        [
            ((LogFormats.TIME, LogFormats.NAME), " -- ", "%d.%m.%Y"),
            ((LogFormats.TIME,), " - ", "%d.%m.%Y %H:%M"),
        ]
    )
    def test_formatter(
            self,
            log_format: Tuple[LogFormats, ...],
            separator: str,
            datetime_format: str,
    ) -> None:
        formatter: LogFormatter = LogFormatter(
            log_format=log_format,
            separator=separator,
            datetime_format=datetime_format,
        )

        result: FormatterDTO = formatter.build_format()

        assert result.datetime_format == datetime_format

        expected_log_format: str = separator.join(str(arg.value) for arg in log_format)

        assert result.log_format == expected_log_format
