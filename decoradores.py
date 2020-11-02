"""
Decorators

- Decorators são funções
- Envolvem outras funções e aprimoram seus comportamentos
- Decorators tem um sintaxe própria, usando "@" (Syntact Sugar)
"""


# Decorators com Syntax Sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer você!")
        funcao()
        print("Tenha um excelente dia!")
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print("Meu nome é Pedro")


apresentando()


@seja_educado_mesmo
def dormir():
    print("Quero dormir")


dormir()
