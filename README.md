# godzilla-sina
SINA Godzilla project, analysis of stack exchange data dumps (https://archive.org/details/stackexchange).


[download csv files](data/download_csvs.md)
[download gaming tsv files](data/download_gaming.md)


# neo4j

running neo4j docker container

```
docker run \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=$HOME/neo4j/data:/data \
    neo4j
```

```
docker run \
     --name testneo4j \
     -p7474:7474 -p7687:7687 \
     -d \
     -v 'c:\Users\mutaz\neo4j\data':/data \
     -v 'c:\Users\mutaz\neo4j\logs':/logs \
     -v 'c:\Users\mutaz\neo4j\import':/var/lib/neo4j/import \
     -v 'c:\Users\mutaz\neo4j\plugins':/plugins \
     --env NEO4J_AUTH=neo4j/test \
     neo4j:latest
```

Loading data into neo4j: 
- [import data into neo4j](https://neo4j.com/blog/import-10m-stack-overflow-questions/)
- [neo4j etl](https://neo4j.com/developer/guide-importing-data-and-etl/#northwind-graph-model)
- [csv import tool](https://neo4j.com/docs/operations-manual/current/tools/import/)
- [import csv data into neo4j](https://neo4j.com/developer/guide-import-csv/#batch-importer)


to connect to running neo4j docker container and use the admin tools 

```
docker container exec -it testneo4j bash
```

## neo4j import tool 

* Syntax of `neo4j-admin import` command: (https://neo4j.com/docs/operations-manual/current/tools/import/syntax/)
*  CSV file header format: (https://neo4j.com/docs/operations-manual/current/tools/import/file-header-format/)
* command options: (https://neo4j.com/docs/operations-manual/current/tools/import/options/)