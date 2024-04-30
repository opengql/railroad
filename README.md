# GQL Railroad Diagrams

## Brief Description
The `GQL Railroad Diagrams` project aims to generate clear railroad diagrams for the GQL grammar, which can be helpful for developers working with this query language. These diagrams are generated using ANTLR4, tidy, and Python3 tools, and are then made available through GitHub Pages.

## Dependencies
The project uses the following tools:
- RRD for ANTLR4, a tool for generating diagrams from ANTLR4 grammar files. [RRD for ANTLR4 GitHub](https://github.com/bkiers/rrd-antlr4)
- tidy, a tool for converting XHTML to HTML5 and cleaning up the code. [tidy Official Website](https://www.html-tidy.org/)
- Python3, used for additional cleaning and customization of the output HTML.

## Workflow
1. Download the GQL grammar file (`GQL.g4`) from the `opengql/grammar` repository.
2. Convert the `GQL.g4` file to XHTML using the RRD for ANTLR4 tool.
3. Convert the generated XHTML to HTML5 and clean it using the tidy tool.
4. Further clean and customize the output HTML using the Python script `clean.py`, adding CSS and other elements.
5. Deploy the page on GitHub Pages.

## Getting Started
To use this project, clone the repository and install the required dependencies. Follow the described workflow to generate and deploy your own railroad diagrams for the GQL grammar.

