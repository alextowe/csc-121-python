def make_sandwich(*items):
    """Print the list of items that have been requested."""
    print("\nRequested items:")
    for item in items:
        print(f"- {item}")

make_sandwich("ham", "cheese", "lettuce", "mayonnaise")
make_sandwich("turkey", "bacon", "avocado")
make_sandwich("peanut butter", "jelly")