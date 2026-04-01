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

The [Zarr Conventions Framework](https://github.com/zarr-conventions/.github/blob/main/profile/README.md) requires a minimum of 3 implementations for Candidate maturity. This section defines additional criteria to ensure those implementations represent genuine, independent validation of the conventions.

### Definitions

An **implementation** is a software library, tool, or application that reads or writes Zarr data conforming to one or more GeoZarr conventions (geo-proj, spatial, multiscales).

A **qualifying implementation** is one that meets all of the criteria below.

### Independence

Qualifying implementations MUST originate from different organizations or development teams. Two implementations completely sharing development effort, funding, or leadership from the same organization count as one for maturity purposes.

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

At least one qualifying implementation MUST support **Full** (read/write) for each convention. Read-only implementations are valid but cannot be the sole basis for advancement.

### Demonstrated interoperability

Since GeoZarr is an Encoding Standard, evidence of implementation includes datasets containing content representative of the standard ([OGC TC Policy §6.6.7](https://docs.ogc.org/pol/05-020r29/05-020r29.html)). Each qualifying implementation MUST successfully read or write at least one dataset from the conformance test suite (once available). Until the test suite is established, implementations must demonstrate correct handling of at least one publicly accessible dataset that uses the convention.

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

The group follows semantic versioning for official releases. Minor editorial or encoding improvements may occur between major releases when consensus allows.

## 8. Roadmap

Work should follow the priorities defined in the roadmap:
[https://geozarr.org/roadmap.html](https://geozarr.org/roadmap.html)
