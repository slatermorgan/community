# World of Warcraft: macros and keybinds

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
| `camera walk` | `ctrl-shift-f8` | TalonCamWalk | see note 3 |
| `spell stop` | `ctrl-shift-f9` | TalonStopCast | `/stopcasting` |
| `mount toggle` | `ctrl-shift-f10` | TalonMount | `/run C_MountJournal.SummonByID(0)` (retail; see note 4) |

### Notes

1. **`npc cycle`.** `/targetfriend` cycles "friendly entities", and the wiki doesn't say whether that includes NPCs. Test it in game. If it only picks players, or picks NPCs you don't want, say so and we'll try a different approach.
2. **Camera.** `FlipCameraYaw(degrees)` rotates the camera about the Z axis by an exact number of degrees. I haven't been able to confirm which direction is positive, so if "camera left" turns right, swap the signs. If the game refuses the script, we'll fall back to a mouse drag. The first run of any `/run` macro may show a "custom script" warning. Allow it.
3. **`camera walk`.** You asked for this to be macro-only. WoW has no single command for "face the camera and walk". Suggested macro for retail: `/run MoveForwardStart()`, bound alongside the "Turn to camera" behaviour, which a right-click does by default. This one is the least settled, so treat it as a starting point and tell me what works.
4. **`mount toggle`.** Retail only. `C_MountJournal.SummonByID(0)` summons a random favorite mount. On Classic clients use `/cast <your mount name>` instead.

## Plain keybindings (no macro)

Set these under Options → Key Bindings if they aren't already bound.

| Voice command | Key | WoW binding |
|---|---|---|
| `walk toggle` | `w` (held) | Move Forward |
| `backwards toggle` | `s` (held) | Move Backward |
| `strafe left/right toggle` | `a` / `d` (held) | Strafe Left / Right |
| `player jump` | `space` | Jump |
| `move auto` | `ctrl-shift-f11` | Toggle Autorun (no default key on Mac) |
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
| `chat open` | `enter` | Chat (default) |
| `spell <modifiers> <number>` | `1`..`0` plus modifiers | Action Bar 1 buttons 1-10 |

`camera zoom in/out` scrolls the mouse wheel over the game window, which needs no binding.

## Not verified

- The macOS bundle id `com.blizzard.worldofwarcraft` is a guess because the game isn't installed on this machine. The `app.name: /warcraft/i` match is the one doing the work. If the commands don't activate, check the app name with `app.name()` in the Talon REPL.
- Keys marked "default" are from memory of the default bindings and may differ by client version.
