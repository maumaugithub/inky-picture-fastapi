"""Tests for hello function."""
from pathlib import Path

import pytest
from inky_picture_service.utils.file_utils import get_root_path
from inky_picture_service.utils.file_utils import get_relative_path
from inky_picture_service.utils.file_utils import get_file_basename_no_ext


@pytest.mark.parametrize("path,expected",
                         [
                             ("some\\some_file.jpg", "some_file"),
                             ("C:\\Users\\I2312343465658765432\\conda-workspace\\inky-picture-fastapi\\test\\asset\\cacti-hi.jpg",
                              "cacti-hi"),
                         ])
def test_get_file_basename_no_ext(path, expected):
    """Example test with parametrization."""
    assert get_file_basename_no_ext(path) == expected


@pytest.mark.parametrize("path,expected",
    [
        (Path("some\\some_file.jpg"), "some\\some_file.jpg"),
        (Path("C:\\Users\\I2312343465658765432\\conda-workspace\\inky-picture-fastapi\\test\\asset\\cacti-hi.jpg"), "asset\\cacti-hi.jpg"),
    ])
def test_get_relative_path(path, expected):
    """Example test with parametrization."""
    assert get_relative_path(path) == expected


@pytest.mark.parametrize("path,expected",
     [
         (Path("C:\\Users\\I2312343465658765432\\conda-workspace\\inky-picture-fastapi\\some_path\\some_file.jpg"),
          "C:\\Users\\I2312343465658765432\\conda-workspace\\inky-picture-fastapi\\some_path\\"),
         (Path("C:\\Users\\I2312343465658765432\\conda-workspace\\inky-picture-fastapi\\test\\asset\\cacti-hi.jpg"),
          "C:\\Users\\I2312343465658765432\\conda-workspace\\inky-picture-fastapi\\test\\asset\\"),
     ])
def test_get_root_path(path, expected):
    """Example test with parametrization."""
    assert get_root_path(path) == expected
