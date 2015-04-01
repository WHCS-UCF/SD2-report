all:
	pdflatex -draftmode whcs.tex && pdflatex whcs.tex

latest : all
	cp whcs.pdf export/latest.pdf
