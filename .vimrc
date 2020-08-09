" Enable line numbers
set number 

" Enable syntax highlighting
syntax on 

" Disable error sounds
set noerrorbells

" Tabs
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set smartindent

" Disable text wrapping
set nowrap

" Disable specific case requirements when searching
set smartcase 

" Disable swapfiles
set noswapfile

" Load search results as you type
set incsearch

" Set default colorscheme
set background=dark
colorscheme iceberg 

" ================[PLUGINS]================

call plug#begin('~/.vim/plugged')

Plug 'jiangmiao/auto-pairs'
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
Plug 'arcticicestudio/nord-vim'
Plug 'cocopon/iceberg.vim'
Plug 'vim-airline/vim-airline'
Plug 'scrooloose/syntastic'
Plug 'ycm-core/YouCompleteMe'

call plug#end()

