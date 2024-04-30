#!/bin/bash

#wget -O GQL.g4 https://raw.githubusercontent.com/opengql/grammar/main/GQL.g4?token=GHSAT0AAAAAACRTZK7WBPWK5LNQKESWTQKQZRPQMYQ

# Sprawdź czy pobranie pliku zakończyło się sukcesem
#if [ $? -eq 0 ]; then
#    echo "Success: current version of GQL.g4 downloaded"
#else
#    echo "Error: current version of GQL.g4 is not downloaded"
#    exit 1
#fi

gh repo clone opengql/grammar
cp -f ./grammar/GQL.g4 .
rm -rf grammar
java -jar rrd-antlr4-0.1.2.jar GQL.g4
tidy -q --tidy-mark no -ashtml --doctype html5 ./output/GQL/index.html > ./output/GQL/temp.html 2>/dev/null
rm ./output/GQL/index.html
python3 clean.py ./output/GQL/temp.html > ./output/GQL/index.html
rm ./output/GQL/temp.html
echo "You can find index.html in ./output/GQL/"
