aws configure set region us-east-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region us-east-1"

aws configure set region us-east-2
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region us-east-2"

aws configure set region us-west-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region us-west-1"

aws configure set region us-west-2
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region us-west-2"

aws configure set region ap-northeast-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region ap-northeast-1"

aws configure set region ap-northeast-2
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region ap-northeast-2"

aws configure set region ap-southeast-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region ap-southeast-1"

aws configure set region ap-southeast-2
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region ap-southeast-2"

aws configure set region ca-central-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region ca-central-1"

aws configure set region eu-central-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region eu-central-1"

aws configure set region eu-west-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region eu-west-1"

aws configure set region eu-west-2
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region eu-west-2"

aws configure set region ap-south-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region ap-south-1"

aws configure set region eu-west-3
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region eu-west-3"

aws configure set region sa-east-1
QUOTA=$(aws service-quotas get-service-quota --service-code ec2 --quota-code L-1216C47A --query 'Quota.Value')

echo "$QUOTA == region sa-east-1"


