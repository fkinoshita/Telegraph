from gettext import gettext as _

from gi.repository import Adw, Gtk, Gio

from .window import TelegraphWindow


class TelegraphApplication(Adw.Application):
    def __init__(self):
        super().__init__(application_id='io.github.fkinoshita.Telegraph',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit_action)
        self.add_action(quit_action)
        self.set_accels_for_action("app.quit", ["<Control>q", "<Control>w"])

        self.create_action('about', self.on_about_action)


    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = TelegraphWindow(application=self)
        win.present()


    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        builder = Gtk.Builder.new_from_resource(
            "/io/github/fkinoshita/Telegraph/about_dialog.ui"
        )
        about_dialog = builder.get_object("about_dialog")
        about_dialog.set_transient_for(self.props.active_window)
        about_dialog.present()


    def on_quit_action(self, widget, _):
        self.quit()


    def create_action(self, name, callback, shortcuts=None):
        """Add an application action.

        Args:
            name: the name of the action
            callback: the function to be called when the action is
              activated
            shortcuts: an optional list of accelerators
        """
        action = Gio.SimpleAction.new(name, None)
        action.connect("activate", callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f"app.{name}", shortcuts)

