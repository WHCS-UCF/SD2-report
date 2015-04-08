all:
	pdflatex -draftmode whcs.tex && pdflatex whcs.tex

# NOTE: when compiling, you MUST NOT mix different draft,final, normal
# compiles. The AUX file will be messed up
draft:
	pdflatex -draftmode "\def\enabledraft{}\input{whcs.tex}" && pdflatex "\def\enabledraft{}\input{whcs.tex}"

final:
	pdflatex -draftmode "\def\enablefinal{}\input{whcs.tex}" && pdflatex "\def\enablefinal{}\input{whcs.tex}"

quick:
	pdflatex "\def\enabledraft{}\input{whcs.tex}"

clean:
	-rm -f *.aux *.log

latest : all
	cp whcs.pdf export/latest.pdf
