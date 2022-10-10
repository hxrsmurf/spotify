resource "google_cloudfunctions2_function" "function" {
  name = "spotify-terraform"
  location = "us-central1"
  description = "Spotify with Terraform"

  build_config {
    runtime = "python39"
    entry_point = "hello_http"  # Set the entry point
    source {
      storage_source {
        bucket = google_storage_bucket.bucket.name
        object = google_storage_bucket_object.object.name
      }
    }
  }

  service_config {
    all_traffic_on_latest_revision = true
    ingress_settings    = "ALLOW_ALL"
    max_instance_count  = 1
    available_memory    = "128Mi"
    timeout_seconds     = 60
  }

  event_trigger {
    trigger_region = "us-central1"
    event_type = "google.cloud.pubsub.topic.v1.messagePublished"
    pubsub_topic = google_pubsub_topic.topic.id
  }

}