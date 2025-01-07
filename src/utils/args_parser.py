import argparse
from pathlib import Path
from typing import List, Tuple


def arguments_parser() -> argparse.Namespace:
    """_summary_

    Returns:
        argparse.Namespace: _description_
    """
    parser = argparse.ArgumentParser(description="Variables required for program to run")
    parser.add_argument("--input_file", type=str, help="Input configuration for run file")
    parser.add_argument("--output_file", type=str, help="Output configuration for run file")
    parser.add_argument("--a", type=float, default=0.0, required=False, help="Molecule position A")
    parser.add_argument("--b", type=float, default=0.0, required=False, help="Molecule position B")
    parser.add_argument("--c", type=float, default=0.0, required=False, help="Molecule position C")
    parser.add_argument("--j", type=int, default=5, required=False, help="Quantum number J")
    parser.add_argument("--ij", type=bool, default=False, help="Calculate for range J=0,1,...,J")
    parser.add_argument("--save_H_matrices", type=bool, default=False, help="Save H matrices to output file")
    parser.add_argument("--save_submatrices", type=bool, default=False, help="Save submatrices to output file")
    args = parser.parse_args()

    return args


def _read_file_content(file_path: Path) -> List[str]:
    """_summary_

    Args:
        file_path (Path): _description_

    Returns:
        List[str]: _description_
    """
    with open(file_path, "r") as f:
        input_file_content = f.read()
    file_content: List[str] = input_file_content.split()

    return file_content


def get_args_from_input_file(file_path: Path) -> Tuple[float, float, float, int]:
    """_summary_

    Args:
        file_path (Path): _description_

    Returns:
        Tuple[float, float, float, int]: _description_
    """
    A: float = 0.0
    B: float = 0.0
    C: float = 0.0
    J: int = 0

    file_content = _read_file_content(file_path)
    for entry in file_content:

        if entry.lower().startswith("a"):
            eq_position = entry.find("=")
            A = float(entry[eq_position + 1 :])

        if entry.lower().startswith("b"):
            eq_position = entry.find("=")
            B = float(entry[eq_position + 1 :])

        if entry.lower().startswith("c"):
            eq_position = entry.find("=")
            C = float(entry[eq_position + 1 :])

        if entry.lower().startswith("j"):
            eq_position = entry.find("=")
            J = int(entry[eq_position + 1 :])

    return (A, B, C, J)
