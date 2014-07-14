import sublime
import sublime_plugin
import re

class ReplaceThis(sublime_plugin.EventListener):
	def on_modified(self, view):
		s = view.sel()
		for region in s:
			line = view.line(region)
			if re.match("^.*[\s;,\({\[\*&\^\!~\-\+=\?:]+this\.[\s;,\({\[\*&\^\!~\-\+=\?:]?.*$", view.substr(line)):
				view.run_command("this", {"start":line.end()-5, "end": line.end()})

class ThisCommand(sublime_plugin.TextCommand):
	def run(self, edit, start, end):
		region = sublime.Region(start, end)
		scopes = self.view.scope_name(start).split(" ")
		if "meta.function.c" in scopes \
			and "comment.line.double-slash.c++" not in scopes\
		 	and "comment.block.c" not in scopes:
			self.view.replace(edit, region, "this->")