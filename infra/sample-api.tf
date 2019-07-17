variable "bucketname" {}

provider "aws" {
  region = "ap-northeast-1"
}

resource "aws_s3_bucket_object" "sample_api" {
  bucket = "${var.bucketname}"
  key = "sample-api.yaml"
  source = "sample-api.yaml"
  etag = "${filemd5("sample-api.yaml")}"
}

resource "aws_cloudformation_stack" "sample_api" {
  name = "sample-api"
  template_url = "https://s3.amazonaws.com/${var.bucketname}/sample-api.yaml"
  capabilities = ["CAPABILITY_NAMED_IAM"]
  tags = [
    { TEMPLATE_VER = "${filemd5("sample-api.yaml")}" }
  ]
  depends_on = [
    "aws_s3_bucket_object.sample_api"
  ]
}

