import sublime
import sublime_plugin

class RemoveSelection(sublime_plugin.TextCommand):
  def run(self, edit, selection):
    if selection > len(self.view.sel()) or len(self.view.sel()) == 1:
      return

    selections = []
    for index, sel in enumerate(self.view.sel()):
      if index == selection:
        continue
      selections.append(sel)

    self.view.sel().clear()
    self.view.sel().add_all(selections)

class RemoveLastSelection(sublime_plugin.TextCommand):
  def run(self, edit):
    sels = self.view.sel()
    if len(sels) <= 1:
      return

    old = []
    for index, sel in enumerate(sels):
      if index == len(sels) - 1:
        continue
      old.append(sel)

    self.view.sel().clear()
    for sel in old:
      self.view.sel().add(sel)

class LeaveLastSelection(sublime_plugin.TextCommand):
  def run(self, edit):
    sels = self.view.sel()
    if len(sels) <= 1:
      return

    last = sels[-1]
    self.view.sel().clear()
    self.view.sel().add(last)