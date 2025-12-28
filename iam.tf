# Platform / Dev Role
resource "aws_iam_role" "platform" {
  name = "PlatformDevRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::<ACCOUNT_ID>:root"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Payments Ingest Role
resource "aws_iam_role" "payments_ingest" {
  name = "PaymentsIngestRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::<ACCOUNT_ID>:root"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}

# Payments Processing Role
resource "aws_iam_role" "payments_processing" {
  name = "PaymentsProcessingRole"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          AWS = "arn:aws:iam::<ACCOUNT_ID>:root"
        }
        Action = "sts:AssumeRole"
      }
    ]
  })
}
