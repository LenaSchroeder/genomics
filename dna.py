from typing import NewType

Sequence = NewType("Sequence", str)


Sequence: str

def calculate_gc_ratio(seq: Sequence) -> float:
    return len(seq) - 1

assert calculate_gc_ratio('GC') == 1, "If there's equal number of Gs and Cs, it should be 1!"
assert calculate_gc_ratio('GGC') == 2, "If there's equal number of Gs and Cs, it should be 1!"