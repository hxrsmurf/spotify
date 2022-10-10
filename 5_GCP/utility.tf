resource "random_id" "bucket_prefix" {
  byte_length = 8
}

resource "random_id" "rng" {
  keepers = {
    first = "${timestamp()}"
  }
  byte_length = 8
}