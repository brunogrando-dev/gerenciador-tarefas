# ==================== FUNÇÕES ====================

# FUNÇÃO 1: Adicionar Tarefas
def adicionar_tarefas(tarefas, nome_tarefa):
    """
    Função que adiciona uma nova tarefa à lista.

    Parâmetros:
        tarefas (list): Lista de tarefas
        nome_tarefa (str): Nome da tarefa a adicionar
    """
    # Cria um dicionário com a estrutura da tarefa
    # 'tarefa' guarda o nome, 'completada' começa como False (não feita)
    tarefa = {'tarefa': nome_tarefa, 'completada': False}

    # Adiciona o dicionário criado ao final da lista de tarefas
    # append() = adiciona um elemento ao final da lista
    tarefas.append(tarefa)

    # Exibe mensagem confirmando que a tarefa foi adicionada
    # f-string = permite usar variáveis dentro da string com {}
    print(f'✅ A tarefa: {nome_tarefa} foi adicionada')

    # return (sem valor) apenas encerra a função
    return


# FUNÇÃO 2: Visualizar Tarefas
def visualizar_tarefas(tarefas):
    """
    Função que exibe todas as tarefas com seus status.

    Parâmetros:
        tarefas (list): Lista de tarefas a exibir
    """
    # Verifica se a lista está vazia (not tarefas = True se lista está vazia)
    if not tarefas:
        # Se não há tarefas, mostra mensagem
        print('❌ Nenhuma tarefa adicionada ainda!')
        # Sai da função sem fazer mais nada
        return

    # Se chegou aqui, significa que tem tarefas
    # Imprime o cabeçalho da lista
    print('\n📋 Lista de tarefas:')

    # enumerate() = percorre a lista com índice e valor
    # start=1 = começa a contagem do 1 (não do 0)
    # i = índice (1, 2, 3...)
    # tarefa = o dicionário com os dados da tarefa
    for i, tarefa in enumerate(tarefas, start=1):
        # Operador ternário: se a tarefa está completa, mostra ✅, senão ❌
        # tarefa['completada'] = acessa o valor 'completada' do dicionário
        status = '✅' if tarefa['completada'] else '❌'

        # Extrai o nome da tarefa do dicionário
        nome_tarefa = tarefa['tarefa']

        # Imprime a tarefa formatada com número, status e nome
        print(f'{i}. [{status}] {nome_tarefa}')


# FUNÇÃO 3: Atualizar Tarefa
def atualizar_tarefa(tarefas, indice_tarefa, nova_tarefa):
    """
    Função que altera o nome de uma tarefa existente.

    Parâmetros:
        tarefas (list): Lista de tarefas
        indice_tarefa (int): Número da tarefa (começa em 1)
        nova_tarefa (str): Novo nome da tarefa
    """
    # Ajusta o índice porque o usuário vê a partir do 1, mas Python começa do 0
    # Se o usuário digita 1, subtraímos 1 para virar índice 0
    indice_tarefa_ajustado = indice_tarefa - 1

    # Valida se o índice está dentro do intervalo válido
    # >= 0 = não é negativo
    # < len(tarefas) = não ultrapassa o tamanho da lista
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        # Se o índice é válido, acessa o dicionário e altera o valor 'tarefa'
        tarefas[indice_tarefa_ajustado]['tarefa'] = nova_tarefa

        # Confirma a atualização com mensagem
        print(f'✏️ Tarefa {indice_tarefa} atualizada para: {nova_tarefa}')
    else:
        # Se o índice não é válido, mostra erro
        print('⚠️ Índice inválido! Digite um número válido.')

    # Encerra a função
    return


# FUNÇÃO 4: Completar Tarefa
def completar_tarefa(tarefas, indice_tarefa):
    """
    Função que marca uma tarefa como concluída.

    Parâmetros:
        tarefas (list): Lista de tarefas
        indice_tarefa (int): Número da tarefa a completar (começa em 1)
    """
    # Ajusta o índice de 1 para 0 (sistema do usuário vs sistema do Python)
    indice_tarefa_ajustado = indice_tarefa - 1

    # Valida se o índice está dentro do intervalo válido
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        # Acessa o dicionário da tarefa e muda 'completada' para True
        tarefas[indice_tarefa_ajustado]['completada'] = True

        # Confirma com mensagem
        print(f'✨ Tarefa {indice_tarefa} marcada como concluída!')
    else:
        # Erro se índice inválido
        print('⚠️ Índice inválido! Digite um número válido.')

    return


# FUNÇÃO 5: Deletar Tarefa
def deletar_tarefa(tarefas, indice_tarefa):
    """
    Função que remove uma tarefa da lista.

    Parâmetros:
        tarefas (list): Lista de tarefas
        indice_tarefa (int): Número da tarefa a deletar (começa em 1)
    """
    # Ajusta o índice de 1 para 0
    indice_tarefa_ajustado = indice_tarefa - 1

    # Valida se o índice está dentro do intervalo válido
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        # Pega o nome da tarefa antes de deletar (para mostrar na mensagem)
        nome_deletado = tarefas[indice_tarefa_ajustado]['tarefa']

        # pop() = remove o elemento do índice especificado
        tarefas.pop(indice_tarefa_ajustado)

        # Confirma a deleção com mensagem
        print(f'🗑️ Tarefa "{nome_deletado}" foi deletada com sucesso!')
    else:
        # Erro se índice inválido
        print('⚠️ Índice inválido! Digite um número válido.')

    return


# ==================== MENU PRINCIPAL ====================

# Cria uma lista vazia para armazenar as tarefas
# Ela vai ser preenchida com dicionários conforme o usuário adiciona
tarefas = []

# Cria um loop infinito que só encerra quando o usuário escolhe "Sair"
while True:
    # Bloco try-except para capturar erros durante a execução
    try:
        # Exibe o menu visual com separadores e opções
        print('\n' + '=' * 40)  # Linha com 40 caracteres "="
        print('📌 GERENCIADOR DE TAREFAS')
        print('=' * 40)
        print('1. Adicionar tarefas')
        print('2. Visualizar tarefas')
        print('3. Editar tarefas')
        print('4. Completar tarefas')
        print('5. Deletar tarefas')
        print('6. Sair')
        print('=' * 40)

        # Pede entrada do usuário e tenta converter para inteiro
        # Se o usuário digitar uma letra, vai dar ValueError
        escolha = int(input('\nDigite a sua escolha (1-6): '))

        # Valida se a escolha está no intervalo válido (1 a 6)
        # Se não estiver, mostra erro e volta ao início do loop com continue
        if escolha < 1 or escolha > 6:
            print('⚠️ Opção inválida! Digite um número entre 1 e 6.')
            # continue = pula o resto do loop e volta ao while
            continue

        # ===== OPÇÃO 1: ADICIONAR TAREFAS =====
        if escolha == 1:
            # Pede o nome da tarefa ao usuário
            nome_tarefa = input('\nDigite o nome da tarefa: ')

            # .strip() = remove espaços em branco do início e fim
            # Verifica se a string não é vazia (não é só espaços)
            if nome_tarefa.strip():
                # Se tem conteúdo, chama a função para adicionar
                adicionar_tarefas(tarefas, nome_tarefa)
            else:
                # Se está vazio, mostra erro
                print('⚠️ O nome da tarefa não pode ser vazio!')

        # ===== OPÇÃO 2: VISUALIZAR TAREFAS =====
        elif escolha == 2:
            # Simplesmente chama a função de visualização
            visualizar_tarefas(tarefas)

        # ===== OPÇÃO 3: EDITAR TAREFAS =====
        elif escolha == 3:
            # Primeiro mostra as tarefas disponíveis
            visualizar_tarefas(tarefas)

            # Verifica se tem tarefas antes de tentar editar
            # if tarefas = True se a lista tem elementos, False se está vazia
            if tarefas:
                # Outro bloco try-except para capturar erro no índice
                try:
                    # Pede o número da tarefa a editar
                    indice_tarefa = int(input('\nDigite o número da tarefa a ser alterada: '))

                    # Pede o novo nome
                    nova_tarefa = input('Digite o novo nome da tarefa: ')

                    # Valida se o novo nome não é vazio
                    if nova_tarefa.strip():
                        # Se válido, chama a função de atualizar
                        atualizar_tarefa(tarefas, indice_tarefa, nova_tarefa)
                    else:
                        # Se vazio, mostra erro
                        print('⚠️ O nome da tarefa não pode ser vazio!')

                # Se o usuário digitar uma letra no índice, ValueError é capturado aqui
                except ValueError:
                    print('⚠️ Erro! Digite um número válido para o índice.')

        # ===== OPÇÃO 4: COMPLETAR TAREFAS =====
        elif escolha == 4:
            # Mostra as tarefas disponíveis
            visualizar_tarefas(tarefas)

            # Verifica se tem tarefas
            if tarefas:
                # Try-except para capturar erro no índice
                try:
                    # Pede o número da tarefa a completar
                    indice_tarefa = int(input('\nDigite o número da tarefa que deseja completar: '))

                    # Chama a função para marcar como concluída
                    completar_tarefa(tarefas, indice_tarefa)

                # Se digitar letra, ValueError é capturado
                except ValueError:
                    print('⚠️ Erro! Digite um número válido para o índice.')

        # ===== OPÇÃO 5: DELETAR TAREFAS =====
        elif escolha == 5:
            # Mostra as tarefas disponíveis
            visualizar_tarefas(tarefas)

            # Verifica se tem tarefas
            if tarefas:
                # Try-except para capturar erro no índice
                try:
                    # Pede o número da tarefa a deletar
                    indice_tarefa = int(input('\nDigite o número da tarefa que deseja deletar: '))

                    # Chama a função para deletar
                    deletar_tarefa(tarefas, indice_tarefa)

                # Se digitar letra, ValueError é capturado
                except ValueError:
                    print('⚠️ Erro! Digite um número válido para o índice.')

        # ===== OPÇÃO 6: SAIR =====
        elif escolha == 6:
            # Mensagem de encerramento
            print('\n👋 Tenha um ótimo dia!')
            # break = sai do loop while, encerrando o programa
            break

    # ===== EXCEÇÕES GERAIS =====

    # Captura ValueError (quando o usuário digita letra no menu)
    except ValueError:
        print('⚠️ Erro! Digite um número válido no menu.')

    # Captura KeyboardInterrupt (quando o usuário pressiona Ctrl + C)
    except KeyboardInterrupt:
        # \n\n = duas quebras de linha para melhor visualização
        print('\n\n👋 Programa encerrado pelo usuário.')
        # break = sai do loop
        break

    # Captura qualquer outra exceção não prevista
    # Exception = classe mãe de todas as exceções
    # as e = armazena o erro em uma variável chamada 'e'
    except Exception as e:
        # Mostra a mensagem de erro de forma amigável
        print(f'❌ Erro inesperado: {e}')