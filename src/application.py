# SPDX-License-Identifier: GPL-3.0-only

import gi
from gettext import gettext as _

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Adw, Gtk, Gio

from .const import APP_ID
from .window import TelegraphWindow


class TelegraphApplication(Adw.Application):
    def __init__(self):
        super().__init__(
            application_id=APP_ID,
            flags=Gio.ApplicationFlags.FLAGS_NONE
        )

        self.setup_actions()
        self.add_global_accelerators()


    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = TelegraphWindow(application=self)
        win.present()


    def setup_actions(self):
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit_action)
        self.add_action(quit_action)

        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.on_about_action)
        self.add_action(about_action)


    def add_global_accelerators(self):
        self.set_accels_for_action("app.quit", ["<Control>q"])
        self.set_accels_for_action("window.close", ["<Control>w"])


    def on_quit_action(self, widget, _):
        self.quit()


    def on_about_action(self, widget, _):
        """Callback for the app.about action."""
        builder = Gtk.Builder.new_from_resource(
            "/io/github/fkinoshita/Telegraph/about_dialog.ui"
        )
        about_dialog = builder.get_object("about_dialog")
        about_dialog.set_transient_for(self.props.active_window)

        about_dialog.set_release_notes(
        """<p>This release makes Telegraph inline with other GNOME 45 apps</p>
           <ul>
             <li>Use of the newer widgets, making Telegraph more consistent with other apps</li>
             <li>Updated metadata</li>
             <li>Updated translations</li>
           </ul>
           <p>If you would like to come with suggestions, report bugs, translate the app, or contribute otherwise, feel free to reach out!</p>
        """)

        about_dialog.present()

