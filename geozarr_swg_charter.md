<!--
Title: OGC (add title text)
doctype: book
encoding: utf-8
lang: en
toc, toclevels: 4
numbered, sectanchors
source-highlighter: pygments
-->

<div align="right">

**Open Geospatial Consortium**

Submission Date: &lt;2026-07-dd&gt;

Approval Date: &lt;2026-07-dd&gt;

Internal reference number of this OGC® document: YY-nnnrx <!-- TODO(ask Scott): request document number for the revised charter (2023 charter was 23-046) -->

Category: OGC® Standards Working Group Charter

Authors: Max Jones

</div>

<div align="center">

# OGC GeoZarr Standards Working Group Charter

**Copyright notice**

Copyright © 2026 Open Geospatial Consortium

To obtain additional rights of use, visit http://www.opengeospatial.org/legal/

</div>

---

To: OGC members & interested parties

The OGC members listed below have proposed a re-chartering of the OGC GeoZarr Standards Working Group (GeoZarr SWG). The GeoZarr SWG seeks a re-charter to better reflect the relationship between GeoZarr, the Zarr Conventions Framework, and the NetCDF CF SWG. The SWG proposal provided in this document meets the requirements of the OGC Technical Committee (TC) Policies and Procedures.

The SWG name, statement of purpose, scope, list of deliverables, audience, and language specified in the proposal will constitute the SWG's official charter. Technical discussions may occur no sooner than the SWG's first meeting.

This SWG will operate under the OGC IPR Policy. The eligibility requirements for becoming a participant in the SWG at the first meeting (see details below) are that:

- You must be an employee of an OGC member organization or an individual member of OGC;
- The OGC member must have signed the OGC Membership agreement;
- You must notify the SWG chair of your intent to participate to the first meeting. Members may do so by logging onto the OGC Portal and navigating to the Observer page and clicking on the link for the SWG they wish to join and;
- You must attend meetings of the SWG. The first meeting of this SWG is at the time and date fixed below. Attendance may be by teleconference.

<!-- TODO(ask Scott): the eligibility bullets above reference the retired OGC Portal / Observer page; confirm the current boilerplate for the Agora-era joining process before submission. -->

Of course, participants also may join the SWG at any time. The OGC and the SWG welcomes all interested parties.

Non-OGC members who wish to participate may contact us about joining the OGC. In addition, the public may access some of the resources maintained for each SWG: the SWG public description, the SWG Charter, Change Requests, and public comments, which will be linked from the SWG's page.

Please feel free to forward this announcement to any other appropriate lists. The OGC is an open standards organization; we encourage your feedback.

## 1. Purpose of the Standards Working Group

<!--
Proposers will describe the purpose of the Standards Working Group and its overall mission in relation to OGC processes, the OGC Standards baseline, and OGC's business plan.
-->

The GeoZarr Standards Working Group (SWG) is chartered to develop a standard and conformance classes for geospatial data stored in the Zarr data format. Zarr specifies a data format for storing arrays and groups in a hierarchical model. The Zarr Conventions Framework enables communities to define and share metadata standards for Zarr data. The Zarr Conventions Framework is lightweight, decentralized, and composable, with its design informed by the successful approach of STAC extensions. The GeoZarr SWG serves several purposes related to the Zarr data format, Zarr conventions, and geospatial data:

- recommend a minimal set of Zarr conventions required to describe geospatial data (i.e., a minimal GeoZarr)
- recommend additional Zarr conventions that are composable with the minimal GeoZarr conventions and add functionality needed for real-world applications, rather than hypothetical use cases
- evaluate the technical merits and maturity (by way of adoption) of Zarr conventions proposed for incorporation into GeoZarr; conventions so incorporated constitute the *GeoZarr Conventions*
- provide conformance classes against which datasets can be tested for conformance to the GeoZarr Conventions
- evaluate new upstream convention releases for incorporation into future GeoZarr versions, to ensure that the licensing, technical design, and interoperability remain appropriate for inclusion in GeoZarr

The GeoZarr SWG will evaluate the technical merits of proposed Zarr conventions in order to accomplish the purposes listed above. Technical assessment will include, but not be limited to, an evaluation of the composability, simplicity, specificity, demonstrated real-world need, and maturity of the Zarr conventions, where real-world need is documented by the proposer through existing datasets, products, or implementations that require the capability, and maturity can be measured both by signals of adoption and by amount of time that the convention has been stable.

The GeoZarr SWG may recommend improvements to upstream communities where appropriate, including the Zarr Conventions Framework, specific Zarr conventions, STAC extensions, and the CF (Climate and Forecast) Metadata Conventions. The SWG may propose changes through those communities' own governance processes.

## 2. Business value proposition

<!--
This section provides a statement describing the value of this standards activity in relation to the OGC Membership, the geospatial community, and the wider IT community. This statement can be in terms of the interoperability problem being solved, processing Change requests to meet market (and Member requirements), a policy requirement and/or some other business value proposition. The proposition described in this section does not have to be in economic terms.
-->

Zarr is a generic data format for n-dimensional arrays that enables efficient storage and access to data in compressed chunks. Zarr's high performance and portability across local, high-performance computing, and cloud systems has made it increasingly popular across domains, including for geospatial purposes. In June 2022, the OGC endorsed the Zarr storage specification version 2.0 as an OGC community standard (OGC 21-050r1). The purpose of this re-charter is to standardize approaches for encoding geospatial metadata in Zarr. This will enable people and machines to use geospatial Zarr data to its fullest potential.

The business value of the GeoZarr standard includes providing data producers with a single target for encoding geospatial data in Zarr and consumers a single target for implementation, backed by the authority of the OGC. Data producers can adopt GeoZarr to ensure data encoded once is readable across the conforming tool ecosystem and understandable in perpetuity. For users, GeoZarr unlocks widespread visualization, subsetting, GIS services, machine learning, and automated and AI-assisted analysis. As GeoZarr enables browser-based approaches, its adoption lowers costs by reducing dependence on back-end services. In addition to these cost- and capability-driven benefits, GeoZarr will provide a target for contract development and evaluation, to ensure any Zarr-backed data and services delivered are widely useful.

GeoZarr standardization offers particularly great value now. While geospatial data has been stored in Zarr informally for a decade, the ad-hoc approach to geospatial metadata has led to bugs, inconsistencies between libraries and languages, and wasted money on development, duplicated storage, and reprocessing. GeoZarr standardization aims to prevent these errors from propagating in the future. Because GeoZarr conventions only add metadata, existing Zarr archives can adopt the standard in place without expensive reprocessing or duplicated storage, while existing Zarr tools continue to work on conformant data.

## 3. Scope of work

<!--
This section describes the scope of work (SOW) for the work of the SWG. There are typically at least three (3) cases that justify the formation of a SWG: A group of members decide to develop a new OGC candidate Standard from scratch, there is a draft submission being discussed by OGC members, or there are outstanding Change Requests for an existing OGC Standard and a revision is required.

The following describes the characteristics of a SOW for each of these cases.

For a SWG focused on defining and documenting a new OGC candidate Standard from "scratch," the SOW SHALL include a statement of the requirements and use cases for the candidate Standard being developed. The SOW SHALL also include a justification statement for developing a new candidate OGC Standard. The SOW SHALL also describe how the new candidate Standard is related to the existing OGC Standards baseline and the OGC Reference Model. The final deliverable of a "from scratch" focused SWG SHALL be a candidate Standard ready for submission using the OGC standards process.

For a SWG focused on processing a draft submission such as a specification developed outside the OGC and submitted into the OGC for consideration, the SOW would include evaluation of the submission in terms of the relationship to the existing OGC Standards baseline (see section below). The final deliverable of such a SWG SHALL be a candidate Standard for consideration by the membership for adoption.

For a SWG focused on revisions to an existing adopted Standard, the SOW should include a statement that the SWG will collect all outstanding Change Request Proposals (CRPs), evaluate each of the proposals, and make edits to the Standard based on CRPs and related decisions of the SWG membership. The SWG, at their discretion, may also ask the membership for any additional change requests that have not been previous submitted. Again, the final deliverable of a revision focused SWG SHALL be a revision of the candidate Standard for consideration by the membership for adoption.

In all cases, the SWG Charter shall provide a basic timeline plan for their activities.
-->

GeoZarr serves three families of geospatial data, with Zarr and geospatial representation as the common thread: data served well today by the CF (Climate and Forecast) Metadata Conventions in netCDF (climate and forecast model output, ocean models, in-situ observations, and satellite swaths); data served well today by GeoTIFF and Cloud Optimized GeoTIFF (imagery and other regularly gridded data with affine georeferencing, coordinate reference system metadata, and overviews); and novel geospatial applications not represented well by either lineage, such as discrete global grid systems (DGGS) and vector data cubes. GeoZarr accomplishes this by standardizing a set of Zarr conventions that are well-designed, composable, and mature, such that they can be used together to fulfill those diverse requirements within the geospatial domain.

The tables below detail planned and potential Zarr conventions for incorporation into GeoZarr, aligned with the families of geospatial data referenced above. Each convention is classified as **domain-agnostic** (its concepts apply to any n-dimensional array, so the convention belongs to the broader Zarr Conventions Framework and is reusable outside the geospatial domain) or **geospatial** (it encodes Earth-referencing, such as a coordinate reference system, planetary coordinate, or geographic feature). A few conventions split into a domain-agnostic mechanism carrying a geospatial vocabulary; these are marked accordingly. The last column cross-references the notes in Section 3.1, which map each convention to the prior standards and specifications it draws on. The tables are illustrative of the anticipated scope rather than a closed enumeration; the SWG may incorporate additional conventions that meet the assessment criteria in Section 1.

The conventions are grouped into proposed GeoZarr versions. Only Version 1 is chartered as the SWG's primary delivery (see Section 4.1). The groupings for subsequent versions are a proposed sequencing that the SWG will refine, and each post-Version-1 deliverable will be brought forward through the SWG Task approval process defined in the OGC TC Policies and Procedures (see Section 4.2). Each GeoZarr version normatively references specific, pinned versions of its constituent conventions, consistent with OGC practice for external normative references. The conventions themselves are versioned by their maintainers and are pre-stable (v0.x, with breaking changes permitted) until they reach v1; evolution of a convention after adoption does not alter an adopted GeoZarr Standard, which continues to reference the pinned versions.

**GeoZarr Version 1 — affine raster core (primary delivery).** Serves the GeoTIFF/COG family of use cases: regularly gridded data with affine georeferencing, coordinate reference system metadata, and multiresolution overviews. All three conventions exist and are targeting Candidate maturity (three or more independent implementations).

| Convention | Purpose | Classification | Existing | Prior art |
|---|---|---|---|---|
| proj | Coordinate reference system description via EPSG code, WKT2, or PROJJSON, including vertical datums. | Geospatial | Yes | [§3.1](#note-proj) |
| spatial | 2-D X/Y affine georeferencing of regular grids. | Geospatial | Yes | [§3.1](#note-spatial) |
| multiscales | Multiresolution pyramids: resolution levels related by scale/translate transforms over any axis. | Domain-agnostic | Yes | [§3.1](#note-multiscales) |

**GeoZarr Version 2 — coordinate and CF-alignment layer (proposed).** Serves the CF/netCDF family of use cases (climate and forecast model output, ocean models, in-situ observations) by adding the coordinate association layer and the interpretation conventions that common CF datasets rely on.

| Convention | Purpose | Classification | Existing | Prior art |
|---|---|---|---|---|
| coordinates | Describes the mapping between the logical index space and physical space, without defining the physical space itself. Supports 1-D, scalar, and multidimensional coordinates, alternative coordinate sets, and discrete/ordinal axes. | Domain-agnostic | In development | [§3.1](#note-coordinates) |
| units | Attaches units of measure to the values in an array, including dimensionless units and unit metadata. | Domain-agnostic | Yes | [§3.1](#note-units) |
| calendar | A specialized convention for time units, including reference-time-based decoding, the calendar mechanism, custom calendars, and leap seconds. | Domain-agnostic | No | [§3.1](#note-calendar) |
| geolocation | Curvilinear and swath geolocation via 2-D latitude/longitude arrays. | Geospatial | Yes | [§3.1](#note-geolocation) |
| missing-data | Sentinel-value and valid-range masking semantics. | Domain-agnostic | No | [§3.1](#note-missing-data) |
| flags | Value-to-label interpretation of integer arrays, covering enumerations and bitfields. | Domain-agnostic | No | [§3.1](#note-flags) |
| CF registration | Declares that unprefixed CF attributes (e.g., descriptive names and provenance) are in use, with the standard-name vocabulary layered on top. | Domain-agnostic mechanism; geospatial vocabulary | Yes | [§3.1](#note-registration) |

**Potential conventions.** Specialized structures — novel geospatial applications, non-raster and vector data, and the remaining CF capabilities. This group is listed to communicate the anticipated shape of the full suite; a potential convention advances to a proposed version only when a proposal demonstrates real-world need — existing datasets, products, or implementations that require the capability — and meets the assessment criteria in Section 1.

| Convention | Purpose | Classification | Existing | Prior art |
|---|---|---|---|---|
| dggs | Mapping between array index space and discrete global grid system zones (cell identifiers and resolution levels). | Geospatial | Proposed | [§3.1](#note-dggs) |
| tile-matrix-set | Binds multiscale resolution levels to registered tile matrix sets for web-tiling clients. | Geospatial | No | [§3.1](#note-tile-matrix-set) |
| geometry | Vector point/line/polygon geometries carried with a coordinate reference system. | Geospatial | No | [§3.1](#note-geometry) |
| dsg | Ragged-array grouping of variable-length features into 1-D arrays, with a feature-type vocabulary layered on top. | Domain-agnostic mechanism; geospatial vocabulary | No | [§3.1](#note-dsg) |
| mesh | Node/edge/face connectivity topology for unstructured meshes. | Domain-agnostic mechanism; geospatial vocabulary | No | [§3.1](#note-mesh) |
| parametric-vertical | Vertical coordinates derived from stored formula terms (e.g., sigma and hybrid coordinates). | Geospatial | No | [§3.1](#note-parametric-vertical) |
| cell-methods | Statistical provenance of values (e.g., mean, maximum, or sum over an axis), with climatological statistics layered on top. | Domain-agnostic mechanism; geospatial vocabulary | No | [§3.1](#note-cell-methods) |
| cell-measures | Associates per-cell area or volume measures for weighting and aggregation. | Domain-agnostic | No | [§3.1](#note-cell-measures) |
| labels | String-valued auxiliary coordinates (per-element axis labels); may be folded into the coordinates convention. | Domain-agnostic | No | [§3.1](#note-labels) |
| domain | A data-less descriptor of a coordinate/dimension domain, with no accompanying data array. | Domain-agnostic | No | [§3.1](#note-domain) |
| ref | Linkage to external and ancillary variables, including externally stored measures and aggregation. | Domain-agnostic | Proposed | [§3.1](#note-ref) |

**Division of change control.** The conventions remain the authoritative source of truth in their respective repositories, governed within the Zarr Conventions Framework community. The GeoZarr SWG owns the selection of conventions, the integration rules, and the conformance classes; it does not fork or independently amend convention content. Technical changes arising from OGC review (including OGC Architecture Board review and public comment) that affect convention content are proposed upstream as issues or pull requests to the relevant convention repository, and are taken up by GeoZarr through a subsequent pinned convention version, not by editing the OGC document alone.


### 3.1. Statement of relationship of planned work to the current OGC Standards baseline

<!--
This section describes the relationship of the proposed standards activity to the existing Standards baseline. For the 3 cases:
If defining a new Standard, a statement of the relationship to the existing Standards baseline including statements related to overlap (if any) with existing OGC Standards functionality, harmonization issues, and so forth.

If processing change requests and performing a revision to an existing Standard, a simple statement to this effect shall be made.

If processing a draft submission of a specification developed outside the OGC process, a clear statement of the relationship to the existing Standards baseline including statements related to overlap (if any) with existing OGC Standards functionality, harmonization issues, and so forth. This information is provided to allow a focus of the discussion on criteria for considering any new solution that may be incompatible with older ones, overlaps existing functionality in the current baseline, and criteria for either deprecating older solutions, or simultaneously endorsing more than one option.
-->

GeoZarr builds directly on several elements of the OGC Standards baseline: the Zarr community standard (OGC 21-050r1, endorsed June 2022); the netCDF encoding standard (OGC 10-090r3) together with the CF (Climate and Forecast) Metadata Conventions, whose standardization is being advanced by the NetCDF CF SWG; GeoTIFF (OGC 19-008r4) and Cloud Optimized GeoTIFF (OGC 21-026); the OGC Two Dimensional Tile Matrix Set standard; and OGC Abstract Specification Topic 21 (Discrete Global Grid Systems). GeoZarr duplicates none of these; it standardizes how the concepts they encode are expressed as composable, safely-ignorable Zarr conventions, so that data now published in netCDF/CF or GeoTIFF/COG can carry the same semantics in Zarr.

Among these prior standards, CF is the most comprehensive metadata model for n-dimensional geospatial arrays, so the SWG uses a systematic decomposition of CF capabilities as the completeness test for the anticipated convention set; the GeoTIFF/COG capability set (affine georeferencing, coordinate reference system metadata, overviews, and sentinel nodata values) maps onto a small subset of the same conventions. The organizing test comes from the Zarr Conventions framework's safely-ignorable contract: if a low-level Zarr implementation ignores a convention, it still obtains the correct array element values. Features that fail this test change how data is encoded rather than how it is interpreted; they belong in the Zarr codec and data-type layer rather than in GeoZarr conventions and are out of scope (see Section 3.2).

The following notes map each convention in the Section 3 table to the prior standards and specifications it draws on:

- <a id="note-coordinates"></a>**coordinates** — The coordinate association core of CF §4–§6: the `coordinates` attribute linking data to coordinate and auxiliary-coordinate variables; 1-D, scalar, and multidimensional coordinates; alternative coordinate sets; and discrete/ordinal axes.
- <a id="note-units"></a>**units** — CF `units` (UDUNITS strings), dimensionless units, and `units_metadata` (e.g., temperature on-scale vs. difference).
- <a id="note-calendar"></a>**calendar** — The CF `"<unit> since <epoch>"` reference-time decoding, the `calendar` attribute, custom calendars (`month_lengths`, `leap_year`, `leap_month`), and leap-second handling (CF Appendix M). Stored time numbers are unchanged; only the number-to-datetime mapping is conventional.
- <a id="note-flags"></a>**flags** — CF `flag_values` (enumerations), `flag_masks` (bitfields), and `flag_meanings`.
- <a id="note-missing-data"></a>**missing-data** — CF `missing_value`, `valid_range` / `valid_min` / `valid_max`, `actual_range`, and treat-sentinel-as-masked semantics; GeoTIFF/COG nodata values share the same sentinel model. `_FillValue` itself is covered by the core Zarr `fill_value` field (see Section 3.2).
- <a id="note-cell-measures"></a>**cell-measures** — The CF `cell_measures` per-cell area/volume association.
- <a id="note-labels"></a>**labels** — CF string-valued auxiliary coordinates providing per-element axis labels.
- <a id="note-domain"></a>**domain** — The data-less CF domain variable: a coordinate/dimension descriptor with no data array.
- <a id="note-ref"></a>**ref** — CF `external_variables`, externally stored `cell_measures`, and `ancillary_variables` linkage; also the natural home for aggregation mechanisms.
- <a id="note-multiscales"></a>**multiscales** — Cloud Optimized GeoTIFF overviews are the primary prior art. Not a CF feature, but provides the per-level coordinate composition that any CF-derived multiresolution pyramid needs.
- <a id="note-dsg"></a>**dsg** — The domain-agnostic mechanism covers CF §9 ragged arrays (`count` / `index` variables); the geospatial vocabulary is the `featureType` taxonomy (trajectory, profile, timeSeries, and so forth).
- <a id="note-mesh"></a>**mesh** — The domain-agnostic mechanism covers UGRID-style node/edge/face connectivity arrays (CF Appendix K); node coordinates are typically supplied via the geolocation convention.
- <a id="note-cell-methods"></a>**cell-methods** — The domain-agnostic mechanism covers CF `cell_methods` and the Appendix E vocabulary; the geospatial vocabulary is climatological statistics (`within` / `over` years or days, `climatology` bounds).
- <a id="note-registration"></a>**CF registration** — The domain-agnostic mechanism declares unprefixed CF attributes in use (e.g., `long_name` and provenance attributes such as `title`, `history`, `source`); the geospatial vocabulary is the `standard_name` table.
- <a id="note-proj"></a>**proj** — Dual heritage: GeoTIFF GeoKeys (OGC 19-008r4) and CF Appendix F grid mappings (the `grid_mapping` linkage, `crs_wkt`, vertical datums). Both vocabularies become importable aliases for the EPSG, WKT2, and PROJJSON forms.
- <a id="note-spatial"></a>**spatial** — The GeoTIFF georeferencing model (OGC 19-008r4): 2-D X/Y affine georeferencing of a regular grid via a geotransform. CF has no affine mechanism — it georeferences through explicit coordinate arrays — which is why this convention stands apart from the coordinates convention.
- <a id="note-geolocation"></a>**geolocation** — CF 2-D curvilinear `lat(y,x)` / `lon(y,x)` coordinates, rotated-pole grids, and swath geolocation arrays.
- <a id="note-geometry"></a>**geometry** — CF §7.5 geometries: `geometry_container`, `node_coordinates`, `node_count`, `part_node_count`, and `interior_ring`, carried with a coordinate reference system.
- <a id="note-parametric-vertical"></a>**parametric-vertical** — CF `formula_terms`, `computed_standard_name`, and the Appendix D parametric vertical coordinate formulas. The derived vertical coordinate is virtual; every stored term array is independently correct, which is why this is a convention rather than a codec.
- <a id="note-dggs"></a>**dggs** — OGC Abstract Specification Topic 21 (Discrete Global Grid Systems). Not represented in CF or GeoTIFF; a Zarr convention proposal and the xdggs community library are the current prior art.
- <a id="note-tile-matrix-set"></a>**tile-matrix-set** — The OGC Two Dimensional Tile Matrix Set standard. Complements the domain-agnostic multiscales convention by binding resolution levels to registered tile matrix sets for web-tiling clients.

### 3.2. What is out of scope?

<!--
A short description of any activities that will be out of scope for the SWG. For example, a SWG may limit consideration of CRPs after a specified date or milestone.
-->

Several components of the CF encoding model fit better as core zarr extensions rather than GeoZarr conventions, because they are domain agnostic and/or must be understood by core Zarr implementations (e.g., Zarr-Python, tensorstore, zarrs). These include:

- Packing (e.g., `scale_factor`,`add_offset`): This CF feature is best represented by a Zarr codec, because this information changes the data types and values of an array.
- `_FillValue`: This CF feature is redundant with the zarr metadata field `fill_value`, which defines the value to be used for uninitialized portions of the array.

Also out of scope:

- Development of Zarr core, codecs, and data types: these belong to the Zarr community's specification and extension processes (e.g., Zarr Enhancement Proposals), which the SWG tracks but does not govern.
- Blocking on upstream changes: where the SWG proposes improvements to the CF conventions or the Zarr Conventions Framework, GeoZarr deliverables do not wait on the acceptance of those proposals.

### 3.3. Specific existing work used as starting point

<!--
This section provides reference information relevant to the work of the SWG. For example, a document reference for a draft submission or a list of CRPs for a SWG focused on revision to an adopted specification.
-->

The SWG starts from work already published or in progress in the Zarr and GeoZarr communities:

- The `spatial`, `proj`, and `multiscales` conventions — the Version 1 suite (https://github.com/zarr-conventions/spatial, https://github.com/zarr-conventions/proj, https://github.com/zarr-conventions/multiscales).
- The Zarr Conventions framework specification (https://github.com/zarr-conventions/zarr-conventions-spec), which defines the `zarr_conventions` attribute and the safely-ignorable contract.
- The prior GeoZarr editor's draft and issue history (https://github.com/zarr-developers/geozarr-spec), the starting point cited by the 2023 charter (OGC 23-046).
- The geozarr-toolkit validation tooling and data models (https://github.com/zarr-developers/geozarr-toolkit).
- geozarr.org, which documents the conventions, roadmap, and implementation matrix.

### 3.4. Is this a persistent SWG

- [x] YES
- [ ] NO

### 3.5. When can the SWG be inactivated

<!--
If this is not a persistent SWG, please define the criteria for determining when the SWG can be inactivated and the project archived. Please note that completion and archiving ensures that all files, wikis, emails, and so forth are archived and available for future viewing and use.
-->

The SWG is persistent. It can be inactivated once the SWG identifies no new tasks and there are no open Change Requests against the adopted GeoZarr Standard.

## 4. Description of deliverables

<!--
This section describes what the deliverables will be for this SWG activity. Deliverables could be a revision to an existing Standard, including revisions to schemas. A deliverable could also be a best practices document.

This section also includes a preliminary schedule of activities. For example, an RFC focused SWG schedule would provide a plan and schedule that includes the start date, target date for release of the candidate Standard for public review, date for consolidation of comments, date for edits to document based on comments, and a final target date for making a recommendation to the Membership. This information will be made public and will also be used as input to a RoadMap for the document. Therefore, the more detail the better.
-->

### 4.1. Initial deliverables

<!--
Describe the initial Standard(s) to be developed by the SWG.
-->

The initial deliverable (primary delivery) is **GeoZarr Version 1**, a candidate Standard comprising:

- **The GeoZarr specification** — a profile document that selects the Version 1 convention suite (`spatial`, `proj`, and `multiscales`; see Section 3), defines the integration rules for using the conventions together, and defines conformance classes against the suite — anticipated as one conformance class per selected convention plus a core class governing their integration, so that conformance can be claimed and tested per convention. The subset of classes the specification designates as required constitutes the minimal GeoZarr identified in Section 1. Normative statements about how to encode a given concern remain in the referenced conventions; the specification references them at pinned versions rather than duplicating them.
- **An abstract test suite** for the conformance classes, accompanied by executable test scripts contributed toward the OGC compliance program.

Preliminary schedule, to be refined by the SWG:

| Milestone | Target |
|---|---|
| Release candidate of the Version 1 convention suite | 2026 Q3 |
| OGC Architecture Board review | 2026 Q3 |
| Public comment period and comment resolution | 2026 Q4 |
| SWG vote to recommend adoption; TC adoption vote | 2026 Q4 |

### 4.2. Additional SWG tasks

<!--
Describe each additional Standard to be developed by the SWG as an additional task after the deliverables from the initial charter have been completed. This section is blank in a new charter, then is populated with each task approval request per the OGC TC Policies and Procedures.
-->

No additional tasks are chartered at this time. Subsequent GeoZarr versions outlined in Section 3 — beginning with the proposed Version 2 coordinate and CF-alignment layer — will each be proposed through the SWG Task approval process defined in the OGC TC Policies and Procedures; approved Tasks will be added to this charter. Each Task proposal will include the evidence of real-world need described in Sections 1 and 3, which also serves as the technical justification the Task approval process presents to the TC.

## 5. IPR Policy for this SWG

- [x] RAND-Royalty Free
- [ ] RAND for fee

## 6. Anticipated audience / participants

<!--
Description of the target participants in this SWG. For example, if the SWG were focused on a candidate spatial query language standard: Those involved in the design, development, implementation, or use of elements listed above in "Scope of the Work". This includes search service providers, prospective users of search services exposed as XML, information architects and bibliographic, metadata, and content provider.

This is not meant as a limiting statement but instead is intended to provide guidance to interested potential participants as to whether they wish to participate in this SWG.
-->

This SWG develops a Standard for general use in the geospatial community and for data exchange beyond it. Anticipated participants include: geospatial data providers publishing gridded and multidimensional products to cloud object storage, including Earth observation agencies and programs producing analysis-ready satellite data; implementers of geospatial software and libraries, such as GDAL, xarray and rioxarray, QGIS, web visualization toolkits, and tiling services; operators of cloud data platforms and catalogs; and organizations that procure or contract for geospatial data delivery and need conformance classes to cite as evaluation criteria.

## 7. Domain Working Group endorsement

<!--
The SWG will list all Domain Working Groups (DWGs) in which the SWG formation was discussed and/or chartered. If a DWG has specifically endorsed the formation of the SWG, then a statement of endorsement should be included.
-->

<!-- TODO(blocking): Identify the home DWG and obtain its approval vote BEFORE this charter goes to vote (TC PnP §4.13.1 requires the home DWG to approve the relationship and be identified here prior to charter approval). Confirm current parent-DWG status with Scott Simmons. -->

&lt;Home DWG to be identified; the home DWG's approval of the relationship is required prior to approval of this charter.&gt;

## 8. Other informative information about the work of this SWG

### 8.1. Collaboration

<!--
Describe the work environment of the SWG, including the use of GitHub or GitLab.
-->

All work of the SWG is public. Standard development takes place in public GitHub repositories under the `zarr-conventions` and `zarr-developers` organizations, using issues and pull requests as the record of technical discussion and decisions. Discussions are mirrored between the OGC Agora platform and GitHub so that OGC members and public contributors see the same material; non-members are encouraged to comment, while votes are limited to SWG voting members.

Repository content is permissively licensed (e.g., CC-BY 4.0); the compiled Standard published by OGC carries the OGC document license and IPR statement, with referenced permissively licensed content acknowledged on the document cover. A contribution statement in the repository governs contributions, and participants in SWG meetings contribute under that statement.

### 8.2. Similar or applicable standards work (OGC and elsewhere)

<!--
The following Standards and projects may be relevant to the SWG's planned work, although none currently provide the functionality anticipated by this committee's deliverables:

OASIS BPEL
IETF HTTP

The SWG intends to seek and if possible maintain liaison with each of the organizations maintaining the above works.
-->

- The OGC NetCDF CF SWG, which is advancing standardization of the CF Metadata Conventions; the GeoZarr SWG maintains a liaison with this group given the shared metadata model (see Section 3.1).
- The OGC GeoDataCube SWG: GeoDataCube specifies service APIs, while GeoZarr defines a cloud-native encoding that such services can serve; coordination between the groups continues.
- The Zarr community's specification and conventions governance (Zarr Enhancement Proposals and the Zarr Conventions Framework), where the core format and the domain-agnostic conventions are governed.
- The STAC (SpatioTemporal Asset Catalog) specification, commonly used for discovery of the assets that GeoZarr encodes.
- The xdggs community library and related DGGS activities, prior art for the prospective dggs convention.

The SWG intends to seek and, where possible, maintain liaison with each of the organizations maintaining the above works.

### 8.3. Details of first meeting

<!--
Example:
The first meeting of the SWG will be held by telephone conference call at 10AM EDT on 1 October 2007. Call-in information will be provided to the SWG's e-mail list and on the portal calendar in advance of the meeting.
-->

The first meeting under the revised charter will be held by web conference within four weeks of charter approval, announced in the SWG's Agora space and on the public meeting calendar.

### 8.4. Projected on-going meeting schedule

<!--
Example:
The work of the SWG will be carried out primarily by email and conference calls, possibly every two weeks, with face-to-face meetings perhaps at each of the OGC TC meetings.
-->

The work of this SWG is carried out primarily on GitHub and via email, web conferences, and sessions at OGC Member Meetings as agreed by the SWG members. Web conferences are scheduled regularly and announced in advance; meetings are open to public participation per the SWG's public-engagement decision. Voting on GeoZarr content is limited to SWG voting members.

### 8.5. Supporters of this Charter

The following people support this proposal and are committed to the Charter and projected meeting schedule. These members are known as SWG Founding or Charter members. The charter members agree to the SoW and IPR terms as defined in this charter. The charter members have voting rights beginning the day the SWG is officially formed. Charter Members are shown on the public SWG page. Extend the table as necessary.

| Name | Organization |
|------|--------------|
|      |              |

### 8.6. Conveners

<!--
Name of individual(s) who started the SWG process. Could be the lead for an RFC submission, an OGC staff person, or an individual who believes it is time for a revision to an adopted Standard.
-->

Max Jones (Development Seed), GeoZarr SWG chair, convener of this re-chartering.

## 9. References

<!--
Optional list of references.
-->

- OGC 21-050r1, Zarr Storage Specification 2.0 Community Standard
- OGC 10-090r3, OGC Network Common Data Form (netCDF) Core Encoding Standard, version 1.0
- OGC 19-008r4, OGC GeoTIFF Standard, version 1.1
- OGC 21-026, Cloud Optimized GeoTIFF Standard
- CF Metadata Conventions, https://cfconventions.org
- Zarr specification, version 3, https://zarr-specs.readthedocs.io
- Zarr Conventions framework specification, https://github.com/zarr-conventions/zarr-conventions-spec
