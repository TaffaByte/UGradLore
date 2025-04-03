from Q4 import *

def get_cheapest_outgoing_supply_route(graph, wh):
    """
    Finds the cheapest outgoing supply route from a given warehouse.

    This function searches for all outgoing connections from the given warehouse
    and determines the route with the lowest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the origin warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the cheapest outgoing supply route.
    None: If the warehouse has no outgoing supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    pass
    
            
def get_cheapest_incoming_supply_route(graph, wh):
    """
    Finds the cheapest incoming supply route for a given warehouse.

    This function searches for all incoming connections to the given warehouse
    and determines the route with the lowest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the cheapest incoming supply route.
    None: If the warehouse has no incoming supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    pass

def get_expensive_outgoing_supply_route(graph, wh):
    """
    Finds the most expensive outgoing supply route from a given warehouse.

    This function searches for all outgoing connections from the given warehouse
    and determines the route with the highest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the origin warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the most expensive outgoing supply route.
    None: If the warehouse has no outgoing supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    pass
            
def get_expensive_incoming_supply_route(graph, wh):
    """
    Finds the most expensive incoming supply route for a given warehouse.

    This function searches for all incoming connections to the given warehouse
    and determines the route with the highest shipment cost.

    Parameters:
    graph (dict): The supply chain graph represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID of the destination warehouse.

    Returns:
    tuple: A tuple containing (origin warehouse, destination warehouse) 
           representing the most expensive incoming supply route.
    None: If the warehouse has no incoming supply routes or does not exist in the graph.
    """

    # WRITE YOUR CODE HERE
    pass
    

def main():
    G = create_supply_chain('supply_chain.csv')
 
    route = get_cheapest_outgoing_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W14', 'W17')
    """
    
    route = get_cheapest_outgoing_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_expensive_outgoing_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W14', 'W1')
    """

    route = get_expensive_outgoing_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_cheapest_incoming_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W16', 'W14')
    """

    route = get_cheapest_incoming_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

    route = get_expensive_incoming_supply_route(G, "W14")
    print(route)

    """
    Expected Output:
    ('W18', 'W14')
    """

    route = get_expensive_incoming_supply_route(G, "W24")
    print(route)

    """
    Expected Output:
    None
    """

if __name__ == "__main__":
    main()
