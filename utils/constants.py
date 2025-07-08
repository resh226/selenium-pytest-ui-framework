# utils/constants.py- sets default timour for wait functions in wait_utils.py

import os

def get_default_timeout():
    try:
        # Detect if running on Selenium Grid
        IS_GRID = bool(os.getenv("GRID_URL"))
        timeout = 80 if IS_GRID else 40
        print(f"DEBUG: IS_GRID={IS_GRID}, timeout={timeout}")
        return timeout
    except Exception as e:
        print(f"ERROR in get_default_timeout: {e}")
        return 40  # fallback timeout