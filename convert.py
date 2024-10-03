import geojson
from geojson import Polygon

# List of (x, y) coordinates
coordinates = [(100.0, 0.0), (101.0, 0.0), (101.0, 1.0), (100.0, 1.0), (100.0, 0.0)]

# Create a GeoJSON Polygon
polygon = Polygon([coordinates])

# Print the GeoJSON Polygon
print(geojson.dumps(polygon, indent=2))
