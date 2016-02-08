set nocompatible              " be iMproved, required
filetype off                  " required

"set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'
Bundle 'dagwieers/asciidoc-vim'
Bundle 'pangloss/vim-javascript'
Bundle 'nvie/vim-flake8'

call vundle#end()            " required
filetype plugin indent on    " required

set hidden
au BufNewFile,BufRead *.adoc setf asciidoc
autocmd BufWritePost *.py call Flake8()
syntax on
set ruler
