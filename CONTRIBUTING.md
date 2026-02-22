# Contributing Guide

> This guide is a draft under construction.

## 1. Read the specification

Consult the latest Editor’s Draft before proposing changes:

* HTML: [https://zarr.dev/geozarr-spec/documents/standard/template/geozarr-spec.html](https://zarr.dev/geozarr-spec/documents/standard/template/geozarr-spec.html)
* PDF: [https://zarr.dev/geozarr-spec/documents/standard/template/geozarr-spec.pdf](https://zarr.dev/geozarr-spec/documents/standard/template/geozarr-spec.pdf)

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

## 6. Versioning and releases

The group follows semantic versioning for official releases. Minor editorial or encoding improvements may occur between major releases when consensus allows.

## 7. Roadmap

Work should follow the priorities defined in the roadmap:
[https://github.com/zarr-developers/geozarr-spec/wiki/First-Release-RoadMap](https://github.com/zarr-developers/geozarr-spec/wiki/First-Release-RoadMap)
