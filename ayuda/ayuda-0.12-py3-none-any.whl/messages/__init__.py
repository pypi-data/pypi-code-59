import os
from os.path import join

teddy = """
 ( \---/ )
 ) . . (
________________________,--._(___Y___)_,--._______________________
 `--'           `--'
"""
doing_backup = '{}\n   Realizando Backup...'.format(teddy)


teddy_save = """
 ( \---/ )
 ) . . (
 ( ._Y_, )
 \ \_/ /
________________________,--.__/_____\__,--._______________________
 `--'           `--'
"""
backup_sucess = '{}\n Backup realizado!'.format(teddy_save)

git_explication = u"""
 cree un nuevo proyecto en gitlab o github

 y copie su url ssh a continuación\nej: git@gitlab.com:<user>/ayuda.git
"""

welcome_url = join(os.path.dirname(os.path.realpath(__file__)), 'welcome.md') # TODO delete this

welcome_icon = """
 .--.              .--.
 : (\\ ". _......_ ." /) :
 '.    `        `    .'
  /'   _        _   `\\
 /     0}      {0     \\
 |       /      \\       |
 |     /'        `\\     |
 \\   | .  .==.  . |   /
  '._ \\.' \\__/ './ _.'
  /  ``'._-''-_.'``  \\

"""
welcome = '{}\n Bienvenido a Ayuda'.format(welcome_icon)