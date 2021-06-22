# Returns the commom directory path for specified array of full filenames.
#
#  @param {array} pathes
#  @return {string}
# Examples:
#
#   ['/web/images/image1.png', '/web/images/image2.png']  => '/web/images/'
#   ['/web/assets/style.css', '/web/scripts/app.js',  'home/setting.conf'] => ''
#   ['/web/assets/style.css', '/.bin/mocha',  '/read.me'] => '/'
#   ['/web/favicon.ico', '/web-scripts/dump', '/webalizer/logs'] => '/'

def get_common_directory_path(pathes):
    paths = [x.split('/') for x in pathes]
    result = []

    for i in zip(*paths):
        if len(set(i)) == 1:
            result.append(i[0])
        else:
            result.append('')
            break
    return '/'.join(result)

# print(get_common_directory_path(['/web/assets/style.css', '/web/scripts/app.js',  'home/setting.conf']))
print(get_common_directory_path(['/web/images/image1.png', '/web/images/image2.png']))