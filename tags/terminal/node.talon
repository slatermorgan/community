tag: terminal
-

# NPM / Yarn / Serverless
N P M install: "npm install"
N P M run <user.text> [over]:
    insert("npm run ")
    insert(text)
    sleep(100ms)
run serverless <user.text> [over]:
    insert("serverless ")
    insert(text)
    sleep(100ms)
yarn install: "yarn install"
