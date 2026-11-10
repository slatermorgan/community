"""World of Warcraft (retail, Classic, Forever, ...) voice commands.

Talon never talks to the game directly. Everything is either a plain key press
or a key that you have bound, in game, to a macro. See
world_of_warcraft_macros.md for every macro and the key it must be bound to.
"""

from talon import Module, actions, app

mod = Module()
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
    "camera_walk": "ctrl-shift-f8",
    "stop_casting": "ctrl-shift-f9",
    "mount_toggle": "ctrl-shift-f10",
    # --- plain keybindings (Blizzard defaults unless noted) ---
    "cycle_party": "ctrl-tab",
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
    "chat_open": "enter",
    "party_1": "f2",
    "party_2": "f3",
    "party_3": "f4",
    "party_4": "f5",
}

# Keys currently held down by Talon, e.g. {"w", "s"}.
held_keys: set[str] = set()

OPPOSITES = {"w": "s", "s": "w", "a": "d", "d": "a"}


def release_all():
    for k in list(held_keys):
        actions.key(f"{k}:up")
    held_keys.clear()


def _on_app_deactivate(application):
    # Never leave W stuck down when alt-tabbing out of the game.
    if held_keys and "warcraft" in (application.name or "").lower():
        release_all()


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

    def wow_camera_zoom(direction: int):
        """Zoom the camera: positive is in, negative is out"""
        actions.mouse_scroll(y=-direction * 200)
