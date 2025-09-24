'''
Question: you are given the following code below. Given this code, what do you think you need to do?

Starter Code:
import re

PARSER_REGEX = r'SELECT\s+(.+?)\s+FROM\s+(\S+)(?:\s+WHERE\s+(.+?))?(?:\s+ORDER\s+BY\s+(.+?))?\s*;'

# Data from the lineItems table
DATA = [
    { "id": 1, "orderId": 1, "itemName": "BMW Z4", "price": 499 },
    { "id": 2, "orderId": 1, "itemName": "Ferrari Monza SP2", "price": 1198 },
    { "id": 3, "orderId": 2, "itemName": "Volkswagen Golf GTI", "price": 99 },
    { "id": 4, "orderId": 2, "itemName": "Ferrari Monza SP2", "price": 1095 },
    { "id": 5, "orderId": 3, "itemName": "Ferrari Monza SP2", "price": 1390 },
]

def run_query(query):
    match = re.match(PARSER_REGEX, query)
    if not match:
        raise Exception("Invalid query")
    parsed_query = match.groups()
    print(parsed_query)


# Insert these in the run_query to test:
run_query("SELECT itemName FROM lineItems WHERE price > 1000;")
# SELECT itemName FROM lineItems WHERE price > 1000;
# SELECT * FROM lineItems WHERE itemName = 'BMW Z4'
# SELECT * FROM lineItems ORDER BY price;
# SELECT * FROM lineItems;
'''

import re
import operator

PARSER_REGEX = r'SELECT\s+(.+?)\s+FROM\s+(\S+)(?:\s+WHERE\s+(.+?))?(?:\s+ORDER\s+BY\s+(.+?))?\s*;'


# Data from the lineItems table
DATA = [
    { "id": 1, "orderId": 1, "itemName": "BMW Z4", "price": 499 },
    { "id": 2, "orderId": 1, "itemName": "Ferrari Monza SP2", "price": 1198 },
    { "id": 3, "orderId": 2, "itemName": "Volkswagen Golf GTI", "price": 99 },
    { "id": 4, "orderId": 2, "itemName": "Ferrari Monza SP2", "price": 1095 },
    { "id": 5, "orderId": 3, "itemName": "Ferrari Monza SP2", "price": 1390 },
]

def parse_value(raw_value):
    '''
    Helper function to parse a value from the query string.
    Example:
        '1000' -> 1000 (int)
        'BMW Z4' -> 'BMW Z4' (str)
    '''
    raw_value = raw_value.strip()
    if (raw_value.startswith("'") and raw_value.endswith("'")) or (raw_value.startswith('"') and raw_value.endswith('"')):
        raw_value = raw_value[1:-1] # strip quotes
    try:
        if '.' not in raw_value:
            return int(raw_value)
        else:
            return float(raw_value)
    except ValueError:
        return raw_value # aka keep it as a string


def run_query(query):
    match = re.match(PARSER_REGEX, query)
    if not match:
        raise Exception("Invalid query")

    # Break down the parsed query into its components
    select_clause, table, where_clause, order_by_clause = match.groups()
    # Example: itemName, lineItems, "price > 1000", None
    print(select_clause, table, where_clause, order_by_clause)

    # 1) FROM validation
    if table != "lineItems":
        raise Exception(f"Table not found: {table}")
    # Shallow copy of DATA so that you don't modify the original data
    #   Notes: This is done so that when we filter, sort, etc. we don't modify the original DATA
    rows = DATA[:]

    # 2) WHERE filtering
    if where_clause:
        # Setup operators for filtering
        operators = {
                     '=': operator.eq,
                     '>': operator.gt,
                     '<': operator.lt,
                     '>=': operator.ge,
                     '<=': operator.le,
                     '!=': operator.ne
                    }
        # Regex to parse the where clause (i.e. "price > 1000" -> ("price", ">", "1000"))
        match = re.match(r'(\S+)\s*(=|>|<|>=|<=|!=)\s*(.+)', where_clause.strip())
        # Catch error if the where clause is invalid
        if not match:
            raise Exception(f"Invalid WHERE clause: {where_clause}")
        field, op, value = match.groups() # price, >, 1000
        value = parse_value(value)
        if field not in rows[0]:
            raise Exception(f"Field not found: {field}")

        # one liner:
        rows = [row for row in rows if operators[op](row[field], value)]
        # expanded version:
        # filtered_rows = []
        # for row in rows:
        #     if operators[op](row[field], value):
        #         filtered_rows.append(row)
        # rows = filtered_rows

    # 3) ORDER BY sorting
    if order_by_clause:
        order_by_field = order_by_clause.strip()
        if order_by_field not in rows[0]:
            raise Exception(f"Field not found: {order_by_field}")
        # Sort rows
        rows = sorted(rows, key=lambda row: row[order_by_field])

    # 4) SELECT projection
    if select_clause.strip() == '*':
        return rows
    else:
        select_fields = [field.strip() for field in select_clause.split(',')]
        for field in select_fields:
            if field not in rows[0]:
                raise Exception(f"Field not found: {field}")
        return [{col: row.get(col) for col in select_fields} for row in rows]

# Insert these in the run_query to test:
print(run_query("SELECT * FROM lineItems WHERE itemName = 'BMW Z4';"))
# SELECT itemName FROM lineItems WHERE price > 1000;
# SELECT * FROM lineItems WHERE itemName = 'BMW Z4';
# SELECT * FROM lineItems ORDER BY price;
# SELECT * FROM lineItems;
