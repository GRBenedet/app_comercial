import os
import sys
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from Funtions.tela_menu import TelaMenu
from Funtions.tela_ruido_ambiental import TelaRuidoAmbiental


def resource_path(relative_path):
    """ Retorna o caminho correto do arquivo, seja no código-fonte ou no executável """
    if hasattr(sys, '_MEIPASS'):  # PyInstaller cria essa variável no executável
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# Carregar os arquivos KV do diretório 'kv'
dir_path = os.path.dirname(os.path.abspath(__file__))
Builder.load_file(os.path.join(dir_path, "telas", "tela_menu.kv"))
Builder.load_file(os.path.join(dir_path, "telas", "tela_ruido_ambiental.kv"))

# Gerenciador de Telas
class GerenciadorTelas(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(TelaMenu(name='menu'))
        self.add_widget(TelaRuidoAmbiental(name='ruido_ambiental'))
        self.current = 'menu'  # Define a tela inicial

class RouteApp(App):
    FONT_PATH = resource_path("assets/fonts/Roboto/static/Roboto-Regular.ttf")

    def build(self):
        return GerenciadorTelas()

if __name__ == "__main__":
    RouteApp().run()