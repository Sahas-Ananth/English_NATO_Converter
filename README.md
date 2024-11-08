# CLI English-NATO Phonetic Alphabet Converter

A CLI tool that converts normal English to NATO phonetic alphabet or decode from NATO back to English. Useful for clear communication.

## Installation
```bash
# Clone repo
git clone https://github.com/Sahas-Ananth/English_NATO_Converter.git
cd English_NATO_Converter/
# Run: In Linux:
./eng2nato.py --help
# Optional: Add to your path. In Linux:
ln -s "$(pwd)/eng2nato.py ~/.local/bin/eng2nato"
```

## Help
```console
foo@bar$ eng2nato -h
usage: eng2nato [-h] [-d] [-i [INPUT]] [string ...]

Convert normal English to NATO phonetic alphabet or decode from NATO back to
English. Useful for clear communication.

positional arguments:
  string                The string to convert.

options:
  -h, --help            show this help message and exit
  -d, --decode          Decode Flag to convert from NATO back to English.
  -i [INPUT], --input [INPUT]
                        Path to input file. If empty, Defaults to stdin.
```

### Example Usage

Via CLI argument:
```bash
eng2nato The Quick Brown Fox Jumps Over The Lazy Dog
```
Via `stdin`:
```bash
echo "The Quick Brown Fox Jumps Over The Lazy Dog" | eng2nato
# or for interactive conversion: (Enter or <cr> converts the line)
eng2nato
```

Via file input:
```bash
eng2nato -i # <PATH TO FILE>
```

## Current Mapping

| Letter | NATO Phonetic Equivalent |
|--------|---------------------------|
| a      | Alfa                      |
| b      | Bravo                     |
| c      | Charlie                   |
| d      | Delta                     |
| e      | Echo                      |
| f      | Foxtrot                   |
| g      | Golf                      |
| h      | Hotel                     |
| i      | India                     |
| j      | Juliett                   |
| k      | Kilo                      |
| l      | Lima                      |
| m      | Mike                      |
| n      | November                  |
| o      | Oscar                     |
| p      | Papa                      |
| q      | Quebec                    |
| r      | Romeo                     |
| s      | Sierra                    |
| t      | Tango                     |
| u      | Uniform                   |
| v      | Victor                    |
| w      | Whiskey                   |
| x      | Xray                      |
| y      | Yankee                    |
| z      | Zulu                      |
| (space)| (space)                   |
