# SQL Insert Generator

## Overview
This Python script simplifies the process of creating SQL insert statements from plain text files. It reads a specified file, processes its content line by line to extract values, and generates a complete SQL insert command saved to a new file. This tool is especially useful for bulk inserting data into a database table from desktop-stored files.

## Features
- **Easy Extraction**: Automatically reads and processes text files to extract values for SQL insertion.
- **Flexible Input**: Customize the input file and target database table directly from the script.
- **Output File Creation**: Generates a ready-to-execute SQL file with insert commands on the desktop.

## Prerequisites
Before running this script, ensure you have Python installed on your system. You can download Python from [here](https://www.python.org/downloads/).

## Usage
To use this script, you need to modify the `nombre_archivo` and `nombre_tabla` variables in the script to reflect your specific use case:

1. `nombre_archivo`: Set this to the name of your text file (e.g., 'example.txt') that you want to process. Make sure this file is located on your desktop.
2. `nombre_tabla`: Set this to the name of the database table where the data should be inserted (e.g., 'your_table_name').

### Running the Script
Navigate to the directory containing the script and run it using Python from your command line:

```bash
python sql-consultas.py
