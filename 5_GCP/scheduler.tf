resource "google_pubsub_topic" "topic" {
  name = "spotify-terraform"
}

resource "google_cloud_scheduler_job" "job" {
  name        = "spotify-terraform"
  description = "Execute Spotify function every two minutes"
  schedule    = "*/2 * * * *"

  pubsub_target {
    # topic.id is the topic's full resource name.
    topic_name = google_pubsub_topic.topic.id
    data       = base64encode("test")
  }
}