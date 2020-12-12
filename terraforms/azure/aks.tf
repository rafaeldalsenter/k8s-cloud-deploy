resource "azurerm_kubernetes_cluster" "aks" {
  name                = "${var.default_name}aks"
  location            = azurerm_resource_group.resource.location
  resource_group_name = azurerm_resource_group.resource.name

  dns_prefix = var.default_name

  default_node_pool {
    name           = "default"
    node_count     = 1
    vm_size        = "Standard_DS2_v2"
    vnet_subnet_id = azurerm_subnet.subnet.id
  }
}
