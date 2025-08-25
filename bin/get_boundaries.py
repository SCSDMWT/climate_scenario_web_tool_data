# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "geopandas",
#     "requests",
# ]
# ///


import geopandas as gpd
import os
import requests


def get_wfs(filename, url, output_dir='boundaries', cache_dir='.tmp'):
    '''Read a file from a WFS source and convert it to GeoJSON'''
    output_file = os.path.join(output_dir, filename)
    if os.path.exists(output_file):
        print(f'Skipping existing file: {output_file}')
        return
    
    #r = requests.get(url)
    #if not r.status_code == 200:
    #    print(f'Could not retrieve data: {r.status_code}')
    #    return

    #tmp_filename = os.path.join(cache_dir, filename)
    #with open(tmp_filename, 'w') as file:
    #    file.write(r.text)

    print(f'Downloading: {output_file}')
    gdf = gpd.read_file(url)
    print(f'Saving: {output_file}')
    with open(output_file, 'w') as file:
        file.write(gdf.to_json())

def main():

    boundaries = [
        ('local_council.json', 'https://geo.spatialhub.scot/geoserver/sh_las/wfs?authkey=b85aa063-d598-4582-8e45-e7e6048718fc&request=GetFeature&service=WFS&version=1.1.0&outputFormat=application%2Fjson&typeName=pub_las'),
        ('fire_rescue.json', 'https://maps.gov.scot/server/services/ScotGov/CrimeJusticeSafety/MapServer/WFSServer?typename=CJS:ScottishFireRescue&request=GetFeature&service=WFS&version=1.1.0'),
        #('police.json', 'https://maps.gov.scot/server/services/ScotGov/CrimeJusticeSafety/MapServer/WFSServer?typename=CJS:ScottishPoliceDivisions&request=GetFeature&service=WFS&version=1.1.0'),
        ('health_integration_authorities.json', 'https://maps.gov.scot/server/services/ScotGov/HealthSocialCare/MapServer/WFSServer?request=GetFeature&service=WFS&version=1.1.0&outputFormat=GML3&typeName=HSC:HealthIntegrationAuthorities'),
        ('health_boards.json', 'https://maps.gov.scot/server/services/ScotGov/HealthSocialCare/MapServer/WFSServer?request=GetFeature&service=WFS&version=1.1.0&outputFormat=GML3&typeName=HSC:HealthIntegrationAuthorities'),
    ]

    for filename, url in boundaries:
        get_wfs(filename, url)

    

if __name__ == "__main__":
    main()
