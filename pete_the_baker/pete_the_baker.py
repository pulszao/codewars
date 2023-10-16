def cakes(recipe, available):
    items_qty = []
    try:
        for item, quantity in recipe.items():
            qty = int(available[item] / quantity)
            items_qty.append(qty)

    except KeyError:
        return 0

    return min(items_qty)
