import sys
import time

from sdk import *
from sdk.memory import *
from sdk.offsets import *
from sdk.threads import *


csgo: pymem.Pymem = None
handle: int = 0
client: int = 0

#vars
glow = Switch()


def _glow():
    glow.cfg = read_config("glow")

    while True:
        while glow.value:
            glow_manager = csgo.read_int(client + dwGlowObjectManager)

            if glow_manager: 
                local_player = csgo.read_int(client + dwLocalPlayer)
                local_player_team = csgo.read_int(local_player + m_iTeamNum)

                for i in range(1, 64):
                    entity = csgo.read_int(client + dwEntityList + i * (0x10))

                    if entity:
                        entity_team = csgo.read_int(entity + m_iTeamNum)
                        entity_glow = csgo.read_int(entity + m_iGlowIndex)

                        if entity_team > 1:
                            if entity_team == local_player_team:
                                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(glow.cfg["color"]["my"][0] / 255))
                                csgo.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(glow.cfg["color"]["my"][1] / 255))
                                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(glow.cfg["color"]["my"][2] / 255))
                                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(glow.cfg["color"]["my"][3] / 100))

                            else:
                                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(glow.cfg["color"]["enemy"][0] / 255))
                                csgo.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(glow.cfg["color"]["enemy"][1] / 255))
                                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(glow.cfg["color"]["enemy"][2] / 255))
                                csgo.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(glow.cfg["color"]["enemy"][3] / 100))
                            
                            csgo.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)



def main(argv):
    global csgo, handle, client

    csgo = getProcess("csgo.exe")
    handle = getProcessHandle("csgo.exe")

    client = getModuleHandle(handle, "client.dll")

    create_thread(_glow)

    run_all_threads()

    glow.value = True
    while True:
        time.sleep(1)


if __name__ == "__main__":
    sys.exit(main(sys.argv))