# 🎮 Busca Semântica com ChromaDB — Base de Jogos

Este projeto demonstra a implementação de um **Banco de Dados Vetorial (Vector Database)** utilizando o **ChromaDB** e o modelo de *embeddings* `all-MiniLM-L6-v2` em Python. 

A aplicação armazena uma base de conhecimento sobre mecânicas de jogos e realiza buscas por **proximidade de significado (semântica)**, permitindo responder a dúvidas dos usuários mesmo quando as palavras exatas da pergunta não constam nos documentos armazenados.

---

## 🚀 Tecnologias Utilizadas

* **[Python 3.10+](https://www.python.org/)** — Linguagem principal do projeto.
* **[ChromaDB](https://www.trychroma.com/)** — Banco de dados vetorial leve e persistente.
* **[Sentence-Transformers](https://www.sbert.net/)** — Modelo `all-MiniLM-L6-v2` para geração de vetores de 384 dimensões.

---

## 📂 Estrutura do Projeto

```
projeto-chroma-jogos/
├── banco.py        # Etapa 1: Conecta ao ChromaDB, cria a collection e popula os documentos
├── ver_banco.py    # Etapas 2 e 3: Inspeciona a quantidade de registros e dimensões do vetor
├── main.py         # Etapas 4, 5 e 6: Executa consultas semânticas e busca com filtro WHERE
├── README.md       # Documentação do projeto
└── chroma_db/      # Diretório criado automaticamente para persistência dos dados
```


### Como instalar as dependências?
```bash
pip install chromadb sentence-transformers
```

---

## ▶️ Como Executar

A execução do projeto deve seguir a ordem lógica abaixo:

### Passo 1: Popular o banco de dados (`banco.py`)
Cria o banco de dados persistente na pasta `chroma_db/` e insere os 10 documentos de jogos.
```bash
python banco.py
```

### Passo 2: Validar o banco de dados (`ver_banco.py`)
Verifica se os 10 documentos foram armazenados e confirma que o vetor possui 384 dimensões.
```bash
python ver_banco.py
```

### Passo 3: Executar buscas e filtros semânticos (`main.py`)
Realiza as perguntas de teste, calcula as distâncias semânticas e executa a consulta com filtro de metadados (`categoria`).
```bash
python main.py
```

---

## 📊 Análise dos Resultados das Consultas

A busca vetorial calcula a **distância** entre o vetor da pergunta e os vetores dos documentos. Quanto **menor a distância**, **maior é a proximidade de significado**.

| Pergunta do Usuário | ID Retornado (Top-1) | Trecho do Documento | Distância | Diagnóstico |
| :--- | :---: | :--- | :---: | :--- |
| *"Como não perder o que já joguei até agora?"* | `jogo-01` | *"Para salvar o progresso, acesse o menu de pausa..."* | `0.4334` | **Excelente:** Relacionou "não perder" com "salvar progresso". |
| *"Quantas pessoas podem participar pela internet?"* | `jogo-02` | *"O modo multiplayer online suporta até 4 jogadores..."* | `0.4280` | **Excelente:** Relacionou "pessoas/internet" com "jogadores/online". |
| *"Onde acho a arma mais forte?"* | `jogo-07` | *"O jogo roda a 60 FPS no modo desempenho..."* | `0.5430` | **Incerteza:** Distância alta (> 0.50). O modelo não isolou a resposta correta devido ao vocabulário. |

### 🎯 Consulta com Filtro (`WHERE`)
* **Pergunta:** *"O que eu ganho matando monstros?"*
* **Filtro Aplicado:** `where={"categoria": "progressao"}`
* **Resultado:** `jogo-06` — *"Os pontos de experiência (XP) são ganhos ao completar missões e derrotar inimigos."*
* **Explicação:** O filtro descarta documentos fora da categoria e a busca semântica conecta *"matando monstros"* com *"derrotar inimigos"*.

---

## 🧠 Como Funciona a Busca Semântica?

1. **Vetorização (Embedding):** Cada texto é convertido em uma lista de 384 números flutuantes (coordenadas numéricas num espaço vetorial multidimensional).
2. **Proximidade Semântica:** Frases com significados semelhantes são posicionadas próximas umas das outras no espaço vetorial, independentemente das palavras utilizadas.
3. **Cálculo de Distância:** Na consulta, o ChromaDB converte a pergunta em vetor e calcula a distância Euclidiana ou de Cosseno até os vetores armazenados, retornando os resultados mais próximos.

