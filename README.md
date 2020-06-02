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