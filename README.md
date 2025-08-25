# Data for the Web Tool

A git LFS repository to hold large data files for the 
[Climate Impact Web Tool](https://github.com/SCSDMWT/climate_scenario_web_tool).

## Data Provinance

### Data layers

From [SCSDMWT/prototype_tool_plotting](https://github.com/SCSDMWT/prototype_tool_plotting).

### Region boundaries

 Region boundaries are from various sources on [spatialdata.gov.scot](https://spatialdata.gov.scot):

 * [Local Authority Areas - Scotland](https://spatialdata.gov.scot/geonetwork/srv/eng/catalog.search#/metadata/1cd57ea6-8d6e-412b-a9dd-d1c89a80ad62)
 * [Scottish Fire and Rescue Service](https://spatialdata.gov.scot/geonetwork/srv/eng/catalog.search#/metadata/e7a1bb0c-68c0-46e4-a794-63280644d660)
 * [NHS Health Boards - Scotland](https://spatialdata.gov.scot/geonetwork/srv/api/records/f12c3826-4b4b-40e6-bf4f-77b9ed01dc14)
 * [Health Integration Authorities](https://spatialdata.gov.scot/geonetwork/srv/eng/catalog.search#/metadata/ac5e870f-8fc2-4c21-8b9c-3bd2311a583f)

A script is provided to download WFS data (usually in GML format) and save the boundaries to GeoJSON:
```console
uv run bin/get_boundaries.py
```

Generate the Pooch registry entries for client projects:
```console
md5sum boundaries/*.json | sed -r "s/([a-z0-9]+)\\ \\ (.*)/'\\2': 'md5:\\1',/"
```




