import os,pathlib,sys
ROOT=pathlib.Path(sys.executable).resolve().parent if getattr(sys,'frozen',False) else pathlib.Path(__file__).resolve().parents[1]
if getattr(sys,'frozen',False) and ROOT.parent.name=='.programs':ROOT=ROOT.parent.parent
DSH_HOME=pathlib.Path(os.environ.get('DSH_HOME',pathlib.Path.home()/'.dsh'))
VERSION='1.0.0'
APP_NAME='爱弥斯DeepSeek桌宠启动'
EXECUTABLE_NAME=APP_NAME+'.exe'
PORTABLE_DIRNAME='爱弥斯DeepSeek桌宠'
AUDIO_SESSION_NAME='爱弥斯 · DeepSeek'
APPLICATION_ID='Doya16.Aemeath.DeepSeek'

UPDATE_REPOSITORY='Doya16/dsh-aemeath'
