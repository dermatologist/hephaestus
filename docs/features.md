# Features

## Command line arguments


| Command | Alternate | Description |
| --- | --- | --- |
| --schema | -s | Database schema to use |
| --emr | -e | EMR/Database to use as input for ETL |
| --num | -n | Top n depending on the context |
| --cui | -c | CUIs to use as input (multiple) |
| --cdm | -d | CDM concepts to use as input (multiple) |
| --fun | -f | Function to execute |
| --cid | -i | Set of IDs to use (Contextual |
| --fun | -f | Function to execute (similar/create/etl/anchor |


## F1: Create CDM schema
* Hephaestus can create a CDM schema for you

```text

python main.py -s myschema -f create


```

## F2: Expand concept set with anchors from Cui2Vec
* [See this article:](https://www.ncbi.nlm.nih.gov/pubmed/28815104)
* In Hephaestus anchors are identified using [Cui2Vec](http://cui2vec.dbmi.hms.harvard.edu)
* Integrates with ATLAS

### How to use 

```bash
python main.py -s ohdsi -i 2 -n 20 -f anchor

```
-s is for schema
-i is the concept_set_id in ATLAS
-n is the Topn
-f function name to execute, anchor in this case.

## F3: Find similar concepts using Cui2Vec

```bash

python main.py -d 140168 -n 20 -f similar

```