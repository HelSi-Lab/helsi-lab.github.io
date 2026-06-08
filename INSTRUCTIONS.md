# HelSi Lab — content files for the Greene Lab Website Template (LWT)

These files are pre-filled with HelSi Lab content, ready to drop into a fresh
copy of the Lab Website Template. Folder layout here matches the repo layout.

## Step 1 — Create your LWT repo (one time, ~10 min)

1. Go to https://github.com/greenelab/lab-website-template → green **Use this template**
   → create a repo named e.g. `helsi-lab-website`, **Public**, leave "Include all branches" unchecked.
2. Repo **Settings → Actions**: give workflows **read and write** permission and allow creating pull requests.
3. Repo **Actions** tab: run the **"first time setup"** workflow manually (~30s).
4. **Settings → Pages**: deploy from the **`gh-pages`** branch.
5. Wait ~3 min for the first build. Your site link appears in the README.

## Step 2 — Drop in these files (replace/add)

| This file | Goes to (in your repo) | Action |
|---|---|---|
| `_config-BASIC-SETTINGS.yaml` | `_config.yaml` | Copy ONLY the basic-settings block into the **top** of the existing `_config.yaml`. **Do not** touch the Jekyll settings below it. |
| `_members/*.md` | `_members/` | Replace the example members with these 5. Rename student files to real names later. |
| `_data/sources.yaml` | `_data/sources.yaml` | Replace. Holds all publications. |
| `index.md` | `index.md` | Replace (home page). |
| `research/index.md` | `research/index.md` | Replace (publications + talks). |
| `projects/index.md` | `projects/index.md` | Replace (projects). |
| `team/index.md` | `team/index.md` | Replace (people). LWT's people page may be `/team` by default. |
| `join/index.md` | `join/index.md` | Add (new page). |
| `contact/index.md` | `contact/index.md` | Replace if present, else add. |
| `images/team/serin-lee.jpg` | `images/team/` | Add (PI photo). |
| `images/proj-*.jpg` | `images/` | Add (project figures). |

After committing, the **cite** workflow runs automatically and turns the DOIs in
`sources.yaml` into full citations on the Research page.

## Notes

- **Publications**: entries with `id: doi:...` are fetched automatically. Two papers
  (HPVsim, the 2021 COVID paper) had no DOI in your .bib, so they're manual entries —
  replace with `- id: doi:...` later for auto thumbnails. Add your **ORCID** in
  `_config.yaml` and as an `orcid-*.yaml` metasource to auto-pull everything.
- **Roles**: member `role:` values (`pi`, `grad`, `undergrad`) control the icon via
  `_data/types.yaml`. Members display regardless; if you want matching icons, add those
  keys in `_data/types.yaml`.
- **Students**: rename the placeholder member files and add `image:` + a bio.
- **Optional preprint**: a commented-out HPV therapeutic-vaccine paper sits at the
  bottom of `sources.yaml`; uncomment to include it.
- LWT controls the visual design/theme — tweak colors in `_styles` / theme file if desired.
