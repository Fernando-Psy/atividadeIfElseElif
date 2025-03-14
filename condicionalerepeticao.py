propaganda_online = [
    {
        "tempo_gasto_site": 68.95,
        "idade": 35,
        "renda_area": 61833.90,
        "tempo_gasto_internet": 256.09,
        "cidade": "Wrightburgh",
        "pais": "Tunisia",
        "clicou_no_ad": 0,
    },
    {
        "tempo_gasto_site": 80.23,
        "idade": 31,
        "renda_area": 68441.85,
        "tempo_gasto_internet": 193.77,
        "cidade": "West Jodi",
        "pais": "Nauru",
        "clicou_no_ad": 0,
    },
    {
        "tempo_gasto_site": 69.47,
        "idade": 26,
        "renda_area": 59785.94,
        "tempo_gasto_internet": 236.50,
        "cidade": "Davidton",
        "pais": "San Marino",
        "clicou_no_ad": 0,
    },
    {
        "tempo_gasto_site": 68.37,
        "idade": 35,
        "renda_area": 73889.99,
        "tempo_gasto_internet": 225.58,
        "cidade": "South Manuel",
        "pais": "Iceland",
        "clicou_no_ad": 0,
    },
    {
        "tempo_gasto_site": 88.91,
        "idade": 33,
        "renda_area": 53852.85,
        "tempo_gasto_internet": 208.36,
        "cidade": "Brandonstad",
        "pais": "Myanmar",
        "clicou_no_ad": 0,
    },
    {
        "tempo_gasto_site": None,
        "idade": 48,
        "renda_area": 24593.33,
        "tempo_gasto_internet": 131.76,
        "cidade": "Port Jefferybury",
        "pais": "Australia",
        "clicou_no_ad": 1,
    },
    {
        "tempo_gasto_site": 74.53,
        "idade": 30,
        "renda_area": 68862.00,
        "tempo_gasto_internet": 221.51,
        "cidade": "West Colin",
        "pais": "Grenada",
    },
    {
        "tempo_gasto_site": 69.88,
        "idade": 20,
        "renda_area": 55642.32,
        "tempo_gasto_internet": 183.82,
        "cidade": "Ramirezton",
        "pais": "Ghana",
        "clicou_no_ad": 0,
    },
]

# Iterar os elementos da lista
print("Dados dos usuários: ")
for dado_de_usuario in propaganda_online:
    print(dado_de_usuario)

# Lista de países que os pais dos usuários tem mais de 30 anos

paises = []
for dado_de_usuario in propaganda_online:
    try:
        if dado_de_usuario.get("idade", 0) > 30:
            pais = dado_de_usuario.get("pais")

            if pais and pais not in paises:
                paises.append(pais)
    except Exception as e:
        print(f'Erro ao processar a idade do usuário: {e}')

print('\nPaíses onde os usuários tem mais de 30 anos:')
print(paises)

# Leads

leads = []

for dado_de_usuario in propaganda_online:
    try:
        if 'clicou_no_ad' in dado_de_usuario:
            if dado_de_usuario['clicou_no_ad'] == 1:
                leads.append(dado_de_usuario)
        else:
            print(f'Usuário da cidade {dado_de_usuario.get("cidade")} não tem informações de cliques')
    except Exception as exc:
        print(f'Erro ao processar o clique do suário: {exc}')
    finally:
        pass

print('\nLeads que clicarm no anúncio: ')
print(leads)

# Cidades que usuários ficaram mais de 70 segundos no site

cidades = []

for dado_de_usuario in propaganda_online:
    try:
        tempo = dado_de_usuario.get('tempo_gasto_site')
        cidade = dado_de_usuario.get('cidade')

        if tempo is not None:
            if tempo > 70:
                if cidade not in cidades:
                    cidades.append(cidade)
            elif tempo > 60:
                print(f'Usuário da cidade {cidade} acessou e ficou entre 60-70 segundos no site')
            else:
                #Pretendo adicionar outras funcionalidades como: pessoas que ficaram menos de 60 segundos
                pass
        else:
            print(f'Usu´rio da cidade {cidade} nao tem informação sobre tempo no site')
    except Exception as exc:
        print(f'Erro ao processar tempo do usuário: {exc}')
print('\nCidades onde usuários passaram mais de 70 segundos no site:')
print(cidades)
