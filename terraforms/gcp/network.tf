resource "google_compute_network" "vpc" {
  name                    = "${var.project_id}-vpc"
  project                 = "${var.project_id}"
  auto_create_subnetworks = "false"
}

resource "google_compute_subnetwork" "subnet" {
  name          = "${var.project_id}-subnet"
  project       = "${var.project_id}"
  region        = var.region
  network       = google_compute_network.vpc.name
  ip_cidr_range = "10.10.0.0/24"
}
