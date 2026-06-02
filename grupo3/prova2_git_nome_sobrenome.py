# ============================================================
#  PROVA PRÁTICA — Git & GitHub
# ============================================================
#
#  INSTRUÇÕES:
#  1. Faça o clone do repositório
#  2. Copie o arquivo prova_git_nome_sobrenome.py e renomei para prova_git_seu_nome_sobrenome.py
#  2. Preencha seus dados na função registrar_aluno() abaixo
#  3. Execute o arquivo para verificar.
#  4. Faça o commit com a mensagem: "prova: SEU_NOME SEU_SOBRENOME"
#  5. Suba com: git push origin main
#
# ============================================================

historico = []


def registrar_aluno(matricula: str, nome: str, sobrenome: str):
    """
    Registra o aluno no histórico da prova.
    Não permite matrícula ou nome duplicado.
    """
    for registro in historico:
        if registro["matricula"] == matricula:
            print(f"  Matrícula {matricula} já registrada.")
            return
        if registro["nome"] == nome and registro["sobrenome"] == sobrenome:
            print(f"   {nome} {sobrenome} já está registrado.")
            return

    historico.append({
        "matricula": matricula,
        "nome":      nome,
        "sobrenome": sobrenome
    })
    print(f"  ✅ Registrado: {matricula} — {nome} {sobrenome}")


def autores_do_repositorio(commits: list) -> list:
    """
    Recebe uma lista de commits (cada um com 'hash' e 'autor')
    e retorna todos os autores que contribuíram, sem repetição
    e em ordem alfabética.
    """
    autores = set()
    for commit in commits:
        autores.add(commit["autor"])
    return sorted(autores)


# ============================================================
#  PREENCHA SEUS DADOS ABAIXO
#  registrar_aluno("matricula", "nome", "sobrenome")
# ============================================================

registrar_aluno("asdasd211", "teste", "tesrsdf")

# ============================================================
#  NÃO ALTERE O CÓDIGO ABAIXO
# ============================================================

def verificar():
    COMMITS = [
        {"hash": "f3a1b2c", "autor": "Carlos Melo"},
        {"hash": "a2c3d4e", "autor": "Ana Lima"},
        {"hash": "b3d4e5f", "autor": "Carlos Melo"},
        {"hash": "c4e5f6a", "autor": "Beatriz Nunes"},
        {"hash": "d5f6a7b", "autor": "Ana Lima"},
        {"hash": "e6a7b8c", "autor": "Diego Souza"},
    ]

    print("\n" + "=" * 44)
    print("  VERIFICAÇÃO")
    print("=" * 44)

    if not historico or not historico[-1]["matricula"].strip():
        print("  ✗ Preencha seus dados em registrar_aluno().")
        print("=" * 44 + "\n")
        return

    aluno = historico[-1]
    print(f"  Aluno: {aluno['matricula']} — {aluno['nome']} {aluno['sobrenome']}")
    print("-" * 44)

    try:
        resultado = autores_do_repositorio(COMMITS)
        esperado  = ["Ana Lima", "Beatriz Nunes", "Carlos Melo", "Diego Souza"]

        assert isinstance(resultado, list), "Deve retornar uma lista."
        assert resultado == esperado, (
            f"Esperado: {esperado}\n  Obtido:   {resultado}"
        )

        print("  [✓] Função correta!")
        print("  Agora faça o commit e o push!")
    except Exception as e:
        print(f"  [✗] Falhou: {e}")

    print("=" * 44 + "\n")


if __name__ == "__main__":
    verificar()