#!/bin/bash

file="log.txt"
log_output="log_output.txt"
replace_word="AUTOMATION"

if [ -e "$file" ]; then

    for line in {63..72}; do
        word=$(sed -n "${line}p" "${file}" | awk '{print $6}')
#take the 6th word (awk '{print $6} from from each line from file

	letter=$(echo "${replace_word}" | cut -c$((line-62)))
#take every letter from AUTOMATION. cut and take one letter for each line (for 1st letter its first line(63) 63-62=1, next iteretion is line 64 (second line) so 64-62=2 which means second letter and so on..
        
	sed -i "${line}s/\<${word}\>/${letter}/" "${file}"
#sed -insert on specific ${line} substitute original word (\<$word}\>) with the processed letter (/${letter}/) in the log.txt ${file}
        
	echo "${word} was replaced with the letter: ${letter}" >> "${log_output}"
    done

    echo "Check the new logfile: '${log_output}'"

else
    echo "File '$file' not found"
fi

