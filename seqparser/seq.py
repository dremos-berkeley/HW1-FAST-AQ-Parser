# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    rna_seq = ""
    if reverse:
        for nuc in seq.upper():
            if nuc in TRANSCRIPTION_MAPPING:
                rna_seq += TRANSCRIPTION_MAPPING[nuc]
        rna_seq = rna_seq[::-1]
    else:
        for nuc in seq.upper():
            if nuc in TRANSCRIPTION_MAPPING:
                rna_seq += TRANSCRIPTION_MAPPING[nuc]
    return rna_seq

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # Hey this is my comment
    # Again!
    return transcribe(seq, reverse=True)