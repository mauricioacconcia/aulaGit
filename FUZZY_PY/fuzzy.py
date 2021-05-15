# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:29:12 2021

@author: Diasi7
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

qualidade = ctrl.Antecedent(np.arange(0, 11, 1), 'qualidade')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0, 21, 1), 'gorjeta')

qualidade.automf(number=3, names=['ruim', 'boa', 'saborosa'])
servico.automf(number=3, names=['ruim', 'aceitavel', 'otimo'])

gorjeta['baixa'] = fuzz.sigmf(gorjeta.universe, 5, -1)
gorjeta['media'] = fuzz.gaussmf(gorjeta.universe, 10, 3)
gorjeta['alta'] = fuzz.pimf(gorjeta.universe, 10, 20, 25, 50)

qualidade.view()

gorjeta.view()

regra1 = ctrl.Rule(qualidade['ruim']|servico['ruim'], gorjeta['baixa'])
regra2 = ctrl.Rule(servico['aceitavel'], gorjeta['media'])
regra3 = ctrl.Rule(servico['otimo']|qualidade['saborosa'], gorjeta['alta'])

sistema = ctrl.ControlSystem([regra1,regra2,regra3])
simulacao = ctrl.ControlSystemSimulation(sistema)

simulacao.input['qualidade'] = 9
simulacao.input['servico'] = 8
simulacao.compute()

print(simulacao.output['gorjeta'])
gorjeta.view(sim=simulacao)










