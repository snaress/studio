import os


rndPath = os.path.normpath("F:/rnd")
rndBinPath = os.path.normpath("D:/rndBin")
appsPath = os.path.normpath("F:/apps")
studioPath = os.path.normpath(os.path.join(rndPath, "workspace", "studio"))

djvPath = os.path.join(appsPath, "djvView", "djv-1.0.3-Windows-64")
djvView = os.path.join(djvPath, "bin", "djv_view.exe")
djvInfo = os.path.join(djvPath, "bin", "djv_info.exe")
djvList = os.path.join(djvPath, "bin", "djv_ls.exe")
djvConvert = os.path.join(djvPath, "bin", "djv_convert.exe")
nConvert = os.path.join(appsPath, 'nConvert', 'nconvert.exe')
ffmpeg = os.path.join(appsPath, 'ffmpeg', 'bin', 'ffmpeg.exe')

nukePath = os.path.join(appsPath, "Nuke5.0v2")
nuke = os.path.join(nukePath, "nuke5.0.exe")
