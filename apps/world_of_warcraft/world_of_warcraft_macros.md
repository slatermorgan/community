# World of Warcraft: macros and keybinds

> The `TalonWoW` addon (see `ADDON.md`) creates all of these macros and binds the keys with `/talon setup`. This file is the manual route, and a reference for what the addon does.

Talon only presses keys. Anything WoW can't do from a default key is a **macro** that you bind to a key. The keys live in one table, `WOW_KEYS` in `world_of_warcraft.py`. Change a key there and in game together.

**Binding a macro to a key:** `/macro` → New → paste the text → drag the macro onto an action bar slot (a hidden bar works) → Key Bindings → bind that slot's button to the key below.

Tip: if `ctrl-shift-F1..F12` is awkward to bind, any key combination works. Update `WOW_KEYS` to match.

## Macros

| Voice command | Key | Macro name | Macro text |
|---|---|---|---|
| `enemy cycle` | `ctrl-shift-f1` | TalonEnemy | `/targetenemy [nodead]` |
| `friend cycle` | `ctrl-shift-f2` | TalonFriend | `/targetfriend` |
| `npc cycle` | `ctrl-shift-f3` | TalonNPC | `/targetfriend [nodead]` (see note 1) |
| `target follow` | `ctrl-shift-f4` | TalonFollow | `/follow` |
| `target trade` | `ctrl-shift-f5` | TalonTrade | `/trade` |
| `camera left` | `ctrl-shift-f6` | TalonCamLeft | `/run FlipCameraYaw(90)` (see note 2) |
| `camera right` | `ctrl-shift-f7` | TalonCamRight | `/run FlipCameraYaw(-90)` (see note 2) |
| `camera walk toggle` | `f8` (held) | none | not a macro: bind `f8` to **Move and Steer** (see note 3) |
| `spell stop` | `ctrl-shift-f9` | TalonStopCast | `/stopcasting` |
| `mount toggle` | `ctrl-shift-f10` | TalonMount | `/run C_MountJournal.SummonByID(0)` (retail; see note 4) |

### Notes

1. **`npc cycle`.** `/targetfriend` cycles "friendly entities", and the wiki doesn't say whether that includes NPCs. Test it in game. If it only picks players, or picks NPCs you don't want, say so and we'll try a different approach.
2. **Camera.** `FlipCameraYaw(degrees)` rotates the camera about the Z axis by an exact number of degrees. I haven't been able to confirm which direction is positive, so if "camera left" turns right, swap the signs. If the game refuses the script, we'll fall back to a mouse drag. The first run of any `/run` macro may show a "custom script" warning. Allow it.
3. **`camera walk toggle`.** Holds `f8`, which should be bound to Move and Steer (WoW's "both mouse buttons" run). That runs toward where the camera faces. Say it again to stop. A `/run MoveForwardStart()` macro would not work, because movement functions are protected and addon or macro script code can't call them.
4. **`mount toggle`.** Retail only. `C_MountJournal.SummonByID(0)` summons a random favorite mount. On Classic clients use `/cast <your mount name>` instead.

## Plain keybindings (no macro)

Set these under Options → Key Bindings if they aren't already bound.

| Voice command | Key | WoW binding |
|---|---|---|
| `backwards toggle` | `s` (held) | Move Backward |
| `back up` | `s` (held 2 s) | Move Backward |
| `strafe left/right toggle` | `a` / `d` (held) | Strafe Left / Right |
| `player jump` | `space` | Jump |
| `look left` / `look right` | `left` / `right` (held about 0.25 s) | Turn Left / Turn Right (default) |
| `party cycle` | `ctrl-tab` | Target Nearest Friend (default) |
| `target interact` | `ctrl-shift-f12` | Interact With Target |
| `target self` | `f1` | Target Self (default) |
| `party one..four` | `f2..f5` | Target Party Member 1-4 (default) |
| `target last` | `g` | Target Last Target (default) |
| `target focus` | `ctrl-shift-home` | Focus Target |
| `target assist` | `ctrl-shift-end` | Assist Target |
| `target clear` | `escape` | Clear Target (default) |
| `bar next` / `bar previous` | `shift-n` / `n` | Next / Previous Action Page (default) |
| `map open` | `m` | World Map (default) |
| `bags open` | `b` | Open All Bags (default) |
| `character open` | `c` | Character Info (default) |
| `quest open` | `l` | Quest Log (default) |
| `professions open` | `k` | Professions (default) |
| `talents open` | `n` | Talents (default on retail; clashes with `bar previous`) |
| `spellbook open` | `p` | Spellbook & Abilities (default) |
| `chat open` | `enter` | Chat (default) |
| `spell hold <modifiers> <number>` / `spell release` | `1`..`0` held until released | needs Options > Gameplay > Combat > **Press and Hold Casting** |
| `spell <modifiers> <number>` | `1`..`0` plus modifiers | Action Bar 1 buttons 1-10 |

`camera zoom in/out` scrolls the mouse wheel over the game window, which needs no binding.

## Not verified

- The macOS bundle id `com.blizzard.worldofwarcraft` is a guess because the game isn't installed on this machine. The `app.name: /warcraft/i` match is the one doing the work. If the commands don't activate, check the app name with `app.name()` in the Talon REPL.
- Keys marked "default" are from memory of the default bindings and may differ by client version.
