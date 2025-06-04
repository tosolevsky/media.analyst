from app.data.sources_data import RSS_FEEDS


def get_sources(category: str, region: str) -> list[str]:
    """Return RSS feed URLs for the given category and region.

    Parameters
    ----------
    category: str
        News category key (case-insensitive).
    region: str
        Region key (case-insensitive).

    Returns
    -------
    list[str]
        List of RSS feed URLs. If the region is not defined for the
        category, the function falls back to the ``global`` feeds. If the
        category does not exist, an empty list is returned.
    """
    category_key = category.lower()
    region_key = region.lower()

    cat_data = RSS_FEEDS.get(category_key)
    if not cat_data:
        return []

    return cat_data.get(region_key) or cat_data.get("global", [])
