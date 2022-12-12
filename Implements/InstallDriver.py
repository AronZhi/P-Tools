import subprocess
import os
import time


class FilterDriverCommand:
    def __init__(self):
        self.sys_dir = "C:\DriverTest\Drivers"
        self.driver_name = self.searchDriverName()
        self.install_cmd = "RUNDLL32.EXE SETUPAPI.DLL,InstallHinfSection DefaultInstall 132 C:\DriverTest\Drivers\%s.inf" % self.driver_name
        self.uninstall_cmd = "RUNDLL32.EXE SETUPAPI.DLL,InstallHinfSection DefaultUninstall 132 C:\DriverTest\Drivers\%s.inf" % self.driver_name
        self.load_cmd = "FLTMC load %s" % self.driver_name
        self.unload_cmd = "FLTMC unload %s" % self.driver_name
        self.check_installed_cmd = "Driverquery | findstr \"%s\"" % self.driver_name
        self.check_loaded_cmd = "FLTMC filters | findstr \"%s\"" % self.driver_name

    def searchDriverName(self):
        for root, ds, fs in os.walk(self.sys_dir):
            for f in fs:
                if f.endswith(".sys"):
                    index = f.find(".sys")
                    drv_name = f[0:index]
                    print("driver name: ", drv_name)
                    return drv_name
        assert False, "can not find .sys file"
    
    def execute_command(self, command: str) -> str:
        proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        proc.wait()
        output = proc.stdout.read()
        ret = output.decode('utf-8','replace')
        print(ret)
        return ret

    def uninstall(self):
        res = self.execute_command(self.check_loaded_cmd)
        if res:
            self.execute_command(self.unload_cmd)
        res = self.execute_command(self.check_installed_cmd)
        if res:
            self.execute_command(self.uninstall_cmd)
    
    def install(self):
        self.uninstall()
        self.execute_command(self.install_cmd)
        self.execute_command(self.load_cmd)
    
    def load(self):
        res = self.execute_command(self.check_installed_cmd)
        if res == "":
            self.execute_command(self.install_cmd)
        res = self.execute_command(self.check_loaded_cmd)
        if res == "":
            self.execute_command(self.load_cmd)

    
    def showInstalled(self):
        print("install stauts: ")
        self.execute_command(self.check_installed_cmd)
        print("load stauts: ")
        self.execute_command(self.check_loaded_cmd)


if __name__ == "__main__":
    command = FilterDriverCommand()
    choice = input("input i to install, u to uninstall, else check status: ")
    print("###############################################################")
    if choice == "i":
        command.install()
    elif choice == "u":
        command.uninstall()
    elif choice == "l":
        command.load()
    else:
        command.showInstalled()
