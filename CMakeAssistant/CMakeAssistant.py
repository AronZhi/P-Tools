import json
import os

class CMakeAssistant(object):
    def __init__(self, json_config_file, output_path):
        self.cmakePath = os.path.join(output_path, 'CMakeLists.txt')
        self.config = dict()
        with open(json_config_file, 'r') as f:
            self.config = json.load(f)
    
    def __convertPath(self, path: str):
        if path.startswith("./"):
            t = path[2:]
            return "${PROJECT_SOURCE_DIR}/%s" % t
        else:
            return path
    
    def __handleCMakeVer(self):
        ver = self.config.get("cmake_version", "3.8")
        return "cmake_minimum_required (VERSION %s)\n" % ver
    
    def __handleProjName(self):
        name = self.config.get("proj", "CMakeProj")
        return "project(%s)\n" % name
    
    def __handleBuild(self):
        info = self.config.get("build", {"type": "debug"})
        text = "set(CMAKE_BUILD_TYPE \"%s\")\n" % info["type"]
        cppStandard = info.get("cpp_standard", None)
        if cppStandard:
            text += "set(CMAKE_CXX_STANDARD %s)\n" % cppStandard
        return text
    
    def __handleIncludeHeaders(self):
        headers = self.config.get("include_headers", None)
        if headers:
            text = "include_directories(\n"
            for f in headers:
                path = self.__convertPath(f)
                text += "\t%s\n" % path
            text += ")\n"
            return text
        return None
    
    def __handleSourceCode(self):
        src = self.config.get("source_code", {"code", "."})
        text = ""
        for k,v in src.items():
            path = self.__convertPath(v)
            text += "aux_source_directory(%s %s)\n" % (path, k)
        return text
    
    def __handleLinkDir(self):
        info = self.config.get("link", None)
        if info and info.get("dir", None):
            dirs = info["dir"]
            text = "link_directories(\n"
            for dir in dirs:
                path = self.__convertPath(dir)
                text += "\t%s\n" % path
            text += ")\n"
            return text
        return None
    
    def __handleOutput(self):
        info = self.config.get("output", {"type": "exe", "name": "CMakeProj"})
        text = ""
        print(info)
        dir = info.get("dir", None)
        build_type = info["type"]
        name = info["name"]
        if dir:
            path = self.__convertPath(dir)
            if build_type.lower() == "execute":
                text += "set(EXECUTABLE_OUTPUT_PATH %s)\n" % path
            else:
                text += "set(LIBRARY_OUTPUT_PATH %s)\n" % path
        
        if build_type.lower() == "execute":
            text += "add_executable(%s" % name
        elif build_type.lower() == "dynamic_lib":
            text += "add_library(%s SHARED" % name
        else:
            text += "add_library(%s STATIC" % name
        src = self.config.get("source_code", {"code", "."})
        for key in src:
            text += " ${%s}" % key
        text += ")\n"
        return text
    
    def __handleLinkLib(self):
        info = self.config.get("link", None)
        if info and info.get("lib", None):
            libs = info["lib"]
            text = text = "target_link_libraries(\n"
            for lib in libs:
                text += "\t%s\n" % lib
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
            self.__handle(f, self.__handleProjName())
            self.__handle(f, self.__handleBuild())
            self.__handle(f, self.__handleIncludeHeaders())
            self.__handle(f, self.__handleSourceCode())
            self.__handle(f, self.__handleLinkDir())
            self.__handle(f, self.__handleOutput())
            self.__handle(f, self.__handleLinkLib())
        
"""
if __name__ == "__main__":
    test = CMakeAssistant(r"C:\WorkSpace\Test\P-Tools\CMakeAssistant\template.json", r"C:\WorkSpace\Test\P-Tools\CMakeAssistant")
    test.generateCmake()
"""