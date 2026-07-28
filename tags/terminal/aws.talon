tag: terminal
-

# AWS
# Example: aws logs tail /aws/lambda/pro-direct-customersV1-dev-getProfile --follow --profile {aws}
logs lambda tail: "aws logs tail /aws/lambda/"
tag follow: "--follow"
tag profile {user.aws}: "--profile {aws}"
