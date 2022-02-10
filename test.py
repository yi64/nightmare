import sdk.memory
import sdk.offsets

csgo = sdk.memory.getProcess("csgo.exe")
client = sdk.memory.getModuleHandle(csgo.process_handle, "client.dll")

print(csgo.read_int(client + sdk.offsets.dwGlowObjectManager))