-- TalonWoW: secure macro buttons that Talon triggers with key presses.
--
-- WoW addons can't receive input from other programs, so Talon presses a key
-- and the key is bound to one of the buttons below. Each button runs a macro,
-- exactly as if you had made it in /macro, but it also works in combat.
--
-- Keep the KEY column in sync with WOW_KEYS in ../../world_of_warcraft.py.

local ADDON_NAME = ...

-- Retail has the mount journal API; Classic clients don't. Edit to taste.
local MOUNT_MACRO = (C_MountJournal and C_MountJournal.SummonByID)
    and "/run C_MountJournal.SummonByID(0)"
    or "/dismount"

local CAMERA_DEGREES = 90 -- flip the signs if "camera left" turns right

-- name = global button name (also used in Bindings.xml)
local BUTTONS = {
    { name = "TalonEnemy",    label = "Cycle enemy",     key = "CTRL-SHIFT-F1",  macro = "/targetenemy [nodead]" },
    { name = "TalonFriend",   label = "Cycle friend",    key = "CTRL-SHIFT-F2",  macro = "/targetfriend" },
    { name = "TalonNPC",      label = "Cycle NPC",       key = "CTRL-SHIFT-F3",  macro = "/targetfriend [nodead]" },
    { name = "TalonFollow",   label = "Target follow",   key = "CTRL-SHIFT-F4",  macro = "/follow" },
    { name = "TalonTrade",    label = "Target trade",    key = "CTRL-SHIFT-F5",  macro = "/trade" },
    { name = "TalonCamLeft",  label = "Camera left",     key = "CTRL-SHIFT-F6",  macro = "/run FlipCameraYaw(" .. CAMERA_DEGREES .. ")" },
    { name = "TalonCamRight", label = "Camera right",    key = "CTRL-SHIFT-F7",  macro = "/run FlipCameraYaw(-" .. CAMERA_DEGREES .. ")" },
    { name = "TalonStopCast", label = "Stop casting",    key = "CTRL-SHIFT-F9",  macro = "/stopcasting" },
    { name = "TalonMount",    label = "Toggle mount",    key = "CTRL-SHIFT-F10", macro = MOUNT_MACRO },
}

-- Built-in WoW actions that /talon setup also binds, so you don't have to.
-- "camera walk" holds F8, which is Move and Steer (both mouse buttons).
local BUILTIN_BINDINGS = {
    { key = "F8",              action = "MOVEANDSTEER" },
    { key = "CTRL-SHIFT-F11",  action = "TOGGLEAUTORUN" },
    { key = "CTRL-SHIFT-F12",  action = "INTERACTTARGET" },
    { key = "CTRL-SHIFT-HOME", action = "TARGETFOCUS" },
    { key = "CTRL-SHIFT-END",  action = "ASSISTTARGET" },
}

local function say(msg)
    print("|cff66ccffTalonWoW:|r " .. msg)
end

-- Key Bindings menu text.
_G["BINDING_HEADER_TALON"] = "Talon Voice"
for _, b in ipairs(BUTTONS) do
    _G["BINDING_NAME_CLICK " .. b.name .. ":LeftButton"] = "Talon: " .. b.label
end

-- Create the secure buttons.
for _, b in ipairs(BUTTONS) do
    local f = CreateFrame("Button", b.name, UIParent, "SecureActionButtonTemplate")
    f:SetAttribute("type", "macro")
    f:SetAttribute("macrotext", b.macro)
    -- Key bindings send a down and an up click. The secure template only acts
    -- on the one that matches your "cast on key press" setting.
    f:RegisterForClicks("AnyDown", "AnyUp")
end

local function setup()
    if InCombatLockdown() then
        say("can't change key bindings in combat. Try again afterwards.")
        return
    end
    for _, b in ipairs(BUTTONS) do
        SetBindingClick(b.key, b.name, "LeftButton")
    end
    for _, b in ipairs(BUILTIN_BINDINGS) do
        SetBinding(b.key, b.action)
    end
    SaveBindings(GetCurrentBindingSet())
    say("default keys bound. Open Options > Key Bindings > AddOns > Talon Voice to review them.")
end

local function status()
    for _, b in ipairs(BUTTONS) do
        local key1 = GetBindingKey("CLICK " .. b.name .. ":LeftButton")
        say(string.format("%-14s %-16s %s", b.label, key1 or "(unbound)", b.macro))
    end
end

SLASH_TALON1 = "/talon"
SlashCmdList["TALON"] = function(msg)
    local cmd, arg = msg:match("^(%S*)%s*(.-)$")
    cmd = cmd:lower()
    if cmd == "setup" then
        setup()
    elseif cmd == "status" then
        status()
    elseif cmd == "camera" then
        local degrees = tonumber(arg)
        if degrees then
            FlipCameraYaw(degrees)
        else
            say("usage: /talon camera <degrees>   (negative turns the other way)")
        end
    else
        say("/talon setup   bind the default keys (one time)")
        say("/talon status  show each command's key and macro")
        say("/talon camera <degrees>   rotate the camera")
    end
end
