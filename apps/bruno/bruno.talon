app: Bruno
-
tag(): user.tabs

^please [<user.text>]$: key("cmd-k")
    sleep(300ms)
    insert(user.text)

import: key(cmd-o)
new: key(cmd-n)
send it: key(cmd-enter)

