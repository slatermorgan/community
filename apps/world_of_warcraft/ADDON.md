# TalonWoW addon

A small addon that gives the Talon voice commands in this folder something to press. Talon can't talk to WoW directly, because addons can't receive input from other programs. So the addon creates the macros for you and binds them to keys, and Talon presses those keys.

> **Status:** written but not yet tested in game. Please read "If something doesn't work" below.

## What it does

- Creates one hidden secure button per macro (`/targetenemy [nodead]`, `/targetfriend`, `/follow`, `/trade`, camera flips, `/stopcasting`, mount). Secure buttons work in combat.
- Lists them in **Options → Key Bindings → AddOns → Talon Voice**.
- `/talon setup` binds the default keys, including a few of WoW's own actions (Move and Steer, interact, focus, assist).

| Voice command | Key | What runs |
|---|---|---|
| `enemy cycle` | `CTRL-SHIFT-F1` | `/targetenemy [nodead]` |
| `friend cycle` | `CTRL-SHIFT-F2` | `/targetfriend` |
| `npc cycle` | `CTRL-SHIFT-F3` | `/targetfriend [nodead]` |
| `target follow` | `CTRL-SHIFT-F4` | `/follow` |
| `target trade` | `CTRL-SHIFT-F5` | `/trade` |
| `camera left` | `CTRL-SHIFT-F6` | `/run FlipCameraYaw(90)` |
| `camera right` | `CTRL-SHIFT-F7` | `/run FlipCameraYaw(-90)` |
| `camera walk toggle` | `F8` (held) | built-in **Move and Steer** |
| `spell stop` | `CTRL-SHIFT-F9` | `/stopcasting` |
| `player sit` | `F16` | `/sit` |
| `mount toggle` | `CTRL-SHIFT-F10` | `C_MountJournal.SummonByID(0)` on retail, `/dismount` on Classic |
| `target interact` | `CTRL-SHIFT-F12` | built-in **Interact With Target** |
| `target focus` | `CTRL-SHIFT-HOME` | built-in **Target Focus** |
| `target assist` | `CTRL-SHIFT-END` | built-in **Assist Target** |

These match `WOW_KEYS` in `world_of_warcraft.py`. If you change a key in one place, change it in the other (`KEY` in `TalonWoW.lua`, and the `WOW_KEYS` table).

## Install

1. Find your game's AddOns folder. It is the `Interface/AddOns` folder next to the game's version folder (`_retail_`, `_classic_`, ...). Typical locations:
   - **Windows:** `C:\Program Files (x86)\World of Warcraft\_retail_\Interface\AddOns\`
   - **macOS:** `/Applications/World of Warcraft/_retail_/Interface/AddOns/`
   - **Linux (Wine, Lutris, etc.):** inside the Wine prefix, e.g. `~/.wine/drive_c/Program Files (x86)/World of Warcraft/_retail_/Interface/AddOns/`. Lutris and Heroic keep their own prefixes, so look in the game's settings for the prefix path.
   - **Forever and Classic clients:** the same, in that client's own version folder. Install the addon once per client.
2. Copy the `TalonWoW` folder from `addon/TalonWoW/` into `AddOns`. The result should be `AddOns/TalonWoW/TalonWoW.toc`.
   - To keep it in sync with this repo while you edit, symlink instead of copying:
     `ln -s ~/.talon/user/community/apps/world_of_warcraft/addon/TalonWoW "<AddOns folder>/TalonWoW"`
3. Start the game. At the character select screen, click **AddOns** and make sure **Talon Voice Commands** is ticked. If it says "out of date", tick **Load out of date AddOns** (see below).
4. Log in and type `/talon setup`.
5. Check the result with `/talon status`, or in **Options → Key Bindings → AddOns → Talon Voice**.

`/talon setup` can't run in combat, and it replaces anything already bound to those keys. It only needs to be run once per character set. If you use per-character key bindings, run it on each.

## Use

With the Talon files from this folder loaded, say the commands from the table above, for example `enemy cycle`, `camera left` or `walk toggle`.

The addon's own slash commands:

| Command | Does |
|---|---|
| `/talon setup` | Binds the default keys |
| `/talon status` | Shows each command's key and macro |
| `/talon camera 45` | Rotates the camera by 45° (negative the other way) |
| `/talon hud` | Unlocks the held-keys HUD so you can drag it; run again to lock it |

## Held-keys HUD

While any of `F8`, `A`-`Z` or `0`-`9` is held down, a small box shows what is held, for example `HOLD W: forward` or `HOLD SHIFT-3`. That includes keys Talon holds for you (`move auto`, `walk toggle`, `spell hold`). It hides when nothing is held, and ignores keys while you type in chat. Use `/talon hud` to move it. The position is saved.

## Customising

- **Change a macro:** edit its `macro =` line in `TalonWoW.lua`, then `/reload`. Macro text can't be changed in combat.
- **Change the camera angle:** edit `CAMERA_DEGREES` at the top of `TalonWoW.lua`.
- **Add a command:** add a row to `BUTTONS` in `TalonWoW.lua` and a matching `<Binding name="CLICK <Name>:LeftButton">` line in `Bindings.xml`. Then add a key for it to `WOW_KEYS` and a command in `world_of_warcraft.talon`.

## If something doesn't work

I wrote this from the WoW addon documentation without being able to run the game, so the likely problems are:

- **"Out of date" or won't load.** `## Interface:` in `TalonWoW.toc` must contain your client's interface number. In game, `/dump (select(4, GetBuildInfo()))` prints it. Put it first in the list. Tick **Load out of date AddOns** to test in the meantime.
- **A command fires twice, or never.** The buttons register both key down and key up. WoW should honour your **Cast on key press** setting (Options → Gameplay → Combat). If they double-fire, change that setting or edit `RegisterForClicks` in `TalonWoW.lua` to `"AnyDown"` or `"AnyUp"`.
- **`camera left` does nothing or errors.** `FlipCameraYaw` may be unavailable to scripts on your client. `/talon camera 90` tells you the error. The fallback is a mouse drag, which would need Talon changes.
- **`camera left` turns right.** Swap the signs in the two camera macros.
- **`npc cycle` picks players.** `/targetfriend` may not distinguish NPCs. Try changing the macro to another targeting command in `TalonWoW.lua`.
- **A built-in binding didn't take.** The names used in `BUILTIN_BINDINGS` (`MOVEANDSTEER`, `INTERACTTARGET`, `TARGETFOCUS`, `ASSISTTARGET`) are from memory and may differ by client. Bind that action by hand in Key Bindings, and tell me which one so the list can be fixed.
- **Talon doesn't react in the game.** On Linux, check the app name matches (`app.name()` and `app.exe()` in `talon repl` with WoW focused). See the comments in `world_of_warcraft.py`.

## Is this allowed?

Each voice command triggers one action, which is the same as pressing one key. Don't use it to chain actions or react to game state. Check Blizzard's current addon and automation policy if in doubt.
