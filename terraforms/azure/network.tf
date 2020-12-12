
resource "azurerm_virtual_network" "vnet" {
  name                = "${var.default_name}vnet"
  location            = azurerm_resource_group.resource.location
  resource_group_name = azurerm_resource_group.resource.name

  address_space = ["10.0.0.0/16"]
}

resource "azurerm_subnet" "subnet" {
  name                 = "${var.default_name}subnet"
  resource_group_name  = azurerm_resource_group.resource.name
  virtual_network_name = azurerm_virtual_network.vnet.name

  address_prefixes  = ["10.0.0.0/24"]
  service_endpoints = ["Microsoft.Sql", "Microsoft.Storage"]
}
