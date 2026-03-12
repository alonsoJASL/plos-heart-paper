#!/bin/bash
usage="
$(basename "$0") [-h] [-d] [-f] [-c] BASENAME -- compile LaTeX to PDF
  -f  Final mode: hides tracked changes, outputs BASENAME-final.pdf
  -d  Debug mode: interactive, stops on errors
  -c  Clean all auxiliary files for BASENAME (both draft and final), then exit
"

finalmode=0
debugmode=0
cleanmode=0
while getopts ':cdfh' option; do
    case "$option" in
        h) echo "$usage"; exit ;;
        d) debugmode=1; echo "DEBUG MODE ON" ;;
        f) finalmode=1; echo "FINAL MODE ON" ;;
        c) cleanmode=1 ;;
        \?) echo "$usage" >&2; exit 1 ;;
    esac
done
shift $((OPTIND-1))

if [ -z "$1" ]; then
    echo "Error: no basename supplied." >&2
    echo "$usage" >&2
    exit 1
fi

BASENAME=$1

if [ "$cleanmode" == "1" ]; then
    AUX_EXTS="aux bbl blg log out toc loc soc synctex.gz"
    for ext in $AUX_EXTS; do
        rm -f "${BASENAME}.${ext}" "${BASENAME}-final.${ext}"
    done
    printf "Cleaned auxiliary files for '${BASENAME}' (draft and final).\n"
    exit 0
fi

if [ "$finalmode" == "1" ]; then
    echo '\finaltrue' > rerun_mode.tex
    JOBNAME="${BASENAME}-final"
else
    echo '\finalfalse' > rerun_mode.tex
    JOBNAME="${BASENAME}"
fi

# Clean aux files for this jobname only
rm -f "${JOBNAME}.aux" "${JOBNAME}.bbl" "${JOBNAME}.blg" \
       "${JOBNAME}.log" "${JOBNAME}.out" "${JOBNAME}.toc"

run_latex() {
    pdflatex -synctex=1 -interaction=${1} -jobname="${JOBNAME}" "${BASENAME}"
}

if [ "$debugmode" == "0" ]; then
    run_latex nonstopmode
    bibtex "${JOBNAME}"
    run_latex nonstopmode
    run_latex nonstopmode
else
    run_latex errorstopmode
    bibtex "${JOBNAME}"
    run_latex errorstopmode
    run_latex errorstopmode
fi

printf "\nCompiling done! Output: ${JOBNAME}.pdf\n"
