all:
	pdflatex -draftmode whcs.tex && pdflatex whcs.tex

# NOTE: when compiling, you MUST NOT mix different draft, final, normal
# compiles. The AUX file will be messed up
draft:
	pdflatex -draftmode "\def\enabledraft{}\input{whcs.tex}" && \
	pdflatex "\def\enabledraft{}\input{whcs.tex}"

final:
	pdflatex -draftmode "\def\enablefinal{}\input{whcs.tex}" && \
	pdflatex "\def\enablefinal{}\input{whcs.tex}"

final-print:
	pdflatex -draftmode "\def\enablefinal{}\def\printable{}\input{whcs.tex}" && \
	pdflatex "\def\enablefinal{}\def\printable{}\input{whcs.tex}"

quick:
	pdflatex -interaction=batchmode "\def\enabledraft{}\input{whcs.tex}"

clean:
	-rm -f *.aux *.log

latest: clean final
	cp whcs.pdf export/latest.pdf

latest-print: clean final-print
	cp whcs.pdf export/latest-print.pdf
