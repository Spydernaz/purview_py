

import purview_py

authToken = purview_py.auth.TokenAuth('a','b','c')

controller = purview_py.Controller()

controller.getType('DataSet') ==> <Class purview_py.TypeDef>
