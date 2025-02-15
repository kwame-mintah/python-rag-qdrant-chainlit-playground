from pydantic import Field
from pydantic_core import Url
from pydantic_settings import BaseSettings


class EnvironmentVariables(BaseSettings):
    QDRANT_DATABASE_URL: Url = Field(
        description="The Qdrant Database URL", default="http://localhost:6333"
    )
    OLLAMA_URL: Url = Field(
        description="The Ollama host URL", default="http://localhost:11434"
    )
    WARFRAME_DROP_TABLES_URL: Url = Field(
        description="The Warframe drop tables CDN URL",
        default="https://warframe-web-assets.nyc3.cdn.digitaloceanspaces.com/uploads/cms/hnfvc0o3jnfvc873njb03enrf56.html",
    )
