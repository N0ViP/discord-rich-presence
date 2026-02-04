# Discord Rich Presence (Python)

> **Important:** This script is intentionally simple, but it is also low-level.
> **You MUST read the script and its comments carefully before running it.**
> Everything you need to configure is explained **inside the file itself**.
> Do not run it blindly.

---

## What this script does

This Python script sets a **custom Discord Rich Presence** using the
[`pypresence`](https://pypi.org/project/pypresence/) library.

It allows you to:
- Set a custom status text
- Optionally set a secondary detail line
- Display an elapsed time counter
- Show a custom large image with hover text

The Rich Presence **only stays active while the script is running**.

---

## Requirements

- **Python 3.8 or newer**
- **Discord Desktop App** (must be running)
- Internet connection

### Python dependency

This script depends on **pypresence**:

```bash
pip install pypresence
```

---

## Discord Application Setup (Required)

Before running the script, you must create a Discord application.

1. Go to: https://discord.com/developers/applications
2. Click **New Application**
3. Give it any name
4. Copy the **Application ID** (this is used in the script)
5. Go to **Rich Presence → Art Assets**
6. Upload at least one image
7. Note the **Asset Name** (not the file name)

⚠️ **If you skip this step, the script will not work.**

---

## How to use (READ FIRST)

### Step 1: Open the script

Open the Python file in a text editor **before running it**.

The script contains a clearly marked **CONFIGURATION SECTION**.

You are expected to:
- Set your **Application ID**
- Understand how the **timer works**
- Use the correct **image asset name**

All of this is documented **directly inside the script as comments**.

> If you do not understand something, **do not run the script yet**.
> Read the comments again.

---

## Running the script

### Linux / macOS

```bash
python3 discord-rich-presence.py
```

### Windows

```powershell
python discord-rich-presence.py
```

The Rich Presence will appear immediately if:
- Discord is running
- The Application ID is correct
- The image asset name exists

---

## Stopping the script

Press:

```text
Ctrl + C
```

The script will exit gracefully and remove the Rich Presence.

---

## Common mistakes

- Using a **bot token** instead of the **Application ID**
- Using the **image filename** instead of the **asset name**
- Forgetting to run Discord Desktop
- Not reading the comments inside the script

---

## Final warning

This script is intentionally minimal.

If you:
- Don’t understand UNIX timestamps
- Don’t know where image asset names come from
- Don’t read comments before running code

**You should stop and read the script again before using it.**

---

## License

MIT

