import sys
import os

class CMakeLists(object):
    def __init__(self, main_file:str, proj_path: str):
        self.main_file = main_file
        self.proj_path = proj_path
        if main_file.endswith(".cpp"):
            self.proj_name:str = main_file[0:-4]
        else:
            self.proj_name:str = main_file[0:-2]
        self.source_files = [main_file]
    
    def _parseIncludes(self, header_file_name: str):
        #添加当前目录下的文件到source_files里
        path_split_char = '/' if header_file_name.find('/') >= 0 else '\\'
        lst = header_file_name.split(path_split_char)
        if len(lst) > 2:
            return
        elif len(lst) == 2 and lst[0] != ".":
            return
        h_file = lst[-1]
        h_name = h_file[0:-4] if h_file.endswith(".hpp") else h_file[0:-2]
        c_file = h_name + ".c"
        cpp_file = h_name + ".cpp"
        for file_name in [h_file, c_file, cpp_file]:
            if os.path.exists(os.path.join(self.proj_path, file_name)):
                self.source_files.append(file_name)

    def _createCmakeList(self):
        with open("cmakelists.txt", "w") as f:
            #检查版本
            f.write("cmake_minimum_required(VERSION 3.0.0)\n")
            #设置C++标准
            f.write("set(CMAKE_CXX_STANDARD 14)\n")
            #设置工程编译语言
            f.write("project(%s LANGUAGES C CXX)\n" % self.proj_name)
            #设置输出路径
            f.write("set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR})\n")
            #设置需要编译的文件
            file_lst = ""
            for cpp_file in self.source_files:
                file_lst += " "
                file_lst += cpp_file

            f.write("set(FILE_LIST%s)\n" % file_lst)
            #编译文件
            f.write("add_executable(%s ${FILE_LIST})" % self.proj_name)
            # 链接
    
    def generate(self):
        with open(self.main_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line.find("#include") == 0:
                    index_1 = line.find('"')
                    index_2 = line.find('"', index_1 + 1)
                    substr = line[index_1 + 1 : index_2]
                    self._parseIncludes(substr)
        self._createCmakeList()


def main():
    args = sys.argv
    if (len(args) < 3):
        assert False
    main_file = args[1]
    proj_path = args[2]
    if main_file.endswith(".cpp") or main_file.endswith(".c"):
        if main_file.startswith(".\\"):
            main_file = main_file[2:]
        cmake_list = CMakeLists(main_file, proj_path)
        cmake_list.generate()
    else:
        assert False

if __name__ == "__main__":
    main()