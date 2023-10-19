import mysql.connector

# Conectando ao banco de dados
db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="aluno",
    database="BDEscolar"
)

# Criando um cursor
cursor = db.cursor()

# Classe Aluno
class Aluno:
    def __init__(self, nome, data_nascimento, turma_id):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.turma_id = turma_id

    def salvar(self):
        query = "INSERT INTO Alunos (Nome, DataNascimento, TurmaID) VALUES (%s, %s, %s)"
        values = (self.nome, self.data_nascimento, self.turma_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM Alunos"
        cursor.execute(query)
        result = cursor.fetchall()
        for aluno in result:
            print(f"ID: {aluno[0]}, Nome: {aluno[1]}, Data de Nascimento: {aluno[2]}, Turma ID: {aluno[3]}")

    @staticmethod
    def alterar(aluno_id, novo_nome):
        query = "UPDATE Alunos SET Nome = %s WHERE ID = %s"
        values = (novo_nome, aluno_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(aluno_id):
        query = "DELETE FROM Alunos WHERE ID = %s"
        values = (aluno_id,)
        cursor.execute(query, values)
        db.commit()

# Classe Professor (semelhante ao Aluno)
class Professor:
    def __init__(self, nome):
        self.nome = nome

    def salvar(self):
        query = "INSERT INTO Professores (Nome) VALUES (%s)"
        values = (self.nome,)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM Professores"
        cursor.execute(query)
        result = cursor.fetchall()
        for professor in result:
            print(f"ID: {professor[0]}, Nome: {professor[1]}")

    @staticmethod
    def alterar(professor_id, novo_nome):
        query = "UPDATE Professores SET Nome = %s WHERE ID = %s"
        values = (novo_nome, professor_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(professor_id):
        query = "DELETE FROM Professores WHERE ID = %s"
        values = (professor_id,)
        cursor.execute(query, values)
        db.commit()

# Classe Turma (semelhante ao Aluno)
class Turma:
    def __init__(self, nome_turma, professor_id):
        self.nome_turma = nome_turma
        self.professor_id = professor_id

    def salvar(self):
        query = "INSERT INTO Turmas (NomeTurma, ProfessorID) VALUES (%s, %s)"
        values = (self.nome_turma, self.professor_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM Turmas"
        cursor.execute(query)
        result = cursor.fetchall()
        for turma in result:
            print(f"ID: {turma[0]}, Nome da Turma: {turma[1]}, Professor ID: {turma[2]}")

    @staticmethod
    def alterar(turma_id, novo_nome):
        query = "UPDATE Turmas SET NomeTurma = %s WHERE ID = %s"
        values = (novo_nome, turma_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(turma_id):
        query = "DELETE FROM Turmas WHERE ID = %s"
        values = (turma_id,)
        cursor.execute(query, values)
        db.commit()

# Classe Disciplina (semelhante ao Aluno)
class Disciplina:
    def __init__(self, nome_disciplina, turma_id):
        self.nome_disciplina = nome_disciplina
        self.turma_id = turma_id

    def salvar(self):
        query = "INSERT INTO Disciplinas (NomeDisciplina, TurmaID) VALUES (%s, %s)"
        values = (self.nome_disciplina, self.turma_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM Disciplinas"
        cursor.execute(query)
        result = cursor.fetchall()
        for disciplina in result:
            print(f"ID: {disciplina[0]}, Nome da Disciplina: {disciplina[1]}, Turma ID: {disciplina[2]}")

    @staticmethod
    def alterar(disciplina_id, novo_nome):
        query = "UPDATE Disciplinas SET NomeDisciplina = %s WHERE ID = %s"
        values = (novo_nome, disciplina_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(disciplina_id):
        query = "DELETE FROM Disciplinas WHERE ID = %s"
        values = (disciplina_id,)
        cursor.execute(query, values)
        db.commit()

# Classe Unidade Escolar (semelhante ao Aluno)
class UnidadeEscolar:
    def __init__(self, nome_unidade, endereco):
        self.nome_unidade = nome_unidade
        self.endereco = endereco

    def salvar(self):
        query = "INSERT INTO UnidadesEscolares (NomeUnidade, Endereco) VALUES (%s, %s)"
        values = (self.nome_unidade, self.endereco)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def listar():
        query = "SELECT * FROM UnidadesEscolares"
        cursor.execute(query)
        result = cursor.fetchall()
        for unidade in result:
            print(f"ID: {unidade[0]}, Nome da Unidade: {unidade[1]}, Endereço: {unidade[2]}")

    @staticmethod
    def alterar(unidade_id, novo_nome, novo_endereco):
        query = "UPDATE UnidadesEscolares SET NomeUnidade = %s, Endereco = %s WHERE ID = %s"
        values = (novo_nome, novo_endereco, unidade_id)
        cursor.execute(query, values)
        db.commit()

    @staticmethod
    def remover(unidade_id):
        query = "DELETE FROM UnidadesEscolares WHERE ID = %s"
        values = (unidade_id,)
        cursor.execute(query, values)
        db.commit()

if __name__ == "__main__":
    while True:
        print("Escolha uma opção:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Alterar Aluno")
        print("4. Remover Aluno")
        print("5. Cadastrar Professor")
        print("6. Listar Professores")
        print("7. Alterar Professor")
        print("8. Remover Professor")
        print("9. Cadastrar Turma")
        print("10. Listar Turmas")
        print("11. Alterar Turma")
        print("12. Remover Turma")
        print("13. Cadastrar Disciplina")
        print("14. Listar Disciplinas")
        print("15. Alterar Disciplina")
        print("16. Remover Disciplina")
        print("17. Cadastrar Unidade Escolar")
        print("18. Listar Unidades Escolares")
        print("19. Alterar Unidade Escolar")
        print("20. Remover Unidade Escolar")
        print("0. Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome do Aluno: ")
            data_nascimento = input("Data de Nascimento (YYYY-MM-DD): ")
            turma_id = int(input("ID da Turma: "))
            aluno = Aluno(nome, data_nascimento, turma_id)
            aluno.salvar()
            print("Aluno cadastrado com sucesso!")

        elif opcao == "2":
            Aluno.listar()

        elif opcao == "3":
            aluno_id = int(input("ID do Aluno: "))
            novo_nome = input("Novo Nome: ")
            Aluno.alterar(aluno_id, novo_nome)
            print("Nome do Aluno alterado com sucesso!")

        elif opcao == "4":
            aluno_id = int(input("ID do Aluno: "))
            Aluno.remover(aluno_id)
            print("Aluno removido com sucesso!")

        elif opcao == "5":
            nome = input("Nome do Professor: ")
            professor = Professor(nome)
            professor.salvar()
            print("Professor cadastrado com sucesso!")

        elif opcao == "6":
            Professor.listar()

        elif opcao == "7":
            professor_id = int(input("ID do Professor: "))
            novo_nome = input("Novo Nome: ")
            Professor.alterar(professor_id, novo_nome)
            print("Nome do Professor alterado com sucesso!")

        elif opcao == "8":
            professor_id = int(input("ID do Professor: "))
            Professor.remover(professor_id)
            print("Professor removido com sucesso!")

        elif opcao == "9":
            nome_turma = input("Nome da Turma: ")
            professor_id = int(input("ID do Professor: "))
            turma = Turma(nome_turma, professor_id)
            turma.salvar()
            print("Turma cadastrada com sucesso!")

        elif opcao == "10":
            Turma.listar()

        elif opcao == "11":
            turma_id = int(input("ID da Turma: "))
            novo_nome = input("Novo Nome da Turma: ")
            Turma.alterar(turma_id, novo_nome)
            print("Nome da Turma alterado com sucesso!")

        elif opcao == "12":
            turma_id = int(input("ID da Turma: "))
            Turma.remover(turma_id)
            print("Turma removida com sucesso!")

        elif opcao == "13":
            nome_disciplina = input("Nome da Disciplina: ")
            turma_id = int(input("ID da Turma: "))
            disciplina = Disciplina(nome_disciplina, turma_id)
            disciplina.salvar()
            print("Disciplina cadastrada com sucesso!")

        elif opcao == "14":
            Disciplina.listar()

        elif opcao == "15":
            disciplina_id = int(input("ID da Disciplina: "))
            novo_nome = input("Novo Nome da Disciplina: ")
            Disciplina.alterar(disciplina_id, novo_nome)
            print("Nome da Disciplina alterado com sucesso!")

        elif opcao == "16":
            disciplina_id = int(input("ID da Disciplina: "))
            Disciplina.remover(disciplina_id)
            print("Disciplina removida com sucesso!")

        elif opcao == "17":
            nome_unidade = input("Nome da Unidade Escolar: ")
            endereco = input("Endereço da Unidade Escolar: ")
            unidade = UnidadeEscolar(nome_unidade, endereco)
            unidade.salvar()
            print("Unidade Escolar cadastrada com sucesso!")

        elif opcao == "18":
            UnidadeEscolar.listar()

        elif opcao == "19":
            unidade_id = int(input("ID da Unidade Escolar: "))
            novo_nome = input("Novo Nome da Unidade Escolar: ")
            novo_endereco = input("Novo Endereço da Unidade Escolar: ")
            UnidadeEscolar.alterar(unidade_id, novo_nome, novo_endereco)
            print("Nome e Endereço da Unidade Escolar alterados com sucesso!")

        elif opcao == "20":
            unidade_id = int(input("ID da Unidade Escolar: "))
            UnidadeEscolar.remover(unidade_id)
            print("Unidade Escolar removida com sucesso!")

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

# Fechar a conexão com o banco de dados
cursor.close()
db.close()
