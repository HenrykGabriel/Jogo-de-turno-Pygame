from config import caminho_asset

Slime_azul = {
    "nome": "Slime azul",
    "vida": 10,
    "dano": 2,
    "esquiva": 1,
    "chance_critico": 1,
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
    "vida": 12,
    "dano": 1,
    "esquiva": 1,
    "chance_critico": 1,
    "critico": 1.2,
    "caminho": caminho_asset("inimigos/Slime_verde.png"),
    "largura": 170,
    "altura": 170,
    "qtd_frames": 10,
    "velocidade_animacao": 70,
    "som_ataque": caminho_asset("sounds/som_inimigos/som_ataque_slime.mpeg")
}

King_slime = {
    "nome": "King Slime",
    "vida": 30,
    "dano": 5,
    "esquiva": 6,
    "chance_critico": 4,
    "critico": 1.75,
    "caminho": caminho_asset("inimigos/chefes/King Slime.png"),
    "largura": 210,
    "altura": 210,
    "qtd_frames": 8,
    "velocidade_animacao": 70,
    "som_ataque": caminho_asset("sounds/som_inimigos/som_ataque_slime.mpeg")
}