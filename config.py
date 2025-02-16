from pydantic import Field
from pydantic_core import Url
from pydantic_settings import BaseSettings


class EnvironmentVariables(BaseSettings):
    QDRANT_DATABASE_URL: Url = Field(
        description="The Qdrant Database URL", default="http://localhost:6333"
    )
    QDRANT_COLLECTION_NAME: str = Field(
        description="The of the Qdrant collection name", default="warframe"
    )
    OLLAMA_URL: Url = Field(
        description="The Ollama host URL", default="http://localhost:11434"
    )
    OLLAMA_LLM_MODEL: str = Field(
        description="The Ollama model to use", default="deepseek-r1:1.5b"
    )
    WARFRAME_DROP_TABLES_URL: Url = Field(
        description="The Warframe drop tables CDN URL",
        default="https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html",
    )
    HUGGING_FACE_EMBED_MODEL_ID: str = Field(
        description="The Hugging Face embeddings name",
        default="sentence-transformers/all-MiniLM-L6-v2",
    )
