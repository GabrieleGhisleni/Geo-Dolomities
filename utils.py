from folium import GeoJson, GeoJsonTooltip, Map, TileLayer, Element
from shapely.geometry.polygon import Polygon
from folium.map import LayerControl
from typing import Tuple
import geopandas as gpd
import pandas as pd
import networkx
import shapely

TAB_10 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
c_colors = ['purple', 'pink', 'cadetblue', 'lightgreen', 'orange', 'darkgreen', 'cadetblue', 'purple', 'pink']


def get_new_map(
    tiles='OpenStreetMap', 
    title=None
  ):
  # center = italy_regions.to_crs(epsg=32632).loc[italy_regions.DEN_REG == 'Trentino-Alto Adige'].centroid
  # center_xy = [i[0] for i in center.to_crs(epsg=4326).values[0].xy]
  # center_xy.reverse() #flip xy (end up in africa :P)
  # center_xy[1] = center_xy[1] + .6
  # [i[0] for i in center.to_crs(epsg=4326).values[0].xy].reverse()
  f_map = Map(
    location = [46.44053471584184, 11.87983020957817], 
    tiles = tiles, 
    zoom_start = 9,
  )

  if title:
    title_html = f"""<h3 align="center" style="font-size:16px"><b>{title}</b></h3>"""
    f_map.get_root().html.add_child(Element(title_html))
  
  return f_map
  
def add_map_infos(
    feature_layers: dict,
     _map: Map, 
     collapsed_legend: bool = True
  ) -> Map:

  # add layers to map
  feature_layers['dolomiti_area'].add_to(_map)
  [feature.add_to(_map) for key, feature in feature_layers.items() if key != 'dolomiti_area']
  # add tiles 
  TileLayer('Stamen Terrain').add_to(_map)
  TileLayer('Stamen Toner').add_to(_map)
  TileLayer('Stamen Water Color').add_to(_map)
  TileLayer('cartodbpositron').add_to(_map)
  TileLayer('OpenStreetMap').add_to(_map)
  LayerControl(collapsed=collapsed_legend).add_to(_map)
  _map.fit_bounds(_map.get_bounds())
  return _map


def element_crosses_or_within_area(
    obs: shapely.geometry.linestring.LineString, 
    reg: pd.DataFrame, 
    col_to_return: str
  ) -> str or None:
  
  for idx, area in reg.iterrows():
    if (
        obs.crosses(area.geometry) or 
        obs.within(area.geometry) 
      ):
      return area[col_to_return]
  return None


def get_info_from_row(row: pd.Series) -> str:
  info = [
          f"{k}: {v}" 
          for k,v in row.to_dict().items() 
          if v and k != 'geometry' and k != 'point' and k != 'path'
        ]
  return '<br/>'.join(info)


def load_centroid_in_graph_common_city(
    G: networkx.classes.multidigraph.MultiDiGraph,
    cities:list = ['Trento', 'Bolzano']
  ) -> dict:
  "return the nodes in the graph"
  
  import osmnx  as ox
  
  res = {}
  Trento = (11.121597, 46.065489)
  Bolzano = (11.346474, 46.492602)

  res['Bolzano'] = ox.nearest_nodes(G, Bolzano[0], Bolzano[1])
  res['Trento'] = ox.nearest_nodes(G, Trento[0], Trento[1])
  return res


def load_italian_north_east_area() -> Tuple[gpd.GeoDataFrame]:
  selected_regions = ['Veneto', 'Trentino-Alto Adige', 'Friuli Venezia Giulia']

  italy_regions = gpd.read_file("data/istat_administrative.gpkg", layer="regions", epsg="EPSG:4326")
  dolomiti_regions = italy_regions.loc[italy_regions.DEN_REG.isin(selected_regions)]

  codice_regioni = dolomiti_regions.COD_REG.unique()

  italy_provincies = gpd.read_file("data/istat_administrative.gpkg", layer="provincies", epsg="EPSG:4326")
  dolomiti_provincies = italy_provincies.loc[italy_provincies.COD_REG.isin(codice_regioni)]

  italy_municipalities = gpd.read_file("data/istat_administrative.gpkg", layer="municipalities", epsg="EPSG:4326")
  dolomiti_municipalities = italy_municipalities.loc[italy_municipalities.COD_REG.isin(codice_regioni)]

  return dolomiti_regions.to_crs(epsg=4326), dolomiti_provincies.to_crs(epsg=4326), dolomiti_municipalities.to_crs(epsg=4326)
###########################################
def element_crosses_within_or_overlaps_area(obs, reg, col_to_return):
  for idx, area in reg.iterrows():
    if obs.crosses(area.geometry) or obs.within(area.geometry) or obs.overlaps(area.geometry):
      return area[col_to_return]


def element_within_area(obs, reg, col_to_return):
  for idx, area in reg.iterrows():
    if obs.within(area.geometry):
      return area[col_to_return]
      



def load_centroid_in_graph_common_city(
    G,
     dolomiti_municipalities, 
     cities=['Trento', 'Bolzano']
  ) -> dict:
  "return the nodes in the graph"
  
  res = {}
  for city in cities:
    area_city = dolomiti_municipalities.loc[dolomiti_municipalities.COMUNE == city].geometry.values[0]
    res[city] = ox.nearest_nodes(G, 
                                   [i[0] for i in area_city.centroid.xy][0],
                                   [i[0] for i in area_city.centroid.xy][1]
                                  )
  
  return res
  
def from_poly_to_point(obs):
  if type(obs) == Polygon:
    obs = obs.centroid
  return obs


def expand_raw_geocode(address_list):
  res = []
  for idx, row_ in address_list.iterrows():
    extra_tag = row_['extratags']
    row = row_['address'] 
    res.append(
      dict(
        municipality = row['municipality']  if 'municipality' in row else row['village'] if 'village' in row else None,
        county = row['county'],
        state = row['state'],
        road_name = row['road']  if 'road' in row else row['locality'] if 'locality' in row else None,
        extended_name = row['amenity']  if 'amenity' in row  else row['tourism'] if 'tourism' in row else None,

        opening_hours = extra_tag["opening_hours"] if 'opening_hours' in extra_tag else None,
        contact_mobile = extra_tag["contact:mobile"] if 'contact:mobile' in extra_tag else None,
        winter_room = extra_tag["winter_room"] if 'winter_room' in extra_tag else None,
        capacity = extra_tag["capacity"] if 'capacity' in extra_tag else None,
        website = extra_tag["website"] if 'website' in extra_tag else None,
        email = extra_tag["email"] if 'email' in extra_tag else None,

        boundingbox = row_['boundingbox'],
        display_name = row_['display_name'],
        type_description = row_['type'],
        geometry = gpd.points_from_xy([row_['lon']], [row_['lat']])[0]
      )
    )
  
  return gpd.GeoDataFrame(res,crs='EPSG:4326')


def check_geom(geom, regions_df):
  res = []
  for idx, region in regions_df.iterrows():
    if (
      geom.within(region.geometry) or 
      geom.overlaps(region.geometry) or 
      geom.touches(region.geometry)
    ): 
      res.append(region['name'])
  return ','.join(res)


# ad hoc readjustment names
names_adj = {
  'Rifugio Mandron': 'Rifugio Mandrone',
  'Rifugio Tosa e Pedrotti' : 'Rifugio Tosa',
  'Rifugio Cremona': 'Rifugio Cremona alla Stua',
  'Rifugio Velo della Madonna': 'Rifugio Pradidali',
  'Rifugio Tuckett e Sella': 'Rifugio Tuckett',
  'Rifugio Oltradige al Roen': 'Rifugio Oltradige',
  
  'Rifugio Settimo Alpini': 'Rifugio 7° alpini',
  'Rifugio Città  di Schio': 'Rifugio Schio',
  'Rifugio Città  di Mestre' : 'Rifugio Pietro Galassi',
  'Rifugio Tiziano' : 'Bivacco Dino e Plinio',
  'Rifugio Giussani': 'Camillo Giussani'
}