provider "azurerm" {
  version     = "~>2.0"
  environment = "public"
  features {}
}

resource "azurerm_resource_group" "resource" {
  name     = "${var.default_name}resource"
  location = var.region
}
