import json
import os
from typing import Text

class CMakeAssistant(object):
    def __init__(self, config_path):
        self.cmakePath = os.path.dirname(config_path)
        self.cmakePath += "\\CMakeLists.txt" 
        self.config = dict()
        with open(config_path, 'r') as f:
            self.config = json.load(f)
    
    def __handleCMakeVer(self):
        ver = self.config.get("cmake_version", "3.8")
        return "cmake_minimum_required (VERSION %s)\n" % ver
    
    def __handleBuildType(self):
        type = self.config.get("build_type", "Debug")
        return "set(CMAKE_BUILD_TYPE \"%s\")\n" % type
    
    def __handleProjName(self):
        name = self.config.get("proj", None)
        if name:
            return "project(\"%s\")\n" % name
        return None
    
    def __handleCode(self):
        files = self.config.get("code", None)
        if files:
            text = "set(Code \n"
            for f in files:
                text += "\t\"%s\"\n"%f
            text += ")\n"
            return text
        return None
    
    def __handleIncludeHeaders(self):
        headers = self.config.get("include_headers", None)
        if headers:
            text = "include_directories(\n"
            for f in headers:
                text += "\t\"%s\"\n" % f
            text += ")\n"
            return text
        return None
    
    def __handleLibPath(self):
        paths = self.config.get("lib_path", None)
        if paths:
            text = "link_directories(\n"
            for f in paths:
                text += "\t\"%s\"\n" % f
            text += ")\n"
            return text
        return None
    
    def __handleOutput(self):
        type = self.config.get("output_type", "execute")
        name = self.config.get("output", "output")
        if type.lower() == "execute":
            return "add_executable(%s ${Code})\n" % name
        elif type.lower() == "dynamic_lib":
            return "add_library(%s SHARED ${Code})\n" % name
        else:
            return "add_library(%s STATIC ${Code})\n" % name

    def __handleLib(self):
        libs = self.config.get("lib", None)
        if libs:
            text = "target_link_libraries(\n"
            for lib in libs:
                text += "\t\"%s\"\n"%lib
            text += ")\n"
            return text
        return None
    
    def __handle(self, writer, text):
        if text:
            writer.write(text)
            writer.write("\n")
    
    def generateCmake(self):
        with open(self.cmakePath, 'w') as f:
            self.__handle(f, self.__handleCMakeVer())
            self.__handle(f, self.__handleBuildType())
            self.__handle(f, self.__handleProjName())
            self.__handle(f, self.__handleCode())
            self.__handle(f, self.__handleIncludeHeaders())
            self.__handle(f, self.__handleLibPath())
            self.__handle(f, self.__handleOutput())
            self.__handle(f, self.__handleLib())
        

if __name__ == "__main__":
    test = CMakeAssistant(r"C:\WorkSpace\Test\P-Tools\CMakeAssistant\template.json")
    test.generateCmake()