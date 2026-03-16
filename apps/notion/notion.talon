os: mac
app: Notion
-
^please [<user.text>]$: key("cmd-k")
    sleep(1000ms)
    insert(user.text)

bar switch: key("cmd-\\")
code that: key("cmd-e")
