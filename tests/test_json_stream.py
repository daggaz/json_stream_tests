import io
from pathlib import Path

import json_stream
import pytest


files = Path('.') / "json-test-suite" / "test_parsing"
positive = [
    (file.name[2:], file.read_bytes()) for file in files.iterdir() if file.name.startswith("y_")
]
negative = [
    (file.name[2:], file.read_bytes()) for file in files.iterdir() if file.name.startswith("n_")
]
undefined = [
    (file.name[2:], file.read_bytes()) for file in files.iterdir() if file.name.startswith("i_")
]


class TestJSONStream:
    @pytest.mark.parametrize("filename,content", positive)
    def test_load_positive_scenarios(self, filename: str, content: bytes) -> None:
        with io.BytesIO(content) as binary_file:
            result = json_stream.load(binary_file)
            if result is not None and not isinstance(result, (int, float, str, bool)):
                result.read_all()

    @pytest.mark.parametrize("filename,content", negative)
    def test_load_negative_scenarios(self, filename: str, content: bytes) -> None:
        with io.BytesIO(content) as binary_file, pytest.raises(Exception):
            result = json_stream.load(binary_file)
            if result is not None and not isinstance(result, (int, float, str, bool)):
                result.read_all()

    @pytest.mark.parametrize("filename,content", positive)
    def test_visit_positive_scenarios(self, filename: str, content: bytes) -> None:
        with io.BytesIO(content) as binary_file:
            json_stream.visit(binary_file, lambda item, path: None)

    @pytest.mark.parametrize("filename,content", negative)
    def test_visit_negative_scenarios(self, filename: str, content: bytes) -> None:
        with io.BytesIO(content) as binary_file, pytest.raises(Exception):
            json_stream.visit(binary_file, lambda item, path: None)

    @pytest.mark.parametrize("filename,content", undefined)
    def test_undefined_scenarios(self, filename: str, content: bytes) -> None:
        """
        Just check that parser do not not crash with segfault or something like that.
        """
        with io.BytesIO(content) as binary_file:
            try:
                json_stream.visit(binary_file, lambda item, path: None)
            except Exception:
                pass

        with io.BytesIO(content) as binary_file:
            try:
                result = json_stream.load(binary_file)
                if result is not None and not isinstance(result, (int, float, str, bool)):
                    result.read_all()
            except Exception:
                pass
