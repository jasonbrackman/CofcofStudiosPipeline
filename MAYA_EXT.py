#variable con orden de tipo de nodo con su sufijo.
namingDicc={
#Joints:
'JSK': 'joint',
'JFA': 'joint',
'JFK': 'joint',
'JIK': 'joint',
'JFR': 'joint',
'IKH': 'joint',
'EFF': 'joint',
#Meshes:
'MSK': 'transform',
'MSKSH': 'mesh',
'MFD': 'transform',
'MFDSH': 'mesh',
'LOW': 'transform',
'LOWSH': 'mesh',
'BBX': 'transform',
'BBXSH': 'mesh',
'MFR': 'transform',
'MFRSH': 'mesh',
'MBL': 'transform',
'MBLSH': 'mesh',
'SHP':'transform',
'SHPSH':'mesh',
'TRF':'offsetgrp',
'SLC':'subdivitionLowCharacter',
'TFATT':'transferAttributes',
'PRC':'polyReduce',
#Nurbs:
'NSK':'transform',
'NSKSH':'nurbsSurface',
#Constraints:
'PCNS': 'pointConstraint',
'ACNS': 'aimConstraint',
'OCNS': 'orientConstraint',
'SCNS': 'scaleConstraint',
'HCNS': 'parentConstraint',
'CCNS': 'curveConstraint',
'VCNS': 'poleVectorConstraint',
#RCNS:'rotatorCuffConstraint',''
#TCNS:'rot360NodeConstraint',''
#UtilityNodes:
'MMX': 'multMatrix',
'CND': 'condition',
'MDN': 'multiplyDivide',
'MDL': 'multDoubleLinear',
'PLS': 'plusMinusAverage',
'DSN': 'distanceDimShape',
'ANG': 'angleBetween',
'CPM': 'closestPointOnMesh',
'VCP': 'vectorProduct',
'PTH': 'motionPath',
'POC': 'pointOnCurve',
'CPC': 'closestPointOnCurve',
'CRVI': 'curveInfo',
'CPS': 'closestPointOnSurface',
#RCT: 'rayContact',
#CYC: 'cycleNode',
'DIS': 'displayNode',
'BLC': 'blendColors',
'DSB': 'distanceBetween',
'CLM': 'clamp',
'TRF': 'transform',
'BLW': 'blendWeighted',
'SPI': 'samplerInfo',
'RVS': 'reverse',
'3DP': 'place3dTexture',
'STR': 'setRange',
'2DP': 'place2dTexture',
'CON': 'contrast',
'GAM': 'gammaCorrect',
'H2R': 'hsvToRgb',
'LUM': 'luminance',
'RMP': 'remapColor',
'RMH': 'remapHsv',
'RMV': 'remapValue',
'R2H': 'rgbToHsv',
'SMR': 'smear',
'SFL': 'surfaceLuminance',
'PRT': 'particleSamplerInfo',
'IMP': 'imagePlane',
'BMP2D': 'bump2d',
'BMP3D': 'bump3d',
'HEI': 'heightField',
'PRJ': 'projection',
'ADD':'addDoubleLinear',
'EXPR':'expression',
#Locator:
'LCH': 'transform',
'LIK': 'transform',
'LCN': 'transform',
'LMC': 'transform',
'ZTR': 'transform',
'TRF': 'transform',
'CST': 'transform',
#Deformers:
'CLS': 'transform',
'CLSSH': 'clusterHandle',
'DCLU': 'cluster',
'DCLUST': 'objectSet',
'LAT': 'transform',
'DLAT': 'ffd',
'DLATSH': 'lattice',
'DWRA': 'wrap',
'DWRAST': 'objectSet',
'BEN': 'transform',
'DBEN': 'deformBend',
'NBEN': 'nonLinear',
'DBENST': 'objectSet',
'FLA': 'transform',
'DFLA': 'deformFlare',
'NFLA': 'nonLinear',
'DFLAST': 'objectSet',
'SIN': 'transform',
'DSIN': 'deformSine',
'NSIN': 'nonLinear',
'DSINST': 'objectSet',
'SQU': 'transform',
'DSQU': 'deformSquash',
'NSQU': 'nonLinear',
'DSQUST': 'objectSet',
'TWI': 'transform',
'DTWI': 'deformTwist',
'NTWI': 'nonLinear',
'DTWIST': 'objectSet',
'WAV': 'transform',
'DWAV': 'deformWave',
'NWAV': 'nonLinear',
'DWAVST': 'objectSet',
'DSCU': 'sculpt',
'DSCULC': 'locator',
'DSCUST': 'objectSet',
'DWIR': 'wire',
'DWIRST': 'objectSet',
'DBLE': 'blendShape',
'DBLEST': 'objectSet',
'SCL' : 'skinCluster',
'TWK' : 'tweak',
'FLC': 'follicle',
#SHAPE:
'CNT': 'transform',
'CNTSH': 'nurbsCurve',
#VSH: [visual help Shape]
#DISPLAY:
'NOTA': 'annotationShape',
#CONTAINER:
'CNTR': 'container',
'CSTR': 'container',
'MSKR': 'container',
'SCER': 'container',
'RENR': 'container',
#CURVES:
'CRV': 'transform',
'CRVSH': 'nurbsCurve',
'CRW': 'nurbsCurve',
'CRU': 'transform',
'CRUSH': 'nurbsCurve',
'CSK': 'transform',
'CSKSH': 'mesh',
#FLUID:
'FLU': 'transform',
'FLUSH': 'fluidShape',
'FLUE': 'fluidEmitter',
#Smooth Nodes:
'SMT': 'polySmoothFace',
'SMP': 'polySmoothProxy',
'SMO': 'mesh',
#Materials:
'MTBLN': 'blinn',
'MTANI': 'anisotropic',
'MTHAI': 'hairTubeShader',
'MTLMB': 'lambert',
'MTLAY': 'layeredShader',
'MTOCE': 'oceanShader',
'MTPHO': 'phong',
'MTPHOE': 'phongE',
'MTRAM': 'rampShader',
'MTSHA': 'shadingMap',
'MTSUR': 'surfaceShader',
'MTBCK': 'useBackground',
'SHDG':'shadingEngine',
'STNC':'stencil',
#Textures:
'TXBUL': 'bulge',
'TXCHE': 'checker',
'TXCLT': 'cloth',
'TXFIL': 'file',
'TXF2D': 'fluidTexture2D',
'TXFRA': 'fractal',
'TXGRI': 'grid',
'TXMOV': 'movie',
'TXMOU': 'mountain',
'TXNOI': 'noise',
'TXOCE': 'ocean',
'TXPSD': 'psdFileTex',
'TXRAM': 'ramp',
'TXWAT': 'water',
'TXBRO': 'brownian',
'TXCLO': 'cloud',
'TXCRA': 'crater',
'TXF3D': 'fluidTexture3D',
'TXGRA': 'granite',
'TXLEA': 'leather',
'TXMAR': 'marble',
'TXROC': 'rock',
'TXSNO': 'snow',
'TXSOL': 'solidFractal',
'TXSTU': 'stucco',
'TXVOL': 'volumeNoise',
'TXWOO': 'wood',
'TXLAY': 'layeredTexture',
#Lights:
'LGAMB': 'transform',
'LGAMBSH': 'ambientLight',
'LGARE':  'transform',
'LGARESH':  'areaLight',
'LGDIR':  'transform',
'LGDIRSH':  'directionalLight',
'LGPOI':  'transform',
'LGPOISH':  'pointLight',
'LGSPO':  'transform',
'LGSPOSH': 'spotLight',
'LGVOL':  'volumeLight',
'LGINF':  'lightInfo',
#MentalRayLights:
'MIMTDGS': 'dgs_material',
'MIMTDIE': 'dielectric_material',
'MIMTCAR': 'mi_car_paint_phen',
#'MIMTMIA': 'mia_material',
'MIMTGLO': 'mib_glossy_reflection',
'MIMTILU': 'mib_illum_blinn',
'MILGSUN': 'mia_physicalsun',
'MILGPOR': 'mia_portal_light',
'MILGBLA': 'mib_blackbody',
'MILGCIE': 'mib_cie_d',
'MILGBLA': 'mib_cie_d',
'MILGOCC': 'mib_fg_occlusion',
'MILGINF': 'mib_light_infinite',
'MILGPHO': 'mib_light_photometric',
'MILGPOI': 'mib_light_point',
'MILGPHY': 'physical_light',
#MentalRay:
'MIAM':'mia_material',
'MIAMX':'mia_material_x',
'MIAMXP':'mia_material_x_passes',
'SSS': 'misss_fast_skin_maya',
'SSTEX': 'mentalrayTexture',
'LMAP': 'misss_fast_lmap_maya',
'BPASST': 'mib_passthrough_bump_map',
'TVECT': 'mib_texture_vector',
'BBYN': 'mib_bump_basis',
'MRIBL': 'mentalrayIblShape',
#Camera
'CAM':'camera',
'SHOT':'shot',
'SCAM':'transform',
'SCAMSH':'stereoRigCamera',
'SCAMF':'stereoRigFrustum',
#Arnold:
'AISDL':'aiSkyDomeLight',
'AIRSW':'aiRaySwitch',
'AIBRN':'aiBarndoor',
'AIGBO':'aiGobo',
'AILBL':'aiLightBlocker',
'AILDK':'aiLightDecay',
'AIDIS':'aiDisplacement',
'AIAO':' aiAmbientOcclusion',
'AIHIR':'aiHair',
'AISDR':'aiStandard',
'AIUTL':'aiUtility',
'AIWRE':'aiWireframe',
'AIFOG':'aiFog',
'AIVSC':'aiVolumeScattering',
'AISKY':'aiSky',
'AIAOV':'aiAOV',
'AIUDC':'aiUserDataColor',
'AITSS':'tripleShadingSwitch',
'AIWTC':'aiWriteColor',
#Alshader:
'ALFN':'alFlowNoise',
#ANIMATION:
'ACN':'animCurveTA'
}