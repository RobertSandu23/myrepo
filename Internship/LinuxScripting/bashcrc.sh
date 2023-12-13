#!/bin/bash

file1="bashcrc"
file2="bashcrc.txt"
if [ -e "$file1" ] && [ -e "$file2" ]; then

	sed -i -e "/^export ARTIFACTORY_API_KEY=/ s/=.*/=$(grep '^ARTIFACTORY_API_KEY=' $file2 | cut -d'=' -f2)/" "$file1"
	sed -i -e "/^export ARTIFACTORY_USER=/ s/=.*/=$(grep '^export ARTIFACTORY_USER=' $file2 | cut -d'=' -f2)/" "$file1"
	# s/=.*/    -> takes all characters (.*) after the given character (=) and substitute with... (=)
        # grep at the data from file2(txt file) use pipe to make the output an input, make '=' a delimiter(-d'='), cut and copy all from the right side of delimiter (-f2)
	echo "Done. Check your bashh file"

else
	echo "No such files"
fi
