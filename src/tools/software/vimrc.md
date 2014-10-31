# vim configure file

## Install script including vundle

```
[ -z "$VUNDLE_URI" ] && VUNDLE_URI="https://github.com/gmarik/vundle.git"

sym_links() {
    ln -sf "$HOME/.hebi/vimrc" "$HOME/.vimrc"
}

clone_vundle() {
    if [ ! -e "$HOME/.vim/bundle/vundle" ]; then
        git clone $VUNDLE_URI "$HOME/.vim/bundle/vundle"
    else
        echo "Opoose, vundle has already installed?"
	exit 1
    fi
}

setup_vundle() {
    system_shell="$SHELL"
    export SHELL='/bin/sh'
    vim +PluginInstall +qall
    export SHELL="$system_shell"
}

sym_links
clone_vundle
setup_vundle

```

## vimrc

```
set nocompatible

" set vundle
filetype off
set rtp+=~/.vim/bundle/vundle
call vundle#begin()
Plugin 'tpope/vim-fugitive'
Plugin 'digitaltoad/vim-jade'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'
Plugin 'tomasr/molokai'
call vundle#end()

filetype plugin indent on
syntax on
set nu

" set term color to 256. Must before colorscheme
set t_Co=256
colorscheme molokai

"disable vim-markdown folding
let g:vim_markdown_folding_disabled=1
```
