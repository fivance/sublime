import sublime
import sublime_plugin


class ConvertToLowercaseCommand(sublime_plugin.TextCommand):
    """Convert selected text (or word under cursor) to lowercase."""

    def run(self, edit):
        for region in self._get_regions():
            text = self.view.substr(region)
            self.view.replace(edit, region, text.lower())

    def _get_regions(self):
        regions = [r for r in self.view.sel() if not r.empty()]
        if regions:
            return regions
        # No selection — use word under cursor
        return [self.view.word(r) for r in self.view.sel()]

    def is_enabled(self):
        return True


class ConvertToUppercaseCommand(sublime_plugin.TextCommand):
    """Convert selected text (or word under cursor) to UPPERCASE."""

    def run(self, edit):
        for region in self._get_regions():
            text = self.view.substr(region)
            self.view.replace(edit, region, text.upper())

    def _get_regions(self):
        regions = [r for r in self.view.sel() if not r.empty()]
        if regions:
            return regions
        return [self.view.word(r) for r in self.view.sel()]

    def is_enabled(self):
        return True
