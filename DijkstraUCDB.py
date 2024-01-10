# ULTIMA ATUALIZAÇÃO 27-11

# O código tem o objetivo de achar o menor caminho entre dois pontos escolhidos num mapa, sendo o mapa escolhido o da UCDB
# Para isso é usada 1 interface com 4 funcionalidades, 1 caixa de entrada para o ponto de partida, 1 caixa de entrada para o ponto de chegada,
# 1 botão para chamar a função achar_caminho() que acha o caminho mínimo por meio de Dijkstra e 1 botão para limpar as caixas de entrada e saída
# O código é composto pelas variáveis UCDB nomes, coord, icones que são usadas para crias os vertices e arestas do grafo do network, além do grafo do Folium
# O Folium é usado para criar o mapa, seus icones, suas arestas, seu grafo e manipular esses componentes, Tkinter é usado na interface gráfica,
# Webbrowser é usado para tranferir o mapa folium para HTML no final do código


from tkinter import messagebox
import folium
import networkx as nx
import webbrowser
from tkinter import *

# Lista de nomes dos locais na UCDB
UCDB_nomes = ["ENTRADA", "BLOCO A", "BLOCO B", "BLOCO C", "BLOCO D", "BLOCO L", "BLOCO M", "HOSPITAL VETERINÁRIO", "BIBLIOTECA", "IGREJA",
              "CAMINHO 1", "CAMINHO 2", "CAMINHO 3", "CAMINHO 4", "CAMINHO 5", "CAMINHO 6", "CAMINHO 7", "CAMINHO 8", "CAMINHO 9",
              "CAMINHO 10", "CAMINHO 11", "CAMINHO 12", "CAMINHO 13", "CAMINHO 14"
              ]

# Coordenadas dos locais na UCDB
UCDB_coord = [[-20.407989964909696, -54.61913735768868],
              [-20.408005798869183, -54.617678543637226],
              [-20.40703299463073, -54.617774467902336],
              [-20.407812613141253, -54.61550017710632],
              [-20.406761742838945, -54.615670734662665],
              [-20.4067960, -54.6166752],
              [-20.404728357699145, -54.61708477102904],
              [-20.403643908677658, -54.6173457004694],
              [-20.40947001984952, -54.616182897329246],
              [-20.40808500432581, -54.616351210804886],  # coordenadas dos BLOCOS
              [-20.40812466777592, -54.61863616634357], [-20.407556497194417, - \
                                                         54.61825290237378], [-20.40748396462183, -54.617657737643086], [-20.408514960035895, -54.61815155852747],
              [-20.40848732875835, -54.61754718072896], [-20.408409615763702, -54.61667746633598], [-20.408295636631866, - \
                                                                                                    54.615448441824455], [-20.407262912775472, -54.61562533288463], [-20.40836982076294, -54.61628932131856],
              [-20.40649178730165, -54.617828336199835], [-20.40636499766834, -54.616356827975785], [-20.40502723132193, - \
                                                                                                     54.61647278171655], [-20.405063457255633, -54.6170497896303], [-20.404062065796246, -54.61710500570806]
              ]

# Icones dos locais na ucdb
UCDB_icones = [
    folium.Icon(icon="glyphicon glyphicon-flag", color="black"),  # Entrada
    folium.Icon(icon="glyphicon glyphicon-pencil",
                color="black"),  # Bloco A (Estudante)
    folium.Icon(icon="glyphicon glyphicon-pencil",
                color="black"),  # Bloco B (Estudante)
    folium.Icon(icon="glyphicon glyphicon-pencil",
                color="black"),  # Bloco C (Estudante)
    folium.Icon(icon="glyphicon glyphicon-pencil",
                color="black"),  # Bloco D (Estudante)
    folium.Icon(icon="glyphicon glyphicon-pencil",
                color="black"),  # Bloco L (Estudante)
    folium.Icon(icon="glyphicon glyphicon-pencil",
                color="black"),  # Bloco M (Estudante)
    folium.Icon(icon="glyphicon glyphicon-plus",
                color="black"),  # Hospital Veterinário
    folium.Icon(icon="glyphicon glyphicon-book", color="black"),  # Biblioteca
    folium.Icon(icon="glyphicon glyphicon-glass", color="black"),  # Igreja
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 1
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 2
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 3
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 4
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 5
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 6
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 7
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 8
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 9
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 10
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 11
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 12
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black"),  # Caminho 13
    folium.Icon(icon="glyphicon glyphicon-map-marker",
                color="black")   # Caminho 14
]


# Cria um mapa Folium
def criar_mapa():
    UCDB_mapa = folium.Map(
        location=[-20.40603626107316, -54.61669205059546], zoom_start=120, control_scale=True)
    folium.TileLayer(tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                     attr='Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community',
                     name="Esri.WorldImagery").add_to(UCDB_mapa)

    # Adiciona nós ao grafo
    for i in range(len(UCDB_coord)):
        coordenada = UCDB_coord[i]
        universidade = UCDB_nomes[i]
        icones = UCDB_icones[i]
        folium.Marker(coordenada, popup=universidade,
                      icon=icones).add_to(UCDB_mapa)
        G.add_node(universidade, coordenada=coordenada)  # mantem as arestas
    return UCDB_mapa


# Cria um grafo
G = nx.Graph()
# Adiciona as arestas dos caminhos COM os blocos
G.add_edge("ENTRADA", "CAMINHO 1", peso=49)
G.add_edge("BLOCO A", "CAMINHO 5", peso=52)
G.add_edge("BLOCO A", "CAMINHO 3", peso=64)
G.add_edge("BLOCO B", "CAMINHO 3", peso=54)
G.add_edge("BLOCO B", "CAMINHO 10", peso=55)
G.add_edge("IGREJA", "CAMINHO 6", peso=51)
G.add_edge("BLOCO C", "CAMINHO 7", peso=61)
G.add_edge("BLOCO C", "CAMINHO 8", peso=61)
G.add_edge("BLOCO D", "CAMINHO 8", peso=57)
G.add_edge("BIBLIOTECA", "CAMINHO 9", peso=118)
G.add_edge("BLOCO M", "CAMINHO 13", peso=38)
G.add_edge("BLOCO M", "CAMINHO 14", peso=75)
G.add_edge("HOSPITAL VETERINÁRIO", "CAMINHO 14", peso=49)
G.add_edge("BLOCO D", "BLOCO L", peso=104)
G.add_edge("BLOCO B", "BLOCO L", peso=119)

# Adiciona as arestas dos caminhos
G.add_edge("CAMINHO 1", "CAMINHO 2", peso=75)
G.add_edge("CAMINHO 1", "CAMINHO 4", peso=67)
G.add_edge("CAMINHO 2", "CAMINHO 3", peso=63)
G.add_edge("CAMINHO 4", "CAMINHO 5", peso=63)
G.add_edge("CAMINHO 5", "CAMINHO 6", peso=94)
G.add_edge("CAMINHO 6", "CAMINHO 9", peso=37)
G.add_edge("CAMINHO 9", "CAMINHO 7", peso=86)
G.add_edge("CAMINHO 10", "CAMINHO 11", peso=157)
G.add_edge("CAMINHO 11", "CAMINHO 12", peso=148)
G.add_edge("CAMINHO 12", "CAMINHO 13", peso=61)


# Função para encontrar o caminho mais curto
def encontrar_caminho():

    # cria um mapa limpo toda vez que a função é usada
    global UCDB_mapa
    UCDB_mapa = criar_mapa()

    # Obtém os pontos de entrada e destino
    # Remover espaços extras e converter para maiúsculas
    comeco = ponto_de_entrada.get().strip().upper()
    fim = ponto_de_destino.get().strip().upper()

    # Verifica se os pontos de entrada e destino são válidos
    if comeco not in map(str.upper, UCDB_nomes) or fim not in map(str.upper, UCDB_nomes):
        messagebox.showerror("Erro", "Pontos de entrada ou destino inválidos.")
        return

    # Cria um dicionário para armazenar a menor distância do nó de partida para cada nó
    menor_distancia = {node: float('inf') for node in G.nodes}
    menor_distancia[comeco] = 0

    # Cria um dicionário para armazenar o nó anterior no caminho mais curto
    no_anterior = {node: None for node in G.nodes}

    # Cria um conjunto para armazenar os nós não visitados
    nos_nao_visitados = set(G.nodes)

    while nos_nao_visitados:
        # Encontra o nó com a menor distância do nó de partida
        no_atual = min(nos_nao_visitados,
                       key=lambda node: menor_distancia[node])

        # Remove o nó atual do conjunto de nós não visitados
        nos_nao_visitados.remove(no_atual)

        # Para se chegarmos ao nó de destino
        if no_atual == fim:
            break

        # Atualiza as distâncias para os nós vizinhos
        for vizinho in G.neighbors(no_atual):
            distancia = menor_distancia[no_atual] + \
                G.edges[no_atual, vizinho]['peso']
            if distancia < menor_distancia[vizinho]:
                menor_distancia[vizinho] = distancia
                no_anterior[vizinho] = no_atual

    # Reconstrói o caminho mais curto
    caminho_mais_curto = []
    no_atual = fim
    while no_atual is not None:
        caminho_mais_curto.insert(0, no_atual)
        no_atual = no_anterior[no_atual]

    # Mostra o caminho mais curto
    texto_caminho["text"] = caminho_mais_curto
    # Mostra a distancia total percorrida
    texto_distancia["text"] = f"Distância total percorrida: {menor_distancia[fim]} metros"

    # Adiciona marcadores para cada nó no caminho mais curto
    for no in caminho_mais_curto:
        coordenada = G.nodes[no]["coordenada"]
        folium.Marker(coordenada, popup=f"{no}", icon=folium.Icon(
            color="red")).add_to(UCDB_mapa)  # adiciona os vertices

    # Adiciona uma linha para mostrar o caminho mais curto com os pesos
    for i in range(len(caminho_mais_curto) - 1):
        no1 = caminho_mais_curto[i]
        no2 = caminho_mais_curto[i + 1]
        peso = G.edges[no1, no2]['peso']
        folium.PolyLine([G.nodes[no1]["coordenada"], G.nodes[no2]["coordenada"]], color="blue", weight=2.5, opacity=1,  # adiciona as arestas
                        popup=f"Peso: {peso}").add_to(UCDB_mapa)

    # Salva o mapa como um arquivo HTML
    UCDB_mapa.save("mapa.html")

    # Abre o arquivo HTML no navegador padrão
    webbrowser.open("mapa.html")


# Cria a interface usando o tkinter
janela = Tk()
janela.title("Google Maps - UCDB")

# Cria texto que explica sua funcionalidade
texto_orientacao = Label(
    janela, text="Este programa calcula e mostra o caminho mais rapido\n entre dois locais na Universidade Católica Dom Bosco. \n")
texto_orientacao.pack()

# Locais disponiveis para escolha
texto_locais = Label(
    janela, text="Locais disponiveis para escolha: \nENTRADA, BLOCO A, BLOCO B, BLOCO C, BLOCO D, BLOCO L, BLOCO M, HOSPITAL VETERINÁRIO, BIBLIOTECA, IGREJA")
texto_locais.pack()

# Cria os rótulos e campos de entrada
label_entrada = Label(janela, text="Ponto de entrada:")
label_entrada.pack()
ponto_de_entrada = Entry(janela)
ponto_de_entrada.pack()

label_destino = Label(janela, text="Ponto de destino:")
label_destino.pack()
ponto_de_destino = Entry(janela)
ponto_de_destino.pack()

# Cria o botão para encontrar o caminho mais curto
botao_encontrar = Button(
    janela, text="Encontrar Caminho", command=encontrar_caminho)
botao_encontrar.pack()

# Função para limpar os campos de entrada


def limpar_campos():
    ponto_de_entrada.delete(0, END)
    ponto_de_destino.delete(0, END)


# Cria o botão para limpar os campos de entrada
botao_limpar = Button(janela, text="Limpar Campos", command=limpar_campos)
botao_limpar.pack()

# Mostra o caminho mais curto
texto_caminho = Label(janela, text="")
texto_caminho.pack()

# Mostra a distancia total percorrida
texto_distancia = Label(janela, text="")
texto_distancia.pack()

janela.mainloop()
