from WickContractions.ops.operator import *
from WickContractions.ops.elemental import *
from WickContractions.ops.quarks import *
from WickContractions.ops.commuting import *

cIdx = lambda c : 'c_{' + str(c) + '}'
sIdx = lambda s : 's_{' + str(s) + '}'
epsilonTensor = lambda c0 : EpsilonTensor([cIdx(c0), cIdx(c0+1), cIdx(c0+2), cIdx(c0+3)])
spinTensor = lambda name, s0: SpinMatrix(name, [sIdx(s0), sIdx(s0+1), sIdx(s0+2), sIdx(s0+3)])

nextSpinIdx = 0
nextColorIdx= 0
nextGammaIdx = 0

def quark(anti, f, t, x):
    global nextSpinIdx, nextColorIdx
    q=Quark(anti, f, sIdx(nextSpinIdx), cIdx(nextColorIdx), t, x)
    nextSpinIdx+=1
    nextColorIdx+=1
    return q

def baryonSource(coef, flavors, x):
    global nextGammaIdx
    eTensor = epsilonTensor(nextColorIdx)
    sTensor = spinTensor('\\Gamma^{'+str(nextGammaIdx)+'}', nextSpinIdx)
    nextGammaIdx+=1

    q0 = quark(True, flavors[0], 't_i', x)
    q1 = quark(True, flavors[1], 't_i', x)
    q2 = quark(True, flavors[2], 't_i', x)
    q3 = quark(True, flavors[3], 't_i', x)

    return ElementalOperator(coef,
        [eTensor, sTensor],
        [q0,q1,q2,q3]
    )

def baryonSink(coef, flavors, x):
    global nextGammaIdx
    eTensor = epsilonTensor(nextColorIdx)
    sTensor = spinTensor('\\Gamma^{'+str(nextGammaIdx)+'}', nextSpinIdx)
    nextGammaIdx+=1

    q0 = quark(False, flavors[0], 't_f', x)
    q1 = quark(False, flavors[1], 't_f', x)
    q2 = quark(False, flavors[2], 't_f', x)
    q3 = quark(False, flavors[3], 't_f', x)

    return ElementalOperator(coef,
        [eTensor, sTensor],
        [q0,q1,q2,q3]
    )


def BBsource(coef, f0, f1, x0, x1):
    global nextGammaIdx
    eTensor1 = epsilonTensor(nextColorIdx)
    sTensor1 = spinTensor('\\Gamma^{'+str(nextGammaIdx)+'}', nextSpinIdx)
    nextGammaIdx+=1

    q0 = quark(True, f0[0], 't_i', x0)
    q1 = quark(True, f0[1], 't_i', x0)
    q2 = quark(True, f0[2], 't_i', x0)
    q3 = quark(True, f0[3], 't_i', x0)

    eTensor2 = epsilonTensor(nextColorIdx)
    sTensor2 = spinTensor('\\Gamma^{'+str(nextGammaIdx)+'}', nextSpinIdx)
    nextGammaIdx+=1

    q4 = quark(True, f1[0], 't_i', x1)
    q5 = quark(True, f1[1], 't_i', x1)
    q6 = quark(True, f1[2], 't_i', x1)
    q7 = quark(True, f1[3], 't_i', x1)

    return ElementalOperator(coef,
        [eTensor1, sTensor1, eTensor2, sTensor2],
        [q0,q1,q2,q3,q4,q5,q6,q7]
    )

def BBsink(coef, f0, f1, x0, x1):
    global nextGammaIdx
    eTensor1 = epsilonTensor(nextColorIdx)
    sTensor1 = spinTensor('\\Gamma^{'+str(nextGammaIdx)+'}', nextSpinIdx)
    nextGammaIdx+=1

    q0 = quark(False, f0[0], 't_f', x0)
    q1 = quark(False, f0[1], 't_f', x0)
    q2 = quark(False, f0[2], 't_f', x0)
    q3 = quark(False, f0[3], 't_f', x0)

    eTensor2 = epsilonTensor(nextColorIdx)
    sTensor2 = spinTensor('\\Gamma^{'+str(nextGammaIdx)+'}', nextSpinIdx)
    nextGammaIdx+=1

    q4 = quark(False, f1[0], 't_f', x1)
    q5 = quark(False, f1[1], 't_f', x1)
    q6 = quark(False, f1[2], 't_f', x1)
    q7 = quark(False, f1[3], 't_f', x1)

    return ElementalOperator(coef,
        [eTensor1, sTensor1, eTensor2, sTensor2],
        [q0,q1,q2,q3,q4,q5,q6,q7]
    )