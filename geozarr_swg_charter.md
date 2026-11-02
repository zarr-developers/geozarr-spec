<!--
Title: OGC GeoZarr Standards Working Group Charter
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

Internal reference number of this OGC® document: YY-nnnrx 

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

The eligibility requirements above apply to SWG voting members. The GeoZarr SWG also has participants who are not OGC members, including members of the Zarr community and wider geospatial communities. These non-OGC member participants take part in the SWG's technical work via its public GitHub repositories (Section 8.1). Non-OGC members may attend SWG meetings as Observers under the OGC SWG Observer Agreement. Observers may comment and make recommendations but do not vote on SWG approvals. Non-OGC members who wish to vote may contact us about joining the OGC. In addition, the public may access some of the resources maintained for each SWG, including the SWG public description, the SWG Charter, Change Requests, and public comments, which will be linked from the SWG's page.

Please feel free to forward this announcement to any other appropriate lists. The OGC is an open standards organization and we encourage your feedback.

## 1. Purpose of the Standards Working Group

<!--
Proposers will describe the purpose of the Standards Working Group and its overall mission in relation to OGC processes, the OGC Standards baseline, and OGC's business plan.
-->

The GeoZarr Standards Working Group (SWG) is chartered to develop a standard and conformance classes for geospatial data stored in the Zarr data format. Zarr specifies a data format for storing arrays and groups in a hierarchical model. The Zarr Conventions Framework enables communities to define and share metadata standards for Zarr data. The Zarr Conventions Framework is lightweight, decentralized, and composable, with its design informed by the successful approach of STAC extensions. The GeoZarr SWG serves several purposes related to the Zarr data format, Zarr conventions, and geospatial data:

- recommend a minimal set of Zarr conventions required to describe geospatial data (i.e., a minimal GeoZarr)
- recommend additional Zarr conventions that are composable with the minimal GeoZarr conventions and add functionality needed for real-world applications (in contrast to supporting hypothetical use cases)
- evaluate the technical merits and maturity (by way of adoption) of Zarr conventions proposed for incorporation into GeoZarr. Conventions so incorporated constitute the *GeoZarr Conventions*
- provide conformance classes against which datasets can be tested for conformance to the GeoZarr Conventions
- evaluate new upstream convention releases for incorporation into future GeoZarr versions, to ensure that the licensing, technical design, and interoperability remain appropriate for inclusion in GeoZarr

The GeoZarr SWG will evaluate the technical merits of proposed Zarr conventions in order to accomplish the purposes listed above. Technical assessment will include, but not be limited to, an evaluation of the composability, simplicity, specificity, demonstrated real-world need, and maturity of the Zarr conventions, where real-world need is documented by the proposer through existing datasets, products, or implementations that require the capability, and maturity can be measured both by signals of adoption and by amount of time that the convention has been stable.

The GeoZarr SWG may recommend improvements to upstream communities where appropriate, including the Zarr Conventions Framework, specific Zarr conventions, STAC extensions, and the CF (Climate and Forecast) Metadata Conventions. The SWG may propose changes through those communities' own governance processes.

## 2. Business value proposition

<!--
This section provides a statement describing the value of this standards activity in relation to the OGC Membership, the geospatial community, and the wider IT community. This statement can be in terms of the interoperability problem being solved, processing Change requests to meet market (and Member requirements), a policy requirement and/or some other business value proposition. The proposition described in this section does not have to be in economic terms.
-->

Zarr is a generic data format for n-dimensional arrays that enables efficient storage and access to data in compressed chunks. Zarr's high performance and portability across local, high-performance computing, and cloud systems has made it increasingly popular across domains, including for geospatial purposes. In June 2022, the OGC endorsed the Zarr storage specification version 2.0 as an OGC community standard (OGC 21-050r1). In January 2024, the OGC announced the formation of the OGC GeoZarr Standards Working Group, with the goal of developing a Zarr encoding for geospatial gridded data in the form of Zarr conventions. The original charter defined Zarr conventions in the context of a draft Zarr Enhancement Proposal. This re-charter aligns the GeoZarr SWG with the stable direction of the broader Zarr community via the Zarr Conventions Framework.

The business value of the GeoZarr standard includes providing data producers with a single target for encoding geospatial data in Zarr and consumers a single target for implementation, backed by the authority of the OGC. Data producers can adopt GeoZarr to ensure data encoded once is readable across the conforming tool ecosystem and understandable in perpetuity. For users, GeoZarr unlocks widespread visualization, subsetting, GIS services, machine learning, and automated and AI-assisted analysis. As GeoZarr enables browser-based approaches, its adoption lowers costs by reducing dependence on back-end services. In addition to these cost- and capability-driven benefits, GeoZarr will provide a target for contract development and evaluation, to ensure any Zarr-backed data and services delivered are widely useful.

GeoZarr standardization offers particularly great value now. While geospatial data has been stored in Zarr informally for a decade, the ad-hoc approach to geospatial metadata has led to bugs, inconsistencies between libraries and languages, and wasted money on development, duplicated storage, and reprocessing. GeoZarr standardization aims to prevent these errors from propagating in the future. Because GeoZarr conventions only add metadata, existing Zarr archives can adopt the standard in place without expensive reprocessing or duplicated storage, while existing Zarr tools continue to work on conformant data.

## 3. Scope of work

### 3.1. General

GeoZarr aims to support a wide variety of geospatial data by encoding their semantics through attribute conventions in Zarr groups and arrays. It currently serves two broad categories of geospatial data: (1) data encoded using the CF (Climate and Forecast) Metadata Conventions in netCDF (climate and forecast model output, ocean models, in-situ observations, and satellite swaths, among others); and (2) data in GeoTIFF and Cloud Optimized GeoTIFF (imagery and other regularly gridded data with affine georeferencing, coordinate reference system metadata, and overviews). GeoZarr aims to eventually support novel and emerging geospatial applications requiring different encodings, such as discrete global grid systems (DGGS) and vector data cubes. GeoZarr will accomplish this by standardizing a set of mature Zarr conventions that are composable such that they can be used together to fulfill the diverse requirements within the geospatial domain.

**Eligibility principle.** A convention is eligible for inclusion in GeoZarr if it describes how geospatial data is interpreted, such as how data relates to a defined coordinate reference frame or the meaning, structure, or provenance of its values. Put another way, we expect all GeoZarr conventions to be safely-ignorable by low-level Zarr implementations. Low-level Zarr implementations must be able to ignore the convention while still obtaining correct array element values. Within that boundary, conventions are evaluated for incorporation against the assessment criteria in Section 1: composability, simplicity, specificity, demonstrated real-world need, and maturity.

**Intended capabilities.**

The table below defines the scope of work for this SWG. The table targets the dominant use cases within the data categories above rather than every conceivable one. Work on capabilities beyond this scope does not necessarily require a re-charter, if the direction is agreed upon by the GeoZarr SWG. Inclusion of a capability in scope does not commit the SWG to delivering it. Deliverables are defined in Section 4 and sequenced through the SWG Task approval process defined in the OGC TC Policies and Procedures.

Each capability is realized by one or more Zarr conventions. The table below deliberately does not name the conventions that will realize each capability, nor the order in which capabilities will be addressed. Conventions are proposed, evaluated against the assessment criteria in Section 1, and incorporated into GeoZarr deliverables through the processes in Section 4. Where more than one candidate convention addresses a capability, the SWG's evaluation process determines which are incorporated. Each capability is classified as **domain-agnostic** (its concepts apply to any n-dimensional array, so the realizing convention belongs to the broader Zarr Conventions Framework and is reusable outside the geospatial domain), **geospatial** (it encodes Earth-referencing, such as a coordinate reference system, planetary coordinate, or geographic feature), or a **domain-agnostic mechanism carrying a geospatial vocabulary**.

The last column records the prior standards and specifications each capability draws on. This prior art is informative only. The prior art documents where a capability comes from and is not binding on how GeoZarr realizes it. A GeoZarr convention may depart from the delineations, vocabularies, or encodings of the prior art where the evaluation process finds that appropriate.

| Capability | Description | Classification | Prior art (non-binding) |
|---|---|---|---|
| Coordinate reference systems | Coordinate reference system description via EPSG code, WKT2, or PROJJSON, including vertical and temporal datums. | Geospatial | Multiple prior implementations, including GeoTIFF GeoKeys (OGC 19-008r4) and CF Appendix F grid mappings ( `grid_mapping` linkage, `crs_wkt`, vertical datums). Both vocabularies become importable aliases for the EPSG, WKT2, and PROJJSON forms. |
| Functional coordinates | Mapping from index space to physical space defined by stored transform parameters (e.g., affine geotransforms), with no stored coordinate arrays. | Geospatial | The GeoTIFF georeferencing model (OGC 19-008r4): 2-D X/Y affine georeferencing of a regular grid via a geotransform. CF has no functional mechanism (it georeferences through explicit coordinate arrays), which is why this capability stands apart from explicit coordinates. |
| Explicit coordinates | Mapping from index space to physical space through stored coordinate arrays: 1-D, scalar, and multidimensional/curvilinear coordinates (including swath geolocation); alternative coordinate sets; discrete/ordinal axes; string-valued labels; and data-less domain descriptions. | Domain-agnostic mechanism; geospatial vocabulary | The coordinate association core of CF §4–§6: the `coordinates` attribute linking data to coordinate and auxiliary-coordinate variables; 1-D, scalar, and multidimensional coordinates (including 2-D curvilinear `lat(y,x)` / `lon(y,x)` coordinates, rotated-pole grids, and swath geolocation arrays); alternative coordinate sets; discrete/ordinal axes; string-valued auxiliary coordinates providing per-element axis labels; and the data-less CF domain variable. |
| Multiresolution pyramids | Resolution levels related by scale/translate transforms over any axis. | Domain-agnostic | Cloud Optimized GeoTIFF overviews (OGC 21-026). |
| Units of measure | Units attached to the values in an array, including dimensionless units and unit metadata. | Domain-agnostic | CF `units` (UDUNITS strings), dimensionless units, and `units_metadata` (e.g., temperature on-scale vs. difference). |
| Time representation | Reference-time-based decoding, calendars, custom calendars, and leap seconds. | Domain-agnostic | The CF `"<unit> since <epoch>"` reference-time decoding, the `calendar` attribute, custom calendars (`month_lengths`, `leap_year`, `leap_month`), and leap-second handling (CF Appendix M). Stored time numbers are unchanged; only the number-to-datetime mapping is conventional. |
| Missing data | Sentinel-value and valid-range masking semantics. | Domain-agnostic | CF `missing_value`, `valid_range` / `valid_min` / `valid_max`, `actual_range`, and treat-sentinel-as-masked semantics; GeoTIFF/COG nodata values share the same sentinel model. `_FillValue` itself is covered by the core Zarr `fill_value` field (see Section 3.3). |
| Value interpretation | Value-to-label interpretation of integer arrays, covering enumerations and bitfields. | Domain-agnostic | CF `flag_values` (enumerations), `flag_masks` (bitfields), and `flag_meanings`. |
| Descriptive metadata | Descriptive names and provenance attributes, and identification of the observed property that the values describe (for example, air temperature at 2 m above the surface) through a controlled vocabulary. | Domain-agnostic mechanism; geospatial vocabulary | The domain-agnostic mechanism declares unprefixed CF attributes in use (e.g., `long_name` and provenance attributes such as `title`, `history`, `source`). The CF `standard_name` table is one observed-property vocabulary; it aggregates property, medium, and sometimes method into a single term, whereas OMS and the I-ADOPT framework describe the observed property from disaggregated components. |
| Observation metadata | How the values were obtained: the observing procedure or method, the observer (sensor, instrument, or model), the feature of interest and any sampling feature the values relate to, and the distinction between phenomenon, result, and valid times. | Domain-agnostic mechanism; geospatial vocabulary | OGC Abstract Specification Topic 20 / ISO 19156:2023, Observations, Measurements and Samples (OMS), and its realizations in the OGC SensorThings API and in CoverageJSON parameter metadata (observed property, observing procedure, and device links). CF covers this only partially, through qualifiers folded into `standard_name`, `cell_methods`, and free-text provenance attributes; GeoTIFF does not represent it. |
| Discrete global grid systems | Mapping between array index space and DGGS zones (cell identifiers and resolution levels). | Geospatial | OGC Abstract Specification Topic 21 (Discrete Global Grid Systems). Not represented in CF or GeoTIFF; a Zarr convention proposal and the xdggs community library are the current prior art. |
| Tile matrix sets | Binding multiresolution levels to registered tile matrix sets for web-tiling clients. | Geospatial | The OGC Two Dimensional Tile Matrix Set standard. Complements the domain-agnostic multiresolution capability by binding resolution levels to registered tile matrix sets for web-tiling clients. |
| Vector geometries | Point/line/polygon geometries carried with a coordinate reference system. | Geospatial | CF §7.5 geometries: `geometry_container`, `node_coordinates`, `node_count`, `part_node_count`, and `interior_ring`, carried with a coordinate reference system. |
| Discrete sampling geometries | Ragged-array grouping of variable-length features into 1-D arrays, with a feature-type vocabulary. | Domain-agnostic mechanism; geospatial vocabulary | The domain-agnostic mechanism covers CF §9 ragged arrays (`count` / `index` variables); the geospatial vocabulary is the `featureType` taxonomy (trajectory, profile, timeSeries, and so forth). |
| Unstructured meshes | Node/edge/face connectivity topology for unstructured meshes. | Domain-agnostic mechanism; geospatial vocabulary | The domain-agnostic mechanism covers UGRID-style node/edge/face connectivity arrays (CF Appendix K); node coordinates are typically supplied via the explicit-coordinates capability. |
| Parametric vertical coordinates | Vertical coordinates derived from stored formula terms (e.g., sigma and hybrid coordinates). | Geospatial | CF `formula_terms`, `computed_standard_name`, and the Appendix D parametric vertical coordinate formulas. The derived vertical coordinate is virtual; every stored term array is independently correct, which is why this is a convention rather than a codec. |
| Statistical provenance | Statistical derivation of values (e.g., mean, maximum, or sum over an axis), with climatological statistics layered on top. | Domain-agnostic mechanism; geospatial vocabulary | The domain-agnostic mechanism covers CF `cell_methods` and the Appendix E vocabulary; the geospatial vocabulary is climatological statistics (`within` / `over` years or days, `climatology` bounds). |
| Cell measures | Per-cell area or volume measures for weighting and aggregation. | Domain-agnostic | The CF `cell_measures` per-cell area/volume association. |
| External linkage | Linkage to external and ancillary variables, including externally stored measures and aggregation. | Domain-agnostic | CF `external_variables`, externally stored `cell_measures`, and `ancillary_variables` linkage; also the natural home for aggregation mechanisms. |

**Integration and interoperability rules.** Beyond the individual capabilities, the SWG defines the rules needed to make conventions work together as consistent, interoperable GeoZarr datasets. This includes integration rules for combining conventions within a store and store-level expectations such as hierarchy layout and metadata consolidation. These rules are expressed in the GeoZarr specification and its conformance classes (Section 4).

**Convention versioning.** Each GeoZarr deliverable normatively references specific, pinned versions of its constituent conventions, consistent with OGC practice for external normative references. The conventions themselves are versioned by their maintainers and are pre-stable (v0.x, with breaking changes permitted) until they reach v1. Evolution of a convention after adoption does not alter an adopted GeoZarr Standard, which continues to reference the pinned versions.

**Division of change control.** The conventions remain the authoritative source of truth in their respective repositories, governed within the Zarr Conventions Framework community. The GeoZarr SWG owns the selection of conventions, the integration rules, and the conformance classes. It does not fork or independently amend convention content. Technical changes arising from OGC review (including OGC Architecture Board review and public comment) that affect convention content are proposed upstream as issues or pull requests to the relevant convention repository, and are taken up by GeoZarr through a subsequent pinned convention version, not by editing the OGC document alone.


### 3.2. Statement of relationship of planned work to the current OGC Standards baseline

GeoZarr builds directly on several elements of the OGC Standards baseline, including the Zarr community standard (OGC 21-050r1, endorsed June 2022); the netCDF encoding standard (OGC 10-090r3) together with the CF (Climate and Forecast) Metadata Conventions, whose standardization is being advanced by the NetCDF CF SWG; GeoTIFF (OGC 19-008r4) and Cloud Optimized GeoTIFF (OGC 21-026); the OGC Two Dimensional Tile Matrix Set standard; OGC Abstract Specification Topic 21 (Discrete Global Grid Systems); and OGC Abstract Specification Topic 20 / ISO 19156:2023, Observations, Measurements and Samples (OMS), for the semantics of how observed values are obtained. GeoZarr duplicates none of these. Instead, GeoZarr standardizes how the concepts they encode are expressed as composable, safely-ignorable Zarr conventions, so that data now published in netCDF/CF or GeoTIFF/COG can carry the same semantics in Zarr.

Among these prior standards, CF is the most comprehensive metadata model for n-dimensional geospatial arrays, so the SWG uses a systematic decomposition of CF capabilities as the completeness test for the scope table in Section 3.1. The GeoTIFF/COG capability set (affine georeferencing, coordinate reference system metadata, overviews, and sentinel nodata values) maps onto a small subset of the same capabilities. OMS contributes the observation-metadata capability. The prior-art column of the table in Section 3.1 records the specific constructs each capability draws on. As stated there, that prior art is non-binding for GeoZarr conventions. Features of these prior standards that control how data is encoded rather than how it is interpreted belong in the Zarr codec and data type layers rather than the GeoZarr conventions and are out of scope (see Section 3.3).

### 3.3. What is out of scope?


Several components of the CF encoding model fit better as core Zarr extensions rather than GeoZarr conventions, because they are domain agnostic and/or must be understood by core Zarr implementations (e.g., Zarr-Python, tensorstore, zarrs). These include:

- Packing (e.g., `scale_factor`, `add_offset`): This CF feature is best represented by a Zarr codec, because this information changes the data types and values of an array.
- `_FillValue`: This CF feature is redundant with the Zarr metadata field `fill_value`, which defines the value to be used for uninitialized portions of the array.

Also out of scope:

- Development of Zarr core, codecs, and data types. These belong to the Zarr community's specification and extension processes (e.g., Zarr Enhancement Proposals), which the SWG tracks but does not govern.
- Waiting on upstream changes. Where the SWG proposes improvements to the CF conventions or the Zarr Conventions Framework, GeoZarr deliverables should not wait on the acceptance of those proposals.

### 3.4. Specific existing work used as starting point

The SWG starts from work already published or in progress in the Zarr and GeoZarr communities:

- The `spatial`, `proj`, and `multiscales` conventions (https://github.com/zarr-conventions/spatial, https://github.com/zarr-conventions/proj, https://github.com/zarr-conventions/multiscales), published in the zarr-conventions organization and implemented by multiple independent libraries. The implementation matrix at geozarr.org documents current support.
- Candidate conventions for the explicit-coordinates capability: the `cs` convention (https://github.com/R-CF/zarr_conventions_cs), at Pilot maturity in the Zarr Conventions Framework with two released implementations by the convention author, and the `coords` convention (https://github.com/christophenoel/zarr-coords), a proposal with one released implementation by an independent developer.
- The Zarr Conventions Framework specification (https://github.com/zarr-conventions/zarr-conventions-spec), which defines the `zarr_conventions` attribute.
- The prior GeoZarr editor's draft and issue history (https://github.com/zarr-developers/geozarr-spec), the starting point cited by the 2023 charter (OGC 23-046).
- The geozarr-toolkit validation tooling and data models (https://github.com/zarr-developers/geozarr-toolkit).
- geozarr.org, which documents the conventions, roadmap, and implementation matrix.

### 3.5. Is this a persistent SWG

- [x] YES
- [ ] NO

### 3.6. When can the SWG be inactivated

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

The initial deliverable (primary delivery) is **GeoZarr Version 1**. Of the capabilities in scope (Section 3.1), Version 1 targets:

- coordinate reference systems
- functional coordinates
- multiresolution pyramids

Together with what core Zarr already provides (chunked storage, compression, and `fill_value`), these are the capabilities needed for the GeoTIFF and Cloud Optimized GeoTIFF family of data, and they are realized by the `spatial`, `proj`, and `multiscales` conventions (Section 3.4). Explicit coordinates are the first additional capability anticipated for a subsequent version. Explicit coordinates are left for a subsequent version because the SWG has not yet converged on a candidate convention. Yet, the GeoZarr SWG recognizes the urgency of explicit coordinate support and will proceed towards consensus simultaneously with finalizing version 1. The Version 1 candidate Standard comprises:

- **The GeoZarr specification** — a profile document that selects the Version 1 convention suite (`spatial`, `proj`, and `multiscales`; see Section 3.4), defines the integration rules for using the conventions together, and defines conformance classes against the suite. This will likely include one conformance class per selected convention plus a core class governing their integration, so that conformance can be claimed and tested per convention. The subset of classes the specification designates as required constitutes the minimal GeoZarr identified in Section 1. Normative statements about how to encode a given concern remain in the referenced conventions. The specification references them at pinned versions rather than duplicating them. The specification also carries informative guidance that maps common application domains (for example, georeferenced imagery) to the recommended combination of conventions, so that data producers can select conventions without evaluating each one in isolation.
- **An abstract test suite** for the conformance classes, accompanied by executable test scripts contributed toward the OGC compliance program.

Preliminary schedule, to be refined by the SWG:

| Milestone | Target |
|---|---|
| Re-charter approval | November 2026 |
| Release candidate of the Version 1 convention suite | December 2026 |
| OGC Architecture Board review | January 2027 |
| Public comment period and comment resolution | February - March 2027 |
| SWG vote to recommend adoption; TC adoption vote | April 2027 |
| Evaluating explicit coordinates approaches and suggesting upstream changes | November 2026 - February 2027 |

### 4.2. Additional SWG tasks


Additional tasks following the V1 release will include supporting the development of conventions for capabilities such as those listed in Section 3.1, evaluating conventions for incorporation into GeoZarr, and developing conformance classes for incorporated GeoZarr conventions.

## 5. IPR Policy for this SWG

- [x] RAND-Royalty Free
- [ ] RAND for fee

## 6. Anticipated audience / participants

This SWG develops a Standard for general use in the geospatial community and for data exchange beyond it. Anticipated participants include geospatial data providers publishing gridded and multidimensional products to cloud object storage, including Earth observation agencies and programs producing analysis-ready satellite data; implementers of geospatial software and libraries, such as GDAL, xarray and rioxarray, QGIS, web visualization toolkits, and tiling services; operators of cloud data platforms and catalogs; and organizations that procure or contract for geospatial data delivery and need conformance classes to cite as evaluation criteria.

## 7. Domain Working Group endorsement


The SWG convenors will discuss the charter with potentially interested Domain Working Groups (DWGs) at the first opportunity.

## 8. Other informative information about the work of this SWG

### 8.1. Collaboration

All work of the SWG is public. Standard development takes place in public GitHub repositories under the `zarr-conventions` and `zarr-developers` organizations, using issues and pull requests as the record of technical discussion and decisions. Discussions are mirrored between the OGC Agora platform and GitHub so that OGC members and public contributors see the same material. Non-members are encouraged to comment, while votes are limited to SWG voting members.

Repository content is permissively licensed (e.g., CC-BY 4.0). The compiled Standard published by OGC carries the OGC document license and IPR statement, with referenced permissively licensed content acknowledged on the document cover. A contribution statement in the repository governs contributions, and participants in SWG meetings contribute under that statement.

### 8.2. Similar or applicable standards work (OGC and elsewhere)


- The OGC NetCDF CF SWG, which is advancing standardization of the CF Metadata Conventions; the GeoZarr SWG maintains a liaison with this group given the shared metadata model (see Section 3.2).
- The OGC GeoDataCube SWG: GeoDataCube specifies service APIs, while GeoZarr defines a cloud-native encoding that such services can serve; coordination between the groups continues.
- The Zarr community's specification and conventions governance (Zarr Enhancement Proposals and the Zarr Conventions Framework), where the core format and the domain-agnostic conventions are governed.
- The STAC (SpatioTemporal Asset Catalog) specification, commonly used for discovery of the assets that GeoZarr encodes.
- The xdggs community library and related DGGS activities, prior art for the prospective dggs convention.
- OGC Abstract Specification Topic 20 / ISO 19156:2023, Observations, Measurements and Samples (OMS), with the OGC SensorThings API and the I-ADOPT framework for observable properties: prior art for the observation-metadata and descriptive-metadata capabilities (Section 3.1). The SWG anticipates that OMS semantics will be realized as a separate, composable convention developed with the OMS community and proposed to the SWG for evaluation, rather than by changes to the GeoZarr core.

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
| Max Jones | Development Seed |

### 8.6. Conveners


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
- Zarr Conventions Framework specification, https://github.com/zarr-conventions/zarr-conventions-spec
