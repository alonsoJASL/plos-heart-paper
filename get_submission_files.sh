 echo "Generating submission files for PLOS ONE..."
 ./rerunpdf.sh manuscript 
 
 ./rerunpdf.sh supplement_main 
 
 ./rerunpdf.sh manuscript
 
 ./rerunpdf.sh supplement_main 


 echo "Final versions"
 ./rerunpdf.sh -f manuscript
 
 ./rerunpdf.sh -f supplement_main
 
 echo "Renaming files for submission..."
 mv manuscript-final.pdf final_submission_changes/plos_manuscript-final.pdf
 
 mv manuscript.pdf final_submission_changes/plos_manuscript-tracked_changes.pdf
 
 mv supplement_main-final.pdf final_submission_changes/plos_supplement.pdf