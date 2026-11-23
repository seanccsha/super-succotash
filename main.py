from pathlib import Path

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(
    "While I was 'offline sick' for GTA 6 launch week, my coding agent fixed the build, told my manager my Wi-Fi was fine, and attached an 11-hour uptime log from my PS5.",
    encoding="utf-8",
)
