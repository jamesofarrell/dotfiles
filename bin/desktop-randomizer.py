#!/usr/bin/python

import i3ipc, os, random, commands

conn = i3ipc.Connection()

wallpaper = {}
picture_path = "~/Pictures/desktop"
full_path = os.path.expanduser(picture_path)

def set_wallpaper(name):
	if not name in wallpaper:
		dirs = os.listdir(full_path)
		wallpaper[name] = random.choice(dirs)
	command = "feh --no-fehbg --bg-fill '" + os.path.join(full_path,wallpaper[name]) + "'"
	status, output = commands.getstatusoutput(command)


# Define a callback to be called when you switch workspaces.
def on_workspace(self, e):
	# The first parameter is the connection to the ipc and the second is an object
	# with the data of the event sent from i3.
	if e.current:
		try:
			set_wallpaper(e.current.name)
		except:
			print(e.current.name)


# Subscribe to the workspace event
conn.on('workspace::focus', on_workspace)

# Start the main loop and wait for events to come in.
conn.main()

