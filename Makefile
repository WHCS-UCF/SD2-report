all:
	pdflatex -draftmode whcs.tex && pdflatex whcs.tex

draft:
	pdflatex -draftmode whcs.tex && pdflatex "\def\enabledraft{}\input{whcs.tex}"

final:
	pdflatex -draftmode whcs.tex && pdflatex "\def\enablefinal{}\input{whcs.tex}"

quick:
	pdflatex "\def\enabledraft{}\input{whcs.tex}"

clean:
	-rm -f *.aux *.log

latest : all
	cp whcs.pdf export/latest.pdf
