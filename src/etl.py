# -----------------------------------------
# ETL - Alternativa 1 (Lista de Usuários)
# -----------------------------------------

# EXTRAÇÃO
usuarios = [
    {"nome": "Ana Souza", "conta": "12345-6", "cartao": "5555 4444 3333 2222"},
    {"nome": "Pedro Lima", "conta": "98765-4", "cartao": "1111 2222 3333 4444"},
    {"nome": "Marcos Silva", "conta": "54321-0", "cartao": "9999 8888 7777 6666"}
]

# TRANSFORMAÇÃO
def gerar_mensagem(usuario):
    return (
        f"Olá, {usuario['nome']}! "
        f"Identificamos que sua conta {usuario['conta']} e cartão {usuario['cartao']} "
        f"estão elegíveis para uma oferta exclusiva. Entre em contato!"
    )

mensagens = []
for u in usuarios:
    mensagens.append({
        "nome": u["nome"],
        "mensagem": gerar_mensagem(u)
    })

# CARREGAMENTO
import csv

with open("mensagens.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.DictWriter(arquivo, fieldnames=["nome", "mensagem"])
    writer.writeheader()
    writer.writerows(mensagens)

print("Arquivo mensagens.csv gerado com sucesso!")
