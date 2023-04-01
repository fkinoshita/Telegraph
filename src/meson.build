moduledir = join_paths(DATA_DIR, 'telegraph')

conf = configuration_data()

conf.set('VERSION', version)
conf.set('APPID', application_id)
conf.set('GETTEXT_PACKAGE', meson.project_name())
conf.set('LOCALE_DIR', join_paths(get_option('prefix'), get_option('datadir'), 'locale'))
conf.set('NAME', project_name)
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('DATA_DIR', DATA_DIR)
conf.set('APPID', application_id)

configure_file(
  input: 'const.py.in',
  output: 'const.py',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

configure_file(
  input: 'telegraph.in',
  output: 'telegraph',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

telegraph_sources = [
  '__init__.py',
  'main.py',
  'application.py',
  'window.py',
]

install_data(telegraph_sources, install_dir: moduledir)
