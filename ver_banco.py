from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def verificar_banco():
    embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    client = PersistentClient(path="chroma_db")
    
    # Usa get_collection em vez de get_or_create pois o banco já deve existir
    collection = client.get_collection(
        name="base_jogos",
        embedding_function=embedding_fn
    )

    # Etapa 2: Mostrar quantos documentos foram armazenados
    print("--- ETAPA 2: Contagem de Documentos ---")
    print(f"Documentos indexados: {collection.count()}")

    # Etapa 3: Recuperar um embedding e demonstrar dimensões
    print("\n--- ETAPA 3: Dimensões do Embedding ---")
    texto_exemplo = ["Demonstrando dimensões"]
    vetor = embedding_fn(texto_exemplo)[0]
    print(f"O embedding gerado possui {len(vetor)} dimensões.")

if __name__ == "__main__":
    verificar_banco()