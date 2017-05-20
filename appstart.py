from ui.console import Ui
from repository.repo import Repo
from domain.entities import Ship
from controller.controller import Controller

repo = Repo()
controller = Controller(repo)
ui = Ui(controller)

ui.start()
