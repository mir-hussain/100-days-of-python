for item in ingredients:
        if resources[item] < ingredients[item]:
            return False