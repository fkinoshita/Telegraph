# window.py
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

import re
from enum import Enum

from gi.repository import Adw
from gi.repository import Gtk, Gdk

morse_table = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

class Mode(Enum):
    TO_MORSE = 1
    FROM_MORSE = 2

@Gtk.Template(resource_path='/com/github/fkinoshita/Telegraph/ui/window.ui')
class TelegraphWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'TelegraphWindow'

    input_group = Gtk.Template.Child()
    output_group = Gtk.Template.Child()

    input_text_view = Gtk.Template.Child()
    output_text_view = Gtk.Template.Child()

    switch_button = Gtk.Template.Child()
    copy_button = Gtk.Template.Child()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_size_request(350, 450)

        self.mode = Mode.TO_MORSE

        input_buffer = self.input_text_view.get_buffer()
        input_buffer.connect('changed', self.__on_input_changed);

        self.switch_button.connect('clicked', self.__on_switch_button_clicked)
        self.copy_button.connect('clicked', self.__on_copy_button_clicked);

        self.input_text_view.grab_focus()


    def __on_input_changed(self, input_buffer):
        (start, end) = input_buffer.get_bounds()
        text = input_buffer.get_text(start, end, False)

        if self.mode == Mode.TO_MORSE:
            output_message = self.translate_to(text)
        if self.mode == Mode.FROM_MORSE:
            output_message = self.translate_from(text)

        output_buffer = self.output_text_view.get_buffer()
        output_buffer.set_text(output_message)

        (start, end) = output_buffer.get_bounds()
        output = output_buffer.get_text(start, end, False)
        if len(output) == 0:
            self.copy_button.set_sensitive(False)
        else:
            self.copy_button.set_sensitive(True)


    def __on_switch_button_clicked(self, button):
        self.switch()

        if self.mode == Mode.FROM_MORSE:
            button.set_tooltip_text(_('Translate to Morse'))
            return
        if self.mode == Mode.TO_MORSE:
            button.set_tooltip_text(_('Translate From Morse'))
            return


    def __on_copy_button_clicked(self, button):
        self.copy()


    def copy(self):
        output_buffer = self.output_text_view.get_buffer()
        (start, end) = output_buffer.get_bounds()
        output = output_buffer.get_text(start, end, False)

        if (len(output) == 0):
            return

        Gdk.Display.get_default().get_clipboard().set(output)


    def switch(self):
        self.input_text_view.grab_focus()

        input_buffer = self.input_text_view.get_buffer()
        (start, end) = input_buffer.get_bounds()
        input_text = input_buffer.get_text(start, end, False)

        output_buffer = self.output_text_view.get_buffer()
        (start, end) = output_buffer.get_bounds()
        output_text = output_buffer.get_text(start, end, False)

        input_buffer.set_text(output_text.lower())
        output_buffer.set_text(input_text.lower())

        if self.mode == Mode.FROM_MORSE:
            self.mode = Mode.TO_MORSE

            self.input_group.set_title(_('Message'))
            self.output_group.set_title(_('Morse Code'))
            self.input_text_view.set_monospace(False)
            self.output_text_view.set_monospace(True)

            return

        if self.mode == Mode.TO_MORSE:
            self.mode = Mode.FROM_MORSE

            self.input_group.set_title(_('Morse Code'))
            self.output_group.set_title(_('Message'))
            self.input_text_view.set_monospace(True)
            self.output_text_view.set_monospace(False)

            return

    def translate_to(self, text):
        text = re.sub(r'[^A-Za-z0-9 \n]+', '', text)

        words = text.lower().replace('\n', ' ').split(' ')
        output = ''

        for outer_index, word in enumerate(words):
            for inner_index, letter in enumerate(word):
                output += morse_table[letter]

                if (inner_index + 1 != len(word)):
                    output += ' '

            if (outer_index + 1 != len(words)):
                output += ' / '

        return output


    def translate_from(self, text):
        text = re.sub(r'[^\-\.0-9 \n/]+', '', text)

        words = text.replace('\n', '/').split('/')
        output = ''
        
        for outer_index, word in enumerate(words):
            word.strip()

            letters = word.split(' ')
            letters = list(filter(None, letters))

            for inner_index, letter in enumerate(letters):
                for key, value in morse_table.items():
                    if letter == value:
                        output += key

            output += ' '

        return output

    
