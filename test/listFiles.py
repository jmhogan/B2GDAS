import os,sys

samplelist = [

'/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',

'/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
'/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/ST_s-channel_top_leptonDecays_13TeV-PSweights_powheg-pythia/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/ST_s-channel_antitop_leptonDecays_13TeV-PSweights_powheg-pythia/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',

'/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
'/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
'/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
'/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
'/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
'/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',

'/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM',
'/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v2/MINIAODSIM',
'/TT_Mtt-700to1000_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',

'/RSGluonToTT_M-500_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-750_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-1000_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-1250_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-1500_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-2000_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-2500_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-3000_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-3500_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-4000_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-4500_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',
'/RSGluonToTT_M-5000_TuneCP5_13TeV-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM',

]

samplenamelist = [

'WJetsToLNuPt100To250',
'WJetsToLNuPt250To400',
'WJetsToLNuPt400To600',
'WJetsToLNuPt600ToInf',
'WJetsToLNuPt50To100',

'STtWantitop',
'STtWtop',
'STtchannelantitop',
'STtchanneltop',
'STschanneltop',
'STschannelantitop',

'QCDHT700to1000',
'QCDHT500to700',
'QCDHT300to500',
'QCDHT200to300',
'QCDHT2000toInf',
'QCDHT1500to2000',
'QCDHT1000to1500',

'TTToHadronic',
'TTToSemiLeptonic',
'TTTo2L2Nu',
'TTMtt700to1000',
'TTMtt1000toInf',

'RSGluonToTTM500',
'RSGluonToTTM750',
'RSGluonToTTM1000',
'RSGluonToTTM1250',
'RSGluonToTTM1500',
'RSGluonToTTM2000',
'RSGluonToTTM2500',
'RSGluonToTTM3000',
'RSGluonToTTM3500',
'RSGluonToTTM4000',
'RSGluonToTTM4500',
'RSGluonToTTM5000',

]


datalist2017 = [
    '/SingleElectron/Run2017B-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017C-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017D-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017E-31Mar2018-v1/MINIAOD',
    '/SingleElectron/Run2017F-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017B-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017C-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017D-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017E-31Mar2018-v1/MINIAOD',
    '/SingleMuon/Run2017F-31Mar2018-v1/MINIAOD',
    ]

datanamelist2017 = [
    'ElecRun2017B',
    'ElecRun2017C',
    'ElecRun2017D',
    'ElecRun2017E',
    'ElecRun2017F',
    'MuonRun2017B',
    'MuonRun2017C',
    'MuonRun2017D',
    'MuonRun2017E',
    'MuonRun2017F',
    ]

i = 0
for sample in samplelist:
    print 'listing files in',sample
    os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query=\"file dataset = '+sample+'\" >& inputfiles/'+sample.split('/')[1]+'.txt')
    
    #print 'creating crab file for',sample
    #os.system('cp crab_submit_mc.py crab_submit_mc_'+samplenamelist[i]+'.py')
    #os.system('sed -i "s|DATASET|'+sample+'|" crab_submit_mc_'+samplenamelist[i]+'.py')
    #os.system('sed -i "s|NAME|'+samplenamelist[i]+'|" crab_submit_mc_'+samplenamelist[i]+'.py')
    #i += 1

i = 0
for sample in datalist2017:
    print 'listing files in',sample
    os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" >& inputfiles/'+sample.split('/')[1]+'_'+sample.split('/')[2]+'.txt')

    #print 'creating crab file for',sample
    #os.system('cp crab_submit_data.py crab_submit_data_'+datanamelist2017[i]+'.py')
    #os.system('sed -i "s|DATASET|'+sample+'|" crab_submit_data_'+datanamelist2017[i]+'.py')
    #os.system('sed -i "s|NAME|'+datanamelist2017[i]+'|" crab_submit_data_'+datanamelist2017[i]+'.py')
    #i += 1
