os: mac
app: Linear
-
^please [<user.text>]$: key("cmd-k")
    sleep(300ms)
    insert(user.text)
    
copy branch name: key("cmd-shift-.")
