resource "aws_kms_key" "credit_card" {
  description             = "KMS key for credit card encryption"
  deletion_window_in_days = 7
}

resource "aws_kms_key_policy" "main" {
  key_id = aws_kms_key.credit_card.key_id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "AllowPlatformGenerateKey"
        Effect    = "Allow"
        Principal = { AWS = aws_iam_role.platform.arn }
        Action    = [
          "kms:GenerateDataKeyWithoutPlaintext"
        ]
        Resource = "*"
      },
      {
        Sid       = "AllowPaymentsIngestEncrypt"
        Effect    = "Allow"
        Principal = { AWS = aws_iam_role.payments_ingest.arn }
        Action    = [
          "kms:Decrypt",
          "kms:Encrypt"
        ]
        Resource = "*"
      },
      {
        Sid       = "AllowPaymentsProcessingDecrypt"
        Effect    = "Allow"
        Principal = { AWS = aws_iam_role.payments_processing.arn }
        Action    = [
          "kms:Decrypt"
        ]
        Resource = "*"
      }
    ]
  })
}
