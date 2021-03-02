
#MODULOS DE IMPRESSÃO

"""imprimir os modelos para a 3d"""
def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_designs = unprinted_design.pop()
        print("Imprimindo Model: {}".format(current_designs))

        completed_models.append(current_designs)


"""mostrar as mais recentes impressões"""
def show_completed_models(completed_models):
    print("\n O seguinte modelo foi impresso: ")
    for completed in completed_models:
        print(completed)