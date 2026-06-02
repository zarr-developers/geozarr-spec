# Contributing Guide

> This guide is a draft under construction.

## 1. Review the roadmap

Familiarize yourself with current priorities and open work items before proposing changes:

* [V1 Roadmap](https://geozarr.org/roadmap.html)

The conventions themselves are developed in their own repositories:

| Convention | Repo |
|------------|------|
| **geo-proj** (`proj:`) | [zarr-conventions/geo-proj](https://github.com/zarr-conventions/geo-proj) |
| **spatial** (`spatial:`) | [zarr-conventions/spatial](https://github.com/zarr-conventions/spatial) |
| **multiscales** | [zarr-conventions/multiscales](https://github.com/zarr-conventions/multiscales) |

The [Editor’s Draft](https://zarr.dev/geozarr-spec/documents/standard/template/geozarr-spec.html) is the formal OGC spec document. It may lag behind the convention repos as it is updated periodically.

## 2. Understand GeoZarr objectives

GeoZarr does not define a new data model. The work  focuses on concrete and thematic Zarr conventions that address specific community needs. Each convention provides a clear and self-contained extension for a defined topic and supports practical adoption.

## 3. Scope and workflow for changes

* Avoid modifying multiple sections at once.
* Propose initial changes in a focused section.
* Use GitHub issues for discussion before drafting large updates.
* Create a branch in the main repository for visible collaborative work.

## 4. Participation

The GeoZarr SWG allows non-OGC members to participate in the development of the Standard in this collaboration environment, per [OGC TC Policy §4.13.7](https://docs.ogc.org/pol/05-020r29/05-020r29.html). As required by OGC, non-member participation does not grant OGC Portal access or SWG voting rights.

* All community members are encouraged to comment on issues, review pull requests, and propose changes.
* Monthly OGC GeoZarr SWG meetings focus on strategic discussion and topics lacking consensus.
* Example datasets can be contributed to [https://github.com/developmentseed/geozarr-examples](https://github.com/developmentseed/geozarr-examples).

## 5. Maintenance structure

### Review and merge authority

Anyone may review and comment on pull requests. Only OGC GeoZarr SWG chairs (or OGC voting members they delegate to) may merge pull requests, ensuring the collaboration environment remains under OGC control per TC Policy.

The [maintenance team](https://github.com/orgs/zarr-developers/teams/geozarr) manages repository access. Requests to join may be made as a post on the [OGC Agora General Space](https://agora.ogc.org/c/overview-716766/) or at an [OGC GeoZarr Monthly meeting](https://agora.ogc.org/c/events-geozarr-swg/).

### Voting

For contested matters, only SWG voting members may cast formal votes. Voting membership is defined by the [OGC TC Policies and Procedures](https://docs.ogc.org/pol/05-020r29/05-020r29.html) (Charter Members, or members who have opted in, completed the 30-day waiting period, and requested voting status).

### Pull request process

* PRs are reviewed asynchronously on GitHub and merged by SWG chairs.
* Rough consensus (per [IETF RFC 7282](https://www.rfc-editor.org/rfc/rfc7282)) is required for merge; the SWG chair determines when consensus has been reached.
* If consensus cannot be reached on GitHub, the topic should be raised at the next SWG meeting for discussion.
* If consensus still cannot be reached, an OGC formal vote may be initiated per the [TC voting procedures](https://docs.ogc.org/pol/05-020r29/05-020r29.html#consensus-and-voting).

## 6. Implementation criteria for Candidate maturity

The [Zarr Conventions Framework](https://github.com/zarr-conventions/.github/blob/main/profile/README.md) requires a minimum of 3 implementations for Candidate maturity. This section defines additional criteria to ensure those implementations represent genuine, independent validation of the conventions. These criteria are consistent with the OGC definition of evidence of implementation for Encoding Standards, which is "data sets containing content representative of the Standard, but not necessarily containing an example of every element in the Standard" ([OGC TC Policies and Procedures §8.2.1](https://docs.ogc.org/pol/05-020r29/05-020r29.html#two-track-Standards-process-criteria)).

### Definitions

An **implementation** is a software library, tool, or application that reads or writes Zarr data conforming to one or more GeoZarr conventions (geo-proj, spatial, multiscales).

A **qualifying implementation** is one that meets all of the criteria below.

### Independence

Qualifying implementations MUST originate from different organizations or development teams. Two implementations that completely share development effort, funding, or leadership from the same organization count as one for maturity purposes.

Independence ensures that conventions are interpretable from the specification alone, without relying on shared institutional knowledge.

### Convention coverage

Each qualifying implementation MUST support at least one complete GeoZarr convention (geo-proj, spatial, or multiscales), including all required fields defined by the convention's JSON Schema.

Partial support does not count toward the 3-implementation threshold for that convention.

### Capability level

Implementations MUST declare their capability level for each supported convention:

| Level | Description |
|-------|-------------|
| **Read** | Can parse and interpret convention metadata from existing Zarr stores |
| **Write** | Can produce valid convention metadata in new or existing Zarr stores |
| **Full** | Both read and write |

For each convention, the 3 qualifying implementations MUST include **at least two independent Write-capable (Write or Full) implementations** and **at least one independent Read-capable (Read or Full) implementation**. Two independent writers demonstrate that the specification text — not shared implementation code — constrains the metadata that is produced, and a separate reader demonstrates that this output is interoperable. A set of implementations that is read-only, or that contains only a single writer, cannot be the basis for advancement.

### Demonstrated interoperability

Each qualifying implementation MUST successfully read or write at least one dataset from the conformance test suite (once available). Collectively, the qualifying implementations for each convention MUST demonstrate at least one successful round trip: a dataset written by one implementation and read by a different, independent implementation.

### Release status

Convention support MUST be included in a released version of the implementation. Unreleased support (e.g., only available on a development branch or in a pre-release) does not count toward the 3-implementation threshold.

### Documentation

Each qualifying implementation MUST provide:

- Public source code or a public release
- Documentation or examples showing how convention metadata is read or written
- A link to the convention version supported

### Dataset diversity (recommended)

It is RECOMMENDED that qualifying implementations collectively demonstrate support for datasets from multiple domains (e.g., earth observation, climate, oceanography) and multiple storage backends (e.g., local filesystem, S3, GCS, Azure).

### Counting

The 3-implementation minimum applies **per convention**. A convention advances to Candidate only when it has 3 qualifying implementations for that specific convention. An implementation supporting all three conventions counts toward each.

Qualifying implementations are tracked in the [implementation matrix](https://geozarr.org/implementations.html). The SWG chair determines when an implementation qualifies, subject to the consensus process described in [§5](#5-maintenance-structure).

## 7. Versioning and releases

### Constituent conventions

Each constituent convention (geo-proj, spatial, multiscales, and any future GeoZarr conventions) is versioned in its own repository, tied to its maturity level in the [Zarr Conventions Framework](https://github.com/zarr-conventions/.github/blob/main/profile/README.md):

- A convention SHOULD tag a pre-stable release (e.g. `v0.x`) once it reaches **Pilot** maturity (examples, a JSON Schema, and at least one implementation).
- A convention SHOULD release an initial stable version once it reaches **Candidate** maturity, as defined by the implementation criteria in [§6](#6-implementation-criteria-for-candidate-maturity).

The version-numbering scheme — for example, integer versions (`v1`) versus `major.minor`, and the relationship to Semantic Versioning — is under discussion in [#102](https://github.com/zarr-developers/geozarr-spec/issues/102) and [zarr-conventions-spec#29](https://github.com/zarr-conventions/zarr-conventions-spec/issues/29). A convention's UUID is permanent and MUST NOT change across versions.

### The GeoZarr specification

The GeoZarr specification is a document that **references** a set of conventions at pinned versions. It is versioned independently of those conventions, on its own editorial cadence: a new GeoZarr release may update prose or re-point a reference without any convention changing, and a convention may release a new version without forcing an immediate GeoZarr release.

Each GeoZarr release records the exact convention versions it references (in the release notes and the specification's normative references), so that a given GeoZarr version resolves to a specific, reproducible set of conventions.

**Release gate.** GeoZarr SHALL NOT release an initial stable version until every convention in the v1 suite — spatial, geo-proj, and multiscales — has reached **Candidate** maturity (per [§6](#6-implementation-criteria-for-candidate-maturity)). This makes a stable GeoZarr release a guarantee that its referenced conventions are individually mature, rather than an independent assertion.

**OGC lifecycle precedence.** If GeoZarr enters the OGC Full Standards track before the release gate is met, OGC lifecycle rules govern the document's version number — under which a Standards document "shall start at 1.0" ([OGC TC Policies and Procedures §7.2](https://docs.ogc.org/pol/05-020r29/05-020r29.html#standards)) — and take precedence over the gate above.

### Out of scope (tracked in [#102](https://github.com/zarr-developers/geozarr-spec/issues/102))

- The version-numbering scheme for conventions and for GeoZarr (integer vs. `major.minor` vs. Semantic Versioning).
- How GeoZarr versions after its initial stable release (e.g. when a referenced convention later issues a breaking change).
- Whether conventions added after the v1 suite (e.g. CF, DGGS, TileMatrixSet) participate in the release gate.

## 8. Roadmap

Work should follow the priorities defined in the roadmap:
[https://geozarr.org/roadmap.html](https://geozarr.org/roadmap.html)
