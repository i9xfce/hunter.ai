#!/usr/bin/env bash
# Creates/updates the CloudFormation stack and uploads the Vite dist/ release.
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STACK_NAME="${STACK_NAME:-aws-clf-c02-exam-simulator}"
REGION="${AWS_REGION:-${AWS_DEFAULT_REGION:-us-east-1}}"
TEMPLATE="$PROJECT_DIR/infrastructure/cloudformation/static-site.yml"

command -v aws >/dev/null || { echo 'AWS CLI v2 is required.' >&2; exit 1; }
command -v npm >/dev/null || { echo 'npm is required.' >&2; exit 1; }

cd "$PROJECT_DIR"
npm run build
aws cloudformation deploy \
  --stack-name "$STACK_NAME" \
  --template-file "$TEMPLATE" \
  --region "$REGION" \
  --no-fail-on-empty-changeset

BUCKET="$(aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" --query "Stacks[0].Outputs[?OutputKey=='SiteBucketName'].OutputValue" --output text)"
DISTRIBUTION_ID="$(aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" --query "Stacks[0].Outputs[?OutputKey=='DistributionId'].OutputValue" --output text)"
aws s3 sync dist/ "s3://$BUCKET" --delete --cache-control 'public,max-age=31536000,immutable' --exclude 'index.html'
aws s3 cp dist/index.html "s3://$BUCKET/index.html" --cache-control 'no-cache'
aws cloudfront create-invalidation --distribution-id "$DISTRIBUTION_ID" --paths '/*' >/dev/null
aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" --query "Stacks[0].Outputs[?OutputKey=='WebsiteUrl'].OutputValue" --output text
