# WHCS Senior Design I Research Report

The source files, build scripts, and source images with references for our
UCF Senior Design I report.

For the work-in-progress, you may view the [latest build](/export/latest.pdf?raw=true)
There is also a [printable version](/export/latest-printable?raw=true).
Page count is determined from the printable version as there are no fancy headings that might not fly so well.
These are updated when there are major releases and for periodic peer review.

### Authors

Grant Hernandez | Jimmy Campbell | Joesph Love
:--------------:|:--------------:|:------------:
Computer Engineer | Computer Engineer | Electrical Engineer

Document typeset by Grant Hernandez using ViM with the help of writer2latex for Google Drive -> ODT -> TeX conversion.
All figures are the copyrights of the members of this group unless stated otherwise.
All trademarks of mentioned companies are referenced for educational purposes.

## Requirements
A working TeX distribution (i.e. MikTeX on windows or TeXLive on *nix), GNU
Make, and a working terminal.

## Workflow
Generating the document is as easy as typing `make`. You'll notice that the
document is built twice in order to pickup references and reflect any TikZ
background changes. This could be optimized to parse `pdflatex` output to
search for invalid reference hints.

The document takes a while to build, especially twice, so by using `make draft`
no images are included to speed up the compilation. Also, the TikZ section
headers slow down the build significantly. These are only included in the
online version of the document.

## Page Count
Page count is the main measure of completion for this project. We need 90 pages
of solid material. Page count is decreased when images are deemed to be
extraneous and when whitespace is wasted due to LaTeX figure placement.

Writing more than 90 pages is a goal for us in order to avoid being under
due to the lost pages.

<hr/>

![Title Page](/export/title-latest.png?raw=true)
