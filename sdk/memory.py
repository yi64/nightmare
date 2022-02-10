# Nightmare
# by @yi64
#
# access to external process
# source -> https://github.com/srounet/Pymem
import pymem


def getProcess(name) -> pymem.Pymem:
    return pymem.Pymem(name)

def getProcessHandle(name) -> int:
    return getProcess(name).process_handle

def getModuleHandle(handle, module) -> int:
    return pymem.process.module_from_name(handle, module).lpBaseOfDll