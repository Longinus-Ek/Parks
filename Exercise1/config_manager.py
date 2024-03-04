import json
import os

def read_configuration():
    if os.path.exists("config.json"):
        with open("config.json", "r") as file:
            data = json.load(file)
            if data:
                print("Conteúdo do arquivo config.json:")
                print(json.dumps(data, indent=4))
            else:
                print("O arquivo config.json está vazio.")
    else:
        print("O arquivo config.json não existe.")

def write_configuration():
    server_name = input("Informe o nome do servidor: ")
    server_ip = input("Informe o IP do servidor: ")
    server_password = input("Informe a senha do servidor: ")

    config_data = {
        "server_name": server_name,
        "server_ip": server_ip,
        "server_password": server_password
    }

    with open("config.json", "w") as file:
        json.dump(config_data, file, indent=4)
        print("Informações salvas com sucesso no arquivo config.json:")
        print(json.dumps(config_data, indent=4))

def main():
    while True:
        print("\nOpções disponíveis:")
        print("1 - Ler configuração")
        print("2 - Escrever configuração")
        choice = input("Escolha uma opção (1 ou 2): ")

        if choice == "1":
            read_configuration()
            break
        elif choice == "2":
            write_configuration()
            break
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()
