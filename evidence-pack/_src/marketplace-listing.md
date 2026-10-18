# Marketplace listing copy

Paste these into the Atlassian Marketplace listing form. Character limits are noted where the form enforces them; check the form for the current limits before submitting.

## English

**App name:** Evidence Pack for Jira: Change Audit Evidence

**Tagline (short):** Audit-ready change management evidence from Jira history, for ISO 27001, SOC 2, DORA and NIS2.

**Summary:**
Stop building audit evidence from screenshots. Evidence Pack reads your Jira history and shows, change by change, whether it was approved, approved before work started, and approved by someone other than the implementer. Download a PDF your auditor can re-check, with a reproducible sample and a SHA-256 fingerprint.

**Highlight 1: Evidence packs in a minute**
Pick changes with JQL and an audit period, test all of them or a seeded random sample, and get every exception with its reason. PDF and CSV, fingerprinted and stored for later.

**Highlight 2: Approval where the work happens**
Approvers approve or reject right on the Jira issue. Self-approval is blocked, emergency changes get a policy window, and every decision is chained so later edits show up.

**Highlight 3: Mapped to the frameworks you report on**
ISO/IEC 27001:2022 A 8.32, SOC 2 CC8.1, DORA Art. 9(4)(e) and NIS2 Art. 21(2)(e). Plus a 12-month trend of how often changes miss the rules, and why.

**More details:**
- Runs entirely on Atlassian Forge. No external servers, no data egress.
- Monthly packs built automatically for the previous month.
- Optional check for linked pull requests, commits, deployments or links.
- Roles: admins configure, Jira groups control who builds packs and who approves.
- Settings change log and full data export.
- English and German, including the PDF.

**Privacy and security answers:**
- Does the app store data outside Atlassian? No. All data is stored in Forge hosted storage.
- Does the app egress data? No.
- Does the app process personal data? It reads Jira user names and account ids from issue history and stores approver account ids and names in Forge storage. It reports stored account ids to Atlassian's personal data reporting API weekly and erases closed accounts.
- Scopes: read:jira-work (read issues and history), read:jira-user (names and groups), write:jira-work (comment and optional transition on approval), storage:app (settings, packs, approvals).

## Deutsch

**Name:** Evidence Pack für Jira: Nachweise für Change-Audits

**Kurzbeschreibung:** Prüfungsfeste Change-Management-Nachweise aus der Jira-Historie, für ISO 27001, SOC 2, DORA und NIS2.

**Zusammenfassung:**
Schluss mit Audit-Nachweisen aus Screenshots. Evidence Pack liest Ihre Jira-Historie und zeigt für jede Änderung, ob sie freigegeben wurde, ob vor Arbeitsbeginn freigegeben wurde und ob jemand anderes als die umsetzende Person freigegeben hat. Laden Sie ein PDF herunter, das Ihr Prüfer nachvollziehen kann, mit reproduzierbarer Stichprobe und SHA-256-Fingerabdruck.

**Highlight 1: Nachweise in einer Minute**
Änderungen per JQL und Prüfzeitraum auswählen, alle prüfen oder eine Zufallsstichprobe mit Seed ziehen, und jede Abweichung mit Grund erhalten. PDF und CSV, mit Fingerabdruck und gespeichert.

**Highlight 2: Freigabe direkt im Ticket**
Freigebende geben direkt im Jira-Vorgang frei oder lehnen ab. Selbstfreigabe ist gesperrt, Notfalländerungen haben ein Regelfenster, und jede Entscheidung ist verkettet, sodass spätere Änderungen auffallen.

**Highlight 3: Zugeordnet zu Ihren Regelwerken**
ISO/IEC 27001:2022 A 8.32, SOC 2 CC8.1, DORA Art. 9 Abs. 4 lit. e und NIS2 Art. 21 Abs. 2 lit. e. Dazu ein 12-Monats-Trend, wie oft Änderungen die Regeln verfehlen und warum.

**Weitere Details:**
- Läuft vollständig auf Atlassian Forge. Keine externen Server, kein Datenabfluss.
- Monatliche Nachweise für den Vormonat werden automatisch erstellt.
- Optionale Prüfung auf verknüpfte Pull Requests, Commits, Deployments oder Links.
- Rollen: Admins konfigurieren, Jira-Gruppen steuern, wer Nachweise erstellt und wer freigibt.
- Änderungsprotokoll der Einstellungen und vollständiger Datenexport.
- Deutsch und Englisch, auch im PDF.
