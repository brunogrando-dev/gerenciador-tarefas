# 📌 Gerenciador de Tarefas

Um gerenciador de tarefas simples desenvolvido em Python durante o curso de Python da RocketSeat.

## 📋 Funcionalidades

- ✅ **Adicionar tarefas** - Adicione novas tarefas à lista
- ✅ **Visualizar tarefas** - Veja todas as tarefas com status (concluída ou não)
- ✅ **Editar tarefas** - Altere o nome de uma tarefa existente
- ✅ **Completar tarefas** - Marque uma tarefa como concluída
- ✅ **Deletar tarefas** - Remova qualquer tarefa da lista
- ✅ **Sair** - Encerre o programa

## 🚀 Como usar

1. Certifique-se de ter Python 3.x instalado
2. Clone este repositório:
```bash
   git clone https://github.com/seu-usuario/gerenciador-tarefas.git
   cd gerenciador-tarefas
```
3. Execute o programa:
```bash
   python main.py
```

## 📚 Funções

### `adicionar_tarefas(tarefas, nome_tarefa)`
Adiciona uma nova tarefa à lista com status "não concluída".

### `visualizar_tarefas(tarefas)`
Exibe todas as tarefas com seus status (✅ concluída / ❌ não concluída).

### `atualizar_tarefa(tarefas, indice_tarefa, nova_tarefa)`
Altera o nome de uma tarefa existente.

### `completar_tarefa(tarefas, indice_tarefa)`
Marca uma tarefa como concluída.

### `deletar_tarefa(tarefas, indice_tarefa)`
Remove uma tarefa da lista.

## 🔄 Fluxo do Programa

1. O programa exibe um menu com 6 opções
2. O usuário digita o número correspondente
3. Dependendo da escolha, o programa executa a função apropriada
4. O loop continua até o usuário escolher "Sair"

## 📖 Conceitos Python Utilizados

- **Funções** - Modularização de código
- **Listas** - Armazenamento de dados
- **Dicionários** - Estrutura de dados das tarefas
- **Loops (while/for)** - Repetição de código
- **Condicionais (if/elif/else)** - Tomada de decisão
- **Métodos de lista** - `append()`, `pop()`, `enumerate()`

## 📝 Licença

Este projeto é de código aberto e pode ser usado livremente para fins educacionais.

---

**Desenvolvido durante o curso de Python da RocketSeat** 🚀