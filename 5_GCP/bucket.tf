
resource "google_storage_bucket" "bucket" {
  name     = "spotify-${random_id.bucket_prefix.hex}"
  location = "US"
  uniform_bucket_level_access = true
  versioning {
    enabled = true
  }
    lifecycle_rule {
        condition {
            age = 3
        }
        action {
            type = "Delete"
        }
    }
}

resource "google_storage_bucket_object" "object" {
  name   = "${random_id.rng.hex}.zip"
  bucket = google_storage_bucket.bucket.name
  source = "./python/requirements.zip"
}