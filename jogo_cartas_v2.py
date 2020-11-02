import random
from typing import List, Tuple, Dict
# https://www.alt-codes.net/suit-cards.php
NAIPES: List[str] = "♠ ♥ ♦ ♣".split()
CARTAS: List[str] = "2 3 4 5 6 7 8 9 10 J Q K A".split()

CARTA = Tuple[str, str]
BARALHO = List[CARTA]

def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """Cria um baralho com 52 cartas"""
    baralho = [(naipe, carta) for carta in CARTAS for naipe in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuir_cartas(baralho: List[Tuple[str]]) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de cartas de acordo com o baralho gerado"""
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores"""
    cartas = criar_baralho(aleatorio=True)
    jogadores = "P1 P2 P3 P4".split()
    maos = {jogador: mao for jogador, mao in zip(jogadores, distribuir_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = " ".join(f"{j}{c}" for (j, c) in cartas)
        print(f"{jogador}: {carta}")


if __name__ == "__main__":
    jogar()
