from chromadb import PersistentClient
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def configurar_banco():
    DOCUMENTOS = [
        ("jogo-01", "Para salvar o progresso, acesse o menu de opções e clique em Salvar Jogo.", {"categoria": "sistema", "tipo": "save"}),
        ("jogo-02", "O modo multiplayer online suporta até 16 jogadores simultâneos na mesma partida.", {"categoria": "modos_de_jogo", "tipo": "multiplayer"}),
        ("jogo-03", "Para derrotar o dragão de fogo, utilize armas com encantamento de gelo.", {"categoria": "combate", "tipo": "dica"}),
        ("jogo-04", "A nova expansão adiciona três novos mapas e duas classes inéditas: Paladino e Bardo.", {"categoria": "conteudo", "tipo": "dlc"}),
        ("jogo-05", "Caso o jogo feche sozinho, verifique se os drivers da placa de vídeo estão atualizados.", {"categoria": "suporte", "tipo": "crash"}),
        ("jogo-06", "Os pontos de experiência (XP) são ganhos ao completar missões e derrotar inimigos.", {"categoria": "progressao", "tipo": "xp"}),
        ("jogo-07", "É possível alterar a dificuldade da campanha a qualquer momento nas configurações.", {"categoria": "sistema", "tipo": "dificuldade"}),
        ("jogo-08", "A espada lendária pode ser encontrada no fundo da caverna escura no nível 50.", {"categoria": "exploracao", "tipo": "item"}),
        ("jogo-09", "Você precisa de uma assinatura ativa para acessar os servidores competitivos.", {"categoria": "modos_de_jogo", "tipo": "assinatura"}),
        ("jogo-10", "As moedas de ouro virtuais não podem ser trocadas por dinheiro real sob nenhuma circunstância.", {"categoria": "suporte", "tipo": "economia"})
    ]

    print("Baixando e carregando o modelo de embeddings...")
    embedding_fn = SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    
    # 1. Criar uma collection no ChromaDB e inserir os 10 documentos
    client = PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection(
        name="base_jogos",
        embedding_function=embedding_fn
    )

    print("Inserindo documentos no banco...")
    collection.upsert(
        ids=[doc[0] for doc in DOCUMENTOS],
        documents=[doc[1] for doc in DOCUMENTOS],
        metadatas=[doc[2] for doc in DOCUMENTOS]
    )
    print("Banco populado com sucesso!")

if __name__ == "__main__":
    configurar_banco()