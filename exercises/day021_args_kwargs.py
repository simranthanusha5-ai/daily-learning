# Day 21: *args and **kwargs

def build_query(table: str, *columns: str, limit: int = 10, **filters) -> str:
    cols = ", ".join(columns) if columns else "*"
    query = f"SELECT {cols} FROM {table}"
    if filters:
        conditions = " AND ".join(f"{k} = '{v}'" for k, v in filters.items())
        query += f" WHERE {conditions}"
    query += f" LIMIT {limit};"
    return query

sql = build_query("users", "id", "name", "email", status="active", role="admin", limit=5)
print("Constructed SQL:", sql)
