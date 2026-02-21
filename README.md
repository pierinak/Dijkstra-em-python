# 🗺️ Dijkstra na UCDB — Menor Caminho entre Pontos do Campus

Este projeto implementa o **Algoritmo de Dijkstra** em Python para calcular e visualizar o menor caminho entre dois pontos no campus da **Universidade Católica Dom Bosco (UCDB)**, em Campo Grande - MS.

---

## 📋 Descrição

O programa exibe um mapa interativo do campus da UCDB com marcadores nos principais locais (blocos, biblioteca, hospital veterinário, etc.) e, a partir da entrada do usuário, calcula e destaca visualmente o caminho mais curto entre dois pontos escolhidos, junto com a distância total percorrida em metros.

A interface gráfica é construída com **Tkinter**, o mapa interativo com **Folium** (renderizado em HTML), e a estrutura de grafo com **NetworkX**.

---

## ✨ Funcionalidades

- Mapa interativo do campus UCDB com satélite (Esri World Imagery)
- Marcadores visuais para todos os pontos do campus
- Cálculo do menor caminho via **Dijkstra** implementado manualmente
- Exibição do caminho percorrido destacado em azul no mapa
- Exibição da distância total em metros
- Interface gráfica simples e intuitiva com Tkinter
- Abertura automática do mapa no navegador padrão

---

## 🏛️ Locais Disponíveis

| Local | Descrição |
|---|---|
| `ENTRADA` | Portão principal do campus |
| `BLOCO A` | Bloco acadêmico A |
| `BLOCO B` | Bloco acadêmico B |
| `BLOCO C` | Bloco acadêmico C |
| `BLOCO D` | Bloco acadêmico D |
| `BLOCO L` | Bloco acadêmico L |
| `BLOCO M` | Bloco acadêmico M |
| `HOSPITAL VETERINÁRIO` | Hospital Veterinário da UCDB |
| `BIBLIOTECA` | Biblioteca do campus |
| `IGREJA` | Igreja do campus |

> Os pontos intermediários (`CAMINHO 1` a `CAMINHO 14`) são nós auxiliares usados internamente para representar as interseções e vias do campus.

---

## 🚀 Como Usar

### 1. Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado. Em seguida, instale as dependências:

```bash
pip install folium networkx
```

> `tkinter` já vem incluído na instalação padrão do Python.

### 2. Executar o programa

```bash
python DijkstraUCDB.py
```

### 3. Usar a interface

1. No campo **"Ponto de entrada"**, digite o local de partida (ex: `ENTRADA`)
2. No campo **"Ponto de destino"**, digite o local de chegada (ex: `BIBLIOTECA`)
3. Clique em **"Encontrar Caminho"**
4. O mapa será aberto automaticamente no seu navegador com o caminho destacado
5. Use **"Limpar Campos"** para resetar as entradas

> A entrada não diferencia maiúsculas de minúsculas.

---

## 🛠️ Tecnologias Utilizadas

| Biblioteca | Uso |
|---|---|
| [Folium](https://python-visualization.github.io/folium/) | Criação e renderização do mapa interativo |
| [NetworkX](https://networkx.org/) | Estrutura de dados do grafo |
| [Tkinter](https://docs.python.org/3/library/tkinter.html) | Interface gráfica |
| [Webbrowser](https://docs.python.org/3/library/webbrowser.html) | Abertura do HTML no navegador |

---

## 📁 Estrutura do Projeto

```
DijkstraUCDB/
│
├── DijkstraUCDB.py   # Código principal
├── mapa.html         # Mapa gerado (criado ao executar o programa)
└── README.md         # Este arquivo
```

---

## 📐 Sobre o Algoritmo

O **Algoritmo de Dijkstra** é um algoritmo clássico de grafos que encontra o caminho de menor custo entre um nó de origem e todos os demais nós de um grafo ponderado com pesos não-negativos.

Neste projeto, cada **aresta** representa um trecho de caminho no campus, e seu **peso** é a distância aproximada em metros entre os dois pontos conectados. O algoritmo percorre o grafo iterativamente, sempre expandindo o nó de menor distância acumulada ainda não visitado, até chegar ao destino.

---

## 📸 Exemplo de Uso

```
Ponto de entrada: ENTRADA
Ponto de destino: BIBLIOTECA

Caminho: ['ENTRADA', 'CAMINHO 1', 'CAMINHO 4', 'CAMINHO 5', 'CAMINHO 6', 'CAMINHO 9', 'BIBLIOTECA']
Distância total percorrida: 424 metros
```

---

Desenvolvido como projeto acadêmico para a **Universidade Católica Dom Bosco (UCDB)**.
