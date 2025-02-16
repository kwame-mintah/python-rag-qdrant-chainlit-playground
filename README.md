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

2. Start Qdrant and Ollama services found in [docker-compose.yaml](docker-compose.yaml) and wait for
   both services to be running and Ollama models have been downloaded.

```shell
docker compose up -d
```

3. Ingest data into the Qdrant database

```pycon
python utils/ingest.py
```

4. Confirm Qdrant collection has been created with data ingested via the Web UI @ http://localhost:6333/dashboard

5. Start Chainlit application

```pycon
chainlit run main.py
```

## Environment variables

The following environment variables are used by this project.

| Environment Variable        | Description                       | Default Value                                                                                            |
|-----------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------|
| QDRANT_DATABASE_URL         | The Qdrant Database URL           | http://localhost:6333                                                                                    |
| QDRANT_COLLECTION_NAME      | The of the Qdrant collection name | warframe                                                                                                 |
| OLLAMA_URL                  | The Ollama host URL               | http://localhost:11434                                                                                   |
| OLLAMA_LLM_MODEL            | The Ollama model to use           | deepseek-r1:1.5b                                                                                         |
| WARFRAME_DROP_TABLES_URL    | The Warframe drop tables CDN URL  | https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html |
| HUGGING_FACE_EMBED_MODEL_ID | The Hugging Face embeddings name  | sentence-transformers/all-MiniLM-L6-v2                                                                   |
