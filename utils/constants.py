import os

def get_default_timeout():
    try:
        grid_url = os.getenv("GRID_URL", "http://selenium-hub:4444")
        IS_GRID = "selenium-hub" in grid_url or "localhost" in grid_url or "4444" in grid_url
        timeout = 80 if IS_GRID else 40
        print(f"DEBUG: IS_GRID={IS_GRID}, timeout={timeout}")
        return timeout
    except Exception as e:
        print(f"ERROR in get_default_timeout: {e}")
        return 40  # fallback timeout
