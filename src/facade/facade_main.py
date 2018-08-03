from walrus import *
from facade.aluno_facade import AlunoFacade
# from facade.historico_facade import HistoricoFacade
from facade.observador_facade import ObservadorFacade
from facade.estrutura_facade import EstruturaFacade
from facade.zInativos_facade import ZinativosFacade
from facade.jogo_facade import OaConcluidoFacade

class Facade(AlunoFacade, OaConcluidoFacade,ObservadorFacade, EstruturaFacade, ZinativosFacade):
    def __init__(self):
        super(Facade, self).__init__()
        # # super(ObservadorFacade, self).__init__()
        ObservadorFacade.__init__(self)
        OaConcluidoFacade.__init__(self)
        EstruturaFacade.__init__(self)
        AlunoFacade.__init__(self)
        # HistoricoFacade.__init__(self)
        ZinativosFacade.__init__(self)

