from loguru import logger

def calcul(n: int) -> int:
    """Retourne le carré de n."""
    res = n * n
    logger.info(f"calcul({n}) = {res}")
    return res
