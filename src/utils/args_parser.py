import argparse
from pathlib import Path
from typing import List, Tuple


def arguments_parser() -> argparse.Namespace:
    """"""
    parser = argparse.ArgumentParser(description="Variables required for program to run")
    parser.add_argument("--input_file", type=str, help="Input configuration for run file") 
    parser.add_argument("--a", type=float, default=0.0, help="Molecule position A")
    parser.add_argument("--b", type=float, default=0.0, help="Molecule position B")
    parser.add_argument("--c", type=float, default=0.0, help="Molecule position C")
    parser.add_argument("--j", type=int, default=5, help="Quantum number J")
    args = parser.parse_args()
    
    return args


def _read_file_content(file_path: Path) -> List[str]:
    """"""
    with open(file_path, "r") as f:
        input_file_content = f.read()
    file_content: List[str] = input_file_content.split()

    return file_content


def get_args_from_input_file(file_path: Path) -> Tuple[float, float, float, int]:
    """"""
    A: float = 0.0
    B: float = 0.0
    C: float = 0.0
    J: int = 0

    file_content = _read_file_content(file_path)
    for entry in file_content:
    
        if entry.lower().startswith("a"):
            eq_position = entry.find("=")
            A = float(entry[eq_position+1:])
    
        if entry.lower().startswith("b"):
            eq_position = entry.find("=")
            B = float(entry[eq_position+1:])

        if entry.lower().startswith("c"):
            eq_position = entry.find("=")
            C = float(entry[eq_position+1:]) 

        if entry.lower().startswith("j"):
            eq_position = entry.find("=")
            J = int(entry[eq_position+1:])

    return (A, B, C, J)
