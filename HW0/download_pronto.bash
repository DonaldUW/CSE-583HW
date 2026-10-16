mkdir -p pronto
echo "This directory contains Pronto Cycle Share year one open data (Seattle bike share)." > pronto/README.txt
mkdir -p pronto/data
curl -L -o pronto/data/open_data_year_one.zip https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip -o pronto/data/open_data_year_one.zip -d pronto/data
head pronto/data/*.csv
