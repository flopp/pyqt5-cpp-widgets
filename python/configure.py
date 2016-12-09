#!/usr/bin/env python3

import sipconfig
import subprocess
import os
import site
from distutils import sysconfig
from PyQt5.QtCore import PYQT_CONFIGURATION

def commandOutput(cmd, arguments):
    return subprocess.check_output([cmd] + arguments).strip().decode('utf-8')

def getEnv(name, default):
    return os.environ.get(name) or default

class Config:
    def __init__(self, qmakePath):
        self.__qmakePath = qmakePath
        self.__sipFlags = PYQT_CONFIGURATION['sip_flags']
        
    def qmakeOutput(self, *arguments):
        return commandOutput(self.__qmakePath, list(arguments))

    def qmakeVariable(self, name):
        return self.qmakeOutput('-query', name)

    def sipFlags(self):
        return self.__sipFlags

def main():
    qmakePath = getEnv('QMAKE', 'qmake')
    sipPath = getEnv('SIP', 'sip')

    sipConfig = sipconfig.Configuration()
    config = Config(qmakePath)

    projectPath = getEnv('PROJECT_PATH', os.getcwd() + '/..')
    libraryPath = getEnv('LIBRARY_PATH', projectPath + '/custom')
    sipFilePath = getEnv('SIP_FILE_PATH', projectPath + '/python/custom.sip')
    pyQtIncludePath = getEnv('PYQT_INCLUDE_PATH', '/usr/share/sip/PyQt5')

    commandOutput(sipPath, config.sipFlags().split(' ') + [
        '-I', pyQtIncludePath,
        '-b', 'custom_python.pro',
        '-o', '-c', '.',
        sipFilePath
        ])

    with open('custom_python.pro', 'a') as pro:
        pro.write(
        '''
        TEMPLATE = lib
        CONFIG += release plugin no_plugin_name_prefix
        QT += widgets
        CONFIG += c++11

        TARGET = $$target
        HEADERS = $$headers
        SOURCES = $$sources

        INCLUDEPATH += "{sipInclude}" "{pythonInclude}" "{projectInclude}" "{projectPythonInclude}"
        LIBS += -Wl,-rpath,"{libraryPath}" -L"{libraryPath}" -lcustom "{pythonLibrary}"

        isEmpty(PREFIX) {{
            PREFIX = "{installPath}"
        }}

        target.path = $$PREFIX
        INSTALLS += target
        '''.format(
            pythonInclude = sysconfig.get_python_inc(),
            sipInclude = sipConfig.sip_inc_dir,
            projectInclude = projectPath,
            projectPythonInclude = projectPath + "/python",
            libraryPath = libraryPath,
            pythonLibrary = sysconfig.get_config_var('LIBDIR') +
                "/" + sysconfig.get_config_var('MULTIARCH') +
                "/" + sysconfig.get_config_var('LDLIBRARY'),
            installPath = site.getusersitepackages()
            ).replace('\n        ', '\n')
        )

if __name__ == "__main__":
    main()
