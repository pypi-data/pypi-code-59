from netmiko import ConnectHandler
import click

@click.command()
@click.help_option()
@click.option('--name', '-n', prompt='Nom de code du magasin', required=True, help='Nom de code du magasin')
@click.option('--fichier', '-f', prompt='Nom du fichier avec les IPs', required=True, help='Nom du fichier avec les IPs')
@click.option('--sortie', '-s', prompt='Nom du fichier de sortie', help='Nom du fichier de sortie', default="scan_result.txt")
@click.option('--username', '-u', prompt=True, required=True, help='Username')
@click.option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True, help='Password')
def scan_super(name,fichier,sortie,username,password):
    devices = open(fichier).readlines()

    for ip in devices:
        cisco = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": username,
            "password": password,
        }

        try:
            net_connect = ConnectHandler(**cisco)
            net_connect.enable()
            commandes_inventaire = [ 'show interface status', 'show cdp neighbors', 'show lldp neighbors', 'show interface', 'show running-config | section interface', 'show interface trunk', 'show interface summary' ]
            output = "Scan du magasin " + name + "\r\n"
            for commande in commandes_inventaire:
                try:
                    output += "\r\n"
                    output += commande + "\r\n"
                    output += "\r\n"
                    output += net_connect.send_command(commande) + "\r\n"
                    print()
                    print("Traitement de l'ip " + ip + "commande : " + commande)
                    print()
                except:
                    print (commande + "FAILED")
                    output += commande + "FAILED"

            net_connect.disconnect()

            f = open(sortie, 'a+')
            f.write(output)
            f.close()

        except:
            print (ip + " is a fail")


if __name__ == '__main__':
    scan_super()
