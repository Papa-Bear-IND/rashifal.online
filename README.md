# 🔮 Rashifal.online

Daily horoscope (राशिफल) website with auto-generated content via Claude API.

## Architecture

```
rashifal.online/
├── index.html                    # Main site (single page, all 12 rashis)
├── content/                      # Daily JSON files (auto-generated)
│   └── 2026-04-06.json          # One file per day
├── scripts/
│   └── generate_content.py      # Claude API content generator
├── .github/workflows/
│   └── daily-generate.yml       # Cron: generates content daily at 5 AM IST
└── README.md
```

## How It Works

1. **GitHub Actions** runs a cron job every night at 5 AM IST
2. **generate_content.py** calls Claude API to produce unique predictions for all 12 rashis in Hindi + English
3. Output is saved as `content/YYYY-MM-DD.json` and committed to the repo
4. **Cloudflare Pages** auto-deploys on every push
5. The static site loads today's JSON and renders predictions

## Setup (One-Time)

### 1. Create GitHub Repo
```bash
# On your machine (PowerShell)
cd E:\rashifal.online
git init
git remote add origin https://github.com/Papa-Bear-IND/rashifal.online.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

### 2. Add Claude API Key to GitHub
- Go to: github.com/Papa-Bear-IND/rashifal.online → Settings → Secrets → Actions
- Add secret: `ANTHROPIC_API_KEY` = your key from console.anthropic.com

### 3. Setup Cloudflare Pages
1. Sign up at cloudflare.com (free)
2. Go to: Workers & Pages → Create → Pages → Connect to Git
3. Select your `rashifal.online` repo
4. Build settings:
   - Build command: (leave empty)
   - Build output directory: `/` (root)
5. Deploy

### 4. Add Custom Domain
1. In Cloudflare Pages → your project → Custom domains
2. Add: `rashifal.online`
3. Cloudflare will tell you to change nameservers at your registrar
4. Update nameservers at your domain registrar (GoDaddy/wherever)
5. SSL is automatic — wait 5-10 minutes

### 5. Test Content Generation
```bash
# Manual test run (needs API key)
export ANTHROPIC_API_KEY=sk-ant-...
python scripts/generate_content.py 2026-04-07
```
Or trigger manually: GitHub repo → Actions → Daily Rashifal Generator → Run workflow

## Costs

| Item | Monthly Cost |
|------|-------------|
| Cloudflare Pages hosting | ₹0 (free) |
| GitHub Actions | ₹0 (free, 2000 min/mo) |
| Claude API (~24 calls/day) | ~₹20-25 |
| Domain renewal | ~₹40/mo (₹500/yr) |
| **Total** | **~₹65/month** |

## Revenue (AdSense)

Replace the `ad-slot` divs in index.html with your Google AdSense code once approved.
Three ad slots are pre-positioned:
- **Top banner** (728×90) — highest visibility
- **Mid content** (336×280) — between rashi grid and features
- **Bottom banner** — footer area

## Future Additions

- [ ] Individual rashi pages (`/mesh/`, `/vrishabh/` etc.) for better SEO
- [ ] Weekly & monthly predictions
- [ ] Panchang / शुभ मुहूर्त section
- [ ] Kundli matching tool
- [ ] E-commerce: gemstones, rudraksha, puja items
- [ ] Push notifications for daily rashifal
- [ ] AMP pages for faster mobile loading
