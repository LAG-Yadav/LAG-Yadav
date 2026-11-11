#!/usr/bin/env python3
"""Generate the Eon-aesthetic SVG assets + README for github.com/LAG-Yadav."""
from pathlib import Path

OUT = Path("/home/kaal/eon-profile")
ASSETS = OUT / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

INK = "#0a0c09"
INK2 = "#101409"
LINE = "#1b2116"
GRID = "#151a11"
LIME = "#d4e32e"
WHITE = "#f2f4ec"
GREY = "#8d948a"
DIM = "#5d635a"
MONO = "'DejaVu Sans Mono','JetBrains Mono',Menlo,Consolas,'Courier New',monospace"


def hero():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 350" width="1200" height="350" role="img" aria-label="Yadav Iserbelas — offensive security engineer">
  <defs>
    <linearGradient id="scan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{LIME}" stop-opacity="0"/>
      <stop offset="45%" stop-color="{LIME}" stop-opacity="0.55"/>
      <stop offset="55%" stop-color="{LIME}" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="{LIME}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="glow" cx="88%" cy="18%" r="52%">
      <stop offset="0%" stop-color="{LIME}" stop-opacity="0.10"/>
      <stop offset="100%" stop-color="{LIME}" stop-opacity="0"/>
    </radialGradient>
    <clipPath id="blink"><rect x="0" y="0" width="11" height="20"/></clipPath>
  </defs>

  <rect width="1200" height="350" fill="{INK}"/>
  <rect width="1200" height="350" fill="url(#glow)"/>

  <g stroke="{GRID}" stroke-width="1">
    {"".join(f'<line x1="{x}" y1="0" x2="{x}" y2="350"/>' for x in range(0, 1200, 48))}
    {"".join(f'<line x1="0" y1="{y}" x2="1200" y2="{y}"/>' for y in range(0, 330, 48))}
  </g>

  <g stroke="{LIME}" stroke-width="1.6" fill="none" opacity="0.9">
    <path d="M28 62 L28 28 L62 28"/>
    <path d="M1172 286 L1172 320 L1138 320"/>
  </g>
  <g stroke="{DIM}" stroke-width="1.2" fill="none" opacity="0.55">
    <path d="M1172 62 L1172 28 L1138 28"/>
    <path d="M28 286 L28 320 L62 320"/>
  </g>

  <g opacity="0.30" fill="none" stroke="{LIME}" stroke-width="1">
    <circle cx="1020" cy="120" r="46"/>
    <circle cx="1020" cy="120" r="78" stroke-dasharray="3 7"/>
    <circle cx="1020" cy="120" r="112" stroke-dasharray="2 11"/>
    <line x1="880" y1="120" x2="1160" y2="120"/>
    <line x1="1020" y1="-10" x2="1020" y2="250"/>
  </g>

  <text x="64" y="60" font-family="{MONO}" font-size="13" fill="{DIM}" letter-spacing="5.5">EON // SECURITY</text>
  <text x="1136" y="60" text-anchor="end" font-family="{MONO}" font-size="13" fill="{DIM}" letter-spacing="3">ZA · GAUTENG</text>

  <text x="62" y="152" font-family="{MONO}" font-size="66" font-weight="bold" fill="{WHITE}" letter-spacing="1.5">YADAV</text>
  <text x="62" y="220" font-family="{MONO}" font-size="66" font-weight="bold" fill="{WHITE}" letter-spacing="1.5">ISERBELAS</text>

  <rect x="62" y="240" width="132" height="3" fill="{LIME}"/>

  <text x="62" y="278" font-family="{MONO}" font-size="15.5" fill="{GREY}" letter-spacing="1.6">OFFENSIVE SECURITY  ·  PENETRATION TESTING  ·  ACTIVE DIRECTORY</text>

  <text x="62" y="308" font-family="{MONO}" font-size="14" fill="{LIME}">yadav@eon:~$</text>
  <text x="186" y="308" font-family="{MONO}" font-size="14" fill="{WHITE}">./recon --authorised-only</text>
  <rect x="452" y="295" width="10" height="17" fill="{LIME}" opacity="0.85">
    <animate attributeName="opacity" values="0.85;0;0.85" dur="1.2s" repeatCount="indefinite"/>
  </rect>

  <rect x="0" y="0" width="1200" height="350" fill="url(#scan)" opacity="0.06"/>
</svg>'''


def section(num, label):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 44" width="1200" height="44" role="img" aria-label="{num} {label}">
  <rect width="1200" height="44" fill="none"/>
  <text x="2" y="29" font-family="{MONO}" font-size="15" font-weight="bold" fill="{LIME}" letter-spacing="2">{num}</text>
  <text x="42" y="29" font-family="{MONO}" font-size="15" font-weight="bold" fill="{WHITE}" letter-spacing="2">//</text>
  <text x="80" y="29" font-family="{MONO}" font-size="15" font-weight="bold" fill="{WHITE}" letter-spacing="3.2">{label}</text>
  <line x1="0" y1="40" x2="1200" y2="40" stroke="{LINE}" stroke-width="1.4"/>
  <line x1="0" y1="40" x2="86" y2="40" stroke="{LIME}" stroke-width="1.8"/>
</svg>'''


def badge(label, logo, slug):
    return (f'<img src="https://img.shields.io/badge/{slug}-0f110d?style=flat-square'
            f'&amp;logo={logo}&amp;logoColor={LIME.lstrip("#")}" alt="{label}" height="20">')


(ASSETS / "hero.svg").write_text(hero(), encoding="utf-8")
sections = [
    ("s01", "01", "whoami"),
    ("s02", "02", "what i do"),
    ("s03", "03", "selected work"),
    ("s04", "04", "stack"),
    ("s05", "05", "contact"),
]
for fname, num, label in sections:
    (ASSETS / f"{fname}.svg").write_text(section(num, label), encoding="utf-8")

stack = [
    ("Python", "python", "Python"),
    ("Bash", "gnubash", "Bash"),
    ("Linux", "linux", "Linux"),
    ("Docker", "docker", "Docker"),
    ("Burp Suite", "burpsuite", "Burp"),
    ("Nmap", "nmap", "Nmap"),
    ("Wireshark", "wireshark", "Wireshark"),
    ("BloodHound", "bloodhound", "BloodHound"),
    ("Microsoft Entra ID", "microsoftazure", "Entra%20ID"),
    ("Cloudflare", "cloudflare", "Cloudflare"),
    ("Flask", "flask", "Flask"),
    ("Git", "git", "Git"),
]
stack_row = " ".join(badge(lbl, lg, slug) for lbl, lg, slug in stack)

readme = f'''<img src="assets/hero.svg" alt="Yadav Iserbelas — offensive security engineer" width="100%">

<p align="center">
  <a href="https://eonsecurity.co.za"><img src="https://img.shields.io/badge/EON%20SECURITY-eonsecurity.co.za-d4e32e?style=flat-square&labelColor=0f110d" alt="Eon Security"></a>
  <a href="mailto:hello@eonsecurity.co.za"><img src="https://img.shields.io/badge/EMAIL-hello@eonsecurity.co.za-0f110d?style=flat-square&logo=maildotru&logoColor=d4e32e" alt="Email"></a>
  <a href="https://github.com/LAG-Yadav"><img src="https://img.shields.io/badge/GITHUB-LAG--Yadav-0f110d?style=flat-square&logo=github&logoColor=d4e32e" alt="GitHub"></a>
</p>

<img src="assets/s01.svg" alt="01 whoami" width="100%">

```console
yadav@eon:~$ whoami
yadav iserbelas — offensive security engineer, south africa

yadav@eon:~$ cat mission.txt
I find the way in before someone less friendly does.
Web applications, internal networks, APIs, cloud, Active Directory.
Then I write it up so the fix is obvious to whoever has to pay for it.

yadav@eon:~$ ls ~/now
eon-security/     penetration testing and Active Directory audits
cyberpro/         the blue side, so I know what noise looks like
nexus-scalers/    client builds, when the testing queue is quiet
agentic-tooling/  machines that do the boring half of the job
```

I run **Eon Security**, a South African security firm that does penetration testing and Active Directory
audits. Most of my work is adversarial: get in the way an attacker would, prove it, then hand over
something a technical team can act on and a board can approve.

The other half is building the tooling that makes that repeatable — agent pipelines that enumerate,
triage and draft findings so the human hours go into the parts that actually need judgement.

<img src="assets/s02.svg" alt="02 what i do" width="100%">

**Offensive security**
Penetration testing across web applications, APIs, internal networks and cloud tenants.
Active Directory and Entra ID assessment: privilege paths, delegation abuse, certificate services,
tier-0 exposure. Incident response and forensic triage when something has already gone wrong — cloud
email takeover, session token replay, data exfiltration.

**Security engineering**
Agentic testing pipelines, detection content, and the unglamorous automation that stops a finding
being rediscovered six months later. I care more about the report being read than it being long.

<img src="assets/s03.svg" alt="03 selected work" width="100%">

| | |
|---|---|
| **EON PentAGI** | Agentic penetration-testing framework. Orchestrated recon, exploitation and reporting profiles driven from one engagement state. |
| **Cloud email takeover response** | Forensic reconstruction of a nine-day AiTM session-hijack against a Microsoft 365 tenant. Full timeline from sign-in logs, exfiltration scope, POPIA exposure and a prioritised remediation roadmap. |
| **Active Directory audit programme** | Repeatable domain assessment covering privilege escalation paths, Kerberos abuse and tier-0 separation, delivered as a technical report plus an executive summary for sign-off. |
| **Security automation** | Herald plugins and CI-side tooling that keep testing evidence, report generation and client delivery in one pipeline instead of four. |

<img src="assets/s04.svg" alt="04 stack" width="100%">

<p align="left">{stack_row}</p>

<img src="assets/s05.svg" alt="05 contact" width="100%">

```console
yadav@eon:~$ contact --work
web       https://eonsecurity.co.za
mail      hello@eonsecurity.co.za
location  Centurion, Gauteng, South Africa (SAST / UTC+2)
status    taking on penetration testing and AD audit engagements
```

<p align="center"><sub>Authorised testing only. No engagement starts without written scope and permission.</sub></p>
'''

(OUT / "README.md").write_text(readme, encoding="utf-8")
print("assets:", sorted(p.name for p in ASSETS.iterdir()))
print("readme bytes:", len(readme))
