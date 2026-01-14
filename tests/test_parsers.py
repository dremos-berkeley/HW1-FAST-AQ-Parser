# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    # Test reading the example fasta file
    parser = FastaParser("data/test.fa")

    records = list(parser)

    # Check that we got records
    assert len(records) > 0, "Parser should read at least one record"

    # Check that each record is a tuple of (header, sequence)
    for i, record in enumerate(records):
        assert len(record) == 2, f"Record {i}: Each FASTA record should have 2 elements (header, sequence)"
        header, sequence = record

        # Verify header is a non-empty string
        assert isinstance(header, str), f"Record {i}: Header should be a string"
        assert len(header) > 0, f"Record {i}: Header should not be empty"

        # Verify sequence is a non-empty string with valid DNA bases
        assert isinstance(sequence, str), f"Record {i}: Sequence should be a string"
        assert len(sequence) > 0, f"Record {i}: Sequence should not be empty"
        assert all(base in "ACGT" for base in sequence), f"Record {i}: Sequence should only contain A, C, G, T"

    # Check first record specifically
    header1, seq1 = records[0]
    assert header1 == "seq0", f"First header should be 'seq0', got '{header1}'"

    # Check that we can iterate through multiple records
    assert len(records) >= 2, "Should have at least 2 records to test"
    header2, seq2 = records[1]
    assert header2 == "seq1", f"Second header should be 'seq1', got '{header2}'"

    # Test edge case: blank file
    with pytest.raises(ValueError):
        parser_blank = FastaParser("tests/blank.fa")
        list(parser_blank)  # Should raise error for empty file


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    # Test that FastaParser correctly parses fasta format
    parser = FastaParser("data/test.fa")

    # Get first record
    for record in parser:
        header, sequence = record
        assert isinstance(header, str), "Header should be a string"
        assert isinstance(sequence, str), "Sequence should be a string"
        assert not header.startswith(">"), "Header should not include '>' character"
        break


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads
    in the example Fastq File.
    """
    # Test reading the example fastq file
    parser = FastqParser("data/test.fq")

    # Convert iterator to list to check all records
    records = list(parser)

    assert len(records) > 0, "Parser should read at least one record"

    # Check that each record contains (header, sequence, quality)
    for i, record in enumerate(records):
        assert len(record) == 3, f"Record {i}: Each FASTQ record should have 3 elements (header, sequence, quality)"
        header, sequence, quality = record

        # Verify header is a non-empty string
        assert isinstance(header, str), f"Record {i}: Header should be a string"
        assert len(header) > 0, f"Record {i}: Header should not be empty"

        # Verify sequence is a non-empty string with valid DNA bases
        assert isinstance(sequence, str), f"Record {i}: Sequence should be a string"
        assert len(sequence) > 0, f"Record {i}: Sequence should not be empty"
        assert all(base in "ACGT" for base in sequence), f"Record {i}: Sequence should only contain A, C, G, T"

        # Verify quality string
        assert isinstance(quality, str), f"Record {i}: Quality should be a string"
        assert len(quality) > 0, f"Record {i}: Quality should not be empty"

        # Check that quality and sequence have same length
        assert len(sequence) == len(quality), f"Record {i} ({header}): Sequence and quality must be same length"

    # Check first record specifically
    header1, seq1, qual1 = records[0]
    assert header1 == "seq0", f"First header should be 'seq0', got '{header1}'"

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    # Test that FastqParser correctly parses fastq format
    parser = FastqParser("data/test.fq")

    # Get first record
    for record in parser:
        header, sequence, quality = record
        assert isinstance(header, str), "Header should be a string"
        assert isinstance(sequence, str), "Sequence should be a string"
        assert isinstance(quality, str), "Quality should be a string"
        assert not header.startswith("@"), "Header should not include '@' character"
        assert len(sequence) == len(quality), "Sequence and quality must be same length"
        break