from pygal_maps_world.maps import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Ameryka Północna, Środkowa i Połodniowa'

wm.add('Ameryka Pólnocna', ['ca', 'mx', 'us'])
wm.add("Ameryka Środkowa", ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('Ameryka Południowa', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gh', 'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.render_to_file('americans.svg')