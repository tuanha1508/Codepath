def organize_fabrics(fabrics):
    sorted_fabrics = sorted(fabrics, key=lambda x: x[1], reverse=True)
    return [name for name, _ in sorted_fabrics]
