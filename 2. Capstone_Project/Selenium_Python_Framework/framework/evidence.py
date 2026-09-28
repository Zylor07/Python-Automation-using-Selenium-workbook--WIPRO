"""Save uniquely named browser screenshots for failures."""
from datetime import datetime, timezone
from pathlib import Path
import re
import uuid
from framework.config import ROOT


def save_failure(driver, test_name: str) -> Path:
    directory = ROOT / "screenshots"
    directory.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]", "_", test_name)[:90]
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    path = directory / f"{safe_name}_{stamp}_{uuid.uuid4().hex[:8]}.png"
    if not driver.save_screenshot(str(path)):
        raise OSError(f"Browser failed to save screenshot: {path}")
    return path
