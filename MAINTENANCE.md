# Hidden Spain Bargains — maintenance routine

Every change to the site:
1. Re-verify every fact in `tools/facts.py` that the change touches (official or reputable source, never Idealista) and update `checked`.
2. Run `python3 tools/build.py`. It refuses to build if a volatile fact is older than 45 days or if the automatic proofreading (`tools/proofcheck.py`) finds errors.
3. Read the changed pages once more as a proofreader (spelling, grammar, awkward sentences, contradictory figures).
4. Commit and push; Netlify publishes automatically.

Weekly (scheduled task, Monday morning): full fact re-verification + full proofreading pass + rebuild + push, with a short report to the owner.

Rules: never mention or link Idealista; only favourable property data except legally required items (energy rating); every figure must have a source.
