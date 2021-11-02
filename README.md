# x_count

A standalone Python tool that counts the number of 'X' characters per sequence in a multi-FASTA file and return the results in CSV format.

## How to install

```bash
gh repo clone ruwaa-mohamed/x_count
```

## How to use

```bash
python3 x_count/x_count.py -f <path/to/file_in.fasta> -o <path/to/file_out.csv>
```

### Example

```bahs
python3 x_count/x_count.py -f input.fasta -o output.csv
```

### Main Arguments

* `-f <fasta_file>`: the path to the input FASTA file. It can handle multi-FASTA file where each record is composed of two lines (header and sequence). It doesn't work on FASTA file with sequence spanning multiple lines (fixed-width FASTA files).
* `-o <output_file>`: the path to the output CSV file.
* `-h | --help`: to print the help message of the tool (the user manual). 

### Date last modified

Nov. 02, 2021