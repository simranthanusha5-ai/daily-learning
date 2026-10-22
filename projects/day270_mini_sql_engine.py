"""Day 270: Mini SQL Query Engine."""

class RelationalTable:
    def __init__(self, columns):
        self.columns = columns
        self.rows = []

    def insert(self, row_dict):
        self.rows.append(row_dict)

    def select(self, fields, where_fn=None):
        out = []
        for row in self.rows:
            if where_fn is None or where_fn(row):
                if fields == ["*"]:
                    out.append(row)
                else:
                    out.append({f: row[f] for f in fields})
        return out

if __name__ == "__main__":
    tbl = RelationalTable(["id", "name", "age"])
    tbl.insert({"id": 1, "name": "Alice", "age": 25})
    tbl.insert({"id": 2, "name": "Bob", "age": 30})
    res = tbl.select(["name"], where_fn=lambda r: r["age"] > 26)
    assert res == [{"name": "Bob"}]
    print("Day 270 Mini SQL tests passed!")
