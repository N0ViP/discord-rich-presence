import time
from pypresence import Presence

# ============================================================
# CONFIGURATION SECTION
# ============================================================

# ----------------------------
# TIMER / ELAPSED TIME
# ----------------------------
# Discord Rich Presence uses UNIX timestamps (seconds since 1970-01-01).
#
# Common options:
#
# 1) Start counting from script launch (recommended):
#    start_time = int(time.time())
#
# 2) Start from UNIX epoch (timer always increasing):
#    start_time = 1
#
# 3) Start from a SPECIFIC date and time:
#    Use a UNIX timestamp converter:
#    https://www.unixtimestamp.com/
#
#    Example:
#    2024-01-01 00:00:00 UTC → 1704067200
#    start_time = 1704067200
#
# 4) Disable the timer completely:
#    Remove the "start=start_time" line in RPC.update()
#
start_time = 1

# ----------------------------
# DISCORD APPLICATION ID
# ----------------------------
# This is NOT your bot token.
# It is the "Application ID" from the Discord Developer Portal.
#
# Steps to get it:
# 1) Go to https://discord.com/developers/applications
# 2) Create or select an application
# 3) Copy the "Application ID"
#
client_id = '1234567890123456789'

# ============================================================
# DISCORD RICH PRESENCE SETUP
# ============================================================

RPC = Presence(client_id)
RPC.connect()

# ----------------------------
# RICH PRESENCE CONTENT
# ----------------------------
# Everything below controls what people see on your profile.

RPC.update(
    # MAIN STATUS LINE (big bold text)
    # Example: "Coding", "Gaming", "AFK", etc.
    state="Working on my own success",

    # SECONDARY LINE (smaller text under the state)
    # Optional — you can comment it out or remove it.
    # details="Grinding silently",

    # TIMER (elapsed time)
    # Uses the start_time defined above
    start=start_time,

    # LARGE IMAGE KEY
    #
    # This MUST match the image asset name in the Developer Portal.
    #
    # How to get the image name:
    # 1) Go to Discord Developer Portal
    # 2) Select your application
    # 3) Go to "Rich Presence" → "Art Assets"
    # 4) Upload an image
    # 5) The "Asset Name" (NOT the filename) is used here
    #
    # Asset names are case-sensitive.
    #
    large_image="bot_img",

    # TEXT SHOWN WHEN HOVERING OVER THE IMAGE
    # Keep it short; long text may be truncated.
    large_text="N0ViP"
)

# ============================================================
# KEEP SCRIPT RUNNING
# ============================================================

try:
    # Rich Presence only works while the script is running.
    # This loop keeps it alive without using CPU.
    while True:
        time.sleep(600)
except KeyboardInterrupt:
    # Stops the script cleanly when pressing Ctrl + C
    print("\nScript terminated gracefully.")
    RPC.close()
