all:
	pdflatex -draftmode whcs.tex && pdflatex whcs.tex

draft:
	pdflatex "\def\enabledraft{}\input{whcs.tex}"

clean:
	-rm -f *.aux *.log

latest : all
	cp whcs.pdf export/latest.pdf
