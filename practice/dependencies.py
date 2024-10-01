async def common_parameters(q: str | None = 'qqqqq', skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}
