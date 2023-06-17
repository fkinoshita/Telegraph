application_id = 'io.github.fkinoshita.Telegraph'

if get_option('profile') == 'development'
  application_id = '@0@.Devel'.format(application_id)
endif

scalable_dir = join_paths('hicolor', 'scalable', 'apps')
install_data(
  join_paths(scalable_dir, ('@0@.svg').format(application_id)),
  install_dir: join_paths(get_option('datadir'), 'icons', scalable_dir)
)

symbolic_dir = join_paths('hicolor', 'symbolic', 'apps')
install_data(
  join_paths(symbolic_dir, ('io.github.fkinoshita.Telegraph-symbolic.svg')),
  install_dir: join_paths(get_option('datadir'), 'icons', symbolic_dir)
)