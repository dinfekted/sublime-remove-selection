# Sublime RemoveSelection plugin

Removes specified cursor.


### Demo

![Demo](https://github.com/shagabutdinov/sublime-remove-selection/raw/master/demo/demo.gif "Demo")

### Installation

This plugin is part of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
plugin set. You can install sublime-enhanced and this plugin will be installed
automatically.

If you would like to install this package separately check "Installing packages
separately" section of [sublime-enhanced](http://github.com/shagabutdinov/sublime-enhanced)
package.


### Features

1. Remove n-th cursor (from 1 to 5 with default key bindings).

2. Remove last cursor

3. Leave only last cursor


### Usage

Hit shortcuts to remove desired cursor or leave only last one.

Example:

```
  # before
  call1|() # <- cursors here
  call2|() # <- cursors here
  call3|() # <- cursors here

  # after "remove 2nd cursor"
  call1|() # <- cursors here
  call2()
  call3|() # <- cursors here

  # after "leave only last cursor"
  call1()
  call2()
  call3|() # <- cursors here
```

### Commands

| Description            | Keyboard shortcuts | Command palette                         |
|------------------------|--------------------|-----------------------------------------|
| Remove 1st cursor      | ctrl+u, ctrl+1     | RemoveSelection: Remove 1st cursor      |
| Remove 2nd cursor      | ctrl+u, ctrl+2     | RemoveSelection: Remove 2nd cursor      |
| Remove 3rd cursor      | ctrl+u, ctrl+3     | RemoveSelection: Remove 3rd cursor      |
| Remove 4th cursor      | ctrl+u, ctrl+4     | RemoveSelection: Remove 4th cursor      |
| Remove 5th cursor      | ctrl+u, ctrl+5     | RemoveSelection: Remove 5th cursor      |
| Remove last cursor     | ctrl+alt+shift+x   | RemoveSelection: Remove last cursor     |
| Leave only last cursor | ctrl+escape        | RemoveSelection: Leave only last cursor |