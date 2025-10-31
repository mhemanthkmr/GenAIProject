CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS embeddings_store (
    id SERIAL PRIMARY KEY,
    chunk TEXT,
    embedding vector(3072)
)

select * from embeddings_store;