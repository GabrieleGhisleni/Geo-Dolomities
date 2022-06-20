
TAB_10 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
c_colors = ['purple', 'pink', 'cadetblue', 'lightgreen', 'orange', 'darkgreen', 'cadetblue', 'purple', 'pink']


def hut_style_ele(elevation):
  if elevation > 2800:
    return  ('black', 2800)
  elif elevation > 2500:
    return  ('darkred', 2500)
  elif elevation > 2000:
    return  ('orange', 2000)
  elif elevation > 1500:
    return  ('green', 1500)
  elif elevation > 1000:
    return  ('lightgreen', 1000)
  return ('gray', 500)


def hut_style_ele_high_peak(elevation):
  if elevation > 3300:
    return  ('black', 3300)
  elif elevation > 3200:
    return ('darkred', 3200)
  elif elevation > 3100:
    return ('red', 3100)
  elif elevation > 3000:
    return  ('orange', 3000)


def style_municipalities(feature):
  map_colors = {
      4: '#2ca02c',
      5: '#d62728',
      6: '#9467bd'
  }

  return {
      'fillColor': map_colors[feature["properties"]['COD_REG']],
      'color': map_colors[feature["properties"]['COD_REG']],
      'fill': True,
      'fillOpacity': .5,
      'weight': 1
  }


def style_dolomiti_municipalities(feature):
  return {
      'fillColor': TAB_10[int(feature['id'])],
      'color': TAB_10[int(feature['id'])],
      'fill': True,
      'fillOpacity': 1,
      'weight': 1
  }



def style_region(feature):
  return {
      'fillColor': TAB_10[int(feature['id'])],
      'color': TAB_10[int(feature['id'])],
      'fill': True,
      'fillOpacity': .1,
      'weight': 2
  }


def style_dolomiti(feature):
  color = ['red', 'orange', 'green','blue', "yellow", "black", "grey", "white", 'white']
  return {
      'fillColor': TAB_10[int(feature['id'])],
      'color': TAB_10[int(feature['id'])],
      'fill': True,
      'fillOpacity': 1,
      'weight': 2
  }

