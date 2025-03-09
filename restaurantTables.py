# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# Function to get a list of all free tables in the chosen timeslot
def find_free_tables(restaurant_tables, timeslot):
    free_tables = []
    tables_row_index = 1  
    # Iterate through all tables (starting from column index 1) to check availability

    for i in range(1, len(restaurant_tables[0])):
        if restaurant_tables[timeslot][i] == 'o':  
            free_tables.append(restaurant_tables[0][i])  # Add table name to the list

    return free_tables

# Function to find a single table that can seat at least the given party size and is free
def find_table_for_party(restaurant_tables, timeslot, party_size):
    table_id = 0
    tables_row_index = 1 

    for i in range(1, len(restaurant_tables[0])):
        if restaurant_tables[timeslot][i] == 'o':
            table_capacity = int(restaurant_tables[0][i].split('(')[1].split(')')[0]) # Extract the table's capacity from its name
            if table_capacity >= party_size:    # Check if the table can fit
                table_id = restaurant_tables[0][i]
                break # Stop after finding the first suitable table

    return table_id

# Function to find all tables that can seat a given party size and are free
def find_tables_for_party(restaurant_tables, timeslot, party_size):
    available_tables = []
    tables_row_index = 1  

    # Iterate through all tables to find those that fit the party size and are available
    for i in range(1, len(restaurant_tables[0])):
        if restaurant_tables[timeslot][i] == 'o':   # Check if the table is available
            table_capacity = int(restaurant_tables[0][i].split('(')[1].split(')')[0])
            if table_capacity >= party_size:     # Check if the table can fit the party
                available_tables.append(restaurant_tables[0][i])
        return available_tables
# Function to find all table combinations (single or adjacent pairs) that can seat the party
def find_table_combinations_for_party(restaurant_tables, timeslot, party_size):
    available_combinations = []
    tables_row_index = 1  

    # Iterate through all tables to check availability
    for i in range(1, len(restaurant_tables[0])):
        if restaurant_tables[timeslot][i] == 'o':
            table_capacity = int(restaurant_tables[0][i].split('(')[1].split(')')[0])  
            # If a single table can fit the party, add it as a valid option
            if table_capacity >= party_size:
                available_combinations.append([restaurant_tables[0][i]])

            # Check if combining two adjacent tables is possible
            if i < len(restaurant_tables[0]) - 1:
                combined_capacity = table_capacity + int(restaurant_tables[0][i+1].split('(')[1].split(')')[0])
            # If combined capacity meets party size and both tables are available, add as a valid option
                if combined_capacity >= party_size and restaurant_tables[timeslot][i+1] == 'o':
                    available_combinations.append([restaurant_tables[0][i], restaurant_tables[0][i+1]])

    return available_combinations

# PSEUDOCODE

# function find_free_tables(restaurant_tables, timeslot):
   # free_tables = []
    
  # For each table in restaurant_tables[timeslot]:
      # If table is 'o':
         # Add table ID to free_tables
    
   # return free_tables

# function find_table_for_party(restaurant_tables, timeslot, party_size):
 #  For each table in restaurant_tables[timeslot]:
     # If table is 'o' and capacity >= party_size:
         # return table ID
    
  # return None

# function find_tables_for_party(restaurant_tables, timeslot, party_size):
  # available_tables = []
    
  #  For each table in restaurant_tables[timeslot]:
    #  If table is 'o' and capacity >= party_size:
         #  Add table ID to available_tables
    
#   return available_tables

# function find_table_combinations_for_party(restaurant_tables, timeslot, party_size):
  # available_combinations = []
    
  # For each table in restaurant_tables[timeslot]:
      # If table is 'o' and capacity >= party_size:
        # Add [table ID] to available_combinations
            
         # If next table exists and is 'o' and combined capacity >= party_size:
            #  Add [table ID, next table ID] to available_combinations
    
 # return available_combinations
 
# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]
