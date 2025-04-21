# 🛝 Retrieval-Augmented Generation (RAG) Qdrant Chainlit Playground

![python](https://img.shields.io/badge/python-3.12.0-informational)

As the name of the repository suggests, it's just a [_playground_](https://dictionary.cambridge.org/dictionary/english/playground).
A place to better understand creating a Retrieval-Augmented Generation (RAG) focused on a specified knowledge base.

## Prerequisites

1. [Qdrant](https://qdrant.tech/documentation/quickstart/)
2. [Chainlit](https://docs.chainlit.io/get-started/overview)
3. [Docker for desktop](https://docs.docker.com/desktop/)
4. [Ollama](https://ollama.com/download)

# Usage

1. Install python packages used for the project

```pycon
pip install -r requirements.txt
```

2. Start [Qdrant](https://qdrant.tech/documentation/quickstart/) vector search database via docker

```shell
docker run -p 6333:6333 -p 6334:6334 \
    -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
    qdrant/qdrant
```

3. Start [Ollama](https://ollama.readthedocs.io/en/quickstart/) and download large language models needed, waiting for the download to complete

```shell
ollama run deepseek-r1:1.5b
```

4. Ingest data into the Qdrant database

```pycon
python utils/ingest.py
```

5. Confirm Qdrant collection has been created with data ingested via the Web UI @ http://localhost:6333/dashboard

6. Start Chainlit application

```pycon
chainlit run main.py
```

## Environment variables

The following environment variables are used by this project.

| Environment Variable        | Description                                      | Default Value                          |
|-----------------------------|--------------------------------------------------|----------------------------------------|
| QDRANT_DATABASE_URL         | The Qdrant Database URL                          | http://localhost:6333                  |
| QDRANT_COLLECTION_NAME      | The name of the Qdrant collection                | warframe                               |
| OLLAMA_URL                  | The Ollama host URL                              | http://localhost:11434                 |
| OLLAMA_LLM_MODEL            | The Ollama model to use                          | deepseek-r1:1.5b                       |
| WIKIPEDIA_PAGE_API_URL      | The WikiMedia page API to be queried for parsing | https://wiki.warframe.com/api.php      |
| HUGGING_FACE_EMBED_MODEL_ID | The Hugging Face embeddings name                 | sentence-transformers/all-MiniLM-L6-v2 |

# Running via Docker Compose

An alternative way of running the stack involves using [docker compose](https://docs.docker.com/compose/), the [`docker-compose.yaml`](docker-compose.yaml)
contains the services needed to run this project, such as starting chainlit, qdrant and ollama.

1. In the root directory start all the services.

```shell
docker compose up -d
```

2. Access the services on the following endpoint in your browser. chainlit (http://localhost:8000/) and qdrant (http://localhost:6333/dashboard)
3. An _optional_ step to run is enabling GPU usage via docker compose, you will need to uncomment out the following lines
   in the yaml found under the Ollama service, providing better performance with large language models (LLM) models.

```yaml
...
#  Enable GPU support using host machine
#  https://docs.docker.com/compose/how-tos/gpu-support/
 deploy:
   resources:
     reservations:
       devices:
         - driver: nvidia
           count: all
           capabilities: [ gpu ]
```
