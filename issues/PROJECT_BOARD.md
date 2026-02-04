# GeoZarr v1 Project Board Organization

> **Strawman Proposal** - This document is a starting point for discussion. Feedback and refinements from SWG members are welcome. Please open an issue or bring comments to the next SWG meeting.

This document describes a proposed structure for organizing a GitHub Project board to track progress toward the GeoZarr v1.0 release.

## Board Views

### 1. Kanban View (Default)

**Columns:**

| Column | Description |
|--------|-------------|
| **Backlog** | Identified work items not yet refined |
| **Ready** | Refined, unblocked, ready to start |
| **In Progress** | Actively being worked on |
| **In Review** | PRs open or awaiting SWG review |
| **Done** | Merged/completed |

### 2. Roadmap View

Timeline view grouped by milestone, showing dependencies and target dates.

### 3. Release Readiness View

Filtered view showing items in v1 milestones (v1-rc, v1-oab, v1-vote), sorted by milestone then status.

---

## Labels

| Label | Color | Description |
|-------|-------|-------------|
| `geo-proj` | `#1d76db` (blue) | CRS convention |
| `spatial` | `#0e8a16` (green) | Spatial transform convention |
| `multiscales` | `#fbca04` (yellow) | Multiscales convention |
| `spec` | `#006b75` (teal) | Core specification document |
| `docs` | `#fef2c0` (yellow) | Documentation |
| `testing` | `#d4c5f9` (purple) | Test cases and validation |
| `interop` | `#f9d0c4` (pink) | Interoperability with external tools |
| `governance` | `#e6e6e6` (gray) | Process and governance |

---

## Milestones

Issues are assigned to milestones to indicate release targeting. Milestones follow the OGC standardization process.

### v1-rc (Release Candidate)
**Target:** TBD

All content complete and ready for formal review. No new features after this point.

**Exit Criteria:**
- [ ] All three conventions finalized (geo-proj, spatial, multiscales)
- [ ] Conformance classes defined
- [ ] Normative language applied throughout
- [ ] JSON Schemas stable and validated
- [ ] At least 3 implementations documented (Candidate maturity)
- [ ] Code owner designated for each convention
- [ ] Test dataset suite available
- [ ] Documentation complete (quickstart, composition guide, compatibility matrix)

### v1-oab (OGC Architecture Board Review)
**Target:** TBD

Submit to OGC Architecture Board for review and public comment.

**Exit Criteria:**
- [ ] Spec document in OGC format
- [ ] Public comment period completed
- [ ] Comments addressed

### v1-vote (SWG Vote)
**Target:** TBD

Final SWG vote for adoption as OGC Standard.

**Exit Criteria:**
- [ ] OAB review complete
- [ ] SWG vote passed
- [ ] Release artifacts published
- [ ] All conventions at Candidate maturity (3+ implementations)

### post-v1
Features and improvements deferred to future releases.

**Zarr Conventions Maturity Reference:**
| Maturity | Min Impl # | Stability |
|----------|------------|-----------|
| Proposal | 0 | Not stable - breaking changes expected |
| Pilot | 1 | Approaching stability |
| **Candidate** | **3** | **Mostly stable - breaking changes require new version** |
| Stable | 6 | Completely stable - review process required |

---

## Issue Templates Location

The following issue templates are available in this directory:

| File | Title | Milestone |
|------|-------|-----------|
| `001-ogc-standard-document.md` | Create formal OGC Standard document | v1-rc |
| `002-conformance-classes.md` | Define conformance classes structure | v1-rc |
| `003-normative-language.md` | Add normative language to specifications | v1-rc |
| `004-version-stability.md` | Define version stability and compatibility policy | v1-rc |
| `005-convention-maturity.md` | Advance conventions from Proposal to Candidate | v1-rc |
| `006-tool-compatibility-matrix.md` | Document tool compatibility matrix | v1-rc |
| `007-gdal-interop-testing.md` | GDAL interoperability test suite | v1-rc |
| `008-quickstart-guide.md` | Create quickstart guide | v1-rc |
| `009-composition-guide.md` | Convention composition guide | v1-rc |
| `010-reference-implementation.md` | Document reference implementation | v1-rc |
| `011-test-dataset-suite.md` | Create conformance test dataset suite | v1-rc |
| `012-linked-datasets-convention.md` | Linked datasets convention | post-v1 |
| `013-chunking-best-practices.md` | Chunking best practices guide | v1-rc |
| `014-oab-review.md` | OGC Architecture Board Review and Public Comment | v1-oab |
| `015-swg-vote.md` | SWG Vote for Standard Adoption | v1-vote |
| `016-guidance-for-additions.md` | Guidance for new components of GeoZarr | v1-vote |
| `017-issues-with-CRS.md` | Opening any major concerns in spatial (Patrick) | v1-vote |

---

## Workflow

### Creating New Issues

1. Use the appropriate template from this directory
2. Apply relevant labels
3. **Assign to a milestone** (this determines release targeting)
4. Link any blocking issues

### Weekly Triage

1. Review backlog for new items
2. Refine items for next sprint
3. Update blocked/blocking relationships
4. Verify milestone assignments

### Milestone Reviews

At each milestone:
1. Review exit criteria checklist
2. Identify remaining blockers
3. Adjust scope if needed
4. Update roadmap timeline
