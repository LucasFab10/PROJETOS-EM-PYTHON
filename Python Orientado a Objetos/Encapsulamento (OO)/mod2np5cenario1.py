class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro "{livro.titulo}" adicionado à biblioteca')

    def removendo_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
               self.livros.remove(livro)
               print(f'Livro "{livro.titulo}" removido da biblioteca "{self.nome}".')
               return
        print(f'Livro com ISBN {isbn} não encontrado na biblioteca "{self.nome}".')

    def listar_livros(self):
            if not self.livros:
                print(f'A biblioteca "{self.nome}" não tem livros.')
            else:
                 print(f'Livros na biblioteca "{self.nome}":')
                 for livro in self.livros:
                    print(f' - {livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')

# Testando as classes

# Criando alguns livros
livro1 = Livro(titulo='O Senhor dos anéis', autor= 'J.R.R Tolkien', isbn= "123")
livro2 = Livro(titulo= '1984', autor= 'George Orwell', isbn='0987654321')
livro3 = Livro(titulo= 'O Apanhador no Campo de Centeio', autor= 'J.D. Salinger', isbn= '1122334455')

# Criando biblioteca
biblioteca = Biblioteca('Biblioteca Central')

# Adicionando os livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

# Removendo um livro da biblioteca
biblioteca.removendo_livro('0987654321')

# Listando todos os livros na biblioteca
biblioteca.listar_livros()