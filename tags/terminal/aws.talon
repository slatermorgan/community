tag: terminal
-

# AWS
# Example: aws logs tail /aws/lambda/pro-direct-customersV1-dev-getProfile --follow --profile {aws}
logs lambda tail: "aws logs tail /aws/lambda/"
tag follow: "--follow"
tag profile {user.aws}: "--profile {aws}"

aws vault mobi coms staging: "aws-vault login mobicomms-staging"
aws vault mobi coms live: "aws-vault login mobicomms-live"
aws vault D M Z live: "aws-vault login mw-dmz-temp-live"
