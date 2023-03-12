# Bash script to ingest data
# This involves scraping the data from the web and then cleaning up and putting in Weaviate.
# Error if any command fails
set -e
# downloaded via moba-xterm, as windows does not have wget utility
#if [ ! -d langchain.readthedocs.io ]; then
#	echo downloading docs
#	wget -r -A.html https://langchain.readthedocs.io/en/latest/
#fi
python ingest.py
