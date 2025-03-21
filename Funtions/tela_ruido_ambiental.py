import requests
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, RoundedRectangle
from docx import Document
import winshell
from pathlib import Path
from kivy.uix.label import Label
import utils.cars

class TelaRuidoAmbiental(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.waypoint_limit = 23  # Padrão: Listagem Padrão (5 waypoints)

    def set_bate_volta(self, instance):
        # Chama a função importada de utils, passando self e o botão (instance)
        utils.cars.set_bate_volta(self, instance)

    def set_padrao(self, instance):
         utils.cars.set_padrao(self, instance)

    def update_button_color(self, button, color):
         utils.cars.update_button_color(self, button, color)
    
    def start_calculation(self):
         utils.cars.start_calculation(self)

    def split_waypoints(self, waypoints):
        return  utils.cars.split_waypoints(self, waypoints)

    def get_route(self, origin, destination, waypoints):
         return  utils.cars.get_route(self, origin, destination, waypoints)

    def get_toll_cost(self, origin, destination, waypoints):
        return  utils.cars.get_toll_cost(self, origin, destination, waypoints)

    def calculate_routes(self, origin, destination, waypoints, filename):
         utils.cars.calculate_routes(self, origin, destination, waypoints, filename)

    def export_to_word(self, routes_data, total_cost, filename):
         utils.export.export_to_word(self, routes_data, total_cost, filename)
    
    def all_reset(self):
         utils.cars.all_reset(self)