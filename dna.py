from typing import NewType
import pytest

Sequence = NewType("Sequence", str)


def calculate_gc_ratio(seq: Sequence) -> float:
    return len(seq) - 1


def test_equal_gcs_is_one():
    assert calculate_gc_ratio("GC") == 1


def test_double_gcs_is_two():
    assert calculate_gc_ratio("GGC") == 2
