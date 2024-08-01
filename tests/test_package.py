from __future__ import annotations

import importlib.metadata

import timeseriesanal as m


def test_version():
    assert importlib.metadata.version("timeseriesanal") == m.__version__
