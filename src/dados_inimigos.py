from config import caminho_asset

Slime_azul = {
    "nome": "Slime azul",
    "vida": 10,
    "dano_max": 3,
    "dano_min": 2,
    "esquiva": 8,
    "chance_critico": 3,
    "critico": 1.1,
    "caminho": caminho_asset("inimigos/Slime_azul.png"),
    "largura": 170,
    "altura": 170,
    "qtd_frames": 10,
    "velocidade_animacao": 70,
    "som_ataque": caminho_asset("sounds/som_inimigos/som_ataque_slime.mpeg")
}

Slime_verde = {
    "nome": "Slime verde",
    "vida": 13,
    "dano_max": 3,
    "dano_min": 2,
    "esquiva": 10,
    "chance_critico": 6,
    "critico": 1.2,
    "caminho": caminho_asset("inimigos/Slime_verde.png"),
    "largura": 170,
    "altura": 170,
    "qtd_frames": 9,
    "velocidade_animacao": 70,
    "som_ataque": caminho_asset("sounds/som_inimigos/som_ataque_slime.mpeg")
}

King_slime = {
    "nome": "King Slime",
    "vida": 32,
    "dano_max": 5,
    "dano_min": 4,
    "esquiva": 6,
    "chance_critico": 7,
    "critico": 1.75,
    "caminho": caminho_asset("inimigos/chefes/King Slime.png"),
    "largura": 210,
    "altura": 210,
    "qtd_frames": 8,
    "velocidade_animacao": 70,
    "som_ataque": caminho_asset("sounds/som_inimigos/som_ataque_slime.mpeg")
}

Esqueleto = {
    "nome": "Esqueleto",
    "vida": 20,
    "dano_max": 4,
    "dano_min": 3,
    "esquiva": 8,
    "chance_critico": 4,
    "critico": 1.75,
    "caminho": caminho_asset("inimigos/Esqueleto.png"),
    "largura": 210,
    "altura": 210,
    "qtd_frames": 4,
    "velocidade_animacao": 90,
    "som_ataque": caminho_asset("sounds/som_inimigos/som_ataque_esqueleto.mp3")
}