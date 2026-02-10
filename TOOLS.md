# TOOLS.md - Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff that's unique to your setup.

## Google API (Docs, Drive, Gmail, Calendar)

### Current Setup
- **Tokens:** `/clawd/google_tokens.json`
- **Auth account:** ea.nikvora@gmail.com (owner)
- **Helper script:** `google_api.py`

### Current Scopes (⚠️ INCOMPLETE)
```
✅ gmail.readonly
✅ gmail.send
✅ gmail.modify
✅ calendar
✅ calendar.events
✅ spreadsheets
✅ documents
❌ drive.readonly (READ ONLY - cannot share/modify permissions)
```

### ⚠️ KNOWN ISSUE: Cannot Share Documents Programmatically
**Problem:** Current token only has `drive.readonly` scope, which allows:
- ✅ Creating documents
- ✅ Reading document content
- ❌ Sharing documents (modifying permissions)
- ❌ Moving/organizing files

**Impact:** When I create Google Docs, I cannot automatically share them. User must manually share.

**Solution for next re-auth:**
Replace `https://www.googleapis.com/auth/drive.readonly` with:
- `https://www.googleapis.com/auth/drive` (full access), OR
- `https://www.googleapis.com/auth/drive.file` (access to app-created files only)

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
- 2026-02-10: Hit this issue creating Jodi PRD — could create doc but not share it
- **Next time:** During re-auth flow, explicitly request `drive` scope, not just `drive.readonly`

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
