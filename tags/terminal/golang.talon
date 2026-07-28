tag: terminal
-

# Go
run go coverage: "go test ./... -v -cover"
run go tests: "go test ./..."
run go mod tidy: "go mod tidy"
run go mod init: "go mod init"
run go main: "go run main.go"
open mod file: "code go.mod"
run go get: "go get -u "
insert replace directive: "replace github.com/this => ../this"
run go replace: "go mod edit -replace this="
