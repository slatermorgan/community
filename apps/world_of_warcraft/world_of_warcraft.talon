app: world_of_warcraft
-
# Movement. W/S/A/D are held with key(x:down) until toggled off.
(walk | run) toggle: user.wow_press("walk_toggle")
backwards toggle: user.wow_toggle_key("s")
strafe left toggle: user.wow_toggle_key("a")
strafe right toggle: user.wow_toggle_key("d")
back up: user.wow_back_up()
move stop: user.wow_stop_moving()
move auto: user.wow_press("autorun")
player jump: key(space)
mount toggle: user.wow_press("mount_toggle")

# Camera
camera left: user.wow_press("camera_left")
camera right: user.wow_press("camera_right")
# F8 is bound to Move and Steer (hold = run toward where the camera faces)
camera walk toggle: user.wow_toggle_key("f8")
# Turns the character about 45 degrees (say it twice for 90). Tune LOOK_SECONDS.
look left: user.wow_look("left")
look right: user.wow_look("right")
camera zoom in: user.wow_camera_zoom(1)
camera zoom out: user.wow_camera_zoom(-1)

# Spells: "spell 1", "spell shift 3", "spell control alt 5". Zero is the 0 key.
spell <user.number_key>: user.wow_spell("", number_key)
spell <user.modifiers> <user.number_key>: user.wow_spell(modifiers, number_key)
# Hold a spell key so it recasts as long as it's held (needs "Press and Hold
# Casting" on). "spell release" lets go; "spell stop" also stops the cast.
spell hold <user.number_key>: user.wow_spell_hold("", number_key)
spell hold <user.modifiers> <user.number_key>: user.wow_spell_hold(modifiers, number_key)
spell release: user.wow_spell_release()
spell stop:
    user.wow_spell_release()
    user.wow_press("stop_casting")
bar next: user.wow_press("bar_next")
bar previous: user.wow_press("bar_previous")

# Targeting
party cycle: user.wow_press("cycle_party")
enemy cycle: user.wow_press("cycle_enemy")
friend cycle: user.wow_press("cycle_friend")
npc cycle: user.wow_press("cycle_npc")
target follow: user.wow_press("target_follow")
target trade: user.wow_press("target_trade")
target self: user.wow_press("target_self")
target last: user.wow_press("target_last")
target focus: user.wow_press("target_focus")
target assist: user.wow_press("target_assist")
target clear: user.wow_press("target_clear")
party one: user.wow_press("party_1")
party two: user.wow_press("party_2")
party three: user.wow_press("party_3")
party four: user.wow_press("party_4")

# UI
target interact: user.wow_press("interact")
map open: user.wow_press("map")
bags open: user.wow_press("bags")
character open: user.wow_press("character_panel")
quest open: user.wow_press("quest_log")
professions open: user.wow_press("professions")
spellbook open: user.wow_press("spellbook")
talents open: user.wow_press("talents")
chat open: user.wow_press("chat_open")

# Mouse: pop (see world_of_warcraft.py) right clicks, so "righty" left clicks.
righty:
    tracking.zoom_cancel()
    mouse_click(0)
