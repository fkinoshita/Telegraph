# main.py
#
# Copyright 2023 Felipe Kinoshita
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Gio, Adw
from .window import TelegraphWindow


class TelegraphApplication(Adw.Application):
    """The main application singleton class."""


    def __init__(self):
        super().__init__(application_id='io.github.fkinoshita.Telegraph',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.on_quit_action)
        self.add_action(quit_action)
        self.set_accels_for_action("app.quit", ["<Control>q"])

        self.create_action('about', self.on_about_action)

        self.create_action('switch', self.on_switch_action)
        self.set_accels_for_action("app.switch", ["<Control>space"])

        self.create_action('copy', self.on_copy_action)
        self.set_accels_for_action("app.copy", ["<Control>c"])


    def do_activate(self):
        """Called when the application is activated.

        We raise the application's main window, creating it if
        necessary.
        """
        win = self.props.active_window
        if not win:
            win = TelegraphWindow(application=self)
        win.present()


    def on_switch_action(self, widget, _):
        win = self.props.active_window
        win.switch()


    def on_copy_action(self, widget, _):
        win = self.props.active_window
        win.copy()


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


def main(version):
    """The application's entry point."""
    app = TelegraphApplication()
    return app.run(sys.argv)
