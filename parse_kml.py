#!/usr/bin/env python3
"""Parse fire_lookouts.kml and extract tower data to GeoJSON."""

import xml.etree.ElementTree as ET
import json
import sys

KML_NS = "{http://www.opengis.net/kml/2.2}"


def parse_kml(kml_path):
    tree = ET.parse(kml_path)
    root = tree.getroot()

    features = []
    for placemark in root.iter(f"{KML_NS}Placemark"):
        name_el = placemark.find(f"{KML_NS}name")
        name = name_el.text if name_el is not None else "Unknown"

        coords_el = placemark.find(f".//{KML_NS}coordinates")
        if coords_el is None:
            continue
        parts = coords_el.text.strip().split(",")
        lon, lat = float(parts[0]), float(parts[1])

        # Extract extended data (SimpleData elements are in the KML namespace)
        props = {"name": name}
        for sd in placemark.iter(f"{KML_NS}SimpleData"):
            field = sd.get("name")
            val = sd.text
            if field and val:
                props[field] = val

        # Parse elevation and viewpoint height as numbers
        ele = None
        if "ele" in props:
            try:
                ele = float(props["ele"])
            except ValueError:
                pass
        props["elevation_m"] = ele

        vp_height = 15.0  # default tower height
        if "height:viewpoint" in props:
            try:
                vp_height = float(props["height:viewpoint"])
            except ValueError:
                pass
        elif "height" in props:
            try:
                vp_height = float(props["height"])
            except ValueError:
                pass
        props["viewpoint_height_m"] = vp_height

        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [lon, lat]},
            "properties": props,
        })

    return {"type": "FeatureCollection", "features": features}


if __name__ == "__main__":
    kml_path = sys.argv[1] if len(sys.argv) > 1 else "/Users/joaopmgoncalves/Downloads/fire_lookouts.kml"
    geojson = parse_kml(kml_path)
    print(f"Parsed {len(geojson['features'])} towers", file=sys.stderr)

    # Report stats
    with_ele = sum(1 for f in geojson["features"] if f["properties"]["elevation_m"] is not None)
    print(f"  {with_ele} have elevation data", file=sys.stderr)

    out_path = "towers.geojson"
    with open(out_path, "w") as f:
        json.dump(geojson, f, indent=2)
    print(f"Written to {out_path}", file=sys.stderr)
