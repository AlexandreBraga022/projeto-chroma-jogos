from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def main() -> None:
    embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    client = PersistentClient(path="chroma_db")
    collection = client.get_collection(
        name="base_jogos",
        embedding_function=embedding_fn
    )
    
    print("--- ETAPAS 4 e 5: Consultas de Busca Semântica ---")
    # ETAPA 4: Definindo as 3 perguntas diferentes
    perguntas = [
        "Como não perder o que já joguei até agora?", 
        "Quantas pessoas podem participar pela internet?", 
        "Onde acho a arma mais forte?" 
    ]
    # O método query gera o embedding da pergunta e busca os 3 mais próximos (Top-3)
    for i, pergunta in enumerate(perguntas, 1):
        print(f"\nPergunta {i}: '{pergunta}'")
        
        resultado = collection.query(
            query_texts=[pergunta],
            n_results=3,
            include=["documents", "metadatas", "distances"]
        )
        # ETAPA 5: Imprimindo ID, Documento (Trecho), Metadata e Distância
        for id_doc, texto, metadata, distancia in zip(
            resultado["ids"][0],
            resultado["documents"][0],
            resultado["metadatas"][0],
            resultado["distances"][0]
        ):
            print(f"  - ID: {id_doc}")
            print(f"    Trecho: {texto}")
            print(f"    Metadata: {metadata}")
            print(f"    Distância: {distancia:.4f}")

    print("\n--- ETAPA 6: Consulta com Filtro (WHERE) ---")
    pergunta_filtro = "O que eu ganho matando monstros?"
    resultado_filtro = collection.query(
        query_texts=[pergunta_filtro],
        n_results=2,
        where={"categoria": "progressao"},
        include=["documents", "metadatas", "distances"]
    )

    print(f"Pergunta filtrada (categoria='progressao'): '{pergunta_filtro}'")
    for texto, metadata in zip(resultado_filtro["documents"][0], resultado_filtro["metadatas"][0]):
        print(f"  - Documento retornado: {texto}")
        print(f"    Metadata: {metadata}")

if __name__ == "__main__":
    main()