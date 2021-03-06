import os
import sys
from utils import path as pathUtils

class DarkSporeServerConfig(object):

    def __init__(self):
        self.serverPath = "/darkspore_server"
        self.config = {
            "SKIP_LAUNCHER": False,
            "VERSION_LOCKED": False,
            "SINGLEPLAYER_ONLY": True,
            "SERVER_HOST": "127.0.0.1",
            "STORAGE_PATH": "../storage",
            "DARKSPORE_INDEX_PAGE_PATH": "index.html",
            "DARKSPORE_LAUNCHER_NOTES_PATH": "bootstrap/launcher/notes.html",
            "DARKSPORE_LAUNCHER_THEMES_PATH": "bootstrap/launcher"
        }

        try:
            serverPath = None
            if getattr(sys, 'frozen', False):
                # When running it after being "compiled" by PyInstaller
                application_path = os.path.dirname(sys.executable)
                serverPath = os.path.abspath(application_path)
            elif __file__:
                # When running directly with Python
                application_path = os.path.dirname(__file__)
                scriptPath = os.path.abspath(application_path)
                serverPath = os.path.dirname(scriptPath)

            self.serverPath = serverPath

            configPath = os.path.join(serverPath, "config.txt")
            configFile = open(configPath,"r")
            lines = configFile.readlines()
            for line in lines:
                if len(line.strip()) > 0 and line.strip().startswith('#') == False:
                    l_comp = line.split('=', 1)
                    if len(l_comp) != 2:
                        raise SyntaxError('Invalid config line: ' + line)
                    key   = l_comp[0].strip()
                    value = l_comp[1].strip()
                    try:
                        value = int(value)
                    except ValueError:
                        if value == "false":
                            value = False
                        if value == "true":
                            value = True
                    self.config[key] = value
        except Exception as e:
            print('')
            print('Error while reading config file: %s' % e)
            print('')

        print self.config

    def get(self,key):
        return self.config[key]

    def host(self):
        if self.singlePlayerOnly():
            return "127.0.0.1"
        return self.get("SERVER_HOST")

    def skipLauncher(self):
        return self.get("SKIP_LAUNCHER") == True

    def singlePlayerOnly(self):
        return self.get("SINGLEPLAYER_ONLY") == True

    def versionLockEnabled(self):
        return self.singlePlayerOnly() == False and self.get("VERSION_LOCKED") == True

    def darksporeIndexPagePath(self):
        return self.get("DARKSPORE_INDEX_PAGE_PATH")

    def darksporeLauncherNotesPath(self):
        return self.get("DARKSPORE_LAUNCHER_NOTES_PATH")

    def darksporeLauncherThemesPath(self):
        themesPath = self.get("DARKSPORE_LAUNCHER_THEMES_PATH")
        while themesPath.endswith('/') or themesPath.endswith('\\'):
            themesPath = themesPath[:-1]
        return themesPath

    def storagePath(self):
        if "docker" in sys.argv:
            return "/darkspore_server_storage"

        storagePath = self.get("STORAGE_PATH")
        if storagePath.startswith('.'):
            storagePath = pathUtils.join(self.serverPath,storagePath)

        while storagePath.endswith('/') or storagePath.endswith('\\'):
            storagePath = storagePath[:-1]
        return storagePath

    def serverDataFilePath(self):
        return pathUtils.join(self.storagePath(),'server.data')
