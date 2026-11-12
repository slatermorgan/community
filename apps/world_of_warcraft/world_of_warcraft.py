"""World of Warcraft (retail, Classic, Forever, ...) voice commands.

Talon never talks to the game directly. Everything is either a plain key press
or a key bound in game to a macro. The TalonWoW addon (addon/TalonWoW, see
ADDON.md) creates those macros and binds the keys below with /talon setup.
world_of_warcraft_macros.md lists the same macros for doing it by hand.
"""

from talon import Context, Module, actions, app

mod = Module()
ctx = Context()
mod.apps.world_of_warcraft = r"""
app.name: /warcraft/i
"""
mod.apps.world_of_warcraft = r"""
os: mac
and app.bundle: com.blizzard.worldofwarcraft
"""
mod.apps.world_of_warcraft = r"""
os: windows
and app.exe: /^wow(classic|b|t)?\.exe$/i
"""
mod.apps.world_of_warcraft = r"""
os: windows
and app.exe: /^wow-64\.exe$/i
"""
# Linux: WoW runs under Wine/Proton (Battle.net via Lutris, Heroic, Steam, ...),
# so the window usually reports as a Wine process. Check `app.name()` and
# `app.exe()` in the Talon REPL (talon repl) with WoW focused if this misses.
mod.apps.world_of_warcraft = r"""
os: linux
and app.name: /wow/i
"""
mod.apps.world_of_warcraft = r"""
os: linux
and app.exe: /wow/i
"""
# Steam/Proton: the app reports as steam_app_<id> running wine64-preloader, so
# neither name nor exe mentions WoW. The window title is the reliable signal.
mod.apps.world_of_warcraft = r"""
os: linux
and win.title: /^World of Warcraft/
"""

ctx.matches = r"""
app: world_of_warcraft
"""

# Every key Talon presses that is not a movement key. Change a key here and in
# the matching WoW keybinding / macro slot (see the .md file).
WOW_KEYS = {
    # --- keys bound to macros (see world_of_warcraft_macros.md) ---
    "cycle_enemy": "ctrl-shift-f1",
    "cycle_friend": "ctrl-shift-f2",
    "cycle_npc": "ctrl-shift-f3",
    "target_follow": "ctrl-shift-f4",
    "target_trade": "ctrl-shift-f5",
    "camera_left": "ctrl-shift-f6",
    "camera_right": "ctrl-shift-f7",
    "stop_casting": "ctrl-shift-f9",
    "mount_toggle": "ctrl-shift-f10",
    # --- plain keybindings (Blizzard defaults unless noted) ---
    "cycle_party": "ctrl-tab",
    "walk_toggle": "num_lock",  # default Toggle Autorun key
    "autorun": "ctrl-shift-f11",  # no default key on Mac: bind "Toggle Autorun"
    "interact": "ctrl-shift-f12",  # not bound by default: bind "Interact With Target"
    "target_self": "f1",
    "target_last": "g",
    "target_focus": "ctrl-shift-home",  # not bound by default
    "target_clear": "escape",
    "target_assist": "ctrl-shift-end",  # not bound by default
    "bar_next": "shift-n",
    "bar_previous": "n",
    "map": "m",
    "bags": "b",
    "character_panel": "c",
    "quest_log": "l",
    "professions": "k",
    "spellbook": "p",
    "talents": "n",
    "chat_open": "enter",
    "party_1": "f2",
    "party_2": "f3",
    "party_3": "f4",
    "party_4": "f5",
    # Default Turn Left / Turn Right. Used by "look left/right".
    "turn_left": "left",
    "turn_right": "right",
}

# Seconds to hold a turn key for one "look" (about 45 degrees). Turn speed is
# time based, so tune this until "look left" twice makes a quarter turn.
LOOK_SECONDS = 0.25

# Seconds "back up" walks backwards.
BACK_UP_SECONDS = 2

# Keys currently held down by Talon, e.g. {"w", "s"}.
held_keys: set[str] = set()

# The action bar key currently held down for "spell hold", e.g. "shift-3".
held_spell: list[str] = []

OPPOSITES = {"w": "s", "s": "w", "a": "d", "d": "a"}


def release_spell():
    for chord in held_spell:
        actions.key(f"{chord}:up")
    held_spell.clear()


def release_all():
    for k in list(held_keys):
        actions.key(f"{k}:up")
    held_keys.clear()


def _on_app_deactivate(application):
    # Never leave W stuck down when alt-tabbing out of the game.
    name = (application.name or "").lower()
    if "warcraft" in name or name.startswith("steam_app_"):
        if held_keys:
            release_all()
        release_spell()


app.register("app_deactivate", _on_app_deactivate)


@mod.action_class
class Actions:
    def wow_toggle_key(key: str):
        """Toggle holding a movement key; holding the opposite key is released first"""
        if key in held_keys:
            actions.key(f"{key}:up")
            held_keys.discard(key)
            return
        opposite = OPPOSITES.get(key)
        if opposite in held_keys:
            actions.key(f"{opposite}:up")
            held_keys.discard(opposite)
        actions.key(f"{key}:down")
        held_keys.add(key)

    def wow_stop_moving():
        """Release every movement key Talon is holding"""
        release_all()

    def wow_press(name: str):
        """Press the key configured for a World of Warcraft command (macro or keybinding)"""
        actions.key(WOW_KEYS[name])

    def wow_spell(modifiers: str, number_key: str):
        """Press an action bar key such as 1-0, optionally with modifiers (empty string for none)"""
        actions.key(f"{modifiers}-{number_key}" if modifiers else number_key)

    def wow_back_up():
        """Walk backwards for a couple of seconds, then stop"""
        if "s" in held_keys:
            return  # already walking backwards via "backwards toggle"
        if "w" in held_keys:
            actions.key("w:up")
            held_keys.discard("w")
        actions.key("s:down")
        actions.sleep(f"{BACK_UP_SECONDS}s")
        actions.key("s:up")

    def wow_look(direction: str):
        """Turn the character about 45 degrees by holding a turn key briefly (left or right)"""
        key = WOW_KEYS[f"turn_{direction}"]
        actions.key(f"{key}:down")
        actions.sleep(LOOK_SECONDS)
        actions.key(f"{key}:up")

    def wow_spell_hold(modifiers: str, number_key: str):
        """Hold an action bar key down so the spell keeps casting until released"""
        release_spell()
        chord = f"{modifiers}-{number_key}" if modifiers else number_key
        actions.key(f"{chord}:down")
        held_spell.append(chord)

    def wow_spell_release():
        """Release the held spell key"""
        release_spell()

    def wow_camera_zoom(direction: int):
        """Zoom the camera: positive is in, negative is out"""
        actions.mouse_scroll(y=-direction * 200)


@ctx.action_class("user")
class UserActions:
    def noise_trigger_pop():
        # In WoW, pop is a right click (turn/interact). "righty" is the left click.
        actions.mouse_click(1)
