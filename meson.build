project(
  'telegraph',
  version: '0.1.0',
  meson_version: '>= 0.59.0',
  license: 'GPL-3.0-only',
)

i18n = import('i18n')
python = import('python')
gnome = import('gnome')

project_id = 'com.github.fkinoshita.Telegraph'
project_name = 'Telegraph'
package_url = 'https://github.com/fkinoshita/Telegraph'
copyright = '© 2023 Felipe Kinoshita.'
contributors = '\n'.join([
    'Felipe Kinoshita',
])
# artists = '\n'.join([
#   '',
# ])

dependency('gtk4', version: '>=4.9')
dependency('libadwaita-1', version: '>=1.2')

DATA_DIR = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())

application_id = project_id
version = meson.project_version()

top_source_dir = meson.current_source_dir()
gettext_package = meson.project_name()

subdir('data')
subdir('po')
subdir('src')

gnome.post_install(
  glib_compile_schemas: true,
  gtk_update_icon_cache: true,
  update_desktop_database: true,
)
