WHCS Senior Design I Research Report
=====================================

The source files, build scripts, and source images with references for our
Senior Design I report.

For the work-in-progress, you may view the <a href="https://github.com/WHCS-UCF/sd1-report/raw/master/export/latest.pdf">latest build</a>. This is updated sporadically, when needed.

Workflow
=========
Generating the document is as easy as typing `make`. You'll notice that the
document is built twice in order to pickup references and reflect any TikZ
background changes. This could be optimized to parse `pdflatex` output to
search for invalid reference hints.

The document takes a while to build, especially twice, so by using `make draft`
no images are included to speed up the compilation.

Requirements
==============
A working TeX distribution (i.e. MikTeX on windows or TeXLive on *nix), GNU
Make, and a working terminal

<hr />

<img src="https://raw.githubusercontent.com/WHCS-UCF/sd1-report/master/export/title-latest.png" alt="WHCS Title Page" />
