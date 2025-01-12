"""
Modified from: https://github.com/symon-storozhenko/pytest-playwright-visual
which nicely crafted and is very easy to use to:

1. change the path where snapshots are written to include the GOV.UK GDS
   Frontend version. That way images are compared against the version that
   was used to generate them so slight changes in styling between GDS versions
   do not trigger test failures. This also allows the snapshots for each
   GDS version to be stored in the same directory, making comparisons easy.

2. flatten the directory tree used for saving snapshots so it is easier to
   navigate when reviewing snapshots, particularly when using an image viewer
   to step through the screenshots for each gds version for a given test.
"""

import os
import shutil
import sys
from io import BytesIO
from pathlib import Path
from typing import Any, Callable

import pytest
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


def pytest_addoption(parser: Any) -> None:
    group = parser.getgroup("assert-snapshot", "Image Snapshot")
    group.addoption(
        "--update-snapshots",
        action="store_true",
        default=False,
        help="Update snapshots.",
    )


@pytest.fixture
def assert_snapshot(
    pytestconfig: Any, request: Any, browser_name: str, settings
) -> Callable:
    gds_version = "gds-%s" % settings.CRISPY_GDS_FRONTEND_VERSION
    test_name = f"{str(Path(request.node.name))}[{str(sys.platform)}]-{gds_version}"

    def compare(
        img: bytes, *, threshold: float = 0.1, name=f"{test_name}.png", fail_fast=False
    ) -> None:
        update_snapshot = pytestconfig.getoption("--update-snapshots")
        test_file_name = str(os.path.basename(Path(request.node.fspath))).strip(".py")

        filepath = (
            Path(request.node.fspath).parent.resolve() / "snapshots" / test_file_name
        )
        filepath.mkdir(parents=True, exist_ok=True)
        file = filepath / name

        # Create a dir where all snapshot test failures will go
        results_dir_name = (
            Path(request.node.fspath).parent.resolve() / "snapshot_tests_failures"
        )
        test_results_dir = results_dir_name / test_file_name

        # Remove a single test's past run dir with actual, diff and expected images
        if test_results_dir.exists():
            shutil.rmtree(test_results_dir)
        if update_snapshot:
            file.write_bytes(img)
            pytest.fail("--> Snapshots updated. Please review images")
        if not file.exists():
            file.write_bytes(img)
            # pytest.fail(
            pytest.fail("--> New snapshot(s) created. Please review images")

        img_a = Image.open(BytesIO(img))
        img_b = Image.open(file)
        img_diff = Image.new("RGBA", img_a.size)
        mismatch = pixelmatch(
            img_a, img_b, img_diff, threshold=threshold, fail_fast=fail_fast
        )

        if mismatch == 0:
            return
        else:
            # Create new test_results folder
            test_results_dir.mkdir(parents=True, exist_ok=True)
            img_diff.save(f"{test_results_dir}/Diff_{name}")
            img_a.save(f"{test_results_dir}/Actual_{name}")
            img_b.save(f"{test_results_dir}/Expected_{name}")
            pytest.fail("--> Snapshots DO NOT match!")

    return compare
