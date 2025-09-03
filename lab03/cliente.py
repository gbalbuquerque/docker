import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://broker:5555")

opcao = input("Entre com a opção: ")
while opcao != "sair":
    match opcao:
        case "adicionar":
            titulo = input("Entre com a tarefa: ")
            descricao = input("Entre com a descrição da tarefa: ")

            request = {
                "opcao": "adicionar",
                "dados": {
                    "titulo": titulo,
                    "desc": descricao
                }
            }

            socket.send_json(request)
            reply = socket.recv_string()
            if reply.split(":")[0] == "ERRO":
                print(reply, flush=True)

        case "atualizar":
            titulo = input("Digite a tarefa: ")
            newTitulo = input("Digite a nova tarefa ")
            newDesc = input("Digite a nova descr: ")

            request = {
                "opcao": "atualizar",
                "dados": {
                    "titulo": titulo,
                    "newTitulo": newTitulo,
                    "newDesc": newDesc,
                }
            }

            socket.send_json(request)
            reply = socket.recv_string()
            if reply.split(":")[0] == "ERRO":
                print(reply, flush=True)
        case "deletar":
            pass
        case "listar":
            pass
        case "buscar":
            pass
        case _:
            print("Opção não encontrada")

