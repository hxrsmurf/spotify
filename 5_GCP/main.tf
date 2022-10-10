terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.39.0"
    }
  }
}

provider "google" {
  # Configuration options
  project     = "spotify-365112"
  region      = "us-central1"
}

output "function_uri" {
  value = google_cloudfunctions2_function.function.service_config[0].uri
}