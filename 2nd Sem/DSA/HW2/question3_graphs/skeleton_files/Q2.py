from Q1 import *


def get_warehouse_connections(graph, wh, option):
    """
    Retrieves a list of connected warehouses based on the given option.

    This function finds all the warehouses that are directly connected to or from 
    the given warehouse in the supply chain graph.

    Parameters:
    graph (dict): The supply chain graph created in Q1, represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID for which connections are being retrieved.
    option (str): A character indicating the type of connections to retrieve:
        - "o" for outbound supply (warehouses receiving shipments from `wh`).
        - "i" for inbound supply (warehouses sending shipments to `wh`).
        - "b" for both inbound and outbound connections (for repeating values, keep only a single reference).

    Returns:
    list: A list of unique warehouse IDs that are connected to the given warehouse.
          If there are no connections, the function returns an empty list.

    Example:
    >>> get_warehouse_connections(G, "W1", 'o')
    (Warehouse, W1 exists so get its outbound connections in a list and return the list)
    ['W11', 'W4']

    >>> get_warehouse_connections(G, "W1", 'i')
    (Warehouse, W1 exists so get its inbound connections in a list and return the list)
    ['W11', 'W14', 'W5']

    >>> get_warehouse_connections(G, "W1", 'b')
    (Warehouse, W1 exists so get both its inbound and outbound links without repeated values in a list and return the list)
    ['W11', 'W4', 'W14', 'W5']

    >>> get_warehouse_connections(G, "W24", 'b')
    (Warehouse, W24 does not exist so no need to check for its connections, and return an empty list)
    []
    """

    # provide implementation here

    outbound = ['o', 'b'] # outbound connections
    inbound = ['i', 'b'] # inbound connections
    op_lst = []

    for key, val in graph.items(): # iterate through the graph

        if option in outbound: # check if the option is outbound
            if key[0] == wh: # check if the warehouse is in the outbound list
                for warehouse in val: # iterate throught the tuple of warehouses
                    wh_id = warehouse[0]
                    if wh_id not in op_lst:
                        op_lst.append(wh_id)

        if option in inbound: # check if the option is inbound
            for warehouse in val: # iterate through the tuple of warehouses
                if wh in warehouse: # check if the warehouse is in the tuple
                    wh_id = key[0]
                    if wh_id not in op_lst:
                        op_lst.append(wh_id)

    return op_lst


def get_number_of_warehouse_connections(graph, wh, option):
    """
    Computes the number of unique warehouse connections based on the given option.

    This function finds the total number of unique warehouses connected to or from 
    the given warehouse in the supply chain graph.

    Parameters:
    graph (dict): The supply chain graph created in Q1, represented as an adjacency map.
    wh (str): The alphanumeric warehouse ID for which the number of connections is being calculated.
    option (str): A character indicating the type of connections to count:
        - "o" for outbound supply (warehouses receiving shipments from `wh`).
        - "i" for inbound supply (warehouses sending shipments to `wh`).
        - "b" for both inbound and outbound connections (for repeating values, keep only a single reference).

    Returns:
    int: The number of unique warehouses connected to the given warehouse.
         If there are no connections or the warehouse does not exist, the function returns 0.
    """

    # provide implementation here

    lst = get_warehouse_connections(graph, wh, option)
    return len(lst) 
    pass


def main():
    G = create_supply_chain('supply_chain.csv')
    f = get_warehouse_connections(G, "W1", 'o')
    print(f)

    """
    EXPECTED OUTPUT:
    ['W11', 'W4']
    """

    f = get_warehouse_connections(G, "W1", 'i')
    print(f)

    """
    EXPECTED OUTPUT:
    ['W11', 'W14', 'W5']
    """
    
    f = get_warehouse_connections(G, "W1", 'b')
    print(f)

    """
    EXPECTED OUTPUT:
    ['W11', 'W4', 'W14', 'W5']
    """

    f = get_warehouse_connections(G, "W24", 'o')
    print(f)

    """
    EXPECTED OUTPUT:
    []
    """

    f = get_warehouse_connections(G, "W24", 'i')
    print(f)

    """
    EXPECTED OUTPUT:
    []
    """
    
    f = get_warehouse_connections(G, "W24", 'b')
    print(f)

    """
    EXPECTED OUTPUT:
    []
    """

    l = get_number_of_warehouse_connections(G, "W1", 'b')
    print(l)

    """
    EXPECTED OUTPUT:
    4
    """

    l = get_number_of_warehouse_connections(G, "W24", 'b')
    print(l)
    
    """
    EXPECTED OUTPUT:
    0
    """


if __name__ == "__main__":
    main()
