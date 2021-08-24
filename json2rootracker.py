import json
import ROOT
import numpy as np
import sys

input_files = sys.argv[1:-1]
output_filename = sys.argv[-1]

MAX_PARTICLES = 100

fo = ROOT.TFile(output_filename, 'RECREATE')
tree = ROOT.TTree('gRooTracker', 'gRooTracker')
EvtNum = np.empty((1,), dtype='i4')
EvtFlags = np.empty((1,), dtype=ROOT.TBits)
EvtCode = np.empty((1,), dtype=ROOT.TObjString)
EvtVtx = np.empty((1, 4), dtype='f8')
EvtXSec = np.empty((1,), dtype='f8')
EvtDXSec = np.empty((1,), dtype='f8')
EvtWght = np.empty((1,), dtype='f8')
EvtProb = np.empty((1,), dtype='f8')
StdHepN = np.empty((1,), dtype='i4')
StdHepPdg = np.empty((MAX_PARTICLES), dtype='i4')
StdHepStatus = np.empty((MAX_PARTICLES), dtype='i4')
StdHepP4 = np.empty((MAX_PARTICLES, 4), dtype='f8')
StdHepX4 = np.empty((MAX_PARTICLES, 4), dtype='f8')
StdHepPolz = np.empty((MAX_PARTICLES, 3), dtype='f8')
StdHepFd = np.empty((MAX_PARTICLES), dtype='i4')
StdHepLd = np.empty((MAX_PARTICLES), dtype='i4')
StdHepFm = np.empty((MAX_PARTICLES), dtype='i4')
StdHepLm = np.empty((MAX_PARTICLES), dtype='i4')
NuParentPdg = np.empty((1,), dtype='i4')
NuParentDecMode = np.empty((1,), dtype='i4')
NuParentDecP4 = np.empty((4,), dtype='f8')
NuParentDecX4 = np.empty((4,), dtype='f8')
NuParentProX4 = np.empty((4,), dtype='f8')
NuParentProP4 = np.empty((4,), dtype='f8')
NuParentProNVtx = np.empty((1,), dtype='i4')
tree.Branch("EvtNum", EvtNum, "EvtNum/I")
tree.Branch("EvtFlags", "TBits", EvtFlags, 32000, 1)
tree.Branch("EvtCode", "TObjString", EvtCode, 32000, 1)
tree.Branch("EvtVtx", EvtVtx, "EvtVtx[4]/D")
tree.Branch("EvtXSec", EvtXSec, "EvtXsec/D")
tree.Branch("EvtDXSec", EvtDXSec, "EvtDXsec/D")
tree.Branch("EvtWght", EvtWght, "EvtWght/D")
tree.Branch("EvtProb", EvtProb, "EvtProb/D")
tree.Branch("StdHepN", StdHepN, "StdHepN/I")
tree.Branch("StdHepPdg", StdHepPdg, "StdHepPdg[StdHepN]/I")
tree.Branch("StdHepStatus", StdHepStatus, "StdHepStatus[StdHepN]/I")
tree.Branch("StdHepP4", StdHepP4, "StdHepP4[StdHepN][4]/D")
tree.Branch("StdHepX4", StdHepX4, "StdHepX4[StdHepN][4]/D")
tree.Branch("StdHepPolz", StdHepPolz, "StdHepPolz[StdHepN][3]/D")
tree.Branch("StdHepFd", StdHepFd, "StdHepFd[StdHepN]/I")
tree.Branch("StdHepLd", StdHepLd, "StdHepLd[StdHepN]/I")
tree.Branch("StdHepFm", StdHepFm, "StdHepFm[StdHepN]/I")
tree.Branch("StdHepLm", StdHepLm, "StdHepLm[StdHepN]/I")
tree.Branch("NuParentPdg", NuParentPdg, "NuParentPdg/I")
tree.Branch("NuParentDecMode", NuParentDecMode, "NuParentDecMode/I")
tree.Branch("NuParentDecP4", NuParentDecP4, "NuParentDecP4[4]/D")
tree.Branch("NuParentDecX4", NuParentDecX4, "NuParentDecX4[4]/D")
tree.Branch("NuParentProP4", NuParentProP4, "NuParentProP4[4]/D")
tree.Branch("NuParentProX4", NuParentProX4, "NuParentProX4[4]/D")
tree.Branch("NuParentProNVtx", NuParentProNVtx, "NuParentProNVtx/I")

for filename in input_files:
    with open(filename, 'r') as fi:
        data = json.load(fi)

    for ev in data:
        EvtNum = data['EvtNum']
        EvtFlags = data['EvtFlags']
        EvtCode = data['EvtCode']
        EvtVtx = data['EvtVtx']
        EvtXSec = data['EvtXSec']
        EvtDXSec = data['EvtDXSec']
        EvtWght = data['EvtWght']
        EvtProb = data['EvtProb']
        StdHepN = data['StdHepN']
        StdHepPdg[:StdHepN] = data['StdHepPdg']
        StdHepStatus[:StdHepN] = data['StdHepStatus']
        StdHepP4[:StdHepN] = data['StdHepP4']
        StdHepX4[:StdHepN] = data['StdHepX4']
        StdHepPolz[:StdHepN] = data['StdHepPolz']
        StdHepFd[:StdHepN] = data['StdHepFd']
        StdHepLd[:StdHepN] = data['StdHepLd']
        StdHepFm[:StdHepN] = data['StdHepFm']
        StdHepLm[:StdHepN] = data['StdHepLm']
        NuParentPdg = data['NuParentPdg']
        NuParentDecMode = data['NuParentDecMode']
        NuParentDecP4 = data['NuParentDecP4']
        NuParentDecX4 = data['NuParentDecX4']
        NuParentProX4 = data['NuParentProX4']
        NuParentProP4 = data['NuParentPro4P']
        NuParentProNVtx = data['NuParentNVtx']

        tree.Fill()

tree.Write()
fo.Close()
