tag: terminal
-

cat make file:
    insert("cat Makefile")
    key("enter")
cat package jason:
    insert("cat package.json")
    key("enter")
cat package jason scripts:
    insert("jq '.scripts' package.json")
    key("enter")

to clip copy: " | pbcopy"
