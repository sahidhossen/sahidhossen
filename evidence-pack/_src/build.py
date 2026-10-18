#!/usr/bin/env python3
"""Builds the Evidence Pack docs site into ../ (the evidence-pack folder).

Edit the CONTACT values and page content below, then run:  python3 _src/build.py
"""
from pathlib import Path
from html import escape

# TODO before publishing: fill these in. They appear on Support, Privacy, Datenschutz and Terms.
CONTACT = {
    "email": "[support email]",
    "name": "[your name or business name]",
    "address": "[street, postcode, city, country]",
}
UPDATED = "18 October 2026"
UPDATED_DE = "18. Oktober 2026"

OUT = Path(__file__).resolve().parent.parent

LOGO = """<svg width="30" height="30" viewBox="0 0 30 30" aria-hidden="true"><rect x="3" y="2" width="20" height="26" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 9h10M8 13h10M8 17h6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="22" cy="22" r="6.5" fill="#2f5bd3"/><path d="m19.2 22 1.9 1.9 3.8-3.8" stroke="#fff" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>"""

NAV = [
    ("Product", [("index.html", "Overview"), ("getting-started.html", "Getting started")]),
    ("Using it", [("checks.html", "How the checks work"), ("approvals.html", "Approving changes"), ("settings.html", "Settings"), ("faq.html", "FAQ")]),
    ("Legal and help", [("support.html", "Support"), ("privacy.html", "Privacy policy"), ("terms.html", "Terms of use")]),
]


def page(slug: str, title: str, body: str, lang: str = "en", desc: str = "") -> None:
    nav = []
    for group, items in NAV:
        links = "".join(
            f'<a href="{href}"{" aria-current=\"page\"" if href == slug else ""}>{escape(label)}</a>' for href, label in items
        )
        nav.append(f"<h2>{escape(group)}</h2>{links}")
    other = '<a href="datenschutz.html">Datenschutzerklärung (Deutsch)</a>' if lang == "en" else '<a href="privacy.html">Privacy policy (English)</a>'
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} | Evidence Pack for Jira</title>
<meta name="description" content="{escape(desc or 'Audit-ready change management evidence from your Jira history.')}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;600&family=Source+Serif+4:opsz,wght@8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<div class="shell">
  <aside class="side" id="side">
    <a class="brand" href="index.html">{LOGO}<b>Evidence Pack</b></a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="side" onclick="var s=document.getElementById('side');var o=s.classList.toggle('open');this.setAttribute('aria-expanded',o)">Menu</button>
    <nav aria-label="Documentation">{''.join(nav)}<p class="lang">{other}</p></nav>
  </aside>
  <main>
    <article class="sheet">
{body}
    </article>
    <p class="foot">Evidence Pack is an app for Jira Cloud. Jira and Atlassian are trademarks of Atlassian. This site is not affiliated with Atlassian.</p>
  </main>
</div>
</body>
</html>
"""
    # Give headings without an id a stable anchor, e.g. "What counts as approval" -> #what-counts-as-approval
    import re

    def anchor(m):
        text = re.sub(r"<[^>]+>", "", m.group(1))
        slug_id = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
        return f'<h2 id="{slug_id}">{m.group(1)}</h2>'

    html = re.sub(r"<h2>(.*?)</h2>", anchor, html)
    (OUT / slug).write_text(html, encoding="utf-8")


EXCERPT = """
<div class="excerpt" role="img" aria-label="Example from an evidence pack: three changes, two with exceptions, and the SHA-256 fingerprint of the pack">
  <div class="excerpt-head"><strong>Exceptions (2 of 25 tested)</strong><span>ISO/IEC 27001:2022 Annex A 8.32, Q3 2026, seed 482913</span></div>
  <table>
    <thead><tr><th>Key</th><th>Change</th><th>Approved first</th><th>Not self-approved</th><th>Reason</th></tr></thead>
    <tbody>
      <tr><td class="key">OPS-212</td><td>Rotate database credentials</td><td><span class="mark ok">✓</span></td><td><span class="mark ok">✓</span></td><td>Passed</td></tr>
      <tr class="ex"><td class="key">OPS-219</td><td>Change firewall rules for VPN</td><td><span class="mark ok">✓</span></td><td><span class="mark no">✕</span></td><td>A. Weber approved and also implemented</td></tr>
      <tr class="ex"><td class="key">OPS-231</td><td>Add index on orders table</td><td><span class="mark no">✕</span></td><td><span class="mark ok">✓</span></td><td>Moved to In Progress before it was approved</td></tr>
    </tbody>
  </table>
  <div class="stamp"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5l-8-3Z" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="m8.5 12 2.4 2.4 4.6-4.6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg><span>SHA-256 <code>a3f9c2e81b7d4f60c5e2a9b13d8f7e6c4b2a1908f7e6d5c4b3a291807f6e5d4c</code></span></div>
</div>
"""

page("index.html", "Overview", f"""
<h1>Change evidence your auditor can check</h1>
<p class="lede">Evidence Pack reads the history of your Jira tickets and shows, change by change, whether it was approved, approved before work started, and approved by someone other than the person who did it. Then it hands you the result as a PDF your auditor can re-check.</p>
{EXCERPT}
<h2>What it replaces</h2>
<p>When an auditor asks for "the full history of these 20 changes", most teams spend days on screenshots and spreadsheet exports. Evidence Pack builds the same evidence from the system of record in about a minute, picks the sample with a recorded seed so nothing looks cherry-picked, and lists every exception with its reason.</p>
<h2>What you get</h2>
<ul>
<li><strong>Evidence packs.</strong> Pick changes with JQL and a period, test all of them or a random sample, and download a PDF and CSV with a SHA-256 fingerprint.</li>
<li><strong>Approval in the ticket.</strong> Approvers approve or reject right on the Jira issue. Each decision is chained to the previous one, so later edits show up.</li>
<li><strong>Emergency changes.</strong> Changes with an emergency label may be approved within a window after work starts, as most change policies allow.</li>
<li><strong>Code evidence.</strong> Optionally require a linked pull request, commit, deployment or link for every change.</li>
<li><strong>Control mapping.</strong> ISO/IEC 27001:2022 A 8.32, SOC 2 CC8.1, DORA Art. 9(4)(e) and NIS2 Art. 21(2)(e).</li>
<li><strong>A 12-month trend.</strong> See how often changes miss the rules and what the most common causes are.</li>
<li><strong>Monthly packs.</strong> Last month's pack is built on the first of every month and stored in the app.</li>
</ul>
<h2>Where your data goes</h2>
<p>Nowhere. Evidence Pack runs entirely on Atlassian's own infrastructure and stores its records inside your Atlassian site. It has no servers of its own and sends no data to any outside service. The developer has no access to your data. See the <a href="privacy.html">privacy policy</a>.</p>
<p><a href="getting-started.html">Get started</a> or read <a href="checks.html">how the checks work</a>.</p>
""", desc="Audit-ready change management evidence from your Jira history, for ISO 27001, SOC 2, DORA and NIS2.")

page("getting-started.html", "Getting started", """
<h1>Getting started</h1>
<p class="lede">You can build your first evidence pack in about five minutes. You need to be a Jira admin for the first step.</p>
<ol class="steps">
<li><strong>Install the app.</strong> Find Evidence Pack in the Atlassian Marketplace and install it on your Jira Cloud site. Open it from <em>Apps</em> in the Jira sidebar. The first time, click <em>Allow access</em> so it can read issue history as you.</li>
<li><strong>Tell it what approval means for you.</strong> Go to <em>Settings</em>. Pick the status that means a change is approved (for example <em>Approved</em> or <em>CAB approved</em>) and the statuses that mean work has started (for example <em>In Progress</em> and <em>Done</em>). Pick the frameworks you report against. Save.</li>
<li><strong>Build a pack.</strong> Go to <em>New pack</em>. Enter JQL for the changes in scope, for example <code>project = OPS AND type = Change</code>, and the audit period. Choose a random sample of 25, or test all changes. Click <em>Generate pack</em>.</li>
<li><strong>Review the exceptions.</strong> The results show every change that failed a check, with the reason. Click a summary to see its full status history.</li>
<li><strong>Hand it over.</strong> Download the PDF for your auditor and the CSV for your own records. Both carry the same SHA-256 fingerprint.</li>
</ol>
<figure><img src="assets/screens/pack.png" alt="A generated evidence pack with population, tested changes, exceptions by check, exceptions by reason and the exceptions table" loading="lazy" width="1840" height="900"><figcaption>A generated pack. Every exception lists the check that failed and why.</figcaption></figure>
<h2>Next steps</h2>
<ul>
<li>Turn on <a href="approvals.html">approval in the ticket</a> so approvers record decisions where the work happens.</li>
<li>Add a monthly schedule in <a href="settings.html#schedules">Settings</a> so a pack for the previous month is ready on the first of every month.</li>
<li>Restrict who can build packs and who can approve in <a href="settings.html#access">Settings</a>.</li>
</ul>
""")

page("checks.html", "How the checks work", """
<h1>How the checks work</h1>
<p class="lede">This page is written for auditors and compliance leads. It describes exactly how Evidence Pack selects changes and decides whether each one passed.</p>
<h2>Which changes are in the population</h2>
<p>The population is every Jira issue that matches the JQL you enter and whose status category changed to <em>Done</em> inside the audit period. The exact query is printed on the first page of every pack, so it can be re-run independently in Jira.</p>
<h2>How the sample is chosen</h2>
<p>The population is sorted by issue id. If you ask for a sample, Evidence Pack draws it with a seeded random generator and prints the seed in the pack. Running the same query with the same seed over the same population returns exactly the same sample, which shows the sample was not hand-picked.</p>
<h2>What counts as approval</h2>
<p>An admin chooses one of three definitions, and the choice is printed in the pack:</p>
<ul>
<li><strong>Status.</strong> The change was moved into one of the configured approval statuses. The person who moved it is the approver.</li>
<li><strong>Evidence Pack approval.</strong> An approver clicked <em>Approve change</em> on the issue. The decision is recorded with the approver, time, note and the status at that moment.</li>
<li><strong>Either.</strong> The earliest of the two counts.</li>
</ul>
<p>A later rejection in Evidence Pack revokes an earlier approval made there.</p>
<h2>The checks</h2>
<table>
<thead><tr><th>Check</th><th>Passes when</th></tr></thead>
<tbody>
<tr><td>Approval recorded</td><td>An approval exists, as defined above.</td></tr>
<tr><td>Approved before implementation</td><td>The approval happened before the change first moved into an implementation status. For changes with the emergency label, approval may follow within the configured window (48 hours by default).</td></tr>
<tr><td>Approver is not the implementer</td><td>The approver did not move the change into an implementation status and is not its assignee.</td></tr>
<tr><td>Code change linked (optional)</td><td>The issue has a linked pull request, commit, deployment, or a link to one.</td></tr>
</tbody>
</table>
<p>A change is an exception when any check fails. When there is no approval at all, the pack lists only that root cause, not the checks that fail as a consequence.</p>
<h2>Where the data comes from</h2>
<p>All facts come from Jira's own issue history (the changelog) and from Evidence Pack's approval records. Nothing is typed in by hand, and nothing is taken from screenshots.</p>
<h2>Integrity</h2>
<ul>
<li>Every pack carries a SHA-256 fingerprint computed from the query, the seed, the settings, and every tested change with its history and results.</li>
<li>Every pack is stored in the app and can be re-downloaded later. The app never edits or deletes stored packs.</li>
<li>Each approval decision is chained to the previous decision on the same issue with SHA-256. If a stored decision is changed, the issue shows <em>Integrity broken</em>.</li>
<li>Every change to the app's settings is logged with who made it and the old and new values.</li>
</ul>
<h2>Control mapping</h2>
<p>The PDF maps the checks to the frameworks you select. The mapping is guidance; the auditor decides whether the evidence is sufficient for a control.</p>
<table>
<thead><tr><th>Framework</th><th>Control</th></tr></thead>
<tbody>
<tr><td>ISO/IEC 27001:2022</td><td>Annex A 8.32, Change management</td></tr>
<tr><td>SOC 2 (Trust Services Criteria)</td><td>CC8.1, Change management</td></tr>
<tr><td>DORA, Regulation (EU) 2022/2554</td><td>Art. 9(4)(e), ICT change management</td></tr>
<tr><td>NIS2, Directive (EU) 2022/2555</td><td>Art. 21(2)(e), Security in acquisition, development and maintenance</td></tr>
</tbody>
</table>
<p class="note">Evidence Pack produces evidence. It does not make an organisation compliant and does not replace an auditor's judgement.</p>
""")

page("approvals.html", "Approving changes", """
<h1>Approving changes in the ticket</h1>
<p class="lede">Approvers can approve or reject a change directly on the Jira issue, so the decision is recorded where the work happens.</p>
<h2>Open the panel</h2>
<p>On any issue, click the Evidence Pack icon below the title and choose <em>Change approval</em>. The panel shows whether the change is compliant, waiting for approval, or has an exception, and why.</p>
<figure><img src="assets/screens/panel.png" alt="The Change approval panel on a Jira issue, showing each check, a note field, the approve and revoke buttons and the decision record" loading="lazy" width="760" height="900" style="max-width:420px"><figcaption>The panel on an approved issue, with its decision record.</figcaption></figure>
<h2>Approve, reject or revoke</h2>
<ul>
<li><strong>Approve change</strong> records your approval with an optional note. If your admin turned it on, the issue also moves to the approval status.</li>
<li><strong>Reject</strong> needs a short reason.</li>
<li><strong>Revoke approval</strong> appears after an approval and records a rejection, which cancels the approval.</li>
</ul>
<p>Every decision also adds a comment to the issue, so the team sees it.</p>
<h2>Who can approve</h2>
<p>By default anyone who can see the issue can approve, except its assignee. Admins can limit approval to Jira groups such as a change advisory board in <a href="settings.html#access">Settings</a>.</p>
<h2>The decision record</h2>
<p>The panel lists every decision on the issue. <em>Integrity verified</em> means each decision still matches the chain of SHA-256 hashes created when it was recorded.</p>
""")

page("settings.html", "Settings", """
<h1>Settings</h1>
<p class="lede">Only Jira admins can change settings. Everyone else sees them read-only. Every change is recorded in the change log at the bottom of the page.</p>
<h2>Frameworks</h2>
<p>Choose the frameworks printed in the PDF's control mapping.</p>
<h2>How changes are judged</h2>
<table>
<thead><tr><th>Setting</th><th>What it does</th></tr></thead>
<tbody>
<tr><td>What counts as approval</td><td>A status, an approval in the ticket panel, or either. See <a href="checks.html#what-counts-as-approval">How the checks work</a>.</td></tr>
<tr><td>Approval statuses</td><td>Moving a change into one of these counts as approval.</td></tr>
<tr><td>Implementation statuses</td><td>Moving a change into one of these means work started. It must happen after approval, by someone else.</td></tr>
<tr><td>Emergency label and window</td><td>Changes with this label may be approved within the window after work starts.</td></tr>
<tr><td>Require code evidence</td><td>Adds a fourth check for a linked pull request, commit, deployment or link.</td></tr>
<tr><td>Block self-approval</td><td>Stops an assignee from approving their own change in the panel.</td></tr>
<tr><td>Move ticket on approval</td><td>Moves the issue to the first approval status when approved in the panel.</td></tr>
</tbody>
</table>
<h2 id="access">Access</h2>
<p><em>Who can build packs</em> and <em>Who can approve changes</em> take Jira groups. Leave them empty to allow everyone. Jira admins always can.</p>
<h2 id="schedules">Monthly packs</h2>
<p>Add a schedule with a name, JQL and sample size. On the first day of each month, a pack for the previous calendar month is built and stored in History. <em>Run now</em> builds last month's pack immediately.</p>
<h2>Your data</h2>
<p><em>Export all data</em> downloads a JSON file with settings, schedules, the change log, the pack log and all approval records.</p>
""")

page("faq.html", "FAQ", """
<h1>Frequently asked questions</h1>
<h3>Does Evidence Pack send my data anywhere?</h3>
<p>No. It runs on Atlassian's Forge platform, stores everything inside your Atlassian site, and makes no calls to outside services.</p>
<h3>Can the developer see our data?</h3>
<p>No. There is no developer-run server or database. The developer cannot access your Jira or the app's stored data.</p>
<h3>Which Jira permissions does it ask for and why?</h3>
<table>
<thead><tr><th>Permission</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Read Jira work</td><td>Read issues and their status history to build packs.</td></tr>
<tr><td>Read Jira users</td><td>Show who approved and who implemented, and check group membership.</td></tr>
<tr><td>Write Jira work</td><td>Add a comment and optionally move the issue when someone approves in the panel.</td></tr>
<tr><td>App storage</td><td>Store settings, packs and approval records inside your site.</td></tr>
</tbody>
</table>
<h3>Whose permissions are used to read issues?</h3>
<p>Packs you build in the app read issues as you, so you only see what you can see in Jira. Background and monthly packs run as the app.</p>
<h3>How large can a pack be?</h3>
<p>Up to 2,000 changes. Packs with more than 100 changes are built in the background; you can leave the page and open the result from History.</p>
<h3>Does it work with team-managed and company-managed projects?</h3>
<p>Yes. It only relies on statuses and issue history, which both project types have.</p>
<h3>Can I change a pack after it is generated?</h3>
<p>No. Packs are stored as generated, with a SHA-256 fingerprint. To include more changes, generate a new pack.</p>
<h3>Is Evidence Pack available in German?</h3>
<p>Yes. The app follows each user's Jira language, and you can choose English or German for each PDF.</p>
<h3>What happens when we uninstall?</h3>
<p>The app's stored data is removed by Atlassian according to its Forge data retention rules. Export your data first if you need to keep it.</p>
""")

page("support.html", "Support", f"""
<h1>Support</h1>
<p class="lede">Questions, bugs and feature requests are welcome.</p>
<p>Email <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a>. Please include your Jira site address and, for bugs, the steps that lead to the problem. Do not send issue contents or personal data unless they are needed to understand the problem.</p>
<h2>Response times</h2>
<p>Support is provided in English and German, Monday to Friday, Central European Time. Most questions get an answer within two business days.</p>
<h2>Security</h2>
<p>To report a security issue, email the same address with "Security" in the subject.</p>
""")

PRIVACY_EN = f"""
<h1>Privacy policy</h1>
<p class="updated">Last updated {UPDATED}</p>
<p>This policy explains what personal data the Evidence Pack app for Jira Cloud processes, where it is stored and who can access it.</p>
<h2>Who we are</h2>
<p>{CONTACT['name']}, {CONTACT['address']}. Contact: <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a>.</p>
<h2>The short version</h2>
<ul>
<li>The app runs entirely on Atlassian's Forge platform.</li>
<li>Everything it stores stays inside your Atlassian site.</li>
<li>It sends no data to us or to any third party.</li>
<li>We have no access to your Jira data or to the app's stored data.</li>
</ul>
<h2>Roles</h2>
<p>Your organisation is the controller of the data in its Jira site. Atlassian hosts and runs the app on its infrastructure as part of Forge, under Atlassian's own privacy policy and data processing terms. Because no data reaches us, we do not process your personal data when the app runs.</p>
<h2>What the app reads</h2>
<p>To build packs and show approval status, the app reads from Jira: issue keys, summaries, types, labels, assignees, status history (including who made each status change and when), development summaries and links. It reads Jira user names and group memberships to show who approved and to apply your access settings.</p>
<h2>What the app stores</h2>
<table>
<thead><tr><th>Data</th><th>Personal data in it</th></tr></thead>
<tbody>
<tr><td>Settings and their change log</td><td>Name and account id of the admin who made each change</td></tr>
<tr><td>Approval decisions</td><td>Approver's account id and name, time, note</td></tr>
<tr><td>Evidence packs</td><td>Names of people in each change's history; name of the person who generated the pack</td></tr>
<tr><td>Schedules</td><td>None</td></tr>
</tbody>
</table>
<p>All of this is stored in Atlassian-hosted app storage that belongs to your site.</p>
<h2>How long it is kept</h2>
<p>Data is kept until your organisation uninstalls the app. Atlassian then removes the app's storage according to its Forge data retention rules. Admins can export all stored data at any time from the app's Settings.</p>
<h2>Closed Atlassian accounts</h2>
<p>The app reports the account ids it stores to Atlassian's personal data reporting service every week. When Atlassian reports that an account has been closed, the app removes that person's name and account id from approval records. The integrity chain remains verifiable because it is built on a one-way hash of the account id.</p>
<h2>Your rights</h2>
<p>Requests to access, correct or erase personal data in your Jira site should go to your organisation, which controls that data. Atlassian account holders can also manage their data through Atlassian.</p>
<h2>Changes</h2>
<p>We will update this page when the app's data handling changes and note the date at the top.</p>
"""
page("privacy.html", "Privacy policy", PRIVACY_EN)

PRIVACY_DE = f"""
<h1>Datenschutzerklärung</h1>
<p class="updated">Stand: {UPDATED_DE}</p>
<p>Diese Erklärung beschreibt, welche personenbezogenen Daten die App Evidence Pack für Jira Cloud verarbeitet, wo sie gespeichert werden und wer darauf zugreifen kann.</p>
<h2>Verantwortlich für diese Seite</h2>
<p>{CONTACT['name']}, {CONTACT['address']}. Kontakt: <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a>.</p>
<h2>Kurz gesagt</h2>
<ul>
<li>Die App läuft vollständig auf der Forge-Plattform von Atlassian.</li>
<li>Alles, was sie speichert, bleibt in Ihrer Atlassian-Site.</li>
<li>Sie übermittelt keine Daten an uns oder an Dritte.</li>
<li>Wir haben keinen Zugriff auf Ihre Jira-Daten oder auf die von der App gespeicherten Daten.</li>
</ul>
<h2>Rollen</h2>
<p>Ihre Organisation ist Verantwortliche für die Daten in ihrer Jira-Site. Atlassian betreibt die App im Rahmen von Forge auf eigener Infrastruktur, nach den Datenschutz- und Auftragsverarbeitungsbedingungen von Atlassian. Da keine Daten zu uns gelangen, verarbeiten wir beim Betrieb der App keine personenbezogenen Daten.</p>
<h2>Was die App liest</h2>
<p>Für Nachweise und den Freigabestatus liest die App aus Jira: Vorgangsschlüssel, Zusammenfassungen, Typen, Labels, Bearbeitende, den Statusverlauf (einschließlich wer wann welchen Status gesetzt hat), Entwicklungszusammenfassungen und Links. Sie liest Namen von Jira-Benutzern und Gruppenmitgliedschaften, um Freigebende anzuzeigen und Ihre Zugriffseinstellungen anzuwenden.</p>
<h2>Was die App speichert</h2>
<table>
<thead><tr><th>Daten</th><th>Enthaltene personenbezogene Daten</th></tr></thead>
<tbody>
<tr><td>Einstellungen und Änderungsprotokoll</td><td>Name und Konto-ID der Admins, die etwas geändert haben</td></tr>
<tr><td>Freigabeentscheidungen</td><td>Konto-ID und Name der freigebenden Person, Zeitpunkt, Notiz</td></tr>
<tr><td>Nachweise</td><td>Namen von Personen im Verlauf jeder Änderung; Name der Person, die den Nachweis erstellt hat</td></tr>
<tr><td>Zeitpläne</td><td>Keine</td></tr>
</tbody>
</table>
<p>Alle Daten liegen im von Atlassian betriebenen App-Speicher Ihrer Site.</p>
<h2>Speicherdauer</h2>
<p>Die Daten bleiben gespeichert, bis Ihre Organisation die App deinstalliert. Danach entfernt Atlassian den App-Speicher gemäß den Aufbewahrungsregeln von Forge. Admins können jederzeit alle gespeicherten Daten in den Einstellungen der App exportieren.</p>
<h2>Geschlossene Atlassian-Konten</h2>
<p>Die App meldet die gespeicherten Konto-IDs wöchentlich an den Dienst von Atlassian zur Meldung personenbezogener Daten. Meldet Atlassian ein Konto als geschlossen, entfernt die App Namen und Konto-ID dieser Person aus den Freigabeentscheidungen. Die Integritätskette bleibt prüfbar, weil sie auf einem Einweg-Hash der Konto-ID beruht.</p>
<h2>Ihre Rechte</h2>
<p>Anfragen auf Auskunft, Berichtigung oder Löschung zu Daten in Ihrer Jira-Site richten Sie bitte an Ihre Organisation als Verantwortliche. Inhaber eines Atlassian-Kontos können ihre Daten außerdem über Atlassian verwalten. Sie haben zudem das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren.</p>
<h2>Änderungen</h2>
<p>Wenn sich der Umgang der App mit Daten ändert, aktualisieren wir diese Seite und das Datum oben.</p>
"""
page("datenschutz.html", "Datenschutzerklärung", PRIVACY_DE, lang="de")

page("terms.html", "Terms of use", f"""
<h1>Terms of use</h1>
<p class="updated">Last updated {UPDATED}</p>
<p>Evidence Pack is sold through the Atlassian Marketplace. Your use of the app is governed by the Atlassian Marketplace terms that apply to cloud apps, together with the additional terms below. If they conflict, the Atlassian terms prevail.</p>
<h2>Provider</h2>
<p>{CONTACT['name']}, {CONTACT['address']}. Contact: <a href="mailto:{CONTACT['email']}">{CONTACT['email']}</a>.</p>
<h2>What the app does and does not do</h2>
<p>Evidence Pack produces evidence about change approvals from data in your Jira site. It does not certify compliance with any law, regulation or standard, and its control mapping is guidance only. Decisions about the sufficiency of evidence remain with you and your auditors.</p>
<h2>Your data</h2>
<p>Your data stays in your Atlassian site and remains yours. How the app handles personal data is described in the <a href="privacy.html">privacy policy</a>.</p>
<h2>Availability and changes</h2>
<p>The app runs on Atlassian's Forge platform and depends on its availability. We may improve or change features; we will not remove core features during a paid subscription period without notice.</p>
<h2>Liability</h2>
<p>To the extent permitted by law, the app is provided as described, and liability is limited as set out in the applicable Atlassian Marketplace terms. Nothing in these terms limits liability that cannot be limited by law.</p>
""")

print("built", sorted(p.name for p in OUT.glob("*.html")))
