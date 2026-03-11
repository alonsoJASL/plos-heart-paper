#!/bin/bash
usage="
$(basename "$0") [-h] [-d] [-f] -- compile LaTeX to PDF
  -f  Final mode (hides tracked changes, shows clean text)
  -d  Debug mode (interactive, stops on errors)
"

finalmode=0
debugmode=0
while getopts ':dfh' option; do
    case "$option" in
        h) echo "$usage"; exit ;;
        d) debugmode=1; echo "DEBUG MODE ON" ;;
        f) finalmode=1; echo "FINAL MODE ON" ;;
        \?) echo "$usage" >&2; exit 1 ;;
    esac
done
shift $((OPTIND-1))

# Build pretex string
if [ "$finalmode" == "1" ]; then
    PRETEX="\finaltrue"
else
    PRETEX="\finalfalse"
fi

PDFLATEX_OPTS="-synctex=1 -interaction=nonstopmode -usepretex=\"$PRETEX\""

mv $1.tex ../
rm -f $1.aux $1.bbl $1.blg $1.log $1.out $1.toc
mv ../$1.tex ./

run_latex() {
    pdflatex -synctex=1 -interaction=${1} -usepretex="$PRETEX" $2
}

if [ "$debugmode" == "0" ]; then
    run_latex nonstopmode $1
    bibtex $1
    run_latex nonstopmode $1
    run_latex nonstopmode $1
else
    run_latex errorstopmode $1
    bibtex $1
    run_latex errorstopmode $1
    run_latex errorstopmode $1
fi

printf "\nCompiling done!\n"