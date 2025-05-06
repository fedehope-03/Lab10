import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        if anno == "":
            self._view.create_alert("Non hai inserito niente!!!")
        else:
            try:
                anno = int(anno)
            except ValueError:
                self._view.create_alert("Non hai inserito un numero!!!")
            if 1815<anno<2017:

                self._model.buildgraph(anno)
                for c in self._model.getNodes():
                    pass


            else:
                self._view.create_alert("Anno sbagliato!!!")
        self._view.update_page()

