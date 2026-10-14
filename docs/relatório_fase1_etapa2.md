# MESAFARTAI - Relatório de Execução da Fase 1 / Etapa 2 (AC-3)
**Motor NLU e Trava de Threshold**

**Projeto:** MESAFARTAI - Logística e Inteligência Assistiva no Combate à Fome  
**Grupo NPC:**
- Pedro Vitor da Silva Oliveira (RA: 130785)
- Nicollas Hardt Urnau (RA: 117763)
- Caio Gabriel Souza dos Santos (RA: 118316)

---

## 1. Quantidade de árvores utilizadas no motor NLU
No módulo `src/nlu.py`, foram configuradas e utilizadas **80 árvores de decisão** (`n_estimators=80`), instanciadas na criação do classificador:

```python
self.classifier = RandomForestClassifier(n_estimators=80, random_state=42)
```

O parâmetro `random_state=42` foi definido para garantir a reprodutibilidade dos resultados durante o treinamento do comitê de árvores.

---

## 2. Valor de threshold utilizado no processo de limiar de confiança
O valor de limiar de confiança adotado foi de **0.60** (ou seja, **60%**):

```python
def __init__(self, limiar_threshold=0.60):
    self.limiar_threshold = limiar_threshold
```

Qualquer predição cuja confiança máxima seja inferior a 0.60 ou cuja classe identificada seja `"fora_de_escopo"` é automaticamente interceptada pela trava de segurança, acionando a mensagem padrão de **Fallback**.

---

## 3. Resultado da primeira execução

A execução do arquivo `src/nlu.py` gerou a seguinte saída no terminal:

```text
 [NLU] Modelo Random Forest e Vetorizador TF-IDF treinados com sucesso!

--- BATERIA DE TESTES DE ESTRESSE NLU ---

Entrada: 'Tenho 30 kg de banana para doar'
Intenção: cadastrar_doacao | Confiança: 0.93
Retorno: Intenção 'cadastrar_doacao' identificada com 92.5% de confiança.

Entrada: 'Nossa instituição precisa de mantimentos'
Intenção: fallback | Confiança: 0.41
Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?

Entrada: 'Qual é a receita de bolo de cenoura?'
Intenção: fallback | Confiança: 0.49
Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?

Entrada: 'coisa comida doar la'
Intenção: fallback | Confiança: 0.42
Retorno: Desculpe, não consegui entender com clareza o seu pedido. 
Você pode refazer a mensagem informando se deseja **doar alimentos** ou **solicitar doações para uma ONG**?
```

---

## 4. Como melhorar os resultados dos testes e aumentar o grau de confiança

Para elevar a precisão e a confiança do motor de NLU, podem ser implementadas as seguintes melhorias:

1. **Aumento e Enriquecimento do Dataset de Treino (Data Augmentation):**
   - Na frase de teste *"Nossa instituição precisa de mantimentos"*, o modelo gerou fallback (confiança de 0.41) porque as palavras *"instituição"* e *"mantimentos"* não constavam com peso suficiente nos dados de treino.
   - Expandir a base com sinônimos frequentes no contexto de doações (ex.: mantimentos, gêneros alimentícios, cestas, marmitas, fardos, hortifrúti, asilo, abrigo, instituição).

2. **Pré-processamento Textual Avançado (NLP):**
   - **Stemming ou Lemmatização (NLTK / spaCy):** Reduzir palavras ao radical (ex.: doar, doando, doação -> doar), permitindo que formas verbais e plurais convirjam para uma representação comum.
   - **Normalização e Remoção de Stopwords:** Padronizar pontuação, acentuação e remover palavras vazias que não agregam carga semântica à intenção.

3. **Ajuste Fino de Hiperparâmetros:**
   - Otimizar o `ngram_range` do TF-IDF e parâmetros de corte como `min_df` e `sublinear_tf=True`.
   - Ajustar parâmetros da Random Forest (como `max_depth`, `min_samples_split` e `criterion='entropy'`).

4. **Uso de Calibração de Probabilidades:**
   - Aplicar `CalibratedClassifierCV` do scikit-learn (via regressão isotônica ou sigmoid de Platt), garantindo que as probabilidades estimadas pela floresta reflitam com exatidão matemática a certeza da classificação.

5. **Evolução para Embeddings Semânticos:**
   - Substituir ou enriquecer a representação puramente léxica (TF-IDF) com embeddings densos (ex.: Word2Vec, FastText ou modelos Transformer como BERTimbau / Sentence-Transformers), capazes de associar *"mantimentos"* a *"alimentos"* por proximidade vetorial semântica.

---

## 5. Por que o Random Forest foi o melhor método de Machine Learning para essa fase

O algoritmo **Random Forest** foi a escolha mais adequada para esta etapa de NLU pelos seguintes fatores técnicos:

1. **Combinação Ensemble (Bagging) e Redução de Variância:**
   - Ao criar múltiplas árvores de decisão sobre subamostras bootstrap do conjunto de dados e sortear subconjuntos de features a cada divisão, o Random Forest atenua drasticamente o risco de *overfitting* (sobreajuste), comum em árvores de decisão simples ao lidar com matrizes esparsas de texto geradas pelo TF-IDF.

2. **Geração Natural de Probabilidades para o Limiar de Threshold (`predict_proba`):**
   - O Random Forest calcula as probabilidades de cada classe através da proporção de votos de todas as 80 árvores. Isso gera uma distribuição contínua e suave de probabilidade, tornando a aplicação da regra de corte por limiar (Threshold de 0.60) muito mais consistente do que em classificadores puramente baseados em margem rígida sem calibração.

3. **Capacidade de Lidar com Dados Esparsos e Não-Linearidades:**
   - Textos vetorizados com unigramas e bigramas produzem espaços vetoriais de alta dimensionalidade. As árvores de decisão particionam esses espaços de maneira não-linear e são naturalmente tolerantes a atributos irrelevantes ou ruídos, sem a necessidade de hipóteses restritivas sobre a distribuição dos dados (como a independência condicional exigida pelo Naive Bayes).

4. **Alta Eficiência e Baixa Latência Local:**
   - O treinamento com 80 árvores e a inferência em tempo de execução são praticamente instantâneos em CPU comum, dispensando infraestrutura pesada (GPU) ou conexões lentas de APIs de terceiros, o que é ideal para integração em tempo real em um assistente de chatbot interativo via Streamlit.
