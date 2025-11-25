from Q3 import *


def get_supply_route_details(graph, warehouse_o, warehouse_i, option):
     """
        Retrieves specific details about the supply route between two warehouses.

        This function checks if there is a direct connection from the origin warehouse to 
        the destination warehouse and returns the requested edge weight detail.

        Parameters:
        graph (dict): The supply chain graph represented as an adjacency map.
        warehouse_o (str): The alphanumeric warehouse ID of the origin vertex.
        warehouse_i (str): The alphanumeric warehouse ID of the destination vertex.
        option (str): Specifies which detail to retrieve from the supply route. 
                    It can be one of the following values:
                    - "time": Returns the Shipment Time.
                    - "cost": Returns the Shipment Cost.
                    - "mode": Returns the Shipping Method.

        Returns:
        int/float/str: The requested detail based on the `option` value:
                    - If "time" is selected, returns the Shipment Time (int).
                    - If "cost" is selected, returns the Shipment Cost (float).
                    - If "mode" is selected, returns the Shipping Method (str).
                    - Returns None if the origin warehouse does not exist in the graph.
                    - Returns -1 if there is no direct connection to the destination warehouse.
    """

     # WRITE YOUR CODE HERE
    pass


def main():
     G = create_supply_chain('supply_chain.csv')
     details = get_supply_route_details(G, "W1", "W11", "time")
     print(details)

     """
     EXPECTED OUTPUT:
     2
     """

     details = get_supply_route_details(G, "W1", "W11", "cost")
     print(details)

     """
     EXPECTED OUTPUT:
     757.96
     """

     details = get_supply_route_details(G, "W1", "W11", "mode")
     print(details)

     """
     EXPECTED OUTPUT:
     Sea
     """

     details = get_supply_route_details(G, "W1", "W13", "time")
     print(details)

     """
     EXPECTED OUTPUT:
     -1
     """

     details = get_supply_route_details(G, "W34", "W14", "cost")
     print(details)

     """
     EXPECTED OUTPUT:
     None
     """
  

if __name__ == "__main__":
    main()
