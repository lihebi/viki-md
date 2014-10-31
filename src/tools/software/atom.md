# Atom

## configure

`~/.atom/keymap.cson`

```
'.platform-linux .editor':
  'ctrl-n': 'core:move-down'
  'ctrl-p': 'core:move-up'
  'ctrl-b': 'core:move-left'
  'ctrl-f': 'core:move-right'
  'ctrl-d': 'core:delete'
  'ctrl-h': 'core:backspace'
  'cmd-f': 'find-and-replace:toggle'
  'cmd-=': 'editor:auto-indent'
  'ctrl-e': 'editor:move-to-end-of-line'
  'ctrl-a': 'editor:move-to-first-character-of-line'
```

## usage

### ctags

`symbol-view` package will use ctags.
Its `lib` folder contains `.ctags` file.
官方说a good start是放到`~`中，运行ctags时，用

* `cmd-shift-r`: check tag(need tags file)
* `cmd-r`: check ref
* `cmd-t`: search

all these 3 command need type something instead of the selection.

## Palette (Cmd-Shift-p)

* styleguide

## Packages

* zentabs: limit tabs under a number
* minimap

## Package Create Tutorial

### 创建工程

`Package Generator: Generate Package`

now I have:

* a package located in `$HOME/.atom/packages/xxx`
* command available `xxx:toggle`
* when execute it, output `Alive` message

### 新的命令

lib/ascii-art.coffee

```
module.exports =
  activate: ->
    atom.workspaceView.command "ascii-art:convert", => @convert()

  convert: ->
    # This assumes the active pane item is an editor
    editor = atom.workspace.activePaneItem
    editor.insertText('Hello, World!')
```

### 激活命令

package.json

```
"activationEvents": ["ascii-art:convert"],
```

### 快捷键

keymaps/ascii-art.cson

```
'.editor':
  'cmd-alt-a': 'ascii-art:convert'
```

### 重启window

`window:reload`, then everything works.

### ASCII

add figlet dependence

```
"dependencies": {
   "figlet": "1.0.8"
}
```

modify `lib/ascii-art.coffee`

```
convert: ->
  # This assumes the active pane item is an editor
  editor = atom.workspace.activePaneItem
  selection = editor.getSelection()

  figlet = require 'figlet'
  figlet selection.getText(), {font: "Larry 3D 2"}, (error, asciiArt) ->
    if error
      console.error(error)
    else
      selection.insertText("\n#{asciiArt}\n")
```
