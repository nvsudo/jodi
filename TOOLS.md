# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## Google API (Docs, Drive, Gmail, Calendar)

### Account Structure ⚠️ IMPORTANT
- **MY account (AI's working account):** ea.nikvora@gmail.com
  - This is where I create docs, check calendar, send emails
  - I should have FULL permissions on this account
- **YOUR account (human's personal account):** nikunj.vora@gmail.com
  - This is where I SHARE things so you can access them
  - Always share docs/sheets/slides with writer/editor access

### Current Setup
- **Tokens:** `/clawd/google_tokens.json`
- **Auth account:** ea.nikvora@gmail.com (MY working account)
- **Helper script:** `google_api.py`

### Current Scopes (✅ COMPLETE as of 2026-02-10)
```
✅ gmail.readonly
✅ gmail.send
✅ gmail.modify
✅ calendar
✅ calendar.events
✅ spreadsheets
✅ documents
✅ presentations
✅ drive (FULL ACCESS - can create, share, organize)
```

### ✅ FIXED: Can Now Share Documents Programmatically
**Status:** Re-authed on 2026-02-10 with full `drive` scope (not `drive.readonly`)

**Now works:**
- ✅ Creating documents, sheets, slides
- ✅ Reading document content
- ✅ Sharing documents (modifying permissions)
- ✅ Moving/organizing files in Drive

### Best Practices
- **Always share with nikunj.vora@gmail.com** (writer/editor access)
- If auto-share fails, return the doc link and ask user to manually share
- Check token expiry before long operations (expires ~1 hour after issue)

### Re-auth Command (when needed)
```bash
# Location of OAuth flow (need to verify actual command)
# This needs full drive scope added to the OAuth consent screen
```

### Lessons Learned
- 2026-02-10 AM: Hit issue creating Jodi PRD — could create doc but not share it (had `drive.readonly`)
- 2026-02-10 PM: **FIXED** — Re-authed with full `drive` scope. Now can share programmatically.
- **For future:** Use `google_reauth.py` script which requests all needed scopes correctly

## What Goes Here

Things like:
- Camera names and locations
- SSH hosts and aliases  
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras
- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
