# Nightmare
# by @yi64
#
# auto-update offsets
# source -> https://github.com/frk1/hazedumper
import requests


#signatures and netvars
m_bSpottedByMask = 0
m_flLastBoneSetupTime = 0
convar_name_hash_table = 0
m_hActiveWeapon = 0
m_bHasHelmet = 0
set_abs_origin = 0
dwMouseEnablePtr = 0
anim_overlays = 0
m_bIsScoped = 0
m_iCompetitiveRanking = 0
dwLocalPlayer = 0
model_ambient_min = 0
dwForceAttack = 0
dwbSendPackets = 0
m_angEyeAnglesX = 0
clientstate_choked_commands = 0
dwClientState_IsHLTV = 0
m_lifeState = 0
dwGameDir = 0
m_dwBoneMatrix = 0
m_hBombDefuser = 0
m_vecVelocity = 0
dwZoomSensitivityRatioPtr = 0
dwWeaponTable = 0
m_flNextAttack = 0
m_flCustomAutoExposureMax = 0
m_iFOV = 0
m_Collision = 0
m_hViewModel = 0
dwInterfaceLinkList = 0
m_bGunGameImmunity = 0
m_bIsQueuedMatchmaking = 0
dwClientState_ViewAngles = 0
dwEntityList = 0
m_flDefuseCountDown = 0
m_yawClassPtr = 0
m_iAccountID = 0
dwWeaponTableIndex = 0
m_bBombPlanted = 0
dwMouseEnable = 0
dwForceRight = 0
dwClientState = 0
dwGlowObjectManager = 0
force_update_spectator_glow = 0
dwClientState_GetLocalPlayer = 0
m_iHealth = 0
m_OriginalOwnerXuidHigh = 0
m_pitchClassPtr = 0
m_pStudioHdr = 0
m_MoveType = 0
m_bBombDefused = 0
dwForceJump = 0
m_viewPunchAngle = 0
m_bFreezePeriod = 0
m_nForceBone = 0
dwClientState_PlayerInfo = 0
m_ArmorValue = 0
dwppDirect3DDevice9 = 0
dwSetClanTag = 0
m_iEntityQuality = 0
dwGameRulesProxy = 0
dwPlayerResource = 0
m_bUseCustomAutoExposureMin = 0
m_OriginalOwnerXuidLow = 0
m_zoomLevel = 0
m_iObserverMode = 0
m_flFallbackWear = 0
clientstate_net_channel = 0
m_iDefaultFOV = 0
m_flNextPrimaryAttack = 0
m_bUseCustomBloomScale = 0
m_flLowerBodyYawTarget = 0
is_c4_owner = 0
m_flFlashDuration = 0
m_bBombTicking = 0
m_flTimerLength = 0
m_flSpawnTime = 0
dwInput = 0
m_aimPunchAngle = 0
m_szCustomName = 0
m_Local = 0
m_iShotsFired = 0
m_bIsDefusing = 0
m_iFOVStart = 0
m_angEyeAnglesY = 0
m_bSpotted = 0
set_abs_angles = 0
clientstate_last_outgoing_command = 0
m_flCustomAutoExposureMin = 0
dwForceAttack2 = 0
m_nViewModelIndex = 0
m_szLastPlaceName = 0
m_iCompetitiveWins = 0
m_aimPunchAngleVel = 0
find_hud_element = 0
m_fFlags = 0
m_vecViewOffset = 0
m_rgflCoordinateFrame = 0
m_nTickBase = 0
m_flDefuseLength = 0
m_bIsValveDS = 0
dwGetAllClasses = 0
dwGlobalVars = 0
dwClientState_State = 0
m_hOwnerEntity = 0
m_iItemIDHigh = 0
m_iState = 0
m_hMyWeapons = 0
m_iTeamNum = 0
dwClientState_MapDirectory = 0
m_nBombSite = 0
dwForceForward = 0
m_hObserverTarget = 0
m_vecOrigin = 0
m_hOwner = 0
m_bHasDefuser = 0
interface_engine_cvar = 0
m_bInReload = 0
dwClientState_MaxPlayer = 0
dwForceBackward = 0
m_bStartedArming = 0
m_flSimulationTime = 0
dwClientState_Map = 0
m_nFallbackSeed = 0
m_CollisionGroup = 0
m_fAccuracyPenalty = 0
m_iMostRecentModelBoneCounter = 0
m_iCrosshairId = 0
m_iItemDefinitionIndex = 0
m_iGlowIndex = 0
dwRadarBase = 0
m_SurvivalRules = 0
m_clrRender = 0
m_flFlashMaxAlpha = 0
m_nFallbackPaintKit = 0
m_nFallbackStatTrak = 0
m_flCustomBloomScale = 0
dwViewMatrix = 0
dwSensitivityPtr = 0
m_thirdPersonViewAngles = 0
m_SurvivalGameRuleDecisionTypes = 0
dwForceLeft = 0
m_bUseCustomAutoExposureMax = 0
m_iClip1 = 0
clientstate_delta_ticks = 0
cs_gamerules_data = 0
dwYawPtr = 0
m_flC4Blow = 0
dwSensitivity = 0
m_bDormant = 0


#parser
resp = requests.request(
    method="GET",
    url="https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.min.json"
)

if resp.status_code == 200:
    obj = resp.json()
    offsets = dict(obj["signatures"].items() | obj["netvars"].items())

    for offset in offsets:
        globals()[offset] = offsets[offset]