import os


rndPath = os.path.normpath("F:/rnd")
rndBinPath = os.path.normpath("D:/rndBin")
prodPath = os.path.normpath("D:/prods")
appsPath = os.path.normpath("F:/apps")
studioPath = os.path.normpath(os.path.join(rndPath, "workspace", "studio"))

djvPath = os.path.join(appsPath, "djvView", "djv-1.0.3-Windows-64")
djvView = os.path.join(djvPath, "bin", "djv_view.exe")
djvInfo = os.path.join(djvPath, "bin", "djv_info.exe")
djvList = os.path.join(djvPath, "bin", "djv_ls.exe")
djvConvert = os.path.join(djvPath, "bin", "djv_convert.exe")
nConvert = os.path.join(appsPath, "nConvert", "nconvert.exe")
ffmpeg = os.path.join(appsPath, "ffmpeg", "bin", "ffmpeg.exe")

pyCharm = '"C:/Program Files (x86)/JetBrains/PyCharm Community Edition 3.4.1/bin/pycharm.exe "'
mayaPath = os.path.join(appsPath, "Autodesk", "Maya2014")
maya = os.path.join(mayaPath, "bin", "maya.exe")
mayaPy = os.path.join(mayaPath, "bin", "mayapy.exe")
mayaBatch = os.path.join(mayaPath, "bin", "mayabatch.exe")
mayaRender = os.path.join(mayaPath, "bin", "Render.exe")
nukePath = os.path.join(appsPath, "Nuke9.0v1")
nuke = os.path.join(nukePath, "nuke9.0.exe")
