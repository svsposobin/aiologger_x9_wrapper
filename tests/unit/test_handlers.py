import pytest

from pathlib import Path

from aiologger_x9_wrapper.dto import FolderHandlerDTO
from aiologger_x9_wrapper.handlers import FolderHandler


class TestFileHandler:
    @pytest.mark.parametrize(
        "folder_path, folder_name",
        [
            (Path(__file__).parent, "logs"),
            ("../my_logs", "my_logs"),
            ("LOGS", Path("my_logs")),
        ]
    )
    def test_file_handler(
            self,
            folder_path: Path | str,
            folder_name: Path | str,
    ) -> None:
        handler: FolderHandler = FolderHandler(
            path=folder_path,
            name=folder_name,
        )

        result: FolderHandlerDTO = handler.build_format()

        assert result.folder_name == Path(folder_name)
        assert result.folder_path == Path(folder_path)
