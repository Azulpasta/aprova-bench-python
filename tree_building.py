class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None

    records = sorted(records, key=lambda x: x.record_id)

    record_ids = [r.record_id for r in records]
    expected_ids = list(range(len(records)))
    if record_ids != expected_ids:
        raise ValueError("Record id is invalid or out of order.")

    nodes = {r.record_id: Node(r.record_id) for r in records}

    root = None
    for r in records:
        if r.record_id == r.parent_id:
            if r.record_id != 0:
                raise ValueError("Only root should have equal record and parent id.")
            root = nodes[r.record_id]
        else:
            if r.parent_id >= r.record_id:
                raise ValueError("Node parent_id should be smaller than it's record_id.")
            parent_node = nodes[r.parent_id]
            parent_node.children.append(nodes[r.record_id])

    return root
