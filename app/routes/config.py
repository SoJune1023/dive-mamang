from flask import Blueprint

config_bp = Blueprint('config_bp', __name__)

@config_bp.routes('/loadConfigValue', methods = ['POST'])
def loadConfigValue():
    # TODO: Load config value from data/user/config.json
    # TODO: Return config value to electron.
    pass

@config_bp.routes('/updateConfigValue', methos = ['POST'])
def updateConfigValue():
    # TODO: Get json
    # payload : dict
    # {
    #     "willUpdate" : str,
    #     "newValue" : str
    # }
    # TODO: update data/user/config.json
    # TODO: return 0
    pass